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
    category: z.enum(['featured', 'product', 'motion', 'systems']),
    order: z.number(),
  }),
});

export const collections = { work };
