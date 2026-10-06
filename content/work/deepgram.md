---
title: Deepgram
summary: Interactive motion that lets people feel what AI voice can do, not just read about it.
role: Interactive Motion Designer & Developer
year: 2025
tools: [Rive]
category: ui-motion
order: 2
---

## The problem
AI voice is invisible. On a web page it's just claims, until you can see and interact with what the product does.

## What I built
Four interactive demonstrations, built as custom Rive components:
- **Voice-to-text:** a UI simulation of speech becoming text
- **Voices:** an interactive avatar experience
- **Voice assistant:** a ring animation that reacts to states
- **Slack walkthrough:** the Saga Messages integration shown step by step

## Design decisions
- **Interactive, not video:** scroll- and hover-triggered, so visitors *drive* the demo. [confirm: why Rive over video/Lottie: interactivity, file size, state machines?]
- **Built for production:** optimized for web performance and tested for playback across devices.
- **Accessible:** respects reduced-motion preferences.
- [TODO: which states does each component have? e.g. idle, listening, speaking. This is interaction design; spell it out.]

## Outcome
[TODO from your own files: number of states/inputs per component, file sizes of the shipped .riv assets]
