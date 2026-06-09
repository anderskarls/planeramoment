# Arkiv v2.1 - designsystem för klassrumspresentationer (reveal.js)

Self-contained specifikation av designsystemet **Arkiv v2.1** för lektionspresentationer. Extraherad från referensimplementationen (momentet "1914-1945 Aktör och struktur", `github.com/anderskarls/varldskrigen-aktor-struktur`). Pluginen är självförsörjande - ingen extern skill behövs.

## Designprinciper

- **Papper, inte skärm:** allt innehåll ligger på papperston `#F4EDE1` (`--paper`), sidans bakgrund är bläcksvart (`--ink`). Mörka slides (question, section, quote, discuss) använder en accentfärg som fond med ljus text.
- **Tre typsnitt, tre röster:** Cormorant Garamond (serif) för rubriker och det eftertänksamma; Inter Tight (sans) för brödtext; JetBrains Mono för metadata (masthead, baseline, eyebrows, etiketter).
- **Bordeaux är signaturfärgen.** Max 2 accentfärger per slide. Paletten: `--bordeaux #7A2E2E`, `--marin #2C3E55`, `--oliv #5A6A3A`, `--ocker #B8862F`, `--kritbla #5A7A9A`, `--mossgron #3E5A3E`, `--tegel #C96442`.
- **Rubriker bär mening:** frågor som titlar där det går, exakt ett kursivt nyckelord per rubrik (`<em>ord</em>`).
- **Max 3 nyckelpunkter per slide.** Diskussionspaus (discuss/question) var 3-4:e slide.
- **Inga emojis.** Bara typografiska tecken: `▸ ● ▪ § №` och `·` som avskiljare.
- **Talarnoter på varje slide** (`<aside class="notes">`) med lärarhandledning, exakta formuleringar och tidsangivelser.

## Betoningsvokabulär (i brödtext och rubriker)

| Markup | Effekt | Används för |
|---|---|---|
| `<em>` | kursiv serif, halvfet | DET kursiva nyckelordet i rubriker; eftertryck i löptext |
| `<strong>` | extra fet | begrepp och nyckeltermer |
| `<mark>` | ockragul överstrykning | det enskilt viktigaste i en mening (sparsamt) |
| `<u>` | tjock bordeaux-underline | kontrasterande nyckelord (ocker på mörka slides) |

`class="fragment"` på listelement ger stegvis avslöjande - använd i bullets, questions, twocol-kolumner och timeline-events.

## Chrome - ramen på varje slide

Varje standardslide omsluts av `<div class="chrome paper">` (ljus) eller `<div class="chrome dark" style="background: var(--FÄRG);">` (mörk; sätt samma färg som inline-bakgrund på `<section>` med `!important`):

- **Masthead** (överst): `<div class="masthead"><span>[Kurs] · [Moment]</span><span>Lektion [N] / [M]</span></div>`
- **Baseline** (nederst): `<div class="baseline"><span>Arkiv · v2.1</span><span>[slide-nr] / [totalt]</span></div>`
- Däremellan: `<div class="body [typ]-slide">...</div>`

Undantag: cover, callout och content-highlight har egen ram (se katalogen).

## Boilerplate - kopiera ordagrant

HTML-skelettet nedan innehåller hela CSS:en. Kopiera det rakt av till varje ny presentation och lägg slides mellan `<div class="slides">` och `</div>`. Ändra inte designtokens.

