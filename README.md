# peptides506.com

Public storefront for Peptides 506, hosted on Netlify (project `peptides506.com`).

- `site/` — everything that gets published (index.html, product photos, /productos/ SEO pages, sitemap.xml, robots.txt).
- `claude/` — helper scripts, not published:
  - `refresh_snapshot.py <site/index.html> <rows.json>` — refresh the built-in product snapshot from `public_catalog_v2()` rows.
  - `build_product_pages.py site` — rebuild /productos/ pages, sitemap.xml and robots.txt. Existing slugs are kept so URLs don't change.

Prices, stock and published products load live from Supabase, so those changes need no deploy.
Photos, new SEO pages and snapshot changes are committed here; Netlify deploys every push to `main`.
