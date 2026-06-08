# Steg 3: Rollsekvens (nivå 4) och brottningsform (nivå 5)

Detta steg fortsätter designdialogen genom Momentplaneringsramverkets nivå 4 (sekvenslogik - 9 roller) och nivå 5 (brottningsform - diskursmål + formvalsprinciper). Här komponeras momentet av **roller**, inte av en generell pedagogisk ansats. M-i, M-ii, M-iii och M-iv aktiveras. Se `pedagogik-ramverk.md`.

Läs in metodreferensen (metodbibliotek organiserat efter funktion - försörjer rollernas konkreta aktiviteter): `references/pedagogiska-metoder.md`

**Kunskapsbasintegration (H4):** Sök vaultet via Local Brain Search efter relevanta reflektioner från liknande moment och permanenta anteckningar om pedagogik:
```bash
./resources/local-brain-search/run_search.sh "[ämnet/temat] pedagogik reflektion" --limit 5 --json
```
Om relevanta resultat hittas, presentera dem kort för läraren: "Jag hittade dessa reflektioner från tidigare undervisning som kan vara relevanta..."

**NotebookLM-forskning:** Om en notebook är aktiv, hämta ämnesinnehåll som grund för rollernas innehåll:
```bash
notebooklm ask --json "Vilka centrala begrepp, teman och perspektiv finns kring [temat]? Vilka källor i notebooken är mest relevanta?"
```
```bash
notebooklm ask --json "Vilka primärkällor, citat eller konkreta exempel finns om [temat] som kan användas i undervisning?"
```
Presentera en kort sammanfattning av vad notebooken innehåller om ämnet för läraren.

### 3.1 Nivå 4 - Rollkomposition

Ett moment komponeras av roller, inte fasta faser. **En roll definieras av vad eleven exit:ar med**, inte aktivitetens yttre form. De nio rollerna:

| # | Roll | Eleven exit:ar med |
|---|------|--------------------|
| 1 | Frågeförankring | Förståelse av brottningsfrågan och varför den är värd att brottas med |
| 2 | Provokation | En produktiv kognitiv dissonans / ett ifrågasatt förgivettagande |
| 3 | Begreppsbygge | Begreppslig precision - kan använda momentets fackbegrepp korrekt |
| 4 | Perspektivbygge | En perspektivinventering - flera synsätt kartlagda, **utan** egen position |
| 5 | Brottning | En försvarad/prövad position i den omtvistade frågan |
| 6 | Syntes | En integrerad helhetsförståelse |
| 7 | Metareflektion | Insikt om sitt eget tänkande/lärande under momentet |
| 8 | Applikation | Förmågan att tillämpa på ett nytt fall |
| 9 | Återbesök | Befäst, spaced retrieval av momentets kärna (ofta i senare moment) |

**Core (måste finnas):** Frågeförankring + Brottning + Syntes.

**Hårda ordningsregler (får inte brytas):**
- Frågeförankring först
- Brottning före Syntes
- Metareflektion sist (om den används)

**Soft default-ordning för övriga** (får brytas med motivering): Frågeförankring → Provokation → Begreppsbygge → Perspektivbygge → Brottning → Syntes → Applikation → Metareflektion → (Återbesök, ofta i senare moment).

**Default-rekommendation (M-i):** Skillen föreslår en rollsekvens härledd från frågetyp (1.8), bedömningsmål (2.2), förutsättningar (2.4) + ev. kursminne. Vägledning för vilka valbara roller som default slås på:

| Signal från Steg 1-2 | Slår default på roll |
|---|---|
| Förutsättningar med **begrepp** att etablera (2.4) | Begreppsbygge |
| Värdefråga / Hess-fråga / tippande fråga (1.8/1.7) | Perspektivbygge (kartlägg positioner före brottning) |
| Etisk eller Existentiell fråga (1.8) | Metareflektion (sist) |
| Bedömningsmål med tillämpning/transfer (2.2) | Applikation |
| Frågan har en stark ingångshändelse/dilemma | Provokation (tidigt) |
| Sekundär frågetyp dokumenterad (1.8) | Väv in i Perspektivbygge eller Metareflektion |

Presentera förslaget som en numrerad rollsekvens. För **varje roll**: ange dess bedömningsmål-relativa exit (vad eleven exit:ar med) i *detta* moment, konkretiserad mot frågan och CI.

**Override-prompt (M-ii):** Om läraren bryter en hård ordningsregel eller väljer bort en core-roll → avvisa och förklara (det är inte en kontextläsningsfråga, det är ramverkets golv). Om läraren avviker från default-urvalet av *valbara* roller eller från soft default-ordningen → fråga: *"Vilken kontextläsning motiverar avvikelsen? Kategori 2-5 (Princip 2)."* Magkänsla utan kategori-2-5-stöd avvisas.

### 3.2 Nivå 5 - Diskursmål och brottningsform

Gäller Brottning-rollen. **Diskursmålet är primärt val; formen är terminal output, deriverad** (Felton, Crowell & Liu 2015: diskursmålet - inte formatets etikett - avgör om my-side-bias uppstår).

**Steg A - Härled diskursmål (M-i).** Fem diskursmål:

