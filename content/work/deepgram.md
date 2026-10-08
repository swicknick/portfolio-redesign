---
title: Deepgram
summary: Interactive motion that lets people feel what AI voice can do, not just read about it.
role: Interactive Motion Designer & Developer
year: 2025
tools: [Rive]
category: ui-motion
order: 2
cover: /work/deepgram/voices.webp
rive:
  - src: /rive/deepgram/voices.riv
    label: Deepgram Voices demo. Select an avatar to hear its voice.
    caption: Voices. Hover the avatars, click one to hear it (sound on).
    ratio: 538 / 310
    poster: /work/deepgram/voices.webp
    stateMachine: State Machine 1
    wide: true
  - src: /rive/deepgram/voice-to-text.riv
    label: Text-to-speech pronunciation demo with play controls and a highlighted transcript.
    caption: Pronunciation. Press play and the transcript follows the audio.
    ratio: 538 / 355
    stateMachine: State Machine 1
    poster: /work/deepgram/voice-to-text.webp
  - src: /rive/deepgram/voice-agent.riv
    label: Voice assistant ring animation.
    caption: Voice assistant. The ring that shows the agent is listening and speaking.
    ratio: 538 / 355
    stateMachine: State Machine 1
  - src: /rive/deepgram/saga-slack.riv
    label: Saga integration walkthrough showing a voice command creating a Slack message.
    caption: Slack walkthrough. A voice command becomes a Slack message, step by step.
    ratio: 2432 / 1180
    poster: /work/deepgram/slack.webp
    stateMachine: State Machine 1
    wide: true
---

## The problem
AI voice is invisible. On a web page it's just claims, until you can see and interact with what the product does.

## What I built
Four interactive demonstrations, built as custom Rive components. The ones above are the real production files, running live:
- **Voices:** an interactive avatar experience with each voice built in
- **Pronunciation:** a UI simulation of speech and text moving together
- **Voice assistant:** a ring animation that reacts to states
- **Slack walkthrough:** the Saga Messages integration shown step by step

## Design decisions
- **Interactive, not video:** visitors *drive* the demo instead of watching it. Audio and images are embedded in each file, so one asset carries the whole experience.
- **State machines over timelines:** each voice is its own trigger, so the demo responds to whatever someone clicks next instead of playing a fixed sequence.
- **Built for production:** optimized for web performance and tested for playback across devices.
- **Accessible:** respects reduced-motion preferences.
