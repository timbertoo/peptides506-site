"""Build one static, crawlable page per storefront product for peptides506.com.

Reads the product snapshot embedded in index.html (PUBLIC_CATALOG_HTML ->
<script id="app-data">), then writes:
  <out>/productos/<slug>/index.html   one page per product
  <out>/sitemap.xml, <out>/robots.txt
and patches index.html: adds `slug` to each storefront item (share links use
it), improves the home page <head> (lang, title, description, canonical, OG).

Items that already have a `slug` keep it, so renaming a product does not
change its URL. Only new items get a slug generated from name + variant.

Usage: python3 build_product_pages.py <deploy_dir>   (edits in place)
"""
import json, re, sys, os, html, datetime

SITE = 'https://peptides506.com'
OUT = sys.argv[1]
INDEX = os.path.join(OUT, 'index.html')

CAT_ES = {
    'Healing & Recovery': 'Recuperación y regeneración',
    'Weight Loss & Metabolic': 'Pérdida de peso y metabolismo',
    'Growth Hormone & Muscle': 'Hormona de crecimiento y músculo',
    'Longevity & Cellular Health': 'Longevidad y salud celular',
    'Sexual Health & Hormones': 'Salud sexual y hormonas',
    'Solvents & Supplies': 'Solventes y suministros',
}
# Spanish copy keyed by the public product name (several variants share one).
GLP1_ES = 'Péptido agonista triple de los receptores GLP-1/GIP/glucagón, estudiado en la pérdida de peso y la salud metabólica.'
DESC_ES = {
    'BPC-157': 'Péptido derivado de una proteína gástrica (Body Protection Compound), ampliamente estudiado en la regeneración de tejidos, la reparación de tendones y ligamentos y la salud intestinal.',
    'Cagrilintide': 'Análogo de amilina de acción prolongada, estudiado en el control del apetito y la pérdida de peso, a menudo combinado con un agonista de GLP-1.',
    'CJC-1295 without DAC': 'Análogo de GHRH (hormona liberadora de hormona de crecimiento) sin DAC, de acción corta, estudiado por estimular pulsos naturales de hormona de crecimiento.',
    'GHK-CU': 'Péptido de cobre (Copper Tripeptide-1) estudiado en la reparación de la piel, la cicatrización de heridas y sus efectos antienvejecimiento.',
    'Ipamorelin': 'Secretagogo selectivo de hormona de crecimiento (agonista del receptor de grelina) que estimula la liberación de GH con un efecto mínimo sobre el cortisol o el apetito.',
    'KPV': 'Tripéptido (lisina-prolina-valina), fragmento de la alfa-MSH, estudiado por sus efectos antiinflamatorios y en la salud intestinal.',
    'MOTS-c': 'Péptido de origen mitocondrial estudiado en la salud metabólica, el rendimiento físico y la longevidad.',
    'NAD+': 'Nicotinamida adenina dinucleótido, una coenzima central en la producción de energía celular, estudiada en el metabolismo y el envejecimiento.',
    'PT-141': 'Bremelanotida, péptido agonista de los receptores de melanocortina estudiado en la excitación y el deseo sexual.',
    'GLP-1': GLP1_ES,
    'GLP-1 (RT) – Agonista Triple': GLP1_ES,
    'SS-31': 'Péptido dirigido a la mitocondria (elamipretida), estudiado en la producción de energía celular y la reducción del estrés oxidativo.',
    'TB-500': 'Fragmento sintético de la Timosina Beta-4, estudiado en la reparación de tejidos, la flexibilidad y la reducción de la inflamación.',
    'Tesamorelin': 'Análogo de GHRH estudiado en la reducción de grasa visceral, además de sus efectos cognitivos y metabólicos.',
    'Tirzepatide': 'Péptido agonista dual de los receptores GLP-1/GIP, estudiado en el control de la glucosa y la pérdida de peso.',
    '5-AMINO-1MQ': 'Molécula pequeña que inhibe la enzima NNMT, estudiada en el metabolismo de las grasas y el control del peso.',
}

