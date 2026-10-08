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
        }),
      )
      .default([]),
    scroll: z
      .array(z.object({ src: z.string(), title: z.string(), text: z.string() }))
      .default([]),
  }),
});

export const collections = { work };
