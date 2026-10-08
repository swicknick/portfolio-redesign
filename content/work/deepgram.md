---
title: Deepgram
summary: Interactive motion that lets people feel what AI voice can do, not just read about it.
role: Interactive Motion Designer & Developer
year: 2025
tools: [Rive]
category: ui-motion
order: 2
cover: /work/deepgram/voices.webp
---

## The problem
AI voice is invisible. On a web page it's just claims, until you can see and interact with what the product does.

## What I built
Four interactive demonstrations, built as custom Rive components:
- **Voice-to-text:** a UI simulation of speech becoming text
- **Voices:** an interactive avatar experience
- **Voice assistant:** a ring animation that reacts to states
- **Slack walkthrough:** the Saga Messages integration shown step by step

<figure>
  <img src="/work/deepgram/voices.webp" alt="Grid of voice avatars from the Deepgram Voices demo" width="1600" height="922" loading="lazy" decoding="async" />
  <figcaption>Voices: pick an avatar and hear it.</figcaption>
</figure>

<div class="pair">
<figure>
  <video data-loop muted loop playsinline preload="none" poster="/work/deepgram/assistant-ring-poster.webp" width="836" height="784" src="/work/deepgram/assistant-ring.mp4" aria-label="Voice assistant ring animation reacting to states"></video>
  <figcaption>Voice assistant: the ring reacts to each state.</figcaption>
</figure>
<figure>
  <img src="/work/deepgram/voice-to-text.webp" alt="Voice-to-text UI simulation with a waveform and transcript" width="1600" height="1056" loading="lazy" decoding="async" />
  <figcaption>Voice-to-text: speech becoming text in real time.</figcaption>
</figure>
</div>

## Design decisions
- **Interactive, not video:** scroll- and hover-triggered, so visitors *drive* the demo instead of watching it.
- **Built for production:** optimized for web performance and tested for playback across devices.
- **Accessible:** respects reduced-motion preferences.

<figure>
  <video data-loop muted loop playsinline preload="none" poster="/work/deepgram/slack-walkthrough-poster.webp" width="1280" height="622" src="/work/deepgram/slack-walkthrough.mp4" aria-label="Slack integration walkthrough animation"></video>
  <figcaption>Slack walkthrough: the integration shown step by step.</figcaption>
</figure>
