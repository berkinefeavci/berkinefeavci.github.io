# Berkin Efe Avcı — Portfolio

Architecture, software and visual production. A bilingual personal portfolio with 14 projects across four disciplines.

**[View portfolio](https://berkinefeavci.github.io)** · **[English](https://berkinefeavci.github.io/en/)** · **[GitHub profile](https://github.com/berkinefeavci)**

## Contents

- Applications: Healthy Battery, SayWords, PanelLight, Portside, Sticker Studio, Flower.
- Web / automation: Kaptan Yangın, TURK-ISHI CAMP, Thrust Rush, AVCI Operasyon, Perde.
- Architecture: Volleyball Hall and Kaptan Yangın Building concept studies.
- Visual work: Rüya Postası, an AI-assisted surreal Istanbul series.

Each project describes its scope and stage. Private application source code and customer data are not included. Architectural concepts are labelled as unbuilt; AI-assisted imagery is identified.

## Maintain

No npm packages or build service required. Python 3 generates static Turkish and English pages from `projects.json`:

```sh
python3 build.py
python3 check.py
```

`style.css` defines the responsive layout. `app.js` progressively adds category filtering and project deep links. Content and native expandable details work without JavaScript. Commit the regenerated `index.html` and `en/index.html` after content changes.

GitHub Pages publishes the root of `main`. `sitemap.xml`, language alternates, canonical URLs, social metadata and a 404 page are included.

## Assets

Project screenshots and existing product identity images belong to their respective projects. The volleyball image is an AI-assisted architectural visualisation with illustrative context. Rüya Postası is AI-assisted artwork. Publication here does not grant a reuse licence to artwork, screenshots or project identities.
