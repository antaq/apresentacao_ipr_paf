# IPR 2.0 e o PAF 2027 — Encontro de Chefias

Deck de 19 slides (GPF/SFC/ANTAQ), publicado em
**https://antaq.github.io/apresentacao_ipr_paf/**

## Estrutura

- `index.html` — casca do deck: navegação, iframe com zoom e índice.
- `slide-01.html` e `slide-19.html` — capa e encerramento, escritos à mão (os dois com fundo escuro).
  A capa está fora de `SLIDES`; o encerramento entra com `raw=True` — declarado para contar
  no total e no índice, e **não** regerado. Sem essa linha o gerador sobrescreve o arquivo.
- `slide-02.html`..`slide-18.html` — gerados por `build_slides.py`.
- `zoom.js` — escala o slide de 1920×1080 para o viewport.
- `assets/` — logos da ANTAQ.

Para regerar os slides 02..18: `python3 build_slides.py`.

O `.slide` é `overflow:hidden` — conteúdo que não cabe some sem aviso. Depois de mexer
no conteúdo, conferir com screenshot headless:

    google-chrome --headless --screenshot=/tmp/s.png --window-size=1920,1080 slide-NN.html

## Como republicar

O GitHub Pages serve o branch `gh-pages` (raiz). Depois de commitar em `main`:

    git push origin main && git push origin main:gh-pages