```html
<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lektion [N] - [Titel]</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter+Tight:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --ink: #1F1A15; --ink-2: #4A3F33;
    --paper: #F4EDE1; --paper-2: #EBE1CF;
    --rule: #2A221A;
    --bordeaux: #7A2E2E; --marin: #2C3E55; --oliv: #5A6A3A; --ocker: #B8862F;
    --kritbla: #5A7A9A; --mossgron: #3E5A3E; --tegel: #C96442;
    --serif: "Cormorant Garamond", Georgia, serif;
    --sans: "Inter Tight", system-ui, sans-serif;
    --mono: "JetBrains Mono", ui-monospace, monospace;
  }
  html, body { background: var(--ink); }
  .reveal { font-family: var(--sans); color: var(--ink); font-size: 28px; font-weight: 500; }
  .reveal .slides { text-align: left; }
  .reveal .slides section { background: var(--paper); padding: 0; height: 100%; }
  .reveal .slides section.present { display: flex !important; flex-direction: column; }

  .chrome { width: 100%; height: 100%; padding: 32px 56px 28px; display: flex; flex-direction: column; position: relative; overflow: hidden; }
  .chrome.paper { background: var(--paper); color: var(--ink); }
  .chrome.dark { color: var(--paper); }
  .chrome .masthead { display: flex; justify-content: space-between; align-items: baseline; font-family: var(--mono); font-size: 16px; letter-spacing: 2px; text-transform: uppercase; font-weight: 600; flex-shrink: 0; padding-bottom: 12px; }
  .chrome .baseline { display: flex; justify-content: space-between; align-items: baseline; font-family: var(--mono); font-size: 15px; letter-spacing: 2px; text-transform: uppercase; font-weight: 600; flex-shrink: 0; padding-top: 12px; }
  .chrome.paper .masthead { color: var(--ink-2); border-bottom: 2px solid var(--rule); }
  .chrome.paper .baseline { color: var(--ink-2); border-top: 2px solid var(--rule); }
  .chrome.dark .masthead { color: var(--paper); opacity: 0.7; border-bottom: 2px solid rgba(244,237,225,0.27); }
  .chrome.dark .baseline { color: var(--paper); opacity: 0.7; border-top: 2px solid rgba(244,237,225,0.27); }
  .chrome .body { flex: 1; display: flex; flex-direction: column; min-height: 0; padding: 32px 0; overflow: hidden; }

  /* Typografi */
  .reveal h1, .reveal h2, .reveal h3 { font-family: var(--serif); color: inherit; font-weight: 600; letter-spacing: -0.015em; text-transform: none; margin: 0; }
  .reveal h1 { line-height: 1; }
  .reveal h3 { font-family: var(--sans); font-size: 22px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; }
  .reveal em { font-style: italic; font-family: var(--serif); font-weight: 600; }
  .reveal strong, .reveal b { font-weight: 800; }
  .reveal mark { background: rgba(184,134,47,0.4); color: inherit; padding: 0 8px; border-radius: 2px; font-weight: 700; }
  .reveal u { text-decoration: underline; text-decoration-color: var(--bordeaux); text-decoration-thickness: 4px; text-underline-offset: 6px; font-weight: 700; }
  .chrome.dark mark { background: rgba(184,134,47,0.55); }
  .chrome.dark u { text-decoration-color: var(--ocker); }

  .eyebrow { font-family: var(--mono); font-size: 18px; letter-spacing: 2px; text-transform: uppercase; font-weight: 700; margin-bottom: 16px; color: var(--bordeaux); }
  .eyebrow::before { content: "▸ "; }
  .chrome.dark .eyebrow { color: var(--ocker); }
  .lede { font-family: var(--serif); font-style: italic; font-weight: 500; font-size: 32px; line-height: 1.3; margin-top: 22px; color: var(--ink-2); max-width: 32ch; }
  .chrome.dark .lede { color: var(--paper); opacity: 0.9; }
  .body-text { font-family: var(--sans); font-size: 28px; line-height: 1.45; max-width: 32em; font-weight: 500; }

  /* COVER */
  .reveal .slides section.cover-outer { background: var(--bordeaux); padding: 36px; }
  .cover-inner { width: 100%; height: 100%; background: var(--paper); padding: 56px 72px; display: flex; flex-direction: column; justify-content: space-between; }
  .cover-inner .top { display: flex; justify-content: space-between; font-family: var(--mono); font-size: 17px; letter-spacing: 2px; text-transform: uppercase; color: var(--bordeaux); font-weight: 700; }
  .cover-inner h1 { font-size: 116px; line-height: 0.95; letter-spacing: -2px; color: var(--ink); }
  .cover-inner .subtitle { font-family: var(--serif); font-size: 36px; font-style: italic; color: var(--ink-2); margin-top: 18px; max-width: 28ch; font-weight: 500; }
  .cover-inner .bottom { display: flex; justify-content: space-between; font-family: var(--mono); font-size: 16px; letter-spacing: 2px; text-transform: uppercase; color: var(--ink-2); font-weight: 600; }

  /* SECTION */
  .section-slide { display: grid !important; grid-template-columns: 1fr 1.1fr; gap: 40px; align-items: center; flex: 1; padding: 0 !important; }
  .section-slide .big-num { font-family: var(--serif); font-size: 340px; font-weight: 500; color: var(--paper); opacity: 0.2; line-height: 0.8; letter-spacing: -8px; }
  .section-slide .kapitel { font-family: var(--mono); font-size: 18px; letter-spacing: 2px; text-transform: uppercase; color: var(--ocker); margin-bottom: 20px; font-weight: 700; }
  .section-slide h1 { font-size: 96px; letter-spacing: -1.5px; color: var(--paper); line-height: 0.98; }
  .section-slide .lede { color: var(--paper); opacity: 0.9; max-width: 26ch; margin-top: 22px; }

  /* QUESTION */
  .question-slide { justify-content: center; }
  .question-slide h1 { font-size: 104px; line-height: 1; letter-spacing: -1.5px; color: var(--paper); max-width: 15ch; }
  .question-slide .lede { color: var(--paper); opacity: 0.92; max-width: 38ch; margin-top: 32px; font-size: 34px; }

  /* CONTENT */
  .content-slide h1 { font-size: 72px; max-width: 18ch; margin-bottom: 36px; color: var(--ink); letter-spacing: -1px; }
  .content-slide .body-text { color: var(--ink); }
  .bullets { list-style: none; padding: 0; margin: 28px 0 0; }
  .bullets li { display: flex; gap: 22px; padding: 16px 0; align-items: baseline; }
  .bullets li + li { border-top: 2px solid rgba(74,63,51,0.2); }
  .bullets .index { font-family: var(--mono); font-size: 24px; color: var(--ocker); font-weight: 700; width: 44px; flex-shrink: 0; }
  .bullets li > span:last-child { font-size: 28px; line-height: 1.4; color: var(--ink); font-weight: 500; }

  /* CONTENT-HIGHLIGHT */
  .ch-grid { width: 100%; height: 100%; display: grid; grid-template-columns: 1.3fr 1fr; }
  .ch-left { background: var(--paper); padding: 32px 56px 28px; display: flex; flex-direction: column; }
  .ch-left .meta-top { font-family: var(--mono); font-size: 16px; letter-spacing: 2px; text-transform: uppercase; color: var(--ink-2); border-bottom: 2px solid var(--rule); padding-bottom: 12px; font-weight: 600; }
  .ch-left .content { flex: 1; padding: 32px 0; display: flex; flex-direction: column; justify-content: center; }
  .ch-left h1 { font-size: 62px; line-height: 1; max-width: 14ch; margin-bottom: 28px; color: var(--ink); letter-spacing: -0.8px; }
  .ch-left .body-text { font-size: 25px; line-height: 1.45; color: var(--ink); }
  .ch-left .meta-bot { font-family: var(--mono); font-size: 15px; letter-spacing: 2px; text-transform: uppercase; color: var(--ink-2); border-top: 2px solid var(--rule); padding-top: 12px; font-weight: 600; }
  .ch-right { padding: 32px 48px 28px; color: var(--paper); display: flex; flex-direction: column; }
  .ch-right .meta-top { font-family: var(--mono); font-size: 16px; letter-spacing: 2px; text-transform: uppercase; color: var(--ocker); border-bottom: 2px solid rgba(244,237,225,0.27); padding-bottom: 12px; font-weight: 700; }
  .ch-right .stat { flex: 1; display: flex; flex-direction: column; justify-content: center; }
  .ch-right .stat-label { font-family: var(--mono); font-size: 16px; letter-spacing: 2px; text-transform: uppercase; color: var(--ocker); margin-bottom: 14px; font-weight: 700; }
  .ch-right .stat-number { font-family: var(--serif); font-size: 190px; font-weight: 600; line-height: 0.9; letter-spacing: -4px; color: var(--paper); }
  .ch-right .stat-caption { font-family: var(--serif); font-size: 26px; font-style: italic; color: var(--paper); opacity: 0.92; margin-top: 18px; line-height: 1.35; font-weight: 500; }
  .ch-right .meta-bot { font-family: var(--mono); font-size: 15px; letter-spacing: 2px; text-transform: uppercase; color: var(--paper); opacity: 0.8; border-top: 2px solid rgba(244,237,225,0.27); padding-top: 12px; text-align: right; font-weight: 600; }

  /* TIMELINE */
  .timeline-slide h1 { font-size: 62px; line-height: 1; margin: 0 0 60px; color: var(--ink); letter-spacing: -1px; }
  .timeline-h { flex: 1; position: relative; display: flex; align-items: flex-start; }
  .timeline-h::before { content: ""; position: absolute; left: 0; right: 0; top: 34px; height: 4px; background: var(--ocker); }
  .timeline-h .events { display: grid; width: 100%; gap: 20px; }
  .timeline-h .event { position: relative; padding-top: 64px; }
  .timeline-h .event .dot { position: absolute; left: 0; top: 24px; width: 22px; height: 22px; border-radius: 11px; background: var(--paper); border: 5px solid var(--bordeaux); }
  .timeline-h .event .year { font-family: var(--mono); font-size: 26px; color: var(--bordeaux); font-weight: 700; letter-spacing: 1px; }
  .timeline-h .event .title { font-family: var(--serif); font-size: 32px; font-style: italic; font-weight: 600; color: var(--ink); margin-top: 8px; line-height: 1.1; }
  .timeline-h .event .note { font-size: 22px; color: var(--ink); margin-top: 12px; line-height: 1.4; font-weight: 500; }

  /* QUOTE */
  .quote-slide { position: relative; padding-left: 96px !important; justify-content: center; }
  .quote-slide .mark-open { position: absolute; top: -40px; left: -10px; font-family: var(--serif); font-size: 240px; line-height: 1; color: var(--ocker); font-weight: 600; }
  .quote-slide blockquote { font-family: var(--serif); font-size: 62px; font-style: italic; line-height: 1.2; color: var(--paper); max-width: 22ch; letter-spacing: -0.5px; font-weight: 600; margin: 0; }
  .quote-slide .attribution { margin-top: 44px; font-size: 30px; font-weight: 700; color: var(--ocker); }
  .quote-slide .attribution::before { content: "— "; }
  .quote-slide .context { margin-top: 10px; font-family: var(--mono); font-size: 16px; letter-spacing: 2px; text-transform: uppercase; color: var(--paper); opacity: 0.8; font-weight: 600; }

  /* CALLOUT */
  .reveal .slides section.callout-outer { padding: 36px; }
  .reveal .slides section.callout-outer.fakta { background: var(--marin); }
  .reveal .slides section.callout-outer.tips { background: var(--oliv); }
  .reveal .slides section.callout-outer.varning { background: var(--bordeaux); }
  .reveal .slides section.callout-outer.kalla { background: var(--ink); }
  .reveal .slides section.callout-outer.begrepp { background: var(--ocker); }
  .callout-inner { width: 100%; height: 100%; background: var(--paper-2); padding: 56px 72px; display: flex; flex-direction: column; justify-content: space-between; }
  .callout-inner .top { display: flex; justify-content: space-between; font-family: var(--mono); font-size: 18px; letter-spacing: 2px; text-transform: uppercase; font-weight: 800; }
  .callout-outer.fakta .callout-inner .top { color: var(--marin); }
  .callout-outer.tips .callout-inner .top { color: var(--oliv); }
  .callout-outer.varning .callout-inner .top { color: var(--bordeaux); }
  .callout-outer.kalla .callout-inner .top { color: var(--ink); }
  .callout-outer.begrepp .callout-inner .top { color: var(--ocker); }
  .callout-inner h1 { font-family: var(--serif); font-size: 64px; font-style: italic; font-weight: 600; line-height: 1.05; color: var(--ink); max-width: 22ch; }
  .callout-inner .body-text { font-size: 30px; line-height: 1.45; color: var(--ink); margin-top: 28px; max-width: 26em; font-weight: 500; }
  .callout-inner .bottom { font-family: var(--mono); font-size: 15px; letter-spacing: 2px; text-transform: uppercase; color: var(--ink-2); display: flex; justify-content: space-between; font-weight: 600; }

  /* DATA */
  .data-slide { justify-content: center; }
  .data-slide .d-eyebrow { font-family: var(--mono); font-size: 18px; letter-spacing: 2px; text-transform: uppercase; color: var(--ink-2); margin-bottom: 8px; font-weight: 700; }
  .data-slide .d-number { font-family: var(--serif); font-size: 260px; line-height: 0.85; font-weight: 600; letter-spacing: -6px; color: var(--bordeaux); }
  .data-slide.ocker .d-number { color: var(--ocker); }
  .data-slide.tegel .d-number { color: var(--tegel); }
  .data-slide.marin .d-number { color: var(--marin); }
  .data-slide .d-caption { font-family: var(--serif); font-size: 46px; font-style: italic; color: var(--ink); margin-top: 14px; max-width: 24ch; line-height: 1.15; font-weight: 600; }
  .data-slide .d-body { font-size: 26px; color: var(--ink); margin-top: 22px; max-width: 36em; line-height: 1.5; font-weight: 500; }

  /* TWOCOL */
  .twocol-slide h1 { font-size: 62px; line-height: 1; color: var(--ink); margin-bottom: 32px; letter-spacing: -1px; }
  .twocol { flex: 1; display: grid; grid-template-columns: 1fr 2px 1fr; gap: 36px; align-items: stretch; }
  .twocol .col { display: flex; flex-direction: column; }
  .twocol .divider { background: var(--rule); }
  .twocol .col-label { font-family: var(--mono); font-size: 18px; letter-spacing: 2px; text-transform: uppercase; font-weight: 700; margin-bottom: 18px; }
  .twocol .col:first-child .col-label { color: var(--bordeaux); }
  .twocol .col:last-child .col-label { color: var(--marin); }
  .twocol .col-body { font-size: 26px; line-height: 1.45; color: var(--ink); font-weight: 500; }

  /* TABLE */
  .table-slide h1 { font-size: 62px; line-height: 1; color: var(--ink); margin-bottom: 32px; letter-spacing: -1px; }
  .arkiv-table { width: 100%; border-collapse: collapse; font-family: var(--sans); }
  .arkiv-table thead th { font-family: var(--mono); font-size: 18px; text-transform: uppercase; letter-spacing: 2px; font-weight: 700; color: var(--bordeaux); padding: 14px 16px; text-align: left; border-bottom: 4px solid var(--rule); }
  .arkiv-table tbody td { font-family: var(--serif); font-size: 26px; font-weight: 500; color: var(--ink); padding: 16px; border-bottom: 2px solid rgba(74,63,51,0.2); }
  .arkiv-table tbody td:first-child { font-weight: 700; }

  /* DISCUSS */
  .discuss-slide h1 { font-size: 62px; font-weight: 600; line-height: 1; margin: 0 0 40px; color: var(--paper); letter-spacing: -0.8px; }
  .questions { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 20px; }
  .questions li { display: flex; gap: 28px; align-items: flex-start; }
  .questions .roman { font-family: var(--serif); font-size: 40px; font-style: italic; color: var(--ocker); width: 60px; flex-shrink: 0; font-weight: 600; }
  .questions li > span:last-child { font-size: 30px; line-height: 1.35; color: var(--paper); font-weight: 500; }

  /* CLOSE */
  .close-slide h1 { font-size: 64px; line-height: 1; color: var(--ink); margin-bottom: 28px; letter-spacing: -0.8px; }
  .takeaways { list-style: none; padding: 0; margin: 0 0 40px; }
  .takeaways li { font-size: 28px; line-height: 1.45; color: var(--ink); font-weight: 500; padding: 12px 0 12px 28px; position: relative; }
  .takeaways li::before { content: "▪"; position: absolute; left: 0; color: var(--bordeaux); font-weight: 700; }
  .next-steps { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 12px; }
  .next-box { padding: 22px 26px; }
  .next-box.box-ocker { background: rgba(184,134,47,0.18); border-left: 5px solid var(--ocker); }
  .next-box.box-marin { background: rgba(44,62,85,0.1); border-left: 5px solid var(--marin); }
  .next-box .label { font-family: var(--mono); font-size: 18px; letter-spacing: 2px; text-transform: uppercase; font-weight: 700; color: var(--ink-2); margin-bottom: 10px; }
  .next-box .text { font-size: 24px; line-height: 1.4; color: var(--ink); font-weight: 500; }

  .reveal .progress { color: var(--bordeaux); }
  .reveal .controls { color: var(--ink-2); }
</style>
</head>
<body>
<div class="reveal">
<div class="slides">

  <!-- slides läggs här -->

</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
<script>
  Reveal.initialize({
    hash: true,
    slideNumber: false,
    width: 1280,
    height: 720,
    margin: 0,
    transition: 'fade',
    controls: true,
    progress: true
  });
</script>
</body>
</html>
```

