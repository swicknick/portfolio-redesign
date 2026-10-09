/*
 * MoonBackground — WebGL2 animated background.
 *
 * Reconstructs a rendered frame sequence from 8 basis textures plus
 * per-frame coefficients:  color = mean + Σ coefficient_i(t) · basis_i
 *
 * No dependencies. ~10 KB of JS + ~49 KB of textures.
 *
 *   import { MoonBackground } from './moon-background.js';
 *   const bg = new MoonBackground(el, { basePath: './textures/' });
 *   await bg.init();
 *
 * See README.md for integration notes.
 */

const VERT = `#version 300 es
in vec2 p; out vec2 uv;
void main(){ uv = p*0.5+0.5; uv.y = 1.0-uv.y; gl_Position = vec4(p,0.,1.); }`;

function fragSource(K) {
  let acc = '';
  for (let i = 0; i < K; i++) {
    acc += `  c += uC[${i}] * dec(texture(uB[${i}], uv).rgb, uBR[${i}]);\n`;
  }
  return `#version 300 es
precision highp float;
in vec2 uv; out vec4 o;
uniform sampler2D uMean;
uniform sampler2D uB[${K}];
uniform vec2 uMeanR;
uniform vec2 uBR[${K}];
uniform float uC[${K}];
uniform float uGrain, uTime, uGBase, uGSlope, uGCorr;

vec3 dec(vec3 t, vec2 r){ return t*(r.y-r.x)+r.x; }
float hash(vec2 q){ return fract(sin(dot(q, vec2(127.1,311.7))) * 43758.5453); }

void main(){
  vec3 c = dec(texture(uMean, uv).rgb, uMeanR);
${acc}  c = clamp(c, 0.0, 1.0);

  if (uGrain > 0.0) {
    // Amplitude fitted from the source residual: stronger in shadow,
    // weaker in highlight. Channels partially correlated (film, not digital).
    float luma = dot(c, vec3(0.2126, 0.7152, 0.0722));
    float amp  = max(uGBase + uGSlope * luma, 0.0) * uGrain;
    vec2  sd   = gl_FragCoord.xy + vec2(uTime*61.0, uTime*37.0);
    float gC   = hash(sd) - 0.5;
    vec3  gI   = vec3(hash(sd+11.3), hash(sd+27.7), hash(sd+43.1)) - 0.5;
    c += amp * (sqrt(uGCorr)*gC + sqrt(1.0-uGCorr)*gI);
  }
  o = vec4(clamp(c, 0.0, 1.0), 1.0);
}`;
}

