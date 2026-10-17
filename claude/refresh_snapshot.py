"""Refresh the storefront snapshot (first paint + overrides) from public_catalog() rows.
Usage: refresh_snapshot.py <index.html> <rows.json>"""
import json, re, sys
P, R = sys.argv[1], sys.argv[2]
rows = json.load(open(R, encoding='utf-8'))
h = open(P, encoding='utf-8').read()
i = h.index('PUBLIC_CATALOG_HTML'); s = h.index('"', i); e = h.index('";\n', i) + 1
c = json.loads(h[s:e]); tag = '<script id="app-data" type="application/json">'
a = c.index(tag) + len(tag); b = c.index('</script>', a)
data = json.loads(c[a:b]); ser = lambda d: json.dumps(d, separators=(',', ':'), ensure_ascii=True)
assert ser(data) == c[a:b]
old = {it['id']: it for it in data['items']}
def dose(l):
    l = re.sub(r'\s*\*+\s*\d+\s*vials?\s*$', '', l or '', flags=re.I)
    return re.sub(r'(\d)\s+(mg|ml|mcg|iu)\b', r'\1\2', l, flags=re.I).strip()
by_prod = {}
for r in rows:
    if r['variant_id'] in old and r['product_id'] not in by_prod: by_prod[r['product_id']] = old[r['variant_id']]
items = []
for r in rows:
    stock = max(0, int(float(r['stock'] or 0)))
    if stock <= 0: continue
    ov = old.get(r['variant_id']); base = ov or by_prod.get(r['product_id']) or {}
    it = {'id': r['variant_id'], 'name': base.get('name') or r['product_name'],
          'category': base.get('category') or r['category'] or 'Peptides', 'desc': '',
          'variant': ov['variant'] if ov else dose(r['variant_label']),
          'sku': r['sku'] or (ov or {}).get('sku') or '',
          'price': float(r['price_usd']), 'available': True, 'stockQty': stock,
          'descEs': base.get('descEs') or r.get('description_es') or r.get('description') or '',
          'descEn': base.get('descEn') or r.get('description') or ''}
    if base.get('internalName'): it['internalName'] = base['internalName']
    if base.get('image'): it['image'] = base['image']
    if ov and ov.get('slug'): it['slug'] = ov['slug']
    items.append(it)
    tag_ = 'UPDATED' if ov else 'NEW'
    print(f"{tag_:7} {it['name']} {it['variant']}  ${it['price']}  stock {stock}  img={it.get('image','-')}")
for k in old:
    if k not in {x['id'] for x in items}: print('REMOVED', old[k]['name'], old[k]['variant'])
data['items'] = items
c = c[:a] + ser(data) + c[b:]
h = h[:s] + json.dumps(c).replace('</script', '<\\/script') + h[e:]
open(P, 'w', encoding='utf-8', newline='').write(h)
