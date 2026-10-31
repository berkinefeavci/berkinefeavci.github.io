"""Check generated pages, local links, content and publication boundaries."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
projects = json.loads((ROOT / 'projects.json').read_text())
assert len({p['id'] for p in projects}) == len(projects) == 14
assert {p['category'] for p in projects} == {'apps', 'web', 'architecture', 'visual'}
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.links=[]; self.categories=[]; self.lang=None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'html': self.lang=a.get('lang')
        if 'data-category' in a: self.categories.append(a['data-category'])
        if tag in ('a','link','img','script'):
            value=a.get('href',a.get('src'))
            if value: self.links.append(value)
        if tag=='img': assert a.get('alt'), 'Missing image alt text'
for path,lang in [(ROOT/'index.html','tr'),(ROOT/'en/index.html','en')]:
    text=path.read_text(); page=Page(); page.feed(text)
    assert page.lang==lang
    assert len(page.ids)==len(set(page.ids)), 'Duplicate IDs'
    assert len(page.categories)==14
    for p in projects:
        assert p['id'] in page.ids
        assert len(p['description'])==len(p['detail'])==len(p['status'])==2
    for link in page.links:
        parsed=urlsplit(link)
        if parsed.scheme or parsed.netloc: continue
        if not parsed.path:
            assert parsed.fragment in page.ids, link
        else:
            target=(path.parent/parsed.path).resolve()
            assert target.is_relative_to(ROOT), link
            assert target.exists(), link
    for forbidden in ['/Users/','localhost','127.0.0.1','sslip.io','teyit edilmedi','Coming soon']:
        assert forbidden not in text, forbidden
assert not list(ROOT.rglob('.env*'))
print('PASS: 28 project cards, 2 languages, 4 categories, local links, image alt text and publication boundaries.')
