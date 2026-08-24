#!/usr/bin/env python3
"""Gera os slides 02..18 da apresentação IPR 2.0 — Encontro de Chefias.

O slide 01 (capa) é escrito à mão, porque é o único com fundo escuro e layout
próprio. Daqui para frente todos compartilham o mesmo esqueleto do template da
Diretoria: barra azul + barra clara no topo, cabeçalho com kicker e título,
corpo livre e rodapé com o número do slide.

Cada slide declara `extra_css` (só o que é dele) e `body` (o miolo). O head, o
cabeçalho e o rodapé saem daqui, para que 17 arquivos não divirjam em detalhe.
"""

from pathlib import Path

DST = Path("/home/pedro/Apresentacoes/EncontroChefias2026/apresentacao_ipr_paf2027")
TOTAL = 18
RODAPE = "IPR 2.0 e o PAF 2027 — Encontro de Chefias · GPF/SFC/ANTAQ"

# Fator global de texto. Cada slide declara o `base` em que foi fechado; este
# fator multiplica todos eles de uma vez. Em 0.90 o texto do corpo encolhe 10%,
# e a folga que sobra vira respiro vertical entre os cards (row-gap, abaixo).
TEXT_SCALE = 0.90

BASE_CSS = """
body { margin:0; padding:0; overflow:hidden; font-family:'Open Sans',sans-serif; }
.slide { width:100vw; height:100vh; position:relative; display:flex; flex-direction:column; overflow:hidden; background:#ffffff; }
.font-montserrat { font-family:'Montserrat',sans-serif; }
.text-brand { color:#003366; }
.bg-brand { background-color:#003366; }
.text-accent { color:#0066CC; }
.bg-accent { background-color:#0066CC; }
.header-bar { height:10px; background:#003366; width:100%; }
.secondary-bar { height:4px; background:#0066CC; width:100%; }

.stat-card {
  background: linear-gradient(135deg, #003366, #004d99);
  border-radius: 16px;
  padding: 20px 18px;
  text-align: center;
  color: white;
  position: relative;
  overflow: hidden;
}
.stat-card::after {
  content: '';
  position: absolute; top: -30px; right: -30px;
  width: 80px; height: 80px;
  border-radius: 50%;
  background: rgba(255,255,255,0.06);
}
.stat-num {
  font-family: 'Montserrat', sans-serif;
  font-weight: 900;
  font-size: calc(48px * var(--tz));
  line-height: 1;
}
.card {
  display: flex; align-items: flex-start; gap: 16px;
  padding: 14px 20px;
  background: #F8FAFC;
  border-radius: 14px;
  border-left: 5px solid #0066CC;
}
.card-green  { background: linear-gradient(135deg,#F0FDF4,#DCFCE7); border-left-color:#22C55E; }
.card-amber  { background: linear-gradient(135deg,#FFFBEB,#FEF3C7); border-left-color:#F59E0B; }
.card-red    { background: linear-gradient(135deg,#FEF2F2,#FEE2E2); border-left-color:#EF4444; }
.ico {
  width:50px; height:50px; border-radius:12px; flex-shrink:0;
  display:flex; align-items:center; justify-content:center;
}
/* As colunas dos slides de duas metades centram o proprio conteudo: a folga
   vertical fica dividida em cima e embaixo, em vez de sobrar toda no rodape.
   O contêiner de conteudo quase sempre E o proprio grid (`class="flex-1 ...
   grid"`), e nao um grid dentro dele — por isso os dois seletores. */
.slide > .flex-1 > .flex.flex-col,
.slide > .flex-1 > .grid > .flex.flex-col { justify-content:center; }

table.tbl { width:100%; border-collapse:collapse; }
table.tbl th {
  background:#F1F5F9; color:#475569; text-align:left;
  font-family:'Montserrat',sans-serif; font-weight:700;
  text-transform:uppercase; letter-spacing:0.06em;
  padding:10px 14px; font-size:calc(15px * var(--tz));
}
table.tbl td { padding:11px 14px; border-top:1px solid #E2E8F0; color:#334155; font-size:calc(18px * var(--tz)); }
table.tbl tr:nth-child(even) td { background:#FAFBFC; }
.num { text-align:right; font-variant-numeric:tabular-nums; }
table.tbl th.num { text-align:right; }
.pill {
  display:inline-block; padding:3px 12px; border-radius:999px;
  font-family:'Montserrat',sans-serif; font-weight:700;
  font-size:calc(14px * var(--tz)); letter-spacing:0.04em;
}
.pill-a { background:#DCFCE7; color:#166534; }
.pill-b { background:#DBEAFE; color:#1E40AF; }
.pill-c { background:#FEE2E2; color:#991B1B; }
.pill-gold { background:#FEF3C7; color:#92400E; }
.formula {
  background:#0F172A; color:#E2E8F0; border-radius:14px;
  padding:18px 24px; font-family:'Courier New',monospace;
  font-size:calc(20px * var(--tz)); letter-spacing:0.02em;
}
.destaque {
  background: linear-gradient(135deg,#003366,#0066CC);
  color:#fff; border-radius:16px; padding:16px 24px;
}
.legenda { color:#64748B; font-size:calc(15px * var(--tz)); line-height:1.5; }
.novo-tag {
  display:inline-flex; align-items:center; gap:7px;
  background:#FFD700; color:#003366; border-radius:999px;
  padding:3px 14px; font-family:'Montserrat',sans-serif;
  font-weight:900; font-size:calc(13px * var(--tz));
  letter-spacing:0.1em; text-transform:uppercase;
}

/* Respiro vertical entre os cards.
   Os utilitarios gap-* do Tailwind valem para as duas direcoes, e mexer no
   `gap` cheio estreitaria as colunas dos grids de duas metades. Por isso aqui
   so o `row-gap` e reescrito: um card fica mais longe do card de baixo, e a
   largura das colunas continua exatamente a mesma. Esta folha vem depois do
   CDN no <head>, entao vence no desempate por ordem. */
.gap-2 { row-gap:18px; }
.gap-3 { row-gap:30px; }
.gap-4 { row-gap:32px; }
.gap-5 { row-gap:34px; }
.gap-6 { row-gap:34px; }
.gap-8 { row-gap:38px; }
"""

HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<link rel="icon" type="image/png" href="favicon.png">
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;700;900&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet"/>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"/>
<style>{css}</style>
</head>
<body>
<div class="slide">
  <div class="header-bar"></div>
  <div class="secondary-bar"></div>

  <div class="px-16 pt-6 pb-2">
    <div class="flex items-center gap-3">
      <div style="width:5px;height:44px;" class="bg-accent"></div>
      <div>
        <p class="font-montserrat font-bold text-gray-400 text-lg uppercase tracking-widest">{kicker}</p>
        <p class="text-5xl font-montserrat font-bold text-brand uppercase tracking-tight">{titulo}</p>
      </div>
      <div class="ml-auto flex items-center gap-3">
        {tag}
        <img src="assets/logo-antaq-azul.png" alt="ANTAQ" style="height:32px;">
        <p class="font-montserrat font-bold text-gray-400 text-sm tracking-widest">GPF</p>
      </div>
    </div>
  </div>

{body}

  <div class="px-16 pb-4 flex justify-between items-center border-t border-gray-100 pt-3 mx-8">
    <p class="text-gray-400 text-sm">{rodape}</p>
    <p class="text-gray-300 text-sm font-mono">{n} / {total}</p>
  </div>
</div>
<script src="zoom.js"></script>
<script>document.addEventListener("keydown",function(e){{if(["ArrowRight","ArrowLeft","PageDown","PageUp","Home","End"," ","f","F"].indexOf(e.key)!==-1){{e.preventDefault();window.parent.postMessage({{type:"slide-nav",key:e.key}},"*");}}}});</script>
</body>
</html>
"""

TAG_NOVO = '<span class="novo-tag"><i class="fas fa-star"></i> Novidade 2027</span>'

SLIDES: list[dict] = []


def slide(n, title, kicker, titulo, body, extra_css="", tag="", base=1.0):
    SLIDES.append(
        dict(n=n, title=title, kicker=kicker, titulo=titulo, body=body,
             extra_css=extra_css, tag=tag, base=base)
    )


# ---------------------------------------------------------------------------
# 02 — Roteiro / o que mudou
# ---------------------------------------------------------------------------
slide(
    2,
    "O que mudou — IPR 2.0",
    "Panorama",
    "O que mudou desde o último PAF",
    """
  <div class="flex-1 px-16 pb-2 flex flex-col gap-4">

    <div class="grid grid-cols-3 gap-4 flex-1">
      <div class="bloco">
        <div class="bloco-top" style="background:linear-gradient(135deg,#003366,#0066CC);">
          <i class="fas fa-gauge-high"></i>
          <span>1 · O risco ficou mais completo</span>
        </div>
        <div class="bloco-body">
          <p><strong>Quem nunca foi fiscalizado deixou de ser &ldquo;risco zero&rdquo;</strong> (ICF).</p>
          <p><strong>O tamanho da operação passou a pesar</strong> (IVO).</p>
          <p><strong>Atividade perigosa tem piso</strong>: travessia nunca cai na faixa mais branda (F_IRA).</p>
          <p><strong>As faixas A1..C4 foram refeitas</strong> para caber na capacidade real da Agência.</p>
          <p><strong>Uma parcela do grupo de baixo risco entra por sorteio auditável.</strong></p>
        </div>
        <div class="bloco-foot"><strong>39%</strong> do universo sem visita recente — e agora isso pesa na nota</div>
      </div>

      <div class="bloco">
        <div class="bloco-top" style="background:linear-gradient(135deg,#065F46,#059669);">
          <i class="fas fa-id-card"></i>
          <span>2 · A lista ficou confiável</span>
        </div>
        <div class="bloco-body">
          <p><strong>Todo CNPJ do PAF é conferido na Receita Federal</strong> antes de a lista fechar.</p>
          <p><strong>Empresa baixada ou suspensa sai da listagem</strong> e vai para uma fila de conferência humana.</p>
          <p><strong>68 outorgas ficaram de fora</strong> do PAF 2027 por esse motivo.</p>
          <p><strong>O dossiê do CNPJ já vem pronto</strong> para instruir a revogação do termo de outorga.</p>
        </div>
        <div class="bloco-foot"><strong>2.133</strong> CNPJs conferidos na Receita Federal</div>
      </div>

      <div class="bloco">
        <div class="bloco-top" style="background:linear-gradient(135deg,#92400E,#D97706);">
          <i class="fas fa-people-carry-box"></i>
          <span>3 · O plano ficou executável</span>
        </div>
        <div class="bloco-body">
          <p><strong>Sabemos quem fiscaliza cada outorga</strong> — 100% do universo tem regional responsável.</p>
          <p><strong>Medimos se o plano cabe na equipe de cada regional</strong>, em horas por ano (PGD).</p>
          <p><strong>O que não cabe pode ser redistribuído</strong>, com régua, registro e decisão humana.</p>
          <p><strong>A missão de apoio deixou de ser informal</strong>: passa a ter dono e trilha de auditoria.</p>
        </div>
        <div class="bloco-foot"><strong>177% &rarr; 95%</strong> de ocupação na regional mais apertada</div>
      </div>
    </div>

    <div class="destaque flex items-center gap-6">
      <i class="fas fa-quote-left text-3xl" style="opacity:0.35;"></i>
      <div>
        <p class="font-montserrat font-bold" style="font-size:calc(23px * var(--tz));">
          O IPR sempre disse <em>quem</em> fiscalizar. O que faltava era dizer
          <em>se dá para fiscalizar</em> — e, quando não dá, <em>o que fazer a respeito</em>.
        </p>
        <p class="text-blue-100 text-lg mt-1">É essa a diferença entre o PAF 2026 e o PAF 2027.</p>
      </div>
    </div>

    <div class="grid grid-cols-4 gap-3">
      <div class="mini"><i class="fas fa-list-check text-accent"></i><span><strong>2.478</strong> outorgas avaliadas</span></div>
      <div class="mini"><i class="fas fa-clipboard-check text-accent"></i><span><strong>2.410</strong> na listagem do PAF 2027</span></div>
      <div class="mini"><i class="fas fa-map-location-dot text-accent"></i><span><strong>14</strong> regionais executoras</span></div>
      <div class="mini"><i class="fas fa-display text-accent"></i><span><strong>11</strong> telas no menu</span></div>
    </div>
  </div>