Reveal-konfigurationen (1280x720, `transition: 'fade'`, `slideNumber: false` - sidnumret bärs av baseline) ingår i skelettet och ska inte ändras.

## Slide-katalog (13 typer)

Varje presentation börjar med **cover** och slutar med **close**. Riktmärke: 10-14 slides för ett instruktionsmoment på 15-20 min.

### 1. Cover - lektionsomslag (alltid först)

```html
<section class="cover-outer">
  <div class="cover-inner">
    <div class="top"><span>Arkiv · Lektionsomslag</span><span>[Kurs] · [Klass]</span></div>
    <div>
      <h1>Rubrik med <em>nyckelord</em></h1>
      <div class="subtitle">Underrubrik i kursiv serif.</div>
    </div>
    <div class="bottom"><span>[Termin] · Lektion [N] / [M]</span><span>01 / [totalt]</span></div>
  </div>
  <aside class="notes">...</aside>
</section>
```

### 2. Question - dagens fråga (mörk)

Tidigt i presentationen; lektionens kärnfråga. Fond: valfri mörk accentfärg (ofta `--mossgron`).

```html
<section style="background: var(--mossgron) !important;">
  <div class="chrome dark" style="background: var(--mossgron);">
    [masthead]
    <div class="body question-slide">
      <div class="eyebrow">Dagens fråga</div>
      <h1>Frågan med <u>nyckelord</u>?</h1>
      <div class="lede">Förtydligande underrad i kursiv serif.</div>
    </div>
    [baseline]
  </div>
  <aside class="notes">...</aside>
</section>
```

