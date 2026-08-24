# IPR 2.0 e o PAF 2027 — Encontro de Chefias

Deck de 18 slides (GPF/SFC/ANTAQ), publicado em
**https://antaq.github.io/apresentacao_ipr_paf/**

## Estrutura

- `index.html` — casca do deck: navegação, iframe com zoom e índice.
- `slide-01.html` — capa, escrita à mão (única com fundo escuro).
- `slide-02.html`..`slide-18.html` — gerados por `build_slides.py`.
- `zoom.js` — escala o slide de 1920×1080 para o viewport.
- `assets/` — logos da ANTAQ.

Para regerar os slides 02..18: `python3 build_slides.py`.

## Como republicar

O GitHub Pages serve o branch `gh-pages` (raiz). Depois de commitar em `main`:

    git push origin main && git push origin main:gh-pages
