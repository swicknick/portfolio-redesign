---
title: Materialize
summary: Showing how live data flows through a real-time data platform.
role: Motion Designer & Illustrator
year: 2025
tools: [After Effects, Lottie]
category: motion
order: 7
cover: /work/materialize/ingestion-poster.webp
howItWorks:
  title: How Materialize Works
  steps:
    - title: Integrate data from disparate systems
      text: Point Materialize at your operational databases, event/queue systems, and services. Sources will appear as continually updating tables in Materialize with sub-second freshness.
    - title: Define views in SQL
      text: Create views that join, aggregate, and shape raw tables into canonical business objects. A common pattern is a medallion architecture that translates source tables from bronze (raw) to silver (intermediate) to gold (final) data products.
    - title: Index views to create data flows
      text: In a traditional database, you would index a table to speed up queries. In Materialize, you index the views themselves. When you do the Materialize optimizer creates dataflows, or computational graphs, that do the minimum amount of work as writes come in to keep views correctly and continually up to date. Now reactive, or pull based computation, becomes proactive and push based.
    - title: Strong consistency across the entire system
      text: Materializes uses virtual time to ensure all objects are coordinated from a single clock. The system moves from one consistent state to another, reflecting things like transaction boundaries in up stream systems, even when views that are hundreds of layers deep.
    - title: Agentic feedback loops are now possible
      text: Expose "gold" data products via MCP to give agents access to a semantic representation of your business. They can take the results of data products as-is, or use SQL to apply additional transformations on-the-fly. This lets them observe the world, think, and take action. Because Materialize can show how the results of those actions impact any other view in the system with sub-second latency, agents can now see the results of their own actions, quickly course correct, and take further actions to proceed toward their goal.
    - title: Make live data available across your entire stack
      text: Push all transformed updates to downstream system like Kafka and Apache Iceberg or subscribe to an interesting subset. You can also take a pull-based approach and query data from Materialize using standard Postgres drivers. While Materialize doesn't have the fastest query engine, because it can do so much work up front, the end-to-end latency for reflecting the result of updates is usually far better than even OLAP systems.
---

## The problem
Materialize turns live data streams into queryable, real-time results. That's hard to picture, and harder to sell if people can't picture it.

<figure>
  <video controls playsinline preload="metadata" poster="/work/materialize/site-hero-poster.webp" width="1920" height="1080" src="/work/materialize/site-hero-original.mp4" aria-label="Materialize homepage hero animation"></video>
  <figcaption>The hero animation on the live site.</figcaption>
</figure>

## What I built
- **Hero animation** introducing the platform
- **Scroll-driven animation** that follows data through the product as you read
- **Three system visualizations:** data ingestion, semantic modeling, and application data access

## Design decisions
- **Scroll-driven:** the explanation moves at the reader's pace, not a video's.
- **Lottie for performance:** vector animation instead of video keeps the page fast.
