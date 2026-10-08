---
title: Deepgram
summary: Interactive motion that lets people feel what AI voice can do, not just read about it.
role: Interactive Motion Designer & Developer
year: 2025
tools: [Rive]
category: ui-motion
order: 2
cover: /work/deepgram/thumb.webp
coverVideo: /work/deepgram/thumb.mp4
rive:
  - src: /rive/deepgram/voices.riv
    label: Deepgram Voices demo. Select an avatar to hear its voice.
    caption: Voices. Hover the avatars, click one to hear it (sound on).
    ratio: 538 / 310
    poster: /work/deepgram/voices.webp
    stateMachine: State Machine 1
    wide: true
    hotspots: # clickable avatars: Andromeda, Atlas, Arcas, Thalia, Odysseus, Luna, Aries
      - { x: 0.3179, y: 0.1966, r: 0.055 }
      - { x: 0.5938, y: 0.1966, r: 0.055 }
      - { x: 0.4138, y: 0.5131, r: 0.055 }
      - { x: 0.5539, y: 0.5131, r: 0.055 }
      - { x: 0.6875, y: 0.5131, r: 0.055 }
      - { x: 0.4450, y: 0.8071, r: 0.055 }
      - { x: 0.7134, y: 0.8071, r: 0.055 }
  - src: /rive/deepgram/voice-to-text.riv
    label: Text-to-speech pronunciation demo with play controls and a highlighted transcript.
    caption: Pronunciation. Press play and the transcript follows the audio; press again to pause.
    ratio: 538 / 355
    stateMachine: State Machine 1
    poster: /work/deepgram/voice-to-text.webp
    pause:
      state: Karaoke Animation
      x: 0.494
      y: 0.7934
      d: 0.0793
      fill: '#e1e1e5'
      icon: '#168559'
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