def slugify(name, variant):
    s = (name + ' ' + variant).lower().replace('+', ' plus ')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return re.sub(r'-+', '-', s)

def esc(s):
    return html.escape(str(s or ''), quote=True)

# ---------- read snapshot ----------
h = open(INDEX, encoding='utf-8').read()
i = h.index('PUBLIC_CATALOG_HTML'); s = h.index('"', i); e = h.index('";\n', i) + 1
cat = json.loads(h[s:e])
tag = '<script id="app-data" type="application/json">'
a = cat.index(tag) + len(tag); b = cat.index('</script>', a)
raw = cat[a:b]; data = json.loads(raw)
ser = lambda d: json.dumps(d, separators=(',', ':'), ensure_ascii=True)
assert ser(data) == raw, 'snapshot format changed'
settings = data['settings']
wa = re.sub(r'[^0-9]', '', settings.get('whatsapp') or '')
items = [it for it in data['items'] if it.get('id')]

# Keep existing slugs (stable URLs); generate only for items without one.
used = {it['slug'] for it in items if it.get('slug')}
for it in items:
    if it.get('slug'):
        continue
    sl = slugify(it['name'], it['variant'])
    base, n = sl, 2
    while sl in used:
        sl = f'{base}-{n}'; n += 1
    used.add(sl)
    it['slug'] = sl

today = datetime.date.today().isoformat()

CSS = """
:root{--bg:#F4F6F9;--surface:#FFFFFF;--ink:#0F172A;--ink-soft:#64748B;--ink-faint:#94A3B8;--accent:#002766;--accent-ink:#FFFFFF;--border:rgba(0,39,102,0.10);--cta:#F26B0F;--cta2:#D9530A;--good:#15803D;--good-soft:#DCFCE7;--bad:#B91C1C;--bad-soft:#FEE2E2;--warn:#92400E;--warn-soft:#FEF3C7;}
@media (prefers-color-scheme: dark){:root{--bg:#0B1220;--surface:#111A2E;--ink:#EAF0FB;--ink-soft:#A9B7D1;--ink-faint:#77869E;--accent:#5B8DEF;--accent-ink:#07142B;--border:#243357;--good:#4ADE80;--good-soft:rgba(74,222,128,.12);--bad:#F87171;--bad-soft:rgba(248,113,113,.12);--warn:#FBBF24;--warn-soft:rgba(251,191,36,.12);} .logo{filter:invert(1);}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:'Montserrat',ui-sans-serif,system-ui,-apple-system,sans-serif;line-height:1.55}
a{color:var(--accent)}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
header{background:var(--surface);border-bottom:1px solid var(--border)}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:72px}
.logo{height:52px;width:auto;display:block}
.top-link{font-weight:700;font-size:14px;text-decoration:none;white-space:nowrap}
@media (max-width:460px){.logo{height:40px}.top-link{font-size:13px}.wrap{padding:0 16px}h1{font-size:26px}}
.crumbs{font-size:13px;color:var(--ink-soft);margin:22px 0 14px}
.crumbs a{color:var(--ink-soft)}
.grid{display:grid;grid-template-columns:minmax(0,380px) minmax(0,1fr);gap:36px;align-items:start}
@media (max-width:760px){.grid{grid-template-columns:1fr;gap:20px}}
.img-box{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px;display:flex;justify-content:center}
.img-box img{max-width:100%;height:auto;max-height:340px;object-fit:contain}
.cat{font-size:12px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--ink-faint);margin:0}
h1{font-size:30px;line-height:1.2;margin:6px 0 10px}
.price{font-size:28px;font-weight:800;color:var(--accent);margin:4px 0 10px}
.price small{font-size:14px;font-weight:600;color:var(--ink-soft)}
.chip{display:inline-block;font-size:12px;font-weight:700;padding:4px 10px;border-radius:999px;text-transform:uppercase}
.chip.in{background:var(--good-soft);color:var(--good)}
.chip.out{background:var(--bad-soft);color:var(--bad)}
.gift{background:var(--warn-soft);color:var(--warn);border-radius:10px;padding:10px 14px;font-size:14px;font-weight:600;margin:14px 0}
.desc{font-size:16px;color:var(--ink-soft);margin:14px 0}
.btns{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 8px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:13px 20px;border-radius:12px;font-weight:700;font-size:15px;text-decoration:none;flex:1 1 200px}
.btn-buy{background:linear-gradient(135deg,var(--cta),var(--cta2));color:#fff}
.btn-wa{background:var(--surface);color:var(--accent);border:1px solid var(--border)}
.note{font-size:13px;color:var(--ink-faint);margin:6px 0 0}
table{width:100%;border-collapse:collapse;margin:28px 0 8px;background:var(--surface);border:1px solid var(--border);border-radius:12px;overflow:hidden}
td{padding:10px 14px;border-top:1px solid var(--border);font-size:14px;vertical-align:top}
tr:first-child td{border-top:0}
td:first-child{color:var(--ink-soft);width:40%}
h2{font-size:20px;margin:36px 0 12px}
.en{font-size:14px;color:var(--ink-soft);border-left:3px solid var(--border);padding-left:12px}
.others{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;padding:0;list-style:none;margin:0}
.others a{display:block;background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:10px 12px;text-decoration:none;font-weight:600;font-size:14px}
.others span{display:block;font-weight:500;color:var(--ink-soft);font-size:13px}
.disclaimer{background:var(--warn-soft);color:var(--warn);border-radius:10px;padding:12px 14px;font-size:13px;margin:32px 0}
footer{border-top:1px solid var(--border);margin-top:40px;padding:22px 0 40px;font-size:13px;color:var(--ink-soft)}
"""

