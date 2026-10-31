"""Build the bilingual portfolio using Python's standard library only."""
import json
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parent
URL = 'https://berkinefeavci.github.io'
PROJECTS = json.loads((ROOT / 'projects.json').read_text())
CATEGORIES = {'apps': ['Uygulamalar', 'Applications'], 'web': ['Web / otomasyon', 'Web / automation'], 'architecture': ['Mimarlık', 'Architecture'], 'visual': ['Görsel işler', 'Visual work']}
COPY = [
 dict(lang='tr', title='Mimarlık, yazılım ve görsel işler', work='Çalışmalar', about='Hakkımda', contact='İletişim', discipline='MİMARLIK / YAZILIM / GÖRSEL ÜRETİM', lead='Mekânlar, uygulamalar<br>ve görsel dünyalar.', intro='Farklı alanlar, aynı merak: bir fikrin nasıl çalıştığını görmek.', explore='Çalışmaları keşfet', selected='Seçilmiş çalışmalar', all='Tümü', projects='proje', detail='Projeyi incele', scope='Çalışma kapsamı', site='Siteyi aç', image='Görseli büyüt', about_title='Fikirden, kullanılabilen<br>bir şeye.', about_body='Ben Berkin Efe Avcı. Mimarlık, yazılım ve görsel üretim arasında çalışıyorum. Günlük bir ihtiyacı uygulamaya, bir mekân fikrini tasarıma, bir görüntüyü hikâyeye dönüştürüyorum.', method='Yapay zekâyı araştırma, geliştirme ve üretim süreçlerimde kullanıyorum. Bu seçkide yayınlanmış ürünler, kişisel araçlar ve devam eden tasarımlar birlikte yer alıyor; her projenin aşamasını kendi kartında görebilirsin.', talk='Bir fikirden<br>konuşalım.', email='E-posta gönder', note='Kişisel portfolyo · 2026', skip='İçeriğe geç', hero_caption='Rüya Postası / Bulut Feneri', hero_note='AI destekli görsel seri', archive='Proje dizini', updated='Son güncelleme: 31 Ekim 2026', top='Başa dön'),
 dict(lang='en', title='Architecture, software and visual work', work='Work', about='About', contact='Contact', discipline='ARCHITECTURE / SOFTWARE / VISUAL PRODUCTION', lead='Spaces, applications<br>and visual worlds.', intro='Different disciplines, the same curiosity: seeing an idea come to life.', explore='Explore the work', selected='Selected work', all='All', projects='projects', detail='Explore project', scope='Scope of work', site='Visit website', image='View full image', about_title='From an idea to<br>something you can use.', about_body="I'm Berkin Efe Avcı. I work across architecture, software and visual production, turning everyday needs into applications, spatial ideas into designs, and images into stories.", method='AI is part of my research, development and production process. This collection brings together published products, personal tools and designs in progress. Each project is labelled with its stage.', talk="Let's talk<br>about an idea.", email='Send an email', note='Personal portfolio · 2026', skip='Skip to content', hero_caption='Rüya Postası / Cloud Lighthouse', hero_note='AI-assisted visual series', archive='Project index', updated='Last updated: 31 October 2026', top='Back to top')
]