### 3. Content - punktlista (ljus)

Arbetshästen. Numrerade bullets (`01`, `02`, ...), max 3 punkter, `fragment` för stegvis avslöjande.

```html
<div class="body content-slide">
  <div class="eyebrow">01 · [Sektionsetikett]</div>
  <h1>Rubrik med <em>nyckelord</em></h1>
  <ul class="bullets">
    <li class="fragment"><span class="index">01</span><span><strong>Begrepp</strong> och förklaring.</span></li>
  </ul>
</div>
```

### 4. Section - kapitelstart (mörk)

Vid byte av avsnitt. Stor siffra + kapiteletikett. Fond: `--bordeaux` eller annan mörk accent.

```html
<div class="body section-slide">
  <div class="big-num">01</div>
  <div>
    <div class="kapitel">§ Kapitel 01</div>
    <h1>Rubrik med <em>nyckelord</em></h1>
    <div class="lede">...</div>
  </div>
</div>
```

### 5. Twocol - jämförelse (ljus)

Två kolumner med divider; etiketterna färgas bordeaux/marin automatiskt.

```html
<div class="body twocol-slide">
  <h1>Två <em>perspektiv</em></h1>
  <div class="twocol">
    <div class="col fragment"><div class="col-label">A</div><div class="col-body">...</div></div>
    <div class="divider"></div>
    <div class="col fragment"><div class="col-label">B</div><div class="col-body">...</div></div>
  </div>
</div>
```