def page(it):
    sl = it['slug']
    url = f'{SITE}/productos/{sl}/'
    full = f"{it['name']} {it['variant']}".strip()
    cat_en = it.get('category') or ''
    cat_es = CAT_ES.get(cat_en, cat_en)
    d_es = DESC_ES.get(it['name']) or it.get('descEs') or ''
    d_en = it.get('descEn') or ''
    img_rel = '/' + it['image'].lstrip('/') if it.get('image') else ''
    img_abs = SITE + img_rel if img_rel else f'{SITE}/product-images/logo.png'
    avail = bool(it.get('available')) and (it.get('stockQty') is None or it.get('stockQty') > 0)
    price = it.get('price')
    price_txt = f'${price:,.2f}' if isinstance(price, (int, float)) else ''
    title = f'{full} | Péptido de investigación | Peptides 506 Costa Rica'
    meta_desc = f'{full}: {d_es} Por vial, envío en Costa Rica. Pedidos por WhatsApp.'
    if len(meta_desc) > 300: meta_desc = meta_desc[:297].rsplit(' ', 1)[0] + '…'
    store_link = f'/#p-{it["id"]}'
    wa_link = ''
    from urllib.parse import quote
    if wa: wa_link = f'https://wa.me/{wa}?text=' + quote(f'Hola! Quiero información / pedir: {full}. ({url})')
    is_water = re.search(r'water|agua', it['name'], re.I)
    ld = {
        '@context': 'https://schema.org', '@type': 'Product',
        'name': full, 'sku': it.get('sku') or None, 'image': [img_abs],
        'description': d_es or d_en, 'category': cat_es,
        'brand': {'@type': 'Brand', 'name': 'Peptides 506'},
        'offers': {'@type': 'Offer', 'url': url, 'priceCurrency': 'USD', 'price': f'{price:.2f}' if price_txt else None,
                   'availability': 'https://schema.org/InStock' if avail else 'https://schema.org/OutOfStock',
                   'itemCondition': 'https://schema.org/NewCondition',
                   'seller': {'@type': 'Organization', 'name': 'Peptides 506'}},
    }
    ld['offers'] = {k: v for k, v in ld['offers'].items() if v is not None}
    ld = {k: v for k, v in ld.items() if v is not None}
    crumbs_ld = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Inicio', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Productos', 'item': SITE + '/productos/'},
        {'@type': 'ListItem', 'position': 3, 'name': full, 'item': url}]}
    ldj = lambda o: json.dumps(o, ensure_ascii=False).replace('</', '<\\/')
    rows = [('Producto', it['name']), ('Contenido del vial', it['variant']), ('Presentación', 'Vial individual'),
            ('Categoría', cat_es), ('SKU', it.get('sku')), ('Uso', 'Solo para investigación'),
            ('Consumo humano', 'No apto para consumo humano ni animal')]
    others = [o for o in items if o['id'] != it['id']]
    others.sort(key=lambda o: (o['name'].lower(), o['variant']))
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta_desc)}">
<link rel="canonical" href="{esc(url)}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="product">
<meta property="og:site_name" content="Peptides 506">
<meta property="og:locale" content="es_CR">
<meta property="og:title" content="{esc(full)} | Peptides 506">
<meta property="og:description" content="{esc(d_es or d_en)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(img_abs)}">
<meta property="og:image:alt" content="{esc(full)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/product-images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<script type="application/ld+json">{ldj(ld)}</script>
<script type="application/ld+json">{ldj(crumbs_ld)}</script>
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap">
  <a href="/" aria-label="Peptides 506 - inicio"><img class="logo" src="/product-images/logo.png" alt="Peptides 506" width="160" height="52"></a>
  <a class="top-link" href="/">Ver catálogo →</a>