def render(i):
    c = COPY[i]
    base = '../' if i else './'
    canonical = URL + ('/en/' if i else '/')
    cards = []
    for n, p in enumerate(PROJECTS, 1):
        name = p.get('enName', p['name']) if i else p['name']
        cat = CATEGORIES[p['category']][i]
        if p.get('image'):
            src = base + 'assets/' + p['image']
            media = f'<figure><a class="project-image" href="{src}" target="_blank" rel="noopener" aria-label="{e(name)} — {c["image"]}"><img src="{src}" alt="{e(name)} — {e(p["caption"][i])}" loading="lazy" width="1200" height="800"></a><figcaption>{e(p["caption"][i])}</figcaption></figure>'
        else:
            media = ''
        links = ''
        if p.get('site'):
            links += f'<a href="{e(p["site"])}" target="_blank" rel="noopener">{c["site"]} <span aria-hidden="true">↗</span></a>'
        if p.get('repo'):
            links += f'<a href="https://github.com/berkinefeavci/{e(p["repo"])}" target="_blank" rel="noopener">GitHub <span aria-hidden="true">↗</span></a>'
        cards.append(f'''<article class="project {'text-project' if not media else ''}" id="{p['id']}" data-category="{p['category']}">
{media}<div class="project-body"><div class="project-meta"><span>{n:02d} / {cat}</span><span>{e(p['status'][i])}</span></div>
<h3>{e(name)}</h3><p class="description">{e(p['description'][i])}</p>
<details><summary>{c['detail']}<span aria-hidden="true">+</span></summary><div class="project-detail"><h4>{c['scope']}</h4><p>{e(p['detail'][i])}</p><p class="tools">{e(p['tools'])}</p><div class="project-links">{links}<a href="#{p['id']}" aria-label="{e(name)} permalink"># {e(name)}</a></div></div></details></div></article>''')
    filters = f'<button type="button" data-filter="all" aria-pressed="true">{c["all"]}<sup>{len(PROJECTS):02d}</sup></button>'
    for cat, labels in CATEGORIES.items():
        count = sum(p['category'] == cat for p in PROJECTS)
        filters += f'<button type="button" data-filter="{cat}" aria-pressed="false">{labels[i]}<sup>{count:02d}</sup></button>'
    profile = {'@context': 'https://schema.org', '@type': 'Person', 'name': 'Berkin Efe Avcı', 'url': URL, 'sameAs': ['https://github.com/berkinefeavci']}
    page = f'''<!doctype html>
<html lang="{c['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Berkin Efe Avcı — {c['title']}</title><meta name="description" content="{e(c['about_body'])}"><meta name="theme-color" content="#f3f0e8">
<link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="tr" href="{URL}/"><link rel="alternate" hreflang="en" href="{URL}/en/"><link rel="alternate" hreflang="x-default" href="{URL}/">
<meta property="og:type" content="website"><meta property="og:title" content="Berkin Efe Avcı — {c['title']}"><meta property="og:description" content="{e(c['intro'])}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{URL}/assets/volleyball.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{base}style.css"><script src="{base}app.js" defer></script><script type="application/ld+json">{json.dumps(profile, ensure_ascii=False)}</script></head>
<body><a class="skip" href="#main">{c['skip']}</a>
<header id="top"><a class="wordmark" href="{base}" aria-label="Berkin Efe Avcı">BEA<span>.</span></a><nav aria-label="{'Ana menü' if i == 0 else 'Main navigation'}"><a href="#work">{c['work']}</a><a href="#about">{c['about']}</a><a href="#contact">{c['contact']}</a></nav><div class="languages"><a href="{base}" lang="tr" {'aria-current="page"' if i == 0 else ''}>TR</a><span>/</span><a href="{base}en/" lang="en" {'aria-current="page"' if i == 1 else ''}>EN</a></div></header>
<main id="main"><section class="hero" aria-labelledby="name"><div class="hero-copy"><p class="eyebrow">{c['discipline']}</p><h1 id="name">Berkin Efe<br><span>Avcı</span><span class="name-dot">.</span></h1><div class="hero-bottom"><h2>{c['lead']}</h2><a class="round-link" href="#work" aria-label="{c['explore']}">↓</a></div><p class="hero-intro">{c['intro']}</p></div><figure class="hero-art"><a href="#ruya-postasi" aria-label="Rüya Postası"><img src="{base}assets/ruya-postasi.jpg" alt="{'Bulutların üzerindeki Galata Kulesi ve vapur; AI destekli sürreal İstanbul görseli' if i == 0 else 'Galata Tower and a ferry above the clouds; an AI-assisted surreal Istanbul image'}" width="3328" height="4992" fetchpriority="high"></a><figcaption><span>{c['hero_caption']}</span><span>{c['hero_note']}</span></figcaption></figure></section>
<section id="work" aria-labelledby="work-title"><div class="section-heading"><p class="eyebrow">01 / {c['archive']}</p><h2 id="work-title">{c['selected']}<sup>14</sup></h2></div><div class="filter-bar"><div class="filters" aria-label="{'Proje kategorileri' if i == 0 else 'Project categories'}" hidden>{filters}</div><p id="result-count" aria-live="polite">14 {c['projects']}</p></div><div class="project-grid">{''.join(cards)}</div></section>
<section class="about" id="about"><p class="eyebrow">02 / {c['about']}</p><div class="about-grid"><h2>{c['about_title']}</h2><div><p class="about-lead">{e(c['about_body'])}</p><p>{e(c['method'])}</p><div class="disciplines"><span>{CATEGORIES['architecture'][i]}</span><span>{'Ürün geliştirme' if i == 0 else 'Product development'}</span><span>{'Görsel üretim' if i == 0 else 'Visual production'}</span></div></div></div></section>
</main><footer id="contact"><p class="eyebrow">03 / {c['contact']}</p><div class="contact-grid"><h2>{c['talk']}</h2><div class="contact-links"><a href="mailto:berkin.mimar@gmail.com">{c['email']} ↗<small>berkin.mimar@gmail.com</small></a><a href="https://github.com/berkinefeavci" target="_blank" rel="noopener">GitHub ↗<small>@berkinefeavci</small></a></div></div><div class="footer-bottom"><span>© Berkin Efe Avcı · {c['note']}</span><span>{c['updated']}</span><a href="#top">{c['top']} ↑</a></div></footer></body></html>'''
    out = ROOT / ('en/index.html' if i else 'index.html')
    out.parent.mkdir(exist_ok=True)
    out.write_text(page)

if __name__ == '__main__':
    for i in range(2):
        render(i)
    (ROOT / '.nojekyll').touch()
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {URL}/sitemap.xml\n')
    (ROOT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{URL}/</loc></url><url><loc>{URL}/en/</loc></url></urlset>')
    (ROOT / '404.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found — Berkin Efe Avcı</title><body style="font:20px system-ui;max-width:700px;margin:80px auto;padding:24px"><h1>404 — Page not found</h1><p>Sayfa bulunamadı.</p><a href="/">Portfolyoya dön / Back to portfolio</a></body></html>')
    print(f'Built 2 languages, {len(PROJECTS)} projects each.')