### 6. Callout - inramat budskap (5 varianter)

Färgad yttre ram + innehåll på `--paper-2`. Varianter: `fakta` (marin), `tips` (oliv), `varning` (bordeaux), `kalla` (ink - för källhänvisningar/primärkällor), `begrepp` (ocker - för begreppsdefinitioner och metaforer).

```html
<section class="callout-outer begrepp">
  <div class="callout-inner">
    <div class="top"><span>▸ Begrepp</span><span>Lektion [N] / [M]</span></div>
    <div>
      <h1>Rubrik med <em>nyckelord</em></h1>
      <div class="body-text">Brödtext med <strong>begrepp</strong> och <mark>betoning</mark>.</div>
    </div>
    <div class="bottom"><span>Arkiv · v2.1 · Begrepp</span><span>[nr] / [totalt]</span></div>
  </div>
</section>
```

### 7. Content-highlight - text + stor siffra (delad)

Ljus vänsterspalt (text) + mörk högerspalt (statistik/årtal). Egen ram (`ch-grid`), ingen chrome.

```html
<section style="background: var(--paper) !important;">
  <div class="ch-grid">
    <div class="ch-left">
      <div class="meta-top">[Kurs] · [Moment]</div>
      <div class="content">
        <div class="eyebrow">02 · [Etikett]</div>
        <h1><em>Nyckelord</em> i rubrik</h1>
        <div class="body-text">...</div>
      </div>
      <div class="meta-bot">Arkiv · v2.1</div>
    </div>
    <div class="ch-right" style="background: var(--marin);">
      <div class="meta-top">[nr] / [totalt]</div>
      <div class="stat">
        <div class="stat-label">[Etikett]</div>
        <div class="stat-number">1914</div>
        <div class="stat-caption">Kort kursiv bildtext.</div>
      </div>
      <div class="meta-bot">[nr] / [totalt]</div>
    </div>
  </div>
</section>
```