</div></header>
<main class="wrap">
  <nav class="crumbs" aria-label="Ruta"><a href="/">Inicio</a> › <a href="/productos/">Productos</a> › {esc(full)}</nav>
  <div class="grid">
    <div class="img-box">{f'<img src="{esc(img_rel)}" alt="{esc(full)} - vial" width="340" height="340">' if img_rel else ''}</div>
    <div>
      <p class="cat">{esc(cat_es)}</p>
      <h1>{esc(full)}</h1>
      <div class="price">{esc(price_txt)} <small>USD por vial</small></div>
      <span class="chip {'in' if avail else 'out'}">{'Disponible' if avail else 'Agotado'}</span>
      {'' if is_water else '<div class="gift">🎁 Incluye 1 vial de Agua Bacteriostática gratis por cada vial de péptido.</div>'}
      <p class="desc">{esc(d_es)}</p>
      <div class="btns">
        <a class="btn btn-buy" href="{esc(store_link)}">Comprar en la tienda</a>
        {f'<a class="btn btn-wa" href="{esc(wa_link)}" target="_blank" rel="noopener">Consultar por WhatsApp</a>' if wa_link else ''}
      </div>
      <p class="note">Se vende por vial individual. Certificado de Análisis (COA) disponible bajo solicitud por WhatsApp.</p>
    </div>
  </div>
  <table><tbody>
    {''.join(f'<tr><td>{esc(k)}</td><td>{esc(v)}</td></tr>' for k, v in rows if v)}
  </tbody></table>
  {f'<h2>In English</h2><p class="en" lang="en"><strong>{esc(full)}</strong> — {esc(d_en)} Sold per single vial. For research use only.</p>' if d_en else ''}
  <div class="disclaimer">Producto exclusivamente para fines de investigación. No está destinado al consumo humano ni animal. Venta solo a mayores de 18 años.</div>
  <h2>Otros productos</h2>
  <ul class="others">
    {''.join(f'<li><a href="/productos/{esc(o["slug"])}/">{esc(o["name"])}<span>{esc(o["variant"])}</span></a></li>' for o in others)}
  </ul>