""",
    extra_css="""
.bloco { background:#fff; border:1px solid #E2E8F0; border-radius:16px; overflow:hidden; display:flex; flex-direction:column; }
.bloco-top {
  color:#fff; padding:13px 20px; display:flex; align-items:center; gap:11px;
  font-family:'Montserrat',sans-serif; font-weight:700; font-size:calc(20px * var(--tz));
}
.bloco-body {
  flex:1; padding:16px 20px; display:flex; flex-direction:column;
  justify-content:space-evenly; gap:10px;
}
.bloco-body p { margin:0; color:#475569; font-size:calc(17px * var(--tz)); line-height:1.5; padding-left:24px; position:relative; }
.bloco-body p::before {
  content:''; position:absolute; left:2px; top:calc(9px * var(--tz));
  width:9px; height:9px; border-radius:50%; background:#0066CC; opacity:0.45;
}
.bloco-body strong { color:#003366; }
.bloco-foot {
  border-top:1px solid #E2E8F0; padding:11px 20px; background:#F8FAFC;
  color:#475569; font-size:calc(15px * var(--tz));
}
.bloco-foot strong { font-family:'Montserrat',sans-serif; font-weight:900; color:#003366; font-size:calc(21px * var(--tz)); }
.mini {
  display:flex; align-items:center; gap:10px;
  background:#F8FAFC; border-radius:12px; padding:10px 16px;
  color:#475569; font-size:calc(15px * var(--tz));
}
.mini strong { color:#003366; font-family:'Montserrat',sans-serif; font-weight:900; font-size:calc(19px * var(--tz)); }
""",
    base=1.33,
)

# ---------------------------------------------------------------------------
# 03 — O que é o IPR
# ---------------------------------------------------------------------------
slide(
    3,
    "O que é o IPR",
    "A base · seção &ldquo;O que é o IPR?&rdquo; da Ajuda",
    "O que é o IPR",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">

    <div class="col-span-7 flex flex-col gap-3">
      <div class="destaque">
        <p class="font-montserrat font-bold" style="font-size:calc(25px * var(--tz));">
          Índice de Perfil de Risco
        </p>
        <p class="text-blue-100 text-xl mt-1">
          Cada outorga recebe uma <strong>nota de 0 a 100</strong> e uma <strong>faixa de A1 a C4</strong>.
          A nota diz onde o esforço de fiscalização rende mais.
        </p>
      </div>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-file-signature text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-2xl">A unidade é a outorga, não a empresa</p>
          <p class="text-gray-600 text-lg mt-1">
            Uma mesma empresa pode ter várias outorgas — uma EBN com quatro linhas de travessia
            tem quatro. Cada uma recebe o <strong>seu próprio IPR</strong>, porque o risco de uma
            travessia no Oiapoque não é o risco de outra em Manaus.
          </p>
        </div>
      </div>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-scale-balanced text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-2xl">A nota mistura duas coisas</p>
          <p class="text-gray-600 text-lg mt-1">
            <strong>O que a empresa já fez</strong> (autuações, reincidência, descumprimento de NoCI,
            denúncias que viraram sanção) e <strong>o que ela é</strong> (o risco próprio da atividade,
            o tamanho da operação e há quanto tempo ninguém a visita).
          </p>
        </div>
      </div>

      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-triangle-exclamation text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-2xl">O IPR não decide sozinho</p>
          <p class="text-gray-600 text-lg mt-1">
            Ele <strong>ordena</strong>. Quem fecha a lista do PAF é a GPF, e quem executa são vocês.
            Toda decisão de exceção fica registrada com autor e fundamento.
          </p>
        </div>
      </div>
    </div>

    <div class="col-span-5 flex flex-col gap-3">
      <p class="font-montserrat font-bold text-brand text-2xl">A faixa define o tratamento</p>
      <div class="grupo grupo-a">
        <div class="grupo-head"><span class="pill pill-a">GRUPO A</span><span>A1 · A2 — risco baixo</span></div>
        <p><strong>Monitoramento por dados</strong>, sem fiscalização programada. Uma parcela entra
        no PAF <strong>por sorteio</strong>, para que ninguém fique fora do radar.</p>
        <p class="qtd">477 outorgas</p>
      </div>
      <div class="grupo grupo-b">
        <div class="grupo-head"><span class="pill pill-b">GRUPO B</span><span>B1 · B2 — risco intermediário</span></div>
        <p><strong>Fiscalização remota documental</strong> agendada — sem viagem. Em B2, ação à
        distância se a análise indicar.</p>
        <p class="qtd">1.686 outorgas</p>
      </div>
      <div class="grupo grupo-c">
        <div class="grupo-head"><span class="pill pill-c">GRUPO C</span><span>C1 a C4 — risco alto</span></div>
        <p><strong>Fiscalização presencial</strong>: programada (C1), surpresa (C2), intensiva (C3),
        intervenção ou suspensão cautelar (C4). É o coração do PAF.</p>
        <p class="qtd">315 outorgas</p>
      </div>
      <p class="legenda">
        Números do ciclo 2027, universo completo. O tratamento de cada faixa está em tabela
        (<code>ipr.solucao_fiscal</code>) — mudar a régua é decisão registrada, não alteração de sistema.
      </p>
    </div>
  </div>
""",
    extra_css="""
.grupo { border-radius:14px; padding:12px 18px; border:1px solid #E2E8F0; }
.grupo-a { background:#F0FDF4; border-color:#BBF7D0; }
.grupo-b { background:#EFF6FF; border-color:#BFDBFE; }
.grupo-c { background:#FEF2F2; border-color:#FECACA; }
.grupo-head {
  display:flex; align-items:center; gap:10px; margin-bottom:6px;
  font-family:'Montserrat',sans-serif; font-weight:700; color:#003366;
  font-size:calc(16px * var(--tz));
}
.grupo p { margin:0; color:#475569; font-size:calc(15px * var(--tz)); line-height:1.45; }
.grupo .qtd {
  margin-top:6px; font-family:'Montserrat',sans-serif; font-weight:900;
  color:#003366; font-size:calc(20px * var(--tz));
}
""",
    base=1.4,
)

# ---------------------------------------------------------------------------
# 04 — O universo
# ---------------------------------------------------------------------------
slide(
    4,
    "O universo do PAF 2027",
    "Seção &ldquo;Universo do PPF&rdquo; da Ajuda",
    "O universo do PAF 2027",
    """
  <div class="px-16 pb-3 grid grid-cols-4 gap-4">
    <div class="stat-card">
      <p class="stat-num">2.478</p>
      <p class="text-blue-200 text-lg font-semibold mt-2">Outorgas avaliadas<br/>no ciclo 2027</p>
    </div>
    <div class="stat-card">
      <p class="stat-num">2.410</p>
      <p class="text-blue-200 text-lg font-semibold mt-2">Na listagem do PAF<br/>(68 fora por cadastro)</p>
    </div>
    <div class="stat-card">
      <p class="stat-num">14</p>
      <p class="text-blue-200 text-lg font-semibold mt-2">Regionais executoras<br/>com carga atribuída</p>
    </div>
    <div class="stat-card">
      <p class="stat-num">100%</p>
      <p class="text-blue-200 text-lg font-semibold mt-2">Do universo com<br/>regional responsável</p>
    </div>
  </div>

  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">
    <div class="col-span-7 flex flex-col gap-3">
      <p class="font-montserrat font-bold text-brand text-2xl">Quanto cada regional responde</p>
      <table class="tbl">
        <thead><tr>
          <th>Regional</th><th class="num">Outorgas</th><th class="num">Grupo C</th>
          <th class="num">Grupo B</th><th class="num">Grupo A</th><th class="num">% do país</th>
        </tr></thead>
        <tbody>
          <tr><td><strong>GREBL</strong> · Belém</td><td class="num">479</td><td class="num">82</td><td class="num">336</td><td class="num">61</td><td class="num">19,9%</td></tr>
          <tr><td><strong>GREMN</strong> · Manaus</td><td class="num">446</td><td class="num">72</td><td class="num">316</td><td class="num">58</td><td class="num">18,5%</td></tr>
          <tr><td><strong>GRERJ</strong> · Rio de Janeiro</td><td class="num">295</td><td class="num">31</td><td class="num">196</td><td class="num">68</td><td class="num">12,2%</td></tr>
          <tr><td><strong>GREST</strong> · Santos</td><td class="num">219</td><td class="num">18</td><td class="num">129</td><td class="num">72</td><td class="num">9,1%</td></tr>
          <tr><td><strong>GRERE</strong> · Recife</td><td class="num">146</td><td class="num">6</td><td class="num">105</td><td class="num">35</td><td class="num">6,1%</td></tr>
          <tr><td><strong>URESN</strong> · Santana</td><td class="num">121</td><td class="num">25</td><td class="num">87</td><td class="num">9</td><td class="num">5,0%</td></tr>
          <tr><td><strong>GREFL</strong> · Florianópolis</td><td class="num">113</td><td class="num">9</td><td class="num">72</td><td class="num">32</td><td class="num">4,7%</td></tr>
          <tr><td colspan="6" style="color:#64748B;">URECB 96 · URESL 96 · URESV 88 · UREPL 85 · UREVT 83 · UREPV 76 · UREFT 67</td></tr>
        </tbody>
      </table>
      <p class="legenda">
        Já <strong>sem</strong> as outorgas retiradas por situação cadastral — a coluna existe para
        dimensionar equipe, e contar o que não será fiscalizado dimensionaria errado.
      </p>
    </div>

    <div class="col-span-5 flex flex-col gap-3">
      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-layer-group text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Cinco segmentos, três áreas</p>
          <p class="text-gray-600 text-lg mt-1">
            Navegação Marítima · Navegação Interior · Instalações Portuárias · Portos Públicos ·
            Arrendamentos e Operadores Portuários.
          </p>
          <p class="text-gray-600 text-lg mt-1">
            No ciclo 2027: <strong>Porto 1.201</strong> · <strong>Interior 698</strong> ·
            <strong>Marítima 579</strong>.
          </p>
        </div>
      </div>
      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-key text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">A &ldquo;Chave&rdquo; da outorga</p>
          <p class="text-gray-600 text-lg mt-1">
            É o identificador que junta CNPJ + modalidade + trecho ou terminal. É por ela que o
            sistema costura o histórico de fiscalização de anos anteriores.
          </p>
          <p class="text-gray-600 text-lg mt-1">
            <strong>Cuidado prático:</strong> trocar o CNPJ de uma outorga troca a chave e
            <strong>desliga a série histórica</strong>. Por isso sucessão de empresa é decisão
            registrada, nunca correção de campo.
          </p>
        </div>
      </div>
      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-clock-rotate-left text-green-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Quatro ciclos carregados</p>
          <p class="text-gray-600 text-lg mt-1">
            2024, 2025, 2026 e 2027 no mesmo painel — dá para ver quem subiu de faixa, quem desceu
            e o que explicou a mudança (tela <strong>Histórico</strong>).
          </p>
        </div>
      </div>
    </div>
  </div>
""",
    base=1.2,
)

# ---------------------------------------------------------------------------
# 05 — Indicadores comportamentais
# ---------------------------------------------------------------------------
slide(
    5,
    "Os indicadores de comportamento",
    "Seção &ldquo;Indicadores comportamentais&rdquo; da Ajuda",
    "O que a empresa já fez",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">
    <div class="col-span-7 flex flex-col gap-3">
      <p class="text-gray-600 text-xl">
        Seis indicadores da <strong>NT 9/2021</strong>. Todos são <strong>proporções</strong>:
        o que deu errado dividido pelo total. Todos olham para os últimos 3 ou 5 anos.
      </p>
      <table class="tbl">
        <thead><tr>
          <th>Sigla</th><th>O que mede</th><th class="num">Peso</th><th>Janela</th>
        </tr></thead>
        <tbody>
          <tr><td class="sg">IRI</td><td>Reincidência — repetiu a mesma infração</td><td class="num"><strong>3</strong></td><td>3 anos</td></tr>
          <tr><td class="sg">IGI</td><td>Gravidade das infrações cometidas</td><td class="num"><strong>3</strong></td><td>5 anos</td></tr>
          <tr><td class="sg">IOC</td><td>Ocorrência crítica — infrações da lista sensível</td><td class="num"><strong>3</strong></td><td>5 anos</td></tr>
          <tr><td class="sg">INN</td><td>Não atendimento a NoCI</td><td class="num"><strong>2</strong></td><td>5 anos</td></tr>
          <tr><td class="sg">IOU</td><td>Denúncia de Ouvidoria que virou sanção</td><td class="num"><strong>2</strong></td><td>5 anos</td></tr>
          <tr><td class="sg">IIN</td><td>Irregularidade normativa — processos com penalidade</td><td class="num"><strong>1</strong></td><td>5 anos</td></tr>
        </tbody>
      </table>
      <p class="legenda">
        Pesos da gravidade no IGI (NT 9/2021, Tabela 4): Leve 1 · Média 3 · Grave 6 · Gravíssima 10.
        Os pesos ficam em tabela no banco e o painel os lê de lá — não há número escondido em código.
      </p>
    </div>

    <div class="col-span-5 flex flex-col gap-3">
      <div class="card card-red">
        <div class="ico" style="background:#FECACA;"><i class="fas fa-circle-exclamation text-red-600 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-2xl">O defeito que isso criava</p>
          <p class="text-gray-600 text-lg mt-1">
            <strong>Todos os seis dependem de fiscalização anterior.</strong> Empresa nunca
            fiscalizada não tem autuação, não tem NoCI, não tem reincidência — e por isso
            marcava <strong>zero em tudo</strong>.
          </p>
          <p class="text-gray-600 text-lg mt-1">
            Zero em tudo caía em <strong>A1, a faixa de menor risco</strong>. Ou seja: quanto
            menos a Agência olhava para uma outorga, mais segura ela parecia.
          </p>
        </div>
      </div>

      <div class="destaque">
        <p class="font-montserrat font-bold" style="font-size:calc(22px * var(--tz));">
          &ldquo;Nunca fiscalizada&rdquo; não é o mesmo que &ldquo;sem problema&rdquo;.
        </p>
        <p class="text-blue-100 text-lg mt-2">
          Corrigir isso é o que os dois próximos indicadores fazem — e é a mudança
          mais importante do IPR 2.0.
        </p>
      </div>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-arrow-trend-down text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">O tamanho do problema</p>
          <p class="text-gray-600 text-lg mt-1">
            <strong>591 outorgas</strong> do ciclo 2027 nunca foram fiscalizadas. Outras
            <strong>378</strong> não recebem visita há mais de cinco anos.
          </p>
        </div>
      </div>
    </div>
  </div>
""",
    extra_css="""
td.sg { font-family:'Montserrat',sans-serif; font-weight:900; color:#003366; letter-spacing:0.04em; }
""",
    base=1.4,
)

# ---------------------------------------------------------------------------
# 06 — ICF
# ---------------------------------------------------------------------------
slide(
    6,
    "ICF — cobertura fiscalizatória",
    "Seção &ldquo;O ICF&rdquo; da Ajuda",
    "ICF: há quanto tempo ninguém olha",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">
    <div class="col-span-5 flex flex-col gap-3">
      <div class="destaque">
        <p class="font-montserrat font-bold" style="font-size:calc(23px * var(--tz));">
          Indicador de Cobertura Fiscalizatória
        </p>
        <p class="text-blue-100 text-xl mt-1">
          O tempo desde a última fiscalização vira nota. Quanto mais antiga a última visita,
          maior a nota — e quem nunca foi visitado leva a nota máxima.
        </p>
      </div>

      <p class="font-montserrat font-bold text-brand text-2xl">A escada</p>
      <div class="escada">
        <div class="deg"><span class="deg-t">Até 12 meses</span><span class="deg-v v0">0,00</span></div>
        <div class="deg"><span class="deg-t">13 a 24 meses</span><span class="deg-v v1">0,20</span></div>
        <div class="deg"><span class="deg-t">25 a 36 meses</span><span class="deg-v v2">0,40</span></div>
        <div class="deg"><span class="deg-t">37 a 48 meses</span><span class="deg-v v3">0,60</span></div>
        <div class="deg"><span class="deg-t">49 a 60 meses</span><span class="deg-v v4">0,80</span></div>
        <div class="deg deg-max"><span class="deg-t">Mais de 60 meses <strong>ou nunca</strong></span><span class="deg-v v5">1,00</span></div>
      </div>
      <p class="legenda">
        Peso 3 na fórmula. Nota máxima soma <strong>15,8 pontos</strong> ao IPR só por ausência
        de cobertura — mais do que qualquer indicador de comportamento isolado.
      </p>
    </div>

    <div class="col-span-7 flex flex-col gap-3">
      <div class="grid grid-cols-3 gap-3">
        <div class="stat-card"><p class="stat-num">969</p><p class="text-blue-200 text-sm font-semibold mt-2">outorgas com ICF = 1,00</p></div>
        <div class="stat-card"><p class="stat-num">39%</p><p class="text-blue-200 text-sm font-semibold mt-2">do universo do ciclo 2027</p></div>
        <div class="stat-card"><p class="stat-num">591</p><p class="text-blue-200 text-sm font-semibold mt-2">nunca fiscalizadas</p></div>
      </div>

      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-eye text-green-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-2xl">O que o ICF conserta</p>
          <p class="text-gray-600 text-lg mt-1">
            Antes, ausência de histórico era lida como ausência de risco. Com o ICF,
            <strong>ausência de informação virou motivo para ir ver</strong> — que é o que o bom
            senso sempre disse.
          </p>
        </div>
      </div>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-rotate text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-2xl">Efeito prático: o índice se renova</p>
          <p class="text-gray-600 text-lg mt-1">
            Fiscalizou? O ICF daquela outorga cai a zero e ela desce de faixa no ciclo seguinte,
            abrindo espaço para outra. <strong>O trabalho de vocês aparece no índice</strong> — e o
            plano do ano seguinte já nasce diferente por causa dele.
          </p>
        </div>
      </div>

      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-calendar-check text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-2xl">De onde sai a data</p>
          <p class="text-gray-600 text-lg mt-1">
            Da <strong>data de início de realização</strong> da ação fiscal registrada no sistema da
            Fiscalização, sempre a mais recente de cada outorga. Ação não registrada é ação que o
            índice não enxerga — o registro é o que faz a conta ficar certa.
          </p>
        </div>
      </div>
    </div>
  </div>
""",
    extra_css="""
.escada { display:flex; flex-direction:column; gap:5px; }
.deg {
  display:flex; align-items:center; justify-content:space-between;
  background:#F8FAFC; border-radius:10px; padding:7px 16px;
  border-left:5px solid #CBD5E1;
}
.deg-max { background:linear-gradient(135deg,#FEF2F2,#FEE2E2); border-left-color:#EF4444; }
.deg-t { color:#475569; font-size:calc(15px * var(--tz)); }
.deg-t strong { color:#991B1B; }
.deg-v {
  font-family:'Montserrat',sans-serif; font-weight:900;
  font-size:calc(18px * var(--tz)); color:#003366;
}
.v0 { color:#16A34A; } .v5 { color:#DC2626; }
""",
    base=1.4,
)

# ---------------------------------------------------------------------------
# 07 — IVO
# ---------------------------------------------------------------------------
slide(
    7,
    "IVO — volume operacional",
    "Seção &ldquo;O IVO&rdquo; da Ajuda",
    "IVO: o tamanho entra na conta",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">
    <div class="col-span-7 flex flex-col gap-3">
      <p class="text-gray-600 text-xl">
        Uma travessia que leva <strong>300 mil passageiros por ano</strong> e outra que leva
        <strong>5 mil</strong> podem ter o mesmo histórico de infrações — mas não colocam a mesma
        coisa em jogo. O IVO faz o <strong>porte da operação</strong> pesar no risco.
      </p>

      <div class="passo">
        <div class="passo-n">1</div>
        <div>
          <p class="passo-t">Medir o volume</p>
          <p class="passo-d">Usa a melhor fonte que existir: primeiro o que foi <strong>realizado</strong>
          (toneladas, TEUs, m³, passageiros, atracações), depois o <strong>declarado</strong> e, só em
          último caso, o <strong>porte cadastrado</strong> (frota, capacidade do terminal). Média dos
          até três últimos anos com movimento.</p>
        </div>
      </div>
      <div class="passo">
        <div class="passo-n">2</div>
        <div>
          <p class="passo-t">Comparar com os pares certos</p>
          <p class="passo-d">Não se compara uma linha de 3 mil passageiros com um terminal de 3 milhões
          de toneladas. Cada outorga é agrupada por <strong>categoria, unidade de medida e porte</strong>
          — o quartil nunca compara uma travessia a um TUP.</p>
        </div>
      </div>
      <div class="passo">
        <div class="passo-n">3</div>
        <div>
          <p class="passo-t">Posicionar dentro do grupo</p>
          <p class="passo-d">Os 25% menores levam <strong>0,10</strong>; a faixa seguinte, 0,30; a
          próxima, 0,60; e os <strong>25% maiores levam 1,00</strong>.</p>
        </div>
      </div>

      <div class="formula">IVO_efetivo &nbsp;=&nbsp; IVO &nbsp;&times;&nbsp; ICF</div>
      <p class="text-gray-600 text-lg">
        <strong>Volume grande só vira risco quando ninguém está olhando.</strong> Um terminal enorme
        fiscalizado há seis meses tem ICF = 0 — logo IVO efetivo = 0, porque a Agência já sabe o que
        se passa lá. O mesmo terminal sem visita há mais de cinco anos leva o volume integral.
      </p>
    </div>

    <div class="col-span-5 flex flex-col gap-3">
      <div class="grid grid-cols-2 gap-3">
        <div class="stat-card"><p class="stat-num">2</p><p class="text-blue-200 text-sm font-semibold mt-2">peso na fórmula<br/>(10,5 pontos no máximo)</p></div>
        <div class="stat-card"><p class="stat-num">195</p><p class="text-blue-200 text-sm font-semibold mt-2">outorgas no quartil<br/>superior de porte</p></div>
      </div>

      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-bullseye text-green-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Para que serve</p>
          <p class="text-gray-600 text-lg mt-1">
            Concentra o esforço onde há <strong>muito em jogo e pouca informação recente</strong> —
            que é exatamente onde uma fiscalização vale mais.
          </p>
        </div>
      </div>

      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-circle-info text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Ressalva declarada — travessia e passageiros</p>
          <p class="text-gray-600 text-lg mt-1">
            <strong>Nenhuma base pública hoje informa passageiros transportados.</strong> O
            Estatístico Aquaviário é um painel de carga. Para travessia e longitudinal de
            passageiros, o IVO usa a <strong>capacidade da frota outorgada</strong>.
          </p>
          <p class="text-gray-600 text-lg mt-1">
            Isso é <strong>oferta, não demanda</strong>: ordena o porte relativo dentro da
            modalidade, mas não mede movimentação. Está escrito na Ajuda e no relatório —
            se alguém tiver a fonte, queremos saber.
          </p>
        </div>
      </div>
    </div>
  </div>
""",
    extra_css="""
.passo { display:flex; gap:14px; align-items:flex-start; }
.passo-n {
  width:34px; height:34px; border-radius:50%; flex-shrink:0;
  background:#0066CC; color:#fff; display:flex; align-items:center; justify-content:center;
  font-family:'Montserrat',sans-serif; font-weight:900; font-size:calc(17px * var(--tz));
}
.passo-t { margin:0; font-family:'Montserrat',sans-serif; font-weight:700; color:#003366; font-size:calc(18px * var(--tz)); }
.passo-d { margin:2px 0 0; color:#475569; font-size:calc(15px * var(--tz)); line-height:1.45; }
""",
    base=1.32,
)

# ---------------------------------------------------------------------------
# 08 — F_IRA
# ---------------------------------------------------------------------------
slide(
    8,
    "F_IRA — o piso de risco da atividade",
    "Seção &ldquo;F_IRA&rdquo; da Ajuda",
    "O piso do risco da atividade",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">
    <div class="col-span-6 flex flex-col gap-3">
      <div class="destaque">
        <p class="font-montserrat font-bold" style="font-size:calc(23px * var(--tz));">
          IRA é da modalidade, não da empresa
        </p>
        <p class="text-blue-100 text-xl mt-1">
          <strong>Travessia tem IRA 73</strong> — não importa quem opere. Longo Curso, 73.
          Contrato de Uso Temporário, 11. É o risco inerente <strong>da atividade</strong>.
        </p>
      </div>

      <p class="text-gray-600 text-xl">
        O IRA sai da <strong>NT_IRA</strong> e combina quatro dimensões:
      </p>
      <div class="grid grid-cols-2 gap-3">
        <div class="dim"><i class="fas fa-life-ring"></i><div><p class="dim-t">Segurança</p><p class="dim-p">35%</p></div></div>
        <div class="dim"><i class="fas fa-coins"></i><div><p class="dim-t">Econômica</p><p class="dim-p">25%</p></div></div>
        <div class="dim"><i class="fas fa-leaf"></i><div><p class="dim-t">Ambiental</p><p class="dim-p">20%</p></div></div>
        <div class="dim"><i class="fas fa-binoculars"></i><div><p class="dim-t">Monitorabilidade</p><p class="dim-p">20%</p></div></div>
      </div>

      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-shield-halved text-green-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">O efeito na prática</p>
          <p class="text-gray-600 text-lg mt-1">
            Uma <strong>travessia nunca fiscalizada jamais cai em A1</strong>. O piso garante que
            atividade perigosa não vá parar na faixa mais branda só porque a empresa ainda não tem
            ficha.
          </p>
        </div>
      </div>
    </div>

    <div class="col-span-6 flex flex-col gap-3">
      <p class="font-montserrat font-bold text-brand text-2xl">Como o piso é aplicado</p>
      <div class="formula">IPR_final &nbsp;=&nbsp; MAIOR( nota calculada , piso da atividade )</div>
      <p class="text-gray-600 text-lg">
        Não é uma soma: é um <strong>mínimo garantido</strong>. Se a nota calculada já passa do piso,
        o piso não faz nada. Se fica abaixo, o piso assume.
      </p>

      <table class="tbl">
        <thead><tr><th>IRA da modalidade</th><th class="num">Piso em pontos</th><th>O que significa</th></tr></thead>
        <tbody>
          <tr><td><strong>70 ou mais</strong></td><td class="num"><strong>13,16</strong></td><td>Garante pelo menos <span class="pill pill-b">B1</span></td></tr>
          <tr><td>51 a 69</td><td class="num">4,21</td><td>Sinal dentro de <span class="pill pill-a">A1</span></td></tr>
          <tr><td>35 a 50</td><td class="num">2,63</td><td>Sinal fraco</td></tr>
          <tr><td>Abaixo de 35</td><td class="num">0,00</td><td>Sem piso</td></tr>
        </tbody>
      </table>

      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-gavel text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Onde o piso aterrissa é decisão, não conta</p>
          <p class="text-gray-600 text-lg mt-1">
            A GPF decidiu que atividade inerentemente arriscada não deve ficar nas faixas mais
            brandas, e a recalibração de 2026 posicionou os limiares de acordo. É política de
            fiscalização escrita em número.
          </p>
        </div>
      </div>
    </div>
  </div>
""",
    extra_css="""
.dim {
  display:flex; align-items:center; gap:12px;
  background:#F8FAFC; border-radius:12px; padding:10px 16px; border-left:5px solid #0066CC;
}
.dim i { color:#0066CC; font-size:calc(20px * var(--tz)); }
.dim-t { margin:0; font-family:'Montserrat',sans-serif; font-weight:700; color:#003366; font-size:calc(16px * var(--tz)); }
.dim-p { margin:0; color:#64748B; font-size:calc(14px * var(--tz)); }
""",
    base=1.35,
)

# ---------------------------------------------------------------------------
# 09 — Fórmula e faixas
# ---------------------------------------------------------------------------
slide(
    9,
    "A fórmula e as faixas A1..C4",
    "Seções &ldquo;Fórmula&rdquo; e &ldquo;Faixas&rdquo; da Ajuda",
    "Da nota para a faixa",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">
    <div class="col-span-6 flex flex-col gap-3">
      <p class="font-montserrat font-bold text-brand text-2xl">A conta</p>
      <div class="formula" style="line-height:1.7;">
        IPR_base = ( IIN&middot;1 + INN&middot;2 + IOU&middot;2 + IRI&middot;3<br/>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+ IGI&middot;3 + IOC&middot;3 + ICF&middot;3 + IVO&middot;2 ) &divide; <strong>19</strong><br/>
        <span style="color:#94A3B8;">&nbsp;</span><br/>
        IPR_final = MAIOR( IPR_base &times; 100 , piso F_IRA )
      </div>
      <p class="text-gray-600 text-lg">
        O <strong>19</strong> é a soma dos pesos dos oito indicadores ativos. Ele não está escrito no
        código: vem de uma tabela versionada. Ligar ou desligar um indicador muda a fórmula,
        muda os pisos e <strong>obriga a recalibrar as faixas</strong>.
      </p>

      <div class="card card-red">
        <div class="ico" style="background:#FECACA;"><i class="fas fa-ban text-red-600 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Por que as faixas foram refeitas</p>
          <p class="text-gray-600 text-lg mt-1">
            Os cortes da NT 9/2021 (5 / 15 / 30 / 40 / 50 / 60 / 70) foram medidos contra o universo
            real: a maior nota do ciclo 2027 é <strong>59,89</strong>. Com aqueles cortes,
            <strong>C3 e C4 nunca teriam ninguém</strong>. Faixa que ninguém alcança não prioriza nada.
          </p>
        </div>
      </div>

      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-users-gear text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">O tamanho do Grupo C tem âncora</p>
          <p class="text-gray-600 text-lg mt-1">
            Está amarrado à <strong>capacidade real de fiscalizar</strong> — na casa de trezentas
            outorgas, o que o PAF consegue de fato programar. Um Grupo C com 800 seria tão
            inútil quanto um vazio.
          </p>
        </div>
      </div>
    </div>

    <div class="col-span-6 flex flex-col gap-3">
      <p class="font-montserrat font-bold text-brand text-2xl">A régua em vigor · ciclo 2027</p>
      <table class="tbl">
        <thead><tr><th>Faixa</th><th>Nota</th><th>Leitura</th><th class="num">Outorgas</th></tr></thead>
        <tbody>
          <tr><td><span class="pill pill-a">A1</span></td><td>até 8,50</td><td>sem sinal relevante</td><td class="num">327</td></tr>
          <tr><td><span class="pill pill-a">A2</span></td><td>8,51 – 13,13</td><td>risco baixo</td><td class="num">150</td></tr>
          <tr><td><span class="pill pill-b">B1</span></td><td>13,14 – 16,84</td><td>piso de atividade e nunca fiscalizadas</td><td class="num">1.169</td></tr>
          <tr><td><span class="pill pill-b">B2</span></td><td>16,85 – 22,11</td><td>histórico próprio começa a pesar</td><td class="num">517</td></tr>
          <tr><td><span class="pill pill-c">C1</span></td><td>22,12 – 26,32</td><td>alto — prioridade no PAF</td><td class="num">242</td></tr>
          <tr><td><span class="pill pill-c">C2</span></td><td>26,33 – 28,70</td><td>muito alto</td><td class="num">20</td></tr>
          <tr><td><span class="pill pill-c">C3</span></td><td>28,71 – 33,83</td><td>crítico</td><td class="num">24</td></tr>
          <tr><td><span class="pill pill-c">C4</span></td><td>acima de 33,83</td><td>extremo — mobilização imediata</td><td class="num">29</td></tr>
        </tbody>
      </table>
      <p class="legenda">
        A régua é <strong>versionada</strong>: os limiares valem para o regime de pesos atual
        (soma 19). Os limiares antigos continuam válidos para os ciclos calculados naquele regime —
        por isso o Histórico compara faixas sem misturar réguas.
      </p>
      <div class="destaque">
        <p class="font-montserrat font-bold" style="font-size:calc(20px * var(--tz));">
          Média do universo: <strong>15,9</strong> &nbsp;·&nbsp; Máxima: <strong>59,89</strong>
        </p>
      </div>
    </div>
  </div>
""",
    base=1.26,
)

# ---------------------------------------------------------------------------
# 10 — Sorteio
# ---------------------------------------------------------------------------
slide(
    10,
    "O sorteio do Grupo A",
    "Seção &ldquo;O sorteio do Grupo A&rdquo; da Ajuda",
    "Por que a sorte entra no PAF",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">
    <div class="col-span-5 flex flex-col gap-3">
      <div class="card card-red">
        <div class="ico" style="background:#FECACA;"><i class="fas fa-circle-question text-red-600 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-2xl">O ponto cego</p>
          <p class="text-gray-600 text-lg mt-1">
            Priorizar só quem tem histórico ruim cria um círculo:
            <strong>quem nunca é fiscalizado nunca gera histórico</strong> — e sem histórico
            continua no Grupo A, que é a maior parte do universo.
          </p>
        </div>
      </div>

      <p class="font-montserrat font-bold text-brand text-2xl">Quanto se sorteia</p>
      <table class="tbl">
        <thead><tr><th>Risco da modalidade</th><th class="num">% do Grupo A</th></tr></thead>
        <tbody>
          <tr><td>IRA 70 ou mais (ex.: travessia)</td><td class="num"><strong>10%</strong></td></tr>
          <tr><td>IRA entre 35 e 69</td><td class="num">7%</td></tr>
          <tr><td>IRA abaixo de 35 ou sem IRA</td><td class="num">5%</td></tr>
        </tbody>
      </table>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-arrow-up-right-dots text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">A sorteada entra com prioridade máxima</p>
          <p class="text-gray-600 text-lg mt-1">
            É tratada como C1 na lista do PAF, <strong>sem que sua faixa calculada mude</strong>.
            Ela lidera a listagem daquele ciclo — e o resultado da visita passa a alimentar o
            histórico dela.
          </p>
        </div>
      </div>
    </div>

    <div class="col-span-7 flex flex-col gap-3">
      <p class="font-montserrat font-bold text-brand text-2xl">Duas etapas separadas no tempo — é isso que o torna confiável</p>

      <div class="etapa">
        <div class="etapa-n">1</div>
        <div>
          <p class="etapa-t">Compromisso</p>
          <p class="etapa-d">
            Congela-se a lista de quem pode ser sorteado, com uma <strong>impressão digital</strong>
            dela, e registra-se <strong>qual número aleatório será usado</strong>: um pulso futuro do
            <strong>NIST Randomness Beacon</strong> — que <strong>ainda não existe</strong> no momento
            do compromisso.
          </p>
        </div>
      </div>
      <div class="seta"><i class="fas fa-arrow-down"></i></div>
      <div class="etapa">
        <div class="etapa-n">2</div>
        <div>
          <p class="etapa-t">Execução</p>
          <p class="etapa-d">
            Publicado o pulso, ele vira a semente do sorteio. O resultado é totalmente previsível a
            partir dos dois: <strong>mesma lista + mesma semente = mesmas sorteadas, sempre</strong>.
          </p>
        </div>
      </div>

      <div class="destaque">
        <p class="font-montserrat font-bold" style="font-size:calc(21px * var(--tz));">
          Como o número é escolhido <em>antes de existir</em>, ninguém pode rodar o sorteio,
          não gostar do resultado e trocar a semente.
        </p>
        <p class="text-blue-100 text-lg mt-2">
          O Beacon é numerado, datado, assinado e encadeado. Qualquer pessoa de fora refaz a conta
          com a lista, a semente e o algoritmo publicado — e tem de chegar exatamente à mesma lista.
          A tela <strong>Sorteio</strong> publica a ata em CSV para essa conferência.
        </p>
      </div>
    </div>
  </div>
""",
    extra_css="""
.etapa { display:flex; gap:16px; align-items:flex-start; background:#F8FAFC; border-radius:14px; padding:14px 20px; border-left:5px solid #0066CC; }
.etapa-n {
  width:40px; height:40px; border-radius:50%; flex-shrink:0;
  background:#003366; color:#fff; display:flex; align-items:center; justify-content:center;
  font-family:'Montserrat',sans-serif; font-weight:900; font-size:calc(19px * var(--tz));
}
.etapa-t { margin:0; font-family:'Montserrat',sans-serif; font-weight:700; color:#003366; font-size:calc(20px * var(--tz)); }
.etapa-d { margin:3px 0 0; color:#475569; font-size:calc(16px * var(--tz)); line-height:1.5; }
.seta { text-align:center; color:#94A3B8; font-size:calc(18px * var(--tz)); margin:-4px 0; }
""",
    base=1.39,
)

# ---------------------------------------------------------------------------
# 11 — Cadastro (NOVO)
# ---------------------------------------------------------------------------
slide(
    11,
    "Cadastro — CNPJ baixado e suspenso",
    "Novo em 2027 · tela Cadastro",
    "O CNPJ existe mesmo?",
    """
  <div class="px-16 pb-3 grid grid-cols-4 gap-4">
    <div class="stat-card"><p class="stat-num">2.133</p><p class="text-blue-200 text-sm font-semibold mt-2">CNPJs conferidos<br/>na Receita Federal</p></div>
    <div class="stat-card"><p class="stat-num">149</p><p class="text-blue-200 text-sm font-semibold mt-2">não estão ativos<br/>(7% do total)</p></div>
    <div class="stat-card"><p class="stat-num">68</p><p class="text-blue-200 text-sm font-semibold mt-2">outorgas fora da<br/>listagem do PAF 2027</p></div>
    <div class="stat-card"><p class="stat-num">0</p><p class="text-blue-200 text-sm font-semibold mt-2">bloqueios sem<br/>tratamento</p></div>
  </div>

  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">
    <div class="col-span-6 flex flex-col gap-3">
      <div class="card card-red">
        <div class="ico" style="background:#FECACA;"><i class="fas fa-file-circle-xmark text-red-600 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-2xl">O caso que motivou tudo</p>
          <p class="text-gray-600 text-lg mt-1">
            A <strong>ODSF nº 568/2026/URECB</strong> foi aberta contra a CPA Armazéns Gerais —
            CNPJ <strong>baixado desde 2022</strong>. Quem opera o terminal de Paranaguá é outra
            empresa, confirmado pela APPA.
          </p>
          <p class="text-gray-600 text-lg mt-1">
            O risco tinha sido calculado, e a fiscalização programada, <strong>sobre a empresa
            errada</strong>. Os sistemas internos não sabem quando um CNPJ é baixado na Receita.
          </p>
        </div>
      </div>

      <p class="font-montserrat font-bold text-brand text-2xl">O que a conferência encontrou</p>
      <table class="tbl">
        <thead><tr><th>Situação</th><th class="num">Outorgas</th><th>O que acontece</th></tr></thead>
        <tbody>
          <tr><td>Conforme</td><td class="num">2.254</td><td>segue no PAF sem ressalva</td></tr>
          <tr><td><strong>Baixada</strong>, sem sucessor</td><td class="num">38</td><td><span class="pill pill-c">sai do PAF</span></td></tr>
          <tr><td><strong>Baixada</strong>, com sucessor provável</td><td class="num">28</td><td><span class="pill pill-c">sai do PAF</span></td></tr>
          <tr><td><strong>Suspensa</strong></td><td class="num">2</td><td><span class="pill pill-c">sai do PAF</span></td></tr>
          <tr><td>Inapta</td><td class="num">83</td><td><span class="pill pill-a">continua no PAF</span></td></tr>
          <tr><td>Ativa, com divergência de cadastro</td><td class="num">73</td><td><span class="pill pill-a">continua no PAF</span></td></tr>
        </tbody>
      </table>
      <p class="legenda">
        <strong>Inapta continua</strong> de propósito: deixar de entregar declaração não extingue a
        empresa nem a obrigação regulatória. Tirar as 83 premiaria justamente quem não declara.
      </p>
    </div>

    <div class="col-span-6 flex flex-col gap-3">
      <p class="font-montserrat font-bold text-brand text-2xl">Quatro coisas que não se pode confundir</p>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-eye-slash text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">1. Inativar não é excluir</p>
          <p class="text-gray-600 text-lg mt-1">
            A outorga <strong>continua visível</strong> no painel, marcada. Ela só não entra na
            listagem do PAF. Ela precisa aparecer justamente na tela onde o problema dela é tratado.
          </p>
        </div>
      </div>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-user-check text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">2. A máquina propõe, a pessoa decide</p>
          <p class="text-gray-600 text-lg mt-1">
            A saída é <strong>imediata e protetiva</strong>; a conferência humana vem depois e pode
            <strong>reverter</strong>. Revertida, a máquina não reinativa enquanto a situação
            cadastral for a mesma. <strong>A decisão humana vence a regra.</strong>
          </p>
        </div>
      </div>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-rotate-left text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">3. CNPJ regularizado volta sozinho</p>
          <p class="text-gray-600 text-lg mt-1">
            Se a empresa se regulariza na Receita, a outorga retorna ao PAF na conferência seguinte —
            desde que a saída ainda fosse proposta da máquina.
          </p>
        </div>
      </div>

      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-folder-open text-green-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">4. O dossiê do CNPJ já vem pronto</p>
          <p class="text-gray-600 text-lg mt-1">
            Extinguir o termo de outorga é ato da área de outorgas, e ela decide sobre o
            <strong>instrumento</strong>. A tela reúne, por CNPJ, <strong>todas as outorgas, os
            283 instrumentos</strong> das quatro fontes (processo de outorga, terminal, operador
            portuário e arrendamento) e o histórico de fiscalização — sem abrir quatro sistemas à mão.
          </p>
        </div>
      </div>
    </div>
  </div>
""",
    tag=TAG_NOVO,
    base=1.05,
)

# ---------------------------------------------------------------------------
# 12 — Força de trabalho (NOVO)
# ---------------------------------------------------------------------------
slide(
    12,
    "Força de Trabalho — o PAF cabe?",
    "Novo em 2027 · tela Força de Trabalho",
    "O PAF cabe em quem o executa?",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">
    <div class="col-span-7 flex flex-col gap-3">
      <div class="formula" style="text-align:center; line-height:1.6;">
        ocupação &nbsp;=&nbsp; horas que o plano exige no ano &nbsp;&divide;&nbsp; horas que a equipe tem livres
      </div>
      <div class="flex gap-2">
        <span class="leg leg-v">abaixo de 70% · folga</span>
        <span class="leg leg-a">70% a 100% · justa</span>
        <span class="leg leg-o">100% a 130% · crítica</span>
        <span class="leg leg-r">acima de 130% · inviável</span>
      </div>

      <table class="tbl">
        <thead><tr>
          <th>Regional</th><th class="num">Equipe</th><th class="num">CNU</th>
          <th class="num">Capacidade c/ CNU</th><th class="num">Demanda h/ano</th>
          <th class="num">Sem reforço</th><th class="num">Com reforço</th>
        </tr></thead>
        <tbody>
          <tr class="row-r"><td><strong>URESN</strong> · Santana</td><td class="num">2</td><td class="num">+1</td><td class="num">918</td><td class="num">1.627</td><td class="num">292%</td><td class="num"><strong>177%</strong></td></tr>
          <tr class="row-o"><td><strong>GREBL</strong> · Belém</td><td class="num">16</td><td class="num">+7</td><td class="num">7.173</td><td class="num">5.601</td><td class="num">121%</td><td class="num"><strong>78%</strong></td></tr>
          <tr class="row-o"><td><strong>GREMN</strong> · Manaus</td><td class="num">14</td><td class="num">+7</td><td class="num">7.045</td><td class="num">4.876</td><td class="num">115%</td><td class="num"><strong>69%</strong></td></tr>
          <tr><td><strong>GRERJ</strong> · Rio de Janeiro</td><td class="num">11</td><td class="num">+2</td><td class="num">7.225</td><td class="num">2.373</td><td class="num">37%</td><td class="num">33%</td></tr>
          <tr><td><strong>UREPV</strong> · Porto Velho</td><td class="num">3</td><td class="num">—</td><td class="num">1.946</td><td class="num">617</td><td class="num">32%</td><td class="num">32%</td></tr>
          <tr><td><strong>URESL</strong> · São Luís</td><td class="num">7</td><td class="num">—</td><td class="num">5.839</td><td class="num">1.443</td><td class="num">25%</td><td class="num">25%</td></tr>
          <tr><td colspan="7" style="color:#64748B;">UREFT 21% · UREVT 21% · UREPL 16% · GREFL 16% · GREST 14% · URECB 8% · URESV 8% · GRERE 7%</td></tr>
        </tbody>
      </table>
      <p class="legenda">
        Cenário base: as 305 outorgas do Grupo C mais a expectativa do sorteio do Grupo A.
        Capacidade &ldquo;com reforço&rdquo; inclui os <strong>20 convocados do CNU</strong> lotados
        nas regionais, já com o rendimento reduzido de quem está começando.
      </p>
    </div>

    <div class="col-span-5 flex flex-col gap-3">
      <div class="destaque">
        <p class="font-montserrat font-bold" style="font-size:calc(24px * var(--tz));">
          O problema não é a Agência. É a distribuição.
        </p>
        <p class="text-blue-100 text-lg mt-2">
          <strong>22 mil horas</strong> de trabalho previsto contra <strong>66 mil horas</strong>
          disponíveis: a rede usa cerca de <strong>um terço</strong> da própria capacidade — e
          mesmo assim uma regional está com quase o dobro do que aguenta.
        </p>
      </div>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-database text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">De onde vêm as horas</p>
          <p class="text-gray-600 text-lg mt-1">
            Dos <strong>planos de trabalho do PGD (Hefesto)</strong>, de janeiro/2025 a julho/2026 —
            o que vocês pactuam e lançam todo mês. Não é estimativa de gabinete.
          </p>
        </div>
      </div>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-stopwatch text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Quanto custa uma fiscalização</p>
          <p class="text-gray-600 text-lg mt-1">
            Medido nos próprios lançamentos: <strong>72 h por processo</strong> na média.
            Porto organizado 92 h · arrendamento 84 h · TUP 72 h · outorga geral 66 h ·
            travessia registrada 58 h. Bate com a Tabela de Atividades da SFC dentro de 25%.
          </p>
        </div>
      </div>

      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-shield text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">A reserva é medida, não arbitrada</p>
          <p class="text-gray-600 text-lg mt-1">
            O PAF não pode ocupar 100% da equipe: há extraordinárias, sancionador, instrução
            processual, gestão e capacitação. Essa fatia sai do <strong>próprio PdT de cada
            regional</strong> — não é um percentual chutado.
          </p>
        </div>
      </div>
    </div>
  </div>
""",
    extra_css="""
.leg { border-radius:999px; padding:4px 14px; font-size:calc(13px * var(--tz)); font-weight:600; }
.leg-v { background:#DCFCE7; color:#166534; }
.leg-a { background:#FEF9C3; color:#854D0E; }
.leg-o { background:#FFEDD5; color:#9A3412; }
.leg-r { background:#FEE2E2; color:#991B1B; }
table.tbl tr.row-r td { background:#FEF2F2; }
table.tbl tr.row-o td { background:#FFF7ED; }
""",
    tag=TAG_NOVO,
    base=1.2,
)

# ---------------------------------------------------------------------------
# 13 — Equalização (NOVO)
# ---------------------------------------------------------------------------
slide(
    13,
    "Equalização da carga entre regionais",
    "Novo em 2027 · tela Equalização",
    "Dividir melhor o trabalho",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">
    <div class="col-span-6 flex flex-col gap-3">
      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-triangle-exclamation text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-2xl">Isso já acontecia — sem regra e sem registro</p>
          <p class="text-gray-600 text-lg mt-1">
            As fiscalizações de Santana vinham sendo feitas por equipes de fora, principalmente de
            Belém, em viagens de apoio. Sem regra escrita, sem registro de quem decidiu, e com as
            <strong>horas lançadas na conta de quem viajou</strong>.
          </p>
          <p class="text-gray-600 text-lg mt-1">
            Efeito colateral: a capacidade de Santana <em>parecia</em> maior do que é. Aqueles
            <strong>177% são piso, não teto</strong>.
          </p>
        </div>
      </div>

      <p class="font-montserrat font-bold text-brand text-2xl">Duas formas diferentes de dividir</p>
      <div class="modo">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-right-left text-accent text-2xl"></i></div>
        <div>
          <p class="modo-t">Transferência</p>
          <p class="modo-d">A outorga <strong>passa a ser de outra regional</strong> neste ciclo.
          Só vale para o que não exige ir ao local — análise documental, navegação marítima.</p>
        </div>
      </div>
      <div class="modo">
        <div class="ico" style="background:#DCFCE7;"><i class="fas fa-plane-departure text-green-700 text-2xl"></i></div>
        <div>
          <p class="modo-t">Missão de apoio</p>
          <p class="modo-d">A outorga <strong>fica onde está</strong> e uma equipe de fora vai até lá
          executar. As horas são debitadas de quem apoia. É o que já se fazia — agora com dono,
          registro e efeito no planejamento.</p>
        </div>
      </div>

      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-sitemap text-green-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">A jurisdição NÃO muda</p>
          <p class="text-gray-600 text-lg mt-1">
            Quem responde institucionalmente por cada outorga continua sendo quem sempre foi.
            A equalização é uma <strong>camada sobreposta, válida para o ciclo</strong> — ela diz
            quem <em>executa</em>, não quem <em>responde</em>.
          </p>
        </div>
      </div>
    </div>

    <div class="col-span-6 flex flex-col gap-3">
      <div class="grid grid-cols-3 gap-3">
        <div class="stat-card"><p class="stat-num" style="font-size:calc(38px * var(--tz));">177%&rarr;95%</p><p class="text-blue-200 text-sm font-semibold mt-2">ocupação de Santana</p></div>
        <div class="stat-card"><p class="stat-num">17</p><p class="text-blue-200 text-sm font-semibold mt-2">movimentos propostos<br/>(752 horas)</p></div>
        <div class="stat-card"><p class="stat-num">0</p><p class="text-blue-200 text-sm font-semibold mt-2">regionais acima<br/>do limite</p></div>
      </div>

      <table class="tbl">
        <thead><tr><th>O que a proposta faz</th><th class="num">Blocos</th><th class="num">Horas</th></tr></thead>
        <tbody>
          <tr><td>Transferências (a outorga muda de carteira)</td><td class="num">8</td><td class="num">110</td></tr>
          <tr><td>Missões de apoio (a equipe é que viaja)</td><td class="num">9</td><td class="num">642</td></tr>
          <tr><td colspan="3" style="color:#64748B;">Destinos: Santos, São Luís, Salvador e Recife — <strong>ninguém recebeu o problema inteiro</strong></td></tr>
        </tbody>
      </table>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-boxes-stacked text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Não se move uma outorga, move-se um bloco</p>
          <p class="text-gray-600 text-lg mt-1">
            Fiscalizar uma travessia ou vinte na mesma localidade custa quase o mesmo em
            deslocamento. Por isso o que viaja é o <strong>bloco inteiro</strong> — e ele não se
            quebra: ou vai todo, ou fica, com o motivo escrito.
          </p>
        </div>
      </div>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-compass text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Como o destino é escolhido</p>
          <p class="text-gray-600 text-lg mt-1">
            Quatro critérios com peso: <strong>folga 40%</strong> · <strong>proximidade 35%</strong> ·
            <strong>afinidade com a carteira 15%</strong> · <strong>jurisdição 10%</strong>.
            O relatório publica quanto a preferência por folga custou em quilômetros.
          </p>
        </div>
      </div>

      <div class="destaque">
        <p class="font-montserrat font-bold" style="font-size:calc(21px * var(--tz));">
          <i class="fas fa-user-pen mr-2"></i>A rodada propõe. Quem decide é gente.
        </p>
        <p class="text-blue-100 text-lg mt-1">
          Nenhum lote muda de responsável antes de alguém aprovar, lote por lote, com
          <strong>fundamento e nº SEI</strong>. Rodada nova não desfaz o que foi aprovado nem
          reapresenta o que foi rejeitado.
        </p>
      </div>
    </div>
  </div>
""",
    extra_css="""
.modo { display:flex; gap:14px; align-items:flex-start; background:#F8FAFC; border-radius:14px; padding:12px 18px; border-left:5px solid #0066CC; }
.modo-t { margin:0; font-family:'Montserrat',sans-serif; font-weight:700; color:#003366; font-size:calc(18px * var(--tz)); }
.modo-d { margin:2px 0 0; color:#475569; font-size:calc(15px * var(--tz)); line-height:1.45; }
""",
    tag=TAG_NOVO,
    base=1.05,
)

# ---------------------------------------------------------------------------
# 14 — De onde vem cada número
# ---------------------------------------------------------------------------
slide(
    14,
    "De onde vem cada número",
    "Seções &ldquo;Pipeline&rdquo; e &ldquo;Arquitetura&rdquo; da Ajuda",
    "De onde vem cada número",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-12 gap-5">
    <div class="col-span-5 flex flex-col gap-3">
      <p class="font-montserrat font-bold text-brand text-2xl">As fontes</p>
      <div class="fonte"><i class="fas fa-server"></i><div><p class="fonte-t">SQL Server da ANTAQ</p><p class="fonte-d">Fiscalização, Outorga, Corporativo, Arrendamento, SCP — o universo e os indicadores de comportamento. <strong>Acesso somente leitura.</strong></p></div></div>
      <div class="fonte"><i class="fas fa-building-columns"></i><div><p class="fonte-t">Receita Federal</p><p class="fonte-d">Situação cadastral de cada CNPJ. <span class="pill pill-gold">novo</span></p></div></div>
      <div class="fonte"><i class="fas fa-user-clock"></i><div><p class="fonte-t">PGD / Hefesto</p><p class="fonte-d">Planos de trabalho, horas por atividade e equipes. <span class="pill pill-gold">novo</span></p></div></div>
      <div class="fonte"><i class="fas fa-chart-column"></i><div><p class="fonte-t">PIF e Estatístico Aquaviário</p><p class="fonte-d">Execução histórica da fiscalização e volume movimentado.</p></div></div>
      <div class="fonte"><i class="fas fa-dice"></i><div><p class="fonte-t">NIST Randomness Beacon</p><p class="fonte-d">A semente pública do sorteio do Grupo A. <span class="pill pill-gold">novo</span></p></div></div>
    </div>

    <div class="col-span-7 flex flex-col gap-3">
      <p class="font-montserrat font-bold text-brand text-2xl">O caminho</p>
      <div class="formula" style="line-height:1.9;">
        SQL Server ANTAQ <span style="color:#64748B;">(somente leitura)</span><br/>
        &nbsp;&nbsp;&darr;&nbsp; extração parametrizada pela data de referência<br/>
        Banco do painel <span style="color:#64748B;">(cópia local, congelada por ciclo)</span><br/>
        &nbsp;&nbsp;&darr;&nbsp; ICF, IVO, sorteio, verificação cadastral, força de trabalho<br/>
        &nbsp;&nbsp;&darr;&nbsp; recálculo do IPR e classificação em A1..C4<br/>
        Painel e API
      </div>

      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-calendar-day text-green-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">A data de referência é 30 de setembro do ano anterior</p>
          <p class="text-gray-600 text-lg mt-1">
            O PAF de 2027 é montado com o corte de <strong>30/09/2026</strong>. Não há exceção —
            é o que permite comparar um ciclo com o outro.
          </p>
        </div>
      </div>

      <div class="card">
        <div class="ico" style="background:#DBEAFE;"><i class="fas fa-fingerprint text-accent text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Mesmo ciclo, mesma data, mesmo resultado</p>
          <p class="text-gray-600 text-lg mt-1">
            Todo cálculo é reproduzível. O retrato bruto de cada ciclo fica
            <strong>congelado antes de qualquer tratamento</strong> — é o que permite reconferir
            depois o que a fonte realmente devolveu.
          </p>
        </div>
      </div>

      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-lock text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Nada é gravado nos sistemas de origem</p>
          <p class="text-gray-600 text-lg mt-1">
            O painel só lê. Correção de dado errado se faz no sistema de origem; quando a origem
            tem lacuna conhecida, a decisão vai para uma <strong>tabela de exceções com autor e
            fundamento</strong> — e nasce para ser aposentada quando a origem for corrigida.
          </p>
        </div>
      </div>
    </div>
  </div>
""",
    extra_css="""
.fonte { display:flex; gap:14px; align-items:flex-start; background:#F8FAFC; border-radius:12px; padding:10px 16px; border-left:5px solid #0066CC; }
.fonte i { color:#0066CC; font-size:calc(19px * var(--tz)); width:26px; text-align:center; margin-top:3px; }
.fonte-t { margin:0; font-family:'Montserrat',sans-serif; font-weight:700; color:#003366; font-size:calc(17px * var(--tz)); }
.fonte-d { margin:2px 0 0; color:#475569; font-size:calc(14px * var(--tz)); line-height:1.4; }
""",
    base=1.2,
)

# ---------------------------------------------------------------------------
# 15 — O painel
# ---------------------------------------------------------------------------
slide(
    15,
    "O painel — as telas",
    "Onde ver tudo isso",
    "O painel, tela por tela",
    """
  <div class="flex-1 px-16 pb-2 flex flex-col gap-4">
    <div class="grid grid-cols-3 gap-3 flex-1 telas-grid">
      <div class="tela"><i class="fas fa-table-columns"></i><div><p class="tela-t">Executiva</p><p class="tela-d">O retrato do ciclo: distribuição por faixa, por segmento e a <strong>carga de cada regional</strong>.</p></div></div>
      <div class="tela"><i class="fas fa-table-list"></i><div><p class="tela-t">Analítica</p><p class="tela-d">A lista completa, filtrável por faixa, regional, UF, modalidade. Exporta em CSV.</p></div></div>
      <div class="tela"><i class="fas fa-clipboard-list"></i><div><p class="tela-t">Apoio ao PAF</p><p class="tela-d">A listagem priorizada do ciclo e o simulador: e se o peso do ICF fosse outro?</p></div></div>
      <div class="tela"><i class="fas fa-id-badge"></i><div><p class="tela-t">Ficha da outorga</p><p class="tela-d">A nota decomposta indicador por indicador, com o histórico de fiscalizações.</p></div></div>
      <div class="tela tela-novo"><i class="fas fa-dice"></i><div><p class="tela-t">Sorteio</p><p class="tela-d">Compromisso, semente do Beacon e a ata em CSV para conferência externa.</p></div></div>
      <div class="tela tela-novo"><i class="fas fa-id-card"></i><div><p class="tela-t">Cadastro</p><p class="tela-d">A fila de validação dos CNPJs baixados e suspensos, com o <strong>dossiê do CNPJ</strong>.</p></div></div>
      <div class="tela tela-novo"><i class="fas fa-gauge-high"></i><div><p class="tela-t">Força de Trabalho</p><p class="tela-d">Demanda × capacidade por regional, com os participantes do PGD por linha.</p></div></div>
      <div class="tela tela-novo"><i class="fas fa-scale-balanced"></i><div><p class="tela-t">Equalização</p><p class="tela-d">A proposta de redistribuição, lote a lote, com aprovar / rejeitar / redirecionar.</p></div></div>
      <div class="tela"><i class="fas fa-triangle-exclamation"></i><div><p class="tela-t">Alertas</p><p class="tela-d">O que está estranho no ciclo: lacunas, saltos de faixa, atribuições fracas.</p></div></div>
      <div class="tela"><i class="fas fa-chart-line"></i><div><p class="tela-t">Histórico</p><p class="tela-d">Os quatro ciclos lado a lado — quem subiu, quem desceu e por quê.</p></div></div>
      <div class="tela"><i class="fas fa-circle-question"></i><div><p class="tela-t">Ajuda</p><p class="tela-d">Esta apresentação inteira, em texto, sempre atualizada com os números do banco.</p></div></div>
      <div class="tela"><i class="fas fa-code"></i><div><p class="tela-t">API</p><p class="tela-d">Para quem quiser puxar os dados para uma planilha ou outro sistema.</p></div></div>
    </div>

    <div class="destaque flex items-center gap-8">
      <div class="flex items-center gap-4" style="flex:0 0 auto;">
        <i class="fas fa-globe text-4xl gold" style="color:#FFD700;"></i>
        <div>
          <p class="text-blue-100 text-sm uppercase tracking-widest font-semibold">Endereço</p>
          <p class="font-montserrat font-bold" style="font-size:calc(24px * var(--tz)); white-space:nowrap;">ipr-paf.up.railway.app</p>
        </div>
      </div>
      <div class="flex items-center gap-4 border-l border-blue-400 pl-8" style="border-color:rgba(255,255,255,0.25); flex:0 0 auto;">
        <i class="fas fa-right-to-bracket text-3xl" style="color:#FFD700;"></i>
        <div>
          <p class="text-blue-100 text-sm uppercase tracking-widest font-semibold">Acesso</p>
          <p class="font-montserrat font-bold text-xl" style="white-space:nowrap;">Login com a sua conta <strong>@antaq.gov.br</strong></p>
        </div>
      </div>
      <div class="ml-auto text-right" style="min-width:0;">
        <p class="text-blue-100 text-base">Dúvida sobre um número da tela?</p>
        <p class="font-montserrat font-bold text-lg">Todo bloco tem um <i class="fas fa-circle-question"></i> que explica de onde ele veio.</p>
      </div>
    </div>
  </div>
""",
    extra_css="""
.telas-grid { align-content:space-around; grid-auto-rows:min-content; }
.tela { display:flex; gap:13px; align-items:flex-start; background:#F8FAFC; border-radius:13px; padding:11px 16px; border-left:5px solid #0066CC; }
.tela-novo { background:linear-gradient(135deg,#FFFBEB,#FEF3C7); border-left-color:#F59E0B; }
.tela i { color:#0066CC; font-size:calc(19px * var(--tz)); width:26px; text-align:center; margin-top:2px; }
.tela-novo i { color:#D97706; }
.tela-t { margin:0; font-family:'Montserrat',sans-serif; font-weight:700; color:#003366; font-size:calc(17px * var(--tz)); }
.tela-d { margin:2px 0 0; color:#475569; font-size:calc(14px * var(--tz)); line-height:1.4; }
""",
    base=1.4,
)

# ---------------------------------------------------------------------------
# 16 — O que muda para a sua Regional
# ---------------------------------------------------------------------------
slide(
    16,
    "O que muda para a sua Regional",
    "O prático",
    "O que muda para a sua Regional",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-2 gap-5">
    <div class="flex flex-col gap-3">
      <p class="font-montserrat font-bold text-brand text-3xl"><i class="fas fa-gift text-accent mr-2"></i>O que vocês ganham</p>

      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-list-check text-green-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Uma lista que não tem empresa extinta</p>
          <p class="text-gray-600 text-lg mt-1">Nenhuma ODSF sai contra CNPJ baixado. Foram 68 casos evitados só em 2027.</p>
        </div>
      </div>
      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-gauge text-green-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">O argumento de carga vira número</p>
          <p class="text-gray-600 text-lg mt-1">&ldquo;Não cabe na equipe&rdquo; deixou de ser impressão: é horas por ano, medidas no PGD de vocês, publicadas na tela.</p>
        </div>
      </div>
      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-handshake-angle text-green-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">Apoio com dono e registro</p>
          <p class="text-gray-600 text-lg mt-1">A missão de apoio deixa de ser combinação informal: tem proposta, aprovação, fundamento e nº SEI — e as horas contam para quem apoia.</p>
        </div>
      </div>
      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-folder-tree text-green-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">O levantamento já vem pronto</p>
          <p class="text-gray-600 text-lg mt-1">O dossiê do CNPJ reúne outorgas, instrumentos e fiscalizações num lugar só — em vez de quatro sistemas abertos à mão.</p>
        </div>
      </div>
    </div>

    <div class="flex flex-col gap-3">
      <p class="font-montserrat font-bold text-brand text-3xl"><i class="fas fa-hand-point-right text-accent mr-2"></i>O que precisamos de vocês</p>

      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-keyboard text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">1. Lançar o PdT com cuidado</p>
          <p class="text-gray-600 text-lg mt-1">A capacidade e o custo por fiscalização saem <strong>daí</strong>. Lançamento genérico vira reserva alta e capacidade baixa — e o número que volta para vocês fica pior do que a realidade.</p>
        </div>
      </div>
      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-clipboard-check text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">2. Registrar a ação fiscal</p>
          <p class="text-gray-600 text-lg mt-1">O ICF lê a data da última fiscalização. Ação não registrada mantém a outorga como &ldquo;nunca visitada&rdquo; e ela volta na lista do ano seguinte.</p>
        </div>
      </div>
      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-map-pin text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">3. Conferir a jurisdição da sua carteira</p>
          <p class="text-gray-600 text-lg mt-1">A tela Executiva mostra quais outorgas estão atribuídas a vocês. Divergência conhecida vira <strong>exceção registrada</strong> — avisem a GPF em vez de resolver por fora.</p>
        </div>
      </div>
      <div class="card card-amber">
        <div class="ico" style="background:#FDE68A;"><i class="fas fa-square-check text-yellow-700 text-2xl"></i></div>
        <div>
          <p class="font-montserrat font-bold text-brand text-xl">4. Decidir o que está na fila</p>
          <p class="text-gray-600 text-lg mt-1">68 casos de cadastro aguardam conferência e 17 lotes de equalização aguardam aprovação. <strong>Nada disso anda sozinho</strong> — é decisão humana, por desenho.</p>
        </div>
      </div>
    </div>
  </div>
""",
    base=1.3,
)

# ---------------------------------------------------------------------------
# 17 — Glossário
# ---------------------------------------------------------------------------
slide(
    17,
    "Glossário",
    "Para consulta",
    "Glossário",
    """
  <div class="flex-1 px-16 pb-2 grid grid-cols-3 gap-x-6 gap-y-0">
    <div class="glos"><span class="g-t">PAF</span><span class="g-d">Plano Anual de Fiscalização — a lista do que será fiscalizado no ano</span></div>
    <div class="glos"><span class="g-t">PPF</span><span class="g-d">Plano Plurianual de Fiscalização (2025–2028)</span></div>
    <div class="glos"><span class="g-t">IPR</span><span class="g-d">Índice de Perfil de Risco — a nota de 0 a 100 de cada outorga</span></div>
    <div class="glos"><span class="g-t">Outorga</span><span class="g-d">O instrumento que autoriza operar: autorização, contrato ou registro</span></div>
    <div class="glos"><span class="g-t">Chave</span><span class="g-d">Identificador da outorga: CNPJ + modalidade + trecho ou terminal</span></div>
    <div class="glos"><span class="g-t">Faixa</span><span class="g-d">A classificação de A1 a C4 que decide o tratamento fiscal</span></div>
    <div class="glos"><span class="g-t">ICF</span><span class="g-d">Indicador de Cobertura Fiscalizatória — há quanto tempo não se fiscaliza</span></div>
    <div class="glos"><span class="g-t">IVO</span><span class="g-d">Indicador de Volume Operacional — o porte da operação</span></div>
    <div class="glos"><span class="g-t">IRA</span><span class="g-d">Indicador de Risco da Atividade — risco próprio da modalidade</span></div>
    <div class="glos"><span class="g-t">F_IRA</span><span class="g-d">O piso de nota que o IRA garante à outorga</span></div>
    <div class="glos"><span class="g-t">IRI · IGI · IOC</span><span class="g-d">Reincidência · gravidade · ocorrência crítica</span></div>
    <div class="glos"><span class="g-t">INN · IOU · IIN</span><span class="g-d">NoCI descumprida · denúncia que virou sanção · irregularidade normativa</span></div>
    <div class="glos"><span class="g-t">NoCI</span><span class="g-d">Notificação para Correção de Irregularidade</span></div>
    <div class="glos"><span class="g-t">ODSF</span><span class="g-d">Ordem de Serviço de Fiscalização</span></div>
    <div class="glos"><span class="g-t">TAC</span><span class="g-d">Termo de Ajustamento de Conduta</span></div>
    <div class="glos"><span class="g-t">TA</span><span class="g-d">Termo de Autorização — o instrumento que a área de outorgas revoga</span></div>
    <div class="glos"><span class="g-t">EBN</span><span class="g-d">Empresa Brasileira de Navegação</span></div>
    <div class="glos"><span class="g-t">TUP · ETC · IPTur</span><span class="g-d">Terminal de Uso Privado · Estação de Transbordo de Cargas · Instalação Portuária de Turismo</span></div>
    <div class="glos"><span class="g-t">PGD · Hefesto</span><span class="g-d">Programa de Gestão por Desempenho e o sistema onde o PdT é pactuado</span></div>
    <div class="glos"><span class="g-t">PdT · TCR</span><span class="g-d">Plano de Trabalho mensal · Termo de Ciência e Responsabilidade</span></div>
    <div class="glos"><span class="g-t">Ocupação</span><span class="g-d">Horas que o plano exige ÷ horas que a equipe tem livres</span></div>
    <div class="glos"><span class="g-t">Reserva</span><span class="g-d">A fatia das horas comprometida com o que não é PAF</span></div>
    <div class="glos"><span class="g-t">Lote</span><span class="g-d">O conjunto de outorgas que viaja junto na equalização</span></div>
    <div class="glos"><span class="g-t">Missão de apoio</span><span class="g-d">A outorga fica; a equipe de outra regional vai executar</span></div>
    <div class="glos"><span class="g-t">Jurisdição</span><span class="g-d">Quem responde institucionalmente pela outorga — não muda com a equalização</span></div>
    <div class="glos"><span class="g-t">CNU</span><span class="g-d">Concurso Nacional Unificado — 20 convocados lotados nas regionais</span></div>
    <div class="glos"><span class="g-t">GPF</span><span class="g-d">Gerência de Planejamento e Inteligência da Fiscalização</span></div>
    <div class="glos"><span class="g-t">SFC</span><span class="g-d">Superintendência de Fiscalização e Coordenação das Unidades Regionais</span></div>
    <div class="glos"><span class="g-t">NT 9 · NT 11 · NT 19</span><span class="g-d">As Notas Técnicas que fundamentam o índice e o plano</span></div>
  </div>
""",
    extra_css="""
.glos { display:flex; flex-direction:column; padding:6px 0; border-bottom:1px solid #F1F5F9; }
.g-t { font-family:'Montserrat',sans-serif; font-weight:900; color:#003366; font-size:calc(15px * var(--tz)); letter-spacing:0.02em; }
.g-d { color:#64748B; font-size:calc(13.5px * var(--tz)); line-height:1.35; }
""",
    base=1.28,
)

# ---------------------------------------------------------------------------
# 18 — Encerramento
# ---------------------------------------------------------------------------
SLIDES.append(dict(n=18, raw=True))


def render(s):
    # `--tz-base` diz ao zoom.js em que tamanho este slide foi fechado; o + / - do
    # usuario multiplica essa base. Slide denso fica perto de 1, slide arejado sobe.
    css = f':root {{ --tz-base: {s.get("base", 1.0) * TEXT_SCALE:.4g}; }}\n' + BASE_CSS + s.get("extra_css", "")
    return HEAD.format(
        title=s["title"],
        css=css,
        kicker=s["kicker"],
        titulo=s["titulo"],
        tag=s.get("tag", ""),
        body=s["body"],
        rodape=RODAPE,
        n=s["n"],
        total=TOTAL,
    )


for s in SLIDES:
    if s.get("raw"):
        continue
    (DST / f"slide-{s['n']:02d}.html").write_text(render(s), encoding="utf-8")
    print(f"slide-{s['n']:02d}.html")