### 8. Timeline - kronologi (ljus)

Horisontell linje med events. Sätt `grid-template-columns: repeat(N, 1fr)` på `.events` efter antal nedslag (3-5 lagom).

```html
<div class="body timeline-slide">
  <h1>Rubrik med <em>nyckelord</em></h1>
  <div class="timeline-h">
    <div class="events" style="grid-template-columns: repeat(5, 1fr);">
      <div class="event fragment">
        <div class="dot"></div>
        <div class="year">1914</div>
        <div class="title">Händelse</div>
        <div class="note">En rad förklaring.</div>
      </div>
    </div>
  </div>
</div>
```

### 9. Quote - citat (mörk, fond `--ink`)

```html
<div class="body quote-slide">
  <div class="mark-open">"</div>
  <blockquote>Citatet, gärna med <u>nyckelord</u>.</blockquote>
  <div class="attribution">Namn</div>
  <div class="context">Verk, år · kort kontext</div>
</div>
```

### 10. Data - en stor siffra (ljus)

Siffran i bordeaux (default) eller med modifierare `ocker`/`tegel`/`marin` på `.data-slide`.

```html
<div class="body data-slide">
  <div class="d-eyebrow">[Etikett]</div>
  <div class="d-number">73%</div>
  <div class="d-caption">Kursiv serif-bildtext.</div>
  <div class="d-body">Förklarande brödtext.</div>
</div>
```