| Diskursmål | Innebörd |
|---|---|
| Övertyga | Vinn argumentet, försvara position |
| Syntes | Integrera bägge sidors starkaste argument |
| Utforska | Öppen kollektiv undersökning, ingen position söks |
| Klargöra | Begreppslig precision - "vad menar vi när vi säger X?" |
| Pröva | Hypotes-test mot källor - håller påståendet? |

Default-mappning från frågetyp (1.8), justeras mot bedömningsmål:

| Frågetyp | Default-diskursmål |
|---|---|
| Hess-fråga / Värdefråga | Övertyga (eller Syntes om bedömningsmålet kräver motpartsförståelse) |
| Analysfråga | Pröva eller Utforska |
| Disciplinär (historia) | Pröva (mot källor) |
| Etisk (historia) | Syntes eller Övertyga |
| Existentiell | Utforska eller Klargöra |

**Låsningskontroll:** Om bedömningsmålet (2.2) redan låser diskursmålet - t.ex. "kan formulera motståndarens starkaste position" → **Syntes är låst** - säg det explicit och hoppa över valet. Annars: presentera default + alternativ, be om val.

**Steg B - Härled form via de fyra formvalsprinciperna (i ordning):**

1. **Härledning från tre inputs:** form följer av (i) diskursmål → DNA, (ii) frågetyp → familj, (iii) bedömningsmål → precisering. Föreslå en konkret form (t.ex. sokratiskt seminarium, strukturerad debatt, fishbowl, SAC - Structured Academic Controversy, Harkness-diskussion, exploratory talk i smågrupp).
2. **Gruppstorleksgolv:** fråga efter gruppstorlek. Storleken sätter *golvet* för möjliga former (sokratiskt seminarium kollapsar vid >18; Harkness designad för 10-14; exploratory talk kräver 3-4/grupp). **Storlek räcker inte - struktur krävs** (Larsson 2007: 3-5 elever dominerar talutrymmet utan strukturerade talturer). Ange den strukturmekanism som säkrar talutrymme.
3. **Hess-gate-tillämpning:** om frågan klassades **tippande** (1.7) - lägg position-tilldelning ovanpå vald form som stark default (skyddar elever med utsatt minoritetsposition).
4. **Variering över moment:** kontrollera mot tidigare valda former i momentet - upprepa inte samma form mer än en gång utan motivering.

Presentera diskursmål + härledd form + gruppstruktur. **Override-prompt (M-ii):** vid avvikelse från default-diskursmål eller default-form - fråga om kontextläsningskategori 2-5.

### 3.3 Differentiering och UDL (M1)

Diskutera **differentiering** mot rollsekvensen: Hur stödjer vi elever som siktar på E genom de tunga rollerna (särskilt Brottning)? Hur utmanar vi elever som siktar på A? Be läraren om input.
- **UDL-informerad (M1):** föreslå minst en alternativ representationsform per roll/lektion (visuellt, auditivt, textbaserat). Vid terminologitunga moment, identifiera särskilda anpassningar för L2-elever.
- **Princip 3-koppling:** elever med dokumenterat stöd har explicit undantag i Brottning-rollen (differentierad tillämpning).

### 3.4 Formativa avstämningar

Diskutera **formativa checkpoints** kopplade till **rollövergångar** - särskilt verifikationen innan Brottning släpps lös (nivå 3, 2.4): utgångsbiljetter, snabbskrivningar, lärpar. En formativ avstämning bör ligga vid övergången till Brottning för att bekräfta att förutsättningarna sitter.

### 3.5 Mönsterlarms-check (M-iii)

Räkna overrides kumulativt från Steg 1-3 (1.7, 1.8, 2.2, 2.3, 2.4, 2.5, 3.1 rollurval, 3.2 diskursmål/form). Samma två triggers som i 2.6 (antal: 3+ totalt; typ-mönster: 3+ i samma kategori). Vid trigger, pausa med medium friktion och kräv skriftlig motivering. Spara i momentplan.md → Override-räknare.

### 3.6 Sammanfattning och uppdatering av momentplan.md (M-iv)

Sammanfatta rollsekvensen och brottningsformen, be läraren bekräfta. Uppdatera `momentplan.md`:

```markdown
## Designval (Momentplaneringsramverket) - forts.

### Nivå 4 - Rollsekvens
[Numrerad sekvens av valda roller i ordning]
1. [Roll] - eleven exit:ar med: [...]
2. ...
- **Core verifierad:** Frågeförankring + Brottning + Syntes finns [Ja/Nej]
- **Ordningsregler:** [uppfyllda / avvikelse med motivering]
- **Default:** [systemets föreslagna sekvens]
- **Valt:** [lärarens sekvens]
- **Override:** [Nej | Ja - kategori X: "..."]

### Nivå 5 - Brottningsform
- **Diskursmål:** [...] ([låst av bedömningsmål / valt])
- **Form:** [...]
- **Gruppstorlek + strukturmekanism:** [...]
- **Position-tilldelning (Hess):** [Ja, tippande fråga | Ej tillämpligt]
- **Variering:** [första formen i momentet | upprepning motiverad: "..."]
- **Default:** [...] / **Valt:** [...] / **Override:** [Nej | Ja - kategori X: "..."]

### Differentiering och formativa avstämningar
- **Differentiering (E/A) per tung roll:** [...]
- **UDL alternativa representationsformer:** [...]
- **Formativ avstämning före Brottning:** [...]
```

Uppdatera även Override-räknare.
