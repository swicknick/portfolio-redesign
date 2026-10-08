---
title: Materialize
summary: Showing how live data flows through a real-time data platform.
role: Motion Designer & Illustrator
year: 2025
tools: [After Effects, Lottie]
category: motion
order: 3
cover: /work/materialize/ingestion-poster.webp
scroll:
  - src: /lottie/materialize/getting-data-in.json
    title: Getting data in
    text: Data streams in from source systems and lands in the platform as it changes.
  - src: /lottie/materialize/semantic-models.json
    title: Building semantic models
    text: Raw streams are shaped into semantic models that stay current as new data arrives.
  - src: /lottie/materialize/apps-pulling-data.json
    title: Apps and agents pulling data
    text: Applications and AI agents pull from those models, shown as live connections on the grid.
---

## The problem
Materialize turns live data streams into queryable, real-time results. That's hard to picture, and harder to sell if people can't picture it.

## What I built
- **Hero animation** introducing the platform
- **Scroll-driven animation** that follows data through the product as you read. The section above runs those production Lottie files, scrubbed frame by frame as you scroll.
- **Three system visualizations:** data ingestion, semantic modeling, and application data access

<figure>
  <video data-loop muted loop playsinline preload="none" poster="/work/materialize/site-hero-poster.webp" width="1280" height="720" src="/work/materialize/site-hero.mp4" aria-label="Materialize homepage hero animation"></video>
  <figcaption>The hero animation on the live site.</figcaption>
</figure>

## Design decisions
- **Scroll-driven:** the explanation moves at the reader's pace, not a video's.
- **Lottie for performance:** vector animation instead of video keeps the page fast. The three scroll animations together are about 370 KB over the wire.

<figure>
  <img src="/work/materialize/architecture.webp" alt="Materialize architecture diagram" width="1600" height="900" loading="lazy" decoding="async" />
</figure>
