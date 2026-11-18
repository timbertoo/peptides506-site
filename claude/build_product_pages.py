"""Build one static, crawlable page per storefront product for peptides506.com.

Reads the product snapshot embedded in index.html (PUBLIC_CATALOG_HTML ->
<script id="app-data">), then writes:
  <out>/productos/<slug>/index.html   one page per product
  <out>/sitemap.xml, <out>/robots.txt
and patches index.html: adds `slug` to each storefront item (share links use
it), improves the home page <head> (lang, title, description, canonical, OG).

Items that already have a `slug` keep it, so renaming a product does not
change its URL. Only new items get a slug generated from name + variant.

Also writes one page per compound (/<compound>-costa-rica/, all strengths)
and per category (/peptidos-.../), with copy from seo_content.py.

Usage: python3 build_product_pages.py <deploy_dir>   (edits in place)
"""
import json, re, sys, os, html, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_content import COMPOUNDS, CATEGORIES, FAQ, EXTRA, HANDLING, MORE

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
    'CJC-1295 without DAC + IPA': 'Mezcla de CJC-1295 sin DAC e ipamorelin en un solo vial (5 mg + 5 mg), que combina un análogo de GHRH con un secretagogo de hormona de crecimiento.',
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
.lead{font-size:18px;color:var(--ink);margin:6px 0 14px;font-weight:500}
.prose p{font-size:16px;color:var(--ink-soft);margin:0 0 14px}
.studied{padding-left:20px;margin:0}.studied li{margin:4px 0}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px;padding:0;margin:0;list-style:none}
.cards a{display:flex;gap:12px;align-items:center;background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:12px;text-decoration:none;color:var(--ink)}
.cards img{width:64px;height:64px;object-fit:contain;flex:none}
.cards b{display:block;font-size:15px}.cards span{display:block;font-size:13px;color:var(--ink-soft)}
.cards .p{color:var(--accent);font-weight:700}
details{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:12px 14px;margin:8px 0}
summary{font-weight:700;cursor:pointer}
details p{margin:8px 0 0;color:var(--ink-soft)}
.catnav{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 0;padding:0;list-style:none}
.catnav a{display:inline-block;background:var(--surface);border:1px solid var(--border);border-radius:999px;padding:7px 14px;font-weight:600;font-size:14px;text-decoration:none}
footer{border-top:1px solid var(--border);margin-top:40px;padding:22px 0 40px;font-size:13px;color:var(--ink-soft)}
"""

def comp_of(it):
    return COMPOUNDS.get(it['name'])

def cat_of(it):
    return CATEGORIES.get(it.get('category') or '')

def crumb_mid(it):
    c, k = comp_of(it), cat_of(it)
    out = f'<a href="/{k["slug"]}/">{esc(k["h1"])}</a> › ' if k else '<a href="/productos/">Productos</a> › '
    if c: out += f'<a href="/{c["slug"]}/">{esc(it["name"])}</a> › '
    return out

def more_link(it):
    c = comp_of(it)
    return f'<p><a href="/{c["slug"]}/"><strong>Más sobre {esc(it["name"])}: qué es, investigación y todas las presentaciones →</strong></a></p>' if c else ''

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
  <nav class="crumbs" aria-label="Ruta"><a href="/">Inicio</a> › {crumb_mid(it)}{esc(full)}</nav>
  <div class="grid">
    <div class="img-box">{f'<img src="{esc(img_rel)}" alt="{esc(full)} - vial" width="340" height="340">' if img_rel else ''}</div>
    <div>
      <p class="cat">{esc(cat_es)}</p>
      <h1>{esc(full)}</h1>
      <div class="price">{esc(price_txt)} <small>USD por vial</small></div>
      <span class="chip {'in' if avail else 'out'}">{'Disponible' if avail else 'Agotado'}</span>
      {'' if is_water else '<div class="gift">🎁 Incluye 1 vial de Agua Bacteriostática gratis por cada vial de péptido.</div>'}
      <p class="desc">{esc(d_es)}</p>
      {more_link(it)}
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
<footer><div class="wrap">© Peptides 506 · Costa Rica · <a href="/">peptides506.com</a> · <a href="/sobre-nosotros/">Sobre nosotros</a> · <a href="/envios/">Envíos y pagos</a> · <a href="/contacto/">Contacto</a>{f' · <a href="mailto:{esc(settings.get("orderEmail"))}">{esc(settings.get("orderEmail"))}</a>' if settings.get('orderEmail') else ''}</div></footer>
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
  <h2>Categorías</h2>
  <ul class="catnav">{''.join(f'<li><a href="/{k["slug"]}/">{esc(k["h1"])}</a></li>' for n, k in CATEGORIES.items() if any(o.get('category') == n for o in items))}</ul>
  <h2>Compuestos</h2>
  <ul class="catnav">{''.join(f'<li><a href="/{c["slug"]}/">{esc(n)}</a></li>' for n, c in sorted(COMPOUNDS.items(), key=lambda x: x[0].lower()) if any(o['name'] == n for o in items))}</ul>
  <h2>Todas las presentaciones</h2>
  <ul class="others">{lis}</ul>
  <div class="disclaimer">Productos exclusivamente para fines de investigación. No destinados al consumo humano ni animal.</div>
</main>
<footer><div class="wrap">© Peptides 506 · Costa Rica · <a href="/">peptides506.com</a> · <a href="/sobre-nosotros/">Sobre nosotros</a> · <a href="/envios/">Envíos y pagos</a> · <a href="/contacto/">Contacto</a></div></footer>
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

def is_avail(o):
    return bool(o.get('available')) and (o.get('stockQty') is None or o.get('stockQty') > 0)

def price_of(o):
    if not is_avail(o): return None
    p = o.get('price')
    return p if isinstance(p, (int, float)) and p > 0 else None

def card(o, label=None):
    img = '/' + o['image'].lstrip('/') if o.get('image') else '/product-images/logo.png'
    p = price_of(o)
    return (f'<li><a href="/productos/{esc(o["slug"])}/"><img src="{esc(img)}" alt="{esc(o["name"])} {esc(o["variant"])}" loading="lazy" width="64" height="64">'
            f'<div><b>{esc(label or o["name"])}</b><span>{esc(o["variant"])}</span>'
            f'{f"<span class=p>${p:,.2f}</span>" if p else "<span>Agotado</span>"}</div></a></li>')

def shell(title, desc, url, img, crumbs, main, ld_list):
    ldj = lambda o: json.dumps(o, ensure_ascii=False).replace('</', '<\\/')
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(url)}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Peptides 506">
<meta property="og:locale" content="es_CR">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:image" content="{esc(img)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/product-images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{''.join(f'<script type="application/ld+json">{ldj(o)}</script>' for o in ld_list)}
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap">
  <a href="/" aria-label="Peptides 506 - inicio"><img class="logo" src="/product-images/logo.png" alt="Peptides 506" width="160" height="52"></a>
  <a class="top-link" href="/">Ver catálogo →</a>
</div></header>
<main class="wrap">
  <nav class="crumbs" aria-label="Ruta">{crumbs}</nav>
{main}
  <div class="disclaimer">Productos exclusivamente para fines de investigación en laboratorio. No destinados al consumo humano ni animal. Venta solo a mayores de 18 años.</div>
</main>
<footer><div class="wrap">© Peptides 506 · Costa Rica · <a href="/">peptides506.com</a> · <a href="/productos/">Todos los productos</a> · <a href="/sobre-nosotros/">Sobre nosotros</a> · <a href="/envios/">Envíos y pagos</a> · <a href="/contacto/">Contacto</a>{f' · <a href="mailto:{esc(settings.get("orderEmail"))}">{esc(settings.get("orderEmail"))}</a>' if settings.get('orderEmail') else ''}</div></footer>
</body>
</html>
'''

def crumbs_ld(pairs):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': n + 1, 'name': nm, 'item': u} for n, (nm, u) in enumerate(pairs)]}

def strength_key(o):
    m = re.match(r'([0-9.]+)', o.get('variant') or '')
    return float(m.group(1)) if m else 0

def compare_table(name, cat):
    rows = []
    for n, cc in COMPOUNDS.items():
        g = sorted([o for o in items if o['name'] == n and o.get('category') == cat], key=strength_key)
        if not g: continue
        mech = dict(EXTRA.get(n, {}).get('specs', [])).get('Mecanismo') or dict(EXTRA.get(n, {}).get('specs', [])).get('Tipo') or ''
        pr = [price_of(o) for o in g if price_of(o)]
        nm = esc(n) if n == name else f'<a href="/{cc["slug"]}/">{esc(n)}</a>'
        rows.append(f'<tr><td>{nm}</td><td>{esc(mech)}<br><span style="color:var(--ink-faint)">{esc(", ".join(o["variant"] for o in g))}{f" · desde ${min(pr):,.0f}" if pr else ""}</span></td></tr>')
    if len(rows) < 2: return ''
    k = CATEGORIES.get(cat)
    return f'<h2>Comparación: {esc(k["h1"].lower() if k else "compuestos relacionados")}</h2><table><tbody>' + ''.join(rows) + '</tbody></table>'

hub_urls = []
from urllib.parse import quote
for name, c in COMPOUNDS.items():
    vs = sorted([o for o in items if o['name'] == name], key=strength_key)
    if not vs: continue
    url = f'{SITE}/{c["slug"]}/'
    x = dict(EXTRA.get(name, {}), **MORE.get(name, {}))
    faqs = [(f'¿Qué es {name}?', c['lead'])] + x.get('faq', []) + FAQ
    k = cat_of(vs[0])
    prices = [price_of(o) for o in vs if price_of(o)]
    frm = f'desde ${min(prices):,.2f} por vial' if prices else ''
    img = SITE + '/' + vs[0]['image'].lstrip('/') if vs[0].get('image') else SITE + '/product-images/logo.png'
    strengths = ', '.join(o['variant'] for o in vs)
    desc = f'{c["lead"]} Presentaciones: {strengths}{", " + frm if frm else ""}. Envío en Costa Rica, pedidos por WhatsApp.'
    wa_link = f'https://wa.me/{wa}?text=' + quote(f'Hola! Quiero información sobre {name}. ({url})') if wa else ''
    pairs = [('Inicio', SITE + '/')] + ([(k['h1'], f'{SITE}/{k["slug"]}/')] if k else []) + [(name, url)]
    ld = [{'@context': 'https://schema.org', '@type': 'Product', 'name': name, 'image': [img], 'description': c['lead'],
           'brand': {'@type': 'Brand', 'name': 'Peptides 506'},
           **({'offers': {'@type': 'AggregateOffer', 'priceCurrency': 'USD', 'lowPrice': f'{min(prices):.2f}', 'highPrice': f'{max(prices):.2f}', 'offerCount': len(vs)}} if prices else {})},
          crumbs_ld(pairs),
          {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
              {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faqs]}]
    crumbs = '<a href="/">Inicio</a> › ' + (f'<a href="/{k["slug"]}/">{esc(k["h1"])}</a> › ' if k else '') + esc(name)
    related = [o for o in items if k and o.get('category') == vs[0].get('category') and o['name'] != name]
    seen, rel = set(), []
    for o in related:
        cc = COMPOUNDS.get(o['name'])
        if cc and cc['slug'] not in seen:
            seen.add(cc['slug']); rel.append((o['name'], cc['slug']))
    main = f'''  <div class="grid">
    <div class="img-box"><img src="{esc(img.replace(SITE, ''))}" alt="{esc(name)} - vial" width="340" height="340"></div>
    <div>
      {f'<p class="cat">{esc(k["h1"])}</p>' if k else ''}
      <h1>{esc(c["h1"])}</h1>
      <p class="lead">{esc(c["lead"])}</p>
      {f'<div class="price">{esc(frm.replace(" por vial", ""))} <small>USD por vial</small></div>' if frm else ''}
      {'<div class="gift">🎁 Incluye 1 vial de Agua Bacteriostática gratis por cada vial de péptido.</div>'}
      <div class="btns">
        <a class="btn btn-buy" href="#presentaciones">Ver presentaciones</a>
        {f'<a class="btn btn-wa" href="{esc(wa_link)}" target="_blank" rel="noopener">Consultar por WhatsApp</a>' if wa_link else ''}
      </div>
    </div>
  </div>
  <h2 id="presentaciones">Presentaciones disponibles</h2>
  <ul class="cards">{''.join(card(o) for o in vs)}</ul>
  <h2>¿Qué es {esc(name)}?</h2>
  <div class="prose">{''.join(f'<p>{esc(p)}</p>' for p in c["body"])}</div>
  {f'<h2>Ficha técnica</h2><table><tbody>' + ''.join(f'<tr><td>{esc(a)}</td><td>{esc(b)}</td></tr>' for a, b in x["specs"]) + '</tbody></table>' if x.get('specs') else ''}
  {f'<h2>Cómo funciona</h2><div class="prose"><p>{esc(x["how"])}</p></div>' if x.get('how') else ''}
  {f'<h2>Contexto</h2><div class="prose"><p>{esc(x["history"])}</p></div>' if x.get('history') else ''}
  <h2>Áreas de investigación</h2>
  <ul class="studied">{''.join(f'<li>{esc(i)}</li>' for i in c["studied"])}</ul>
  {f'<h2>Tipos de estudios</h2><ul class="studied">' + ''.join(f'<li><strong>{esc(a)}:</strong> {esc(b)}</li>' for a, b in x["research"]) + '</ul>' if x.get('research') else ''}
  {compare_table(name, vs[0].get('category'))}
  {f'<h2>Límites de la evidencia</h2><div class="prose"><p>{esc(x["limits"])}</p></div>' if x.get('limits') else ''}
  <h2>Presentación y manejo</h2>
  <ul class="studied">{''.join(f'<li>{esc(i)}</li>' for i in HANDLING)}</ul>
  <h2>Preguntas frecuentes</h2>
  {''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faqs[1:])}
  <h2>In English</h2>
  <p class="en" lang="en">{esc(c["en"])}</p>
  {f'<h2>Relacionados</h2><ul class="catnav">' + ''.join(f'<li><a href="/{sl}/">{esc(n)}</a></li>' for n, sl in rel) + '</ul>' if rel else ''}'''
    d = os.path.join(OUT, c['slug']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(
        shell(f'{name} en Costa Rica | {strengths} | Peptides 506', desc, url, img, crumbs, main, ld))
    hub_urls.append((url, '0.8'))

# ---------- info pages: about, shipping & payment, contact ----------
wa_pretty = f'+{wa[:3]} {wa[3:7]} {wa[7:]}' if len(wa) == 11 else f'+{wa}'
email = settings.get('orderEmail') or ''
org_ld = {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'Peptides 506', 'url': SITE + '/',
          'logo': SITE + '/product-images/logo.png', 'areaServed': 'CR',
          'contactPoint': {'@type': 'ContactPoint', 'contactType': 'customer service', 'telephone': wa_pretty.replace(' ', '-'),
                           **({'email': email} if email else {}), 'availableLanguage': ['Spanish', 'English'], 'areaServed': 'CR'}}
wa_btn = f'<a class="btn btn-buy" href="https://wa.me/{wa}" target="_blank" rel="noopener">Escríbenos por WhatsApp</a>' if wa else ''
mail_btn = f'<a class="btn btn-wa" href="mailto:{esc(email)}">{esc(email)}</a>' if email else ''
INFO = [
  ('sobre-nosotros', 'Sobre nosotros | Peptides 506 Costa Rica', 'Sobre nosotros',
   'Peptides 506 es un negocio costarricense que ofrece péptidos de investigación por vial individual, con COA disponible y atención directa por WhatsApp.',
   f'''  <h1>Sobre Peptides 506</h1>
  <p class="lead">Un negocio costarricense dedicado a ofrecer péptidos de investigación de forma clara, sencilla y con atención directa.</p>
  <div class="prose">
  <p>Peptides 506 nació para que investigadores en Costa Rica puedan acceder a péptidos de investigación sin tener que importarlos por su cuenta ni comprar kits completos. El 506 de nuestro nombre es el código telefónico del país: atendemos exclusivamente dentro de Costa Rica.</p>
  </div>
  <h2>Cómo trabajamos</h2>
  <ul class="studied">
    <li><strong>Venta por vial individual:</strong> compras solo lo que necesitas, sin kits de diez viales.</li>
    <li><strong>Agua bacteriostática incluida:</strong> un vial gratis por cada vial de péptido.</li>
    <li><strong>Certificado de Análisis (COA):</strong> disponible bajo solicitud para cada lote.</li>
    <li><strong>Información clara:</strong> cada producto tiene su propia página con ficha técnica y una descripción honesta de lo que la investigación muestra y lo que no.</li>
    <li><strong>Atención directa:</strong> respondemos personalmente por WhatsApp, en español o en inglés.</li>
  </ul>
  <h2>Solo para investigación</h2>
  <div class="prose"><p>Todos nuestros productos se ofrecen exclusivamente para fines de investigación en laboratorio. No son medicamentos, no están destinados al consumo humano ni animal, y no ofrecemos recomendaciones de uso ni de dosificación. La venta es solo para mayores de 18 años.</p></div>
  <h2>In English</h2>
  <p class="en" lang="en">Peptides 506 is a Costa Rican business offering research peptides by the single vial, with a free bacteriostatic water vial per peptide, COA on request and direct WhatsApp service in Spanish or English. We serve Costa Rica only. For research use only.</p>
  <div class="btns">{wa_btn}{mail_btn}</div>''', [org_ld]),
  ('envios', 'Envíos y formas de pago | Peptides 506 Costa Rica', 'Envíos y pagos',
   'Enviamos a todo Costa Rica por servicio de mensajería. Pagos por SINPE Móvil, transferencia bancaria o efectivo contra entrega. Costo de envío según la zona.',
   f'''  <h1>Envíos y formas de pago</h1>
  <p class="lead">Enviamos a todo Costa Rica por servicio de mensajería.</p>
  <h2>Cobertura</h2>
  <div class="prose"><p>Hacemos entregas en las siete provincias del país: San José, Alajuela, Cartago, Heredia, Guanacaste, Puntarenas y Limón. No realizamos envíos fuera de Costa Rica.</p></div>
  <h2>Costo de envío</h2>
  <div class="prose"><p>El costo depende de la zona de entrega. Te lo confirmamos por WhatsApp junto con el total de tu pedido, antes de que pagues.</p></div>
  <h2>Tiempo de entrega</h2>
  <div class="prose"><p>El tiempo de entrega varía según la zona y la disponibilidad del servicio de mensajería. Te confirmamos la fecha estimada al momento de coordinar tu pedido.</p></div>
  <h2>Formas de pago</h2>
  <ul class="studied">
    <li><strong>SINPE Móvil</strong></li>
    <li><strong>Transferencia bancaria</strong></li>
    <li><strong>Efectivo contra entrega</strong></li>
  </ul>
  <h2>Cómo hacer un pedido</h2>
  <ul class="studied">
    <li>Elige tus productos en la <a href="/">tienda</a> y agrégalos al carrito, o escríbenos directamente.</li>
    <li>Completa tus datos de contacto y la dirección de entrega.</li>
    <li>Confirma el pedido por WhatsApp. Te indicamos el costo de envío, el total y la fecha estimada.</li>
    <li>Realiza el pago por el medio que prefieras y coordinamos la entrega.</li>
  </ul>
  <h2>¿Algún problema con tu pedido?</h2>
  <div class="prose"><p>Si tu pedido llega incompleto o con algún problema, escríbenos por WhatsApp con tu nombre y una foto del paquete, y lo resolvemos contigo.</p></div>
  <h2>In English</h2>
  <p class="en" lang="en">We ship anywhere in Costa Rica by courier (Costa Rica only). Shipping cost depends on the area and is confirmed on WhatsApp before you pay, along with the estimated delivery date. Payment by SINPE Móvil, bank transfer or cash on delivery.</p>
  <div class="btns">{wa_btn}</div>''', [org_ld]),
  ('contacto', 'Contacto | Peptides 506 Costa Rica', 'Contacto',
   f'Contacta a Peptides 506 por WhatsApp {wa_pretty} o por correo{" " + email if email else ""}. Atención en español e inglés, pedidos en todo Costa Rica.',
   f'''  <h1>Contacto</h1>
  <p class="lead">La forma más rápida de comunicarte con nosotros es por WhatsApp.</p>
  <table><tbody>
    {f'<tr><td>WhatsApp</td><td><a href="https://wa.me/{wa}" target="_blank" rel="noopener">{esc(wa_pretty)}</a></td></tr>' if wa else ''}
    {f'<tr><td>Correo</td><td><a href="mailto:{esc(email)}">{esc(email)}</a></td></tr>' if email else ''}
    <tr><td>Sitio web</td><td><a href="/">peptides506.com</a></td></tr>
    <tr><td>Cobertura</td><td>Todo Costa Rica</td></tr>
    <tr><td>Idiomas</td><td>Español e inglés</td></tr>
  </tbody></table>
  <h2>¿En qué te podemos ayudar?</h2>
  <ul class="studied">
    <li>Hacer o confirmar un pedido.</li>
    <li>Consultar disponibilidad y precios.</li>
    <li>Solicitar el Certificado de Análisis (COA) de un lote.</li>
    <li>Conocer el costo y el tiempo de envío a tu zona.</li>
  </ul>
  <div class="prose"><p>No ofrecemos asesoría médica ni recomendaciones de uso o dosificación. Nuestros productos son exclusivamente para fines de investigación.</p></div>
  <h2>In English</h2>
  <p class="en" lang="en">Reach us on WhatsApp ({esc(wa_pretty)}){f" or by email at {esc(email)}" if email else ""}. We answer in Spanish or English and deliver anywhere in Costa Rica.</p>
  <div class="btns">{wa_btn}{mail_btn}</div>''', [org_ld]),
]
for slug, title, crumb, desc, main, ld in INFO:
    url = f'{SITE}/{slug}/'
    d = os.path.join(OUT, slug); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(
        shell(title, desc, url, f'{SITE}/product-images/hero-banner.jpg', f'<a href="/">Inicio</a> › {esc(crumb)}', main,
              ld + [crumbs_ld([('Inicio', SITE + '/'), (crumb, url)])]))
    hub_urls.append((url, '0.5'))

for cname, k in CATEGORIES.items():
    vs = [o for o in items if o.get('category') == cname]
    if not vs: continue
    url = f'{SITE}/{k["slug"]}/'
    names = []
    for o in vs:
        if o['name'] not in names: names.append(o['name'])
    comp_cards = ''
    for n in names:
        group = sorted([o for o in vs if o['name'] == n], key=strength_key)
        cc = COMPOUNDS.get(n)
        img = '/' + group[0]['image'].lstrip('/') if group[0].get('image') else '/product-images/logo.png'
        prices = [price_of(o) for o in group if price_of(o)]
        href = f'/{cc["slug"]}/' if cc else f'/productos/{group[0]["slug"]}/'
        comp_cards += (f'<li><a href="{href}"><img src="{esc(img)}" alt="{esc(n)}" loading="lazy" width="64" height="64">'
                       f'<div><b>{esc(n)}</b><span>{esc(", ".join(o["variant"] for o in group))}</span>'
                       f'{f"<span class=p>desde ${min(prices):,.2f}</span>" if prices else ""}</div></a></li>')
    others = ''.join(f'<li><a href="/{kk["slug"]}/">{esc(kk["h1"])}</a></li>' for nn, kk in CATEGORIES.items() if nn != cname and any(o.get('category') == nn for o in items))
    main = f'''  <h1>{esc(k["h1"])}</h1>
  <div class="prose">{''.join(f'<p>{esc(p)}</p>' for p in k["body"])}</div>
  <ul class="cards">{comp_cards}</ul>
  <p class="en" lang="en" style="margin-top:24px">{esc(k["en"])}</p>
  <h2>Otras categorías</h2>
  <ul class="catnav">{others}</ul>'''
    desc = f'{k["body"][0][:220].rsplit(" ", 1)[0]}… Venta por vial, envío en Costa Rica.'
    ld = [crumbs_ld([('Inicio', SITE + '/'), (k['h1'], url)]),
          {'@context': 'https://schema.org', '@type': 'ItemList', 'itemListElement': [
              {'@type': 'ListItem', 'position': n + 1, 'name': nm, 'url': f'{SITE}/{COMPOUNDS[nm]["slug"]}/'} for n, nm in enumerate([x for x in names if x in COMPOUNDS])]}]
    d = os.path.join(OUT, k['slug']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(
        shell(f'{k["title"]} | Peptides 506', desc, url, f'{SITE}/product-images/hero-banner.jpg',
              f'<a href="/">Inicio</a> › {esc(k["h1"])}', main, ld))
    hub_urls.append((url, '0.8'))

urls = [(SITE + '/', '1.0'), (SITE + '/productos/', '0.8')] + hub_urls + [(f'{SITE}/productos/{it["slug"]}/', '0.7') for it in items]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{u}</loc><lastmod>{today}</lastmod><priority>{p}</priority></url>\n' for u, p in urls) + '</urlset>\n'
open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write(sm)
open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')

# ---------- home page: plain-HTML content inside #app-root ----------
# Shown to anything that reads the raw page (Google, ad tools, link previews,
# visitors without JavaScript). The app replaces #app-root with the live
# catalog as soon as its script runs, so regular visitors see the same
# catalog as before. Rebuilt between the two markers on every run.
def home_block():
    cats = [(n, k) for n, k in CATEGORIES.items() if any(o.get('category') == n for o in items)]
    sec = ''
    for n, k in cats:
        lis = ''
        for cname, c in COMPOUNDS.items():
            vs = [o for o in items if o['name'] == cname and o.get('category') == n]
            if not vs: continue
            pr = [price_of(o) for o in vs if price_of(o)]
            lis += (f'<li><a href="/{c["slug"]}/">{esc(cname)}</a> <span>{esc(", ".join(o["variant"] for o in sorted(vs, key=strength_key)))}'
                    f'{f" · desde ${min(pr):,.0f}" if pr else ""}</span></li>')
        sec += f'<section><h2><a href="/{k["slug"]}/">{esc(k["h1"])}</a></h2><p>{esc(k["body"][0])}</p><ul>{lis}</ul></section>'
    faq = ''.join(f'<h3>{esc(q)}</h3><p>{esc(a)}</p>' for q, a in FAQ)
    wa_txt = f'<a href="https://wa.me/{wa}">WhatsApp +{wa}</a>' if wa else 'WhatsApp'
    email = settings.get('orderEmail') or ''
    return f"""<!--seo-home-start-->
