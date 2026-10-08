---
title: Sequence to Shader
summary: An AI-built tool that turns After Effects renders into tiny, measurably accurate web shaders.
role: Designer & builder
year: 2026
tools: [Claude Code, Python, WebGL, After Effects]
category: product
order: 4
---

## The problem
Motion designers hand off beautiful backgrounds (gradients, glows, light effects) and they die in production. Developers get a choice between two bad options:

- **Ship the video:** tens of MB, slow page loads, decode cost on mobile.
- **Rebuild it by hand in CSS or shaders:** it never quite matches. A big reason: the colors in the project file aren't the colors on screen. Grading, glows, and blend modes change them after the fact, so anything rebuilt from the source file is copying colors that never appear in the final render.

I've been on the motion side of that handoff for years. I wanted a third option.

## The approach
Instead of rebuilding the effect, **measure the finished render and compress it mathematically.**

Smooth motion graphics turn out to be extremely compressible: a handful of base images, mixed over time, can reproduce every frame. The tool finds those base images from the rendered frames, and a small WebGL shader mixes them back together live in the browser.

Because it works from the final render, it doesn't matter how many layers, blurs, or effects made the original. It captures what the viewer actually sees.

## Designing it as a product, not a script
The users are the **developers receiving the handoff**, so the output had to be something a dev team could drop in, not a demo:

- **Drop-in module:** play, pause, seek, and scroll-driven progress.
- **Respects the user:** honors reduced-motion settings, pauses when off-screen, and falls back to a poster image.
- **Honest numbers:** every handoff ships with a README reporting measured error and file size for *that* asset. No "looks close."
- **Grain that looks real:** film grain is measured and rebuilt separately. It is stronger in shadows and partially correlated across color channels, because flat digital noise reads as fake.

## Status
Built and used as an internal production tool. A public demo on a personal animation, with measured size and error numbers, is next.