export class MoonBackground {
  /**
   * @param {HTMLElement} container  positioned element to fill
   * @param {object} opts
   *   basePath   {string}  where textures/ live            default './textures/'
   *   loop       {boolean} restart after the last frame    default true
   *   autoplay   {boolean} start on init                   default true
   *   playOnce   {boolean} play once when scrolled in,
   *                        then hold the final frame       default false
   *   grain      {number}  0 disables, 1 = fitted amount   default 1
   *   maxDPR     {number}  device pixel ratio cap          default 2
   *   speed      {number}  playback rate multiplier        default 0.25 (1 = AE speed)
   *   data       {object}  pre-parsed model.json — skips fetching
   *                        basePath + 'model.json'          default none
   *   images     {object}  name -> data:/blob: URI ('mean', 'b0'...) —
   *                        skips fetching basePath + name + '.webp'.
   *                        For a fully offline/inlined page.  default none
   */
  constructor(container, opts = {}) {
    this.el = container;
    this.o = Object.assign({
      basePath: './textures/', loop: true, autoplay: true, playOnce: false,
      grain: 1, maxDPR: 2, speed: 0.25,   // 0.25x the After Effects speed (1 = original)
    }, opts);

    this.canvas = document.createElement('canvas');
    Object.assign(this.canvas.style, {
      position: 'absolute', inset: '0', width: '100%', height: '100%',
      display: 'block',
    });

    this.frame = 0;
    this.playing = false;
    this.visible = true;
    this.ready = false;
    this._raf = null;
    this._played = false;

    this.reducedMotion =
      window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  async init() {
    const gl = this.canvas.getContext('webgl2', { antialias: false, alpha: false });
    if (!gl) { this._fallback(); return false; }
    this.gl = gl;

    // opts.data lets a caller supply an already-parsed model.json (e.g. a
    // fully inlined preview page with no network/file fetch at all — plain
    // fetch() of local files is CORS-blocked under file:// in Chrome, even
    // for same-directory files). Falls back to fetching basePath/model.json
    // for normal served-over-http production use.
    if (this.o.data) {
      this.meta = this.o.data;
    } else {
      const res = await fetch(this.o.basePath + 'model.json');
      if (!res.ok) { this._fallback(); return false; }
      this.meta = await res.json();
    }
    const K = this.K = this.meta.K;
    this.coef = this.meta.coef;
    this.nFrames = this.coef.length;
    this.fps = this.meta.fps || 25;

    // Build program
    const vs = this._shader(gl.VERTEX_SHADER, VERT);
    const fs = this._shader(gl.FRAGMENT_SHADER, fragSource(K));
    const prog = gl.createProgram();
    gl.attachShader(prog, vs); gl.attachShader(prog, fs); gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) {
      console.error(gl.getProgramInfoLog(prog)); this._fallback(); return false;
    }
    gl.useProgram(prog);
    this.prog = prog;

    // Fullscreen triangle
    const vb = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vb);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 3,-1, -1,3]),
                  gl.STATIC_DRAW);
    const pl = gl.getAttribLocation(prog, 'p');
    gl.enableVertexAttribArray(pl);
    gl.vertexAttribPointer(pl, 2, gl.FLOAT, false, 0, 0);

    // Textures. opts.images (name -> data: URI or blob: URL) skips the file
    // fetch entirely, same reasoning as opts.data above — Image().src on a
    // data: URI never touches the network/file layer, so it works under
    // file:// with no CORS restriction regardless.
    const names = ['mean', ...Array.from({length: K}, (_, i) => 'b' + i)];
    let imgs;
    try {
      imgs = await Promise.all(names.map(n =>
        this._img(this.o.images ? this.o.images[n] : this.o.basePath + n + '.webp')));
    } catch (e) { console.error(e); this._fallback(); return false; }
    imgs.forEach((im, i) => this._tex(im, i));

    gl.uniform1i(gl.getUniformLocation(prog, 'uMean'), 0);
    gl.uniform2f(gl.getUniformLocation(prog, 'uMeanR'),
                 this.meta.mean.lo, this.meta.mean.hi);
    for (let i = 0; i < K; i++) {
      gl.uniform1i(gl.getUniformLocation(prog, `uB[${i}]`), i + 1);
      gl.uniform2f(gl.getUniformLocation(prog, `uBR[${i}]`),
                   this.meta.layers[i].lo, this.meta.layers[i].hi);
    }
    const g = this.meta.grain || { base: 0, slope: 0, chanCorr: 0.4 };
    gl.uniform1f(gl.getUniformLocation(prog, 'uGBase'), g.base);
    gl.uniform1f(gl.getUniformLocation(prog, 'uGSlope'), g.slope);
    gl.uniform1f(gl.getUniformLocation(prog, 'uGCorr'), g.chanCorr);

    this.uC = gl.getUniformLocation(prog, 'uC');
    this.uGrain = gl.getUniformLocation(prog, 'uGrain');
    this.uTime = gl.getUniformLocation(prog, 'uTime');

    this.el.appendChild(this.canvas);
    this.ready = true;

    // Pause the render loop while off-screen.
    if ('IntersectionObserver' in window) {
      this._io = new IntersectionObserver(([e]) => {
        this.visible = e.isIntersecting;
        if (this.visible && this.o.playOnce && !this._played && !this.reducedMotion) {
          this._played = true; this.frame = 0; this.playing = true;
        }
      }, { threshold: 0.01 });
      this._io.observe(this.el);
    }

    if (this.reducedMotion) {
      this.frame = this.nFrames - 1;   // hold the final, fully-bloomed state
      this.playing = false;
      this._renderOnce();
    } else if (this.o.autoplay && !this.o.playOnce) {
      this.play();
    } else {
      this._renderOnce();
    }

    this._last = performance.now();
    this._raf = requestAnimationFrame(this._tick);
    return true;
  }

  play()  { if (this.ready) { this.playing = true;  this._last = performance.now(); } }
  pause() { this.playing = false; }

  /** Jump to a frame (0 .. nFrames-1). Pauses playback. */
  seek(f) {
    this.frame = Math.max(0, Math.min(this.nFrames - 1, f));
    this.playing = false;
    this._renderOnce();
  }

  /** Progress through the animation, 0..1. Useful for scroll-driven playback. */
  setProgress(p) { this.seek(Math.max(0, Math.min(1, p)) * (this.nFrames - 1)); }

  /** Grain amount, 0..1 (0 disables). Takes effect on the next drawn frame. */
  setGrain(amount) { this.o.grain = amount; }

  /** Whether playback restarts after the last frame. */
  setLoop(loop) { this.o.loop = loop; }

  destroy() {
    if (this._raf) cancelAnimationFrame(this._raf);
    if (this._io) this._io.disconnect();
    const lose = this.gl && this.gl.getExtension('WEBGL_lose_context');
    if (lose) lose.loseContext();
    if (this.canvas.parentNode) this.canvas.parentNode.removeChild(this.canvas);
    this.ready = false;
  }

  // ---- internals ----

  _shader(type, src) {
    const gl = this.gl, s = gl.createShader(type);
    gl.shaderSource(s, src); gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
      throw new Error(gl.getShaderInfoLog(s));
    }
    return s;
  }

  _img(src) {
    return new Promise((res, rej) => {
      const im = new Image();
      im.onload = () => res(im);
      im.onerror = () => rej(new Error('failed to load ' + src));
      im.src = src;
    });
  }

  _tex(img, unit) {
    const gl = this.gl, t = gl.createTexture();
    gl.activeTexture(gl.TEXTURE0 + unit);
    gl.bindTexture(gl.TEXTURE_2D, t);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB8, gl.RGB, gl.UNSIGNED_BYTE, img);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    return t;
  }

  _fallback() {
    // No WebGL2 (or assets failed): show the poster still.
    this.el.style.backgroundImage =
      `url("${this.o.basePath.replace(/textures\/$/, '')}poster.webp")`;
    this.el.style.backgroundSize = 'cover';
    this.el.style.backgroundPosition = 'center';
  }

  _coefAt(f) {
    const a = Math.max(0, Math.min(this.nFrames - 1, Math.floor(f)));
    const b = Math.min(this.nFrames - 1, a + 1);
    const m = f - a, out = new Float32Array(this.K);
    for (let i = 0; i < this.K; i++) {
      out[i] = this.coef[a][i] * (1 - m) + this.coef[b][i] * m;
    }
    return out;
  }

  _size() {
    const d = Math.min(window.devicePixelRatio || 1, this.o.maxDPR);
    const w = Math.round(this.canvas.clientWidth * d);
    const h = Math.round(this.canvas.clientHeight * d);
    if (w > 0 && h > 0 && (this.canvas.width !== w || this.canvas.height !== h)) {
      this.canvas.width = w; this.canvas.height = h;
      this.gl.viewport(0, 0, w, h);
    }
  }

  _draw(now) {
    const gl = this.gl;
    this._size();
    gl.uniform1fv(this.uC, this._coefAt(this.frame));
    gl.uniform1f(this.uGrain, this.o.grain);
    gl.uniform1f(this.uTime, (now || 0) * 0.001);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  }

  _renderOnce() { if (this.ready) this._draw(performance.now()); }

  _tick = (now) => {
    this._raf = requestAnimationFrame(this._tick);
    if (!this.ready) return;
    const dt = (now - this._last) / 1000;
    this._last = now;
    if (!this.visible) return;            // off-screen: skip GPU work entirely

    if (this.playing) {
      this.frame += dt * this.fps * this.o.speed;
      if (this.frame >= this.nFrames - 1) {
        if (this.o.loop && !this.o.playOnce) {
          this.frame = 0;
        } else {
          this.frame = this.nFrames - 1;
          this.playing = false;
        }
      }
    } else if (this.o.grain <= 0) {
      return;                             // static and grainless: nothing changes
    }
    this._draw(now);
  };
}

export default MoonBackground;