<style>.p5h{{font-family:Montserrat,system-ui,sans-serif;max-width:960px;margin:0 auto;padding:20px;color:#0F172A;line-height:1.55;zoom:1.25}}.p5h a{{color:#002766}}.p5h h1{{font-size:30px;line-height:1.2}}.p5h h2{{font-size:21px;margin:28px 0 6px}}.p5h h3{{font-size:16px;margin:14px 0 2px}}.p5h ul{{padding-left:20px}}.p5h li span{{color:#64748B}}.p5h .note{{background:#FEF3C7;color:#92400E;border-radius:10px;padding:12px 14px;font-size:14px}}.p5h h1,.p5h h2,.p5h h3{{font-family:inherit}}</style>
<div class="p5h">
<p><a href="/"><img src="/product-images/logo.png" alt="Peptides 506" width="160" height="52"></a></p>
<h1>Peptides 506: péptidos de investigación en Costa Rica</h1>
<p>Catálogo de péptidos de investigación con venta por vial individual y envío dentro de Costa Rica. Haz tu pedido en la tienda o directamente por WhatsApp; coordinamos el pago y la entrega contigo.</p>
<ul>
<li><strong>Venta por vial:</strong> no necesitas comprar kits completos.</li>
<li><strong>Agua bacteriostática gratis:</strong> un vial incluido por cada vial de péptido.</li>
<li><strong>Certificado de Análisis (COA):</strong> disponible bajo solicitud para cada lote.</li>
</ul>
<p><a href="/productos/">Ver todos los productos</a> · <a href="/sobre-nosotros/">Sobre nosotros</a> · <a href="/envios/">Envíos y pagos</a> · <a href="/contacto/">Contacto</a> · {wa_txt}{f' · <a href="mailto:{esc(email)}">{esc(email)}</a>' if email else ''}</p>
{sec}
<h2>Cómo hacer un pedido</h2>
<p>1) Elige tus productos y agrégalos al carrito. 2) Completa tus datos de contacto y envío. 3) Confirma el pedido por WhatsApp; te escribimos para coordinar el pago y la entrega.</p>
<h2>Preguntas frecuentes</h2>
{faq}
<h2>In English</h2>
<p lang="en">Peptides 506 is a research-peptide catalog in Costa Rica: sold per single vial, a free bacteriostatic water vial with every peptide, COA on request, ordering by WhatsApp. Categories: weight loss and metabolic, recovery and repair, growth hormone, longevity and cellular health. For research use only.</p>
<p class="note">Productos exclusivamente para fines de investigación en laboratorio. No destinados al consumo humano ni animal. Venta solo a mayores de 18 años.</p>
</div>
<script>/* JS is on: the live catalog takes over in a moment, so skip the text-only flash. */document.currentScript.previousElementSibling.style.display='none';</script>
<!--seo-home-end-->"""

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
hb = home_block()
if '<!--seo-home-start-->' in h:
    x = h.index('<!--seo-home-start-->'); y = h.index('<!--seo-home-end-->') + len('<!--seo-home-end-->')
    h = h[:x] + hb + h[y:]
else:
    assert h.count('<div id="app-root"></div>') == 1
    h = h.replace('<div id="app-root"></div>', '<div id="app-root">' + hb + '</div>', 1)
open(INDEX, 'w', encoding='utf-8', newline='').write(h)
print('pages:', len(items))
for it in items: print(' ', f'/productos/{it["slug"]}/')
