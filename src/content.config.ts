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
    draft: z.boolean().default(false),
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
    scroll: z
      .array(z.object({ src: z.string(), title: z.string(), text: z.string() }))
      .default([]),
  }),
});

export const collections = { work };
