import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const work = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './content/work' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    role: z.string(),
    year: z.number(),
    tools: z.array(z.string()),
    category: z.enum(['featured', 'ui-motion', 'product', 'motion', 'concept']),
    order: z.number(),
    cover: z.string().optional(),
    coverVideo: z.string().optional(), // 4:3 muted loop for the home card, played on hover; cover is its first frame
    // Live shader for the home card instead of a video: an ES module in /public, its export, and its basePath.
    coverShader: z.object({ module: z.string(), name: z.string(), basePath: z.string() }).optional(),
    draft: z.boolean().default(false),
    customPage: z.boolean().default(false), // has its own src/pages/work/<id>.astro; the entry only feeds the home card
    rive: z
      .array(
        z.object({
          src: z.string(),
          label: z.string(),
          caption: z.string().optional(),
          ratio: z.string().optional(),
          stateMachine: z.string().optional(),
          artboard: z.string().optional(),
          poster: z.string().optional(),
          wide: z.boolean().optional(),
          // Clickable areas (fractions of artboard width/height; r is a fraction of width), used
          // to show a pointer cursor. The runtime has no hit-test API, so these are measured.
          hotspots: z.array(z.object({ x: z.number(), y: z.number(), r: z.number() })).optional(),
          // Adds play/pause to a file that only has "play": the button's hotspot (fractions of the
          // artboard width/height), the state that means "playing", and the colors of the play icon.
          pause: z
            .object({
              state: z.string(),
              x: z.number(),
              y: z.number(),
              d: z.number(),
              fill: z.string(),
              icon: z.string(),
            })
            .optional(),
        }),
      )
      .default([]),
    howItWorks: z
      .object({
        label: z.string(),
        notes: z.array(z.object({ title: z.string(), text: z.string() })),
      })
      .optional(),
  }),
});

export const collections = { work };
