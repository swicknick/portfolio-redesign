import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

// Every public page, for search engines. Drafts stay out.
export const GET: APIRoute = async ({ site }) => {
  const work = await getCollection('work', (w) => !w.data.draft);
  const paths = ['/', '/reel/', '/about/', '/contact/', ...work.map((w) => `/work/${w.id}/`)];
  const urls = paths.map((p) => `  <url><loc>${new URL(p, site)}</loc></url>`).join('\n');
  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`,
    { headers: { 'Content-Type': 'application/xml' } },
  );
};