</main>
<footer><div class="wrap">© Peptides 506 · Costa Rica · <a href="/">peptides506.com</a>{f' · <a href="mailto:{esc(settings.get("orderEmail"))}">{esc(settings.get("orderEmail"))}</a>' if settings.get('orderEmail') else ''}</div></footer>
</body>
</html>
"""

def index_page():
    lis = ''.join(
        f'<li><a href="/productos/{esc(o["slug"])}/">{esc(o["name"])}<span>{esc(o["variant"])} · {CAT_ES.get(o.get("category"), o.get("category") or "")}</span></a></li>'
        for o in sorted(items, key=lambda o: (o['name'].lower(), o['variant'])))
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Productos | Péptidos de investigación | Peptides 506 Costa Rica</title>
<meta name="description" content="Catálogo de péptidos de investigación de Peptides 506 en Costa Rica: BPC-157, TB-500, Tirzepatide, CJC-1295, Ipamorelin y más. Venta por vial, pedidos por WhatsApp.">
<link rel="canonical" href="{SITE}/productos/">
<meta property="og:title" content="Productos | Peptides 506">
<meta property="og:url" content="{SITE}/productos/">
<meta property="og:image" content="{SITE}/product-images/hero-banner.jpg">
<link rel="icon" type="image/png" href="/product-images/favicon.png">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap">
  <a href="/" aria-label="Peptides 506 - inicio"><img class="logo" src="/product-images/logo.png" alt="Peptides 506" width="160" height="52"></a>
  <a class="top-link" href="/">Ir a la tienda →</a>
</div></header>
<main class="wrap">
  <nav class="crumbs"><a href="/">Inicio</a> › Productos</nav>
  <h1>Péptidos de investigación</h1>
  <p class="desc">Todos nuestros productos se venden por vial individual. Haz tu pedido en la tienda o por WhatsApp.</p>
  <ul class="others">{lis}</ul>
  <div class="disclaimer">Productos exclusivamente para fines de investigación. No destinados al consumo humano ni animal.</div>
</main>
<footer><div class="wrap">© Peptides 506 · Costa Rica · <a href="/">peptides506.com</a></div></footer>
</body>
</html>
"""

# ---------- write pages ----------
pdir = os.path.join(OUT, 'productos')
os.makedirs(pdir, exist_ok=True)
for it in items:
    d = os.path.join(pdir, it['slug']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(it))
open(os.path.join(pdir, 'index.html'), 'w', encoding='utf-8').write(index_page())

urls = [(SITE + '/', '1.0'), (SITE + '/productos/', '0.8')] + [(f'{SITE}/productos/{it["slug"]}/', '0.7') for it in items]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{u}</loc><lastmod>{today}</lastmod><priority>{p}</priority></url>\n' for u, p in urls) + '</urlset>\n'
open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')

# ---------- patch index.html: slugs in snapshot + home <head> ----------
cat = cat[:a] + ser(data) + cat[b:]
h = h[:s] + json.dumps(cat).replace('</script', '<\\/script') + h[e:]
if '<html lang="en">' in h[:200]:
    h = h.replace('<html lang="en">', '<html lang="es">', 1)
HOME_TITLE = '<title>Peptides 506 | Péptidos de investigación en Costa Rica</title>'
if '<title>Peptides 506</title>' in h[:2000]:
    home_meta = (HOME_TITLE +
        '\n<meta name="description" content="Péptidos de investigación en Costa Rica: BPC-157, TB-500, Tirzepatide, CJC-1295, Ipamorelin, GHK-CU y más. Venta por vial individual, pedidos por WhatsApp.">'
        f'\n<link rel="canonical" href="{SITE}/">'
        '\n<meta property="og:type" content="website">\n<meta property="og:site_name" content="Peptides 506">'
        '\n<meta property="og:title" content="Peptides 506 | Péptidos de investigación en Costa Rica">'
        '\n<meta property="og:description" content="Péptidos de investigación, listos para pedir por WhatsApp. Venta por vial individual.">'
        f'\n<meta property="og:url" content="{SITE}/">\n<meta property="og:image" content="{SITE}/product-images/hero-banner.jpg">')
    h = h.replace('<title>Peptides 506</title>', home_meta, 1)
open(INDEX, 'w', encoding='utf-8', newline='').write(h)
print('pages:', len(items))
for it in items: print(' ', f'/productos/{it["slug"]}/')