### 11. Table - tabell (ljus)

```html
<div class="body table-slide">
  <h1>Rubrik med <em>nyckelord</em></h1>
  <table class="arkiv-table">
    <thead><tr><th>Kolumn</th><th>Kolumn</th></tr></thead>
    <tbody><tr><td>Radetikett</td><td>Innehåll</td></tr></tbody>
  </table>
</div>
```

### 12. Discuss - diskussionsfrågor / exit ticket (mörk)

Romerska siffror, max 3 frågor. Används för EPA-stopp och som exit ticket-slide (eyebrow: "Diskutera · Exit ticket").

```html
<div class="body discuss-slide">
  <div class="eyebrow">Diskutera</div>
  <h1>Rubrik med <em>nyckelord</em></h1>
  <ol class="questions">
    <li class="fragment"><span class="roman">I.</span><span>Fråga ett.</span></li>
    <li class="fragment"><span class="roman">II.</span><span>Fråga två.</span></li>
  </ol>
</div>
```

### 13. Close - sammanfattning (ljus, alltid sist)

Takeaways (max 3) + två next-boxar (typiskt Läxa/Förberedelse + Nästa lektion).

```html
<div class="body close-slide">
  <div class="eyebrow">Sammanfattning</div>
  <h1>Det vi <em>byggde</em> idag</h1>
  <ul class="takeaways">
    <li class="fragment"><strong>Kärnpunkt</strong> ett.</li>
  </ul>
  <div class="next-steps">
    <div class="next-box box-ocker"><div class="label">Läxa</div><div class="text">...</div></div>
    <div class="next-box box-marin"><div class="label">Nästa lektion</div><div class="text">...</div></div>
  </div>
</div>
```

## Komposition - typiskt flöde

1. **Cover** → 2. **Question** (dagens fråga, mörk) → 3. **Content** (lektionens mål) → 4. **Section** (kapitelstart) → kärninnehåll i block om 2-3 slides (content / twocol / callout / content-highlight / timeline / data / table) → **discuss** var 3-4:e slide → ev. **quote** som ankare → 12. **Discuss** (exit ticket) → 13. **Close**.

Mörka slides (question, section, quote, discuss) fungerar som visuella andningspauser - placera dem så att två mörka aldrig följer direkt på varandra annat än avsiktligt.

## Talarnoter

Varje slide får `<aside class="notes">` med: vad läraren säger (gärna ordagrant i citattecken), vad läraren gör (dela ut, cirkulera, peka), och tidsangivelse där det är relevant. Exit ticket-sliden ska i noterna beskriva insamling och hur högarna styr nästa lektions retrieval-öppning.
