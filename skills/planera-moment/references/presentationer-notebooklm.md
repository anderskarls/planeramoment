# Steg 6: Presentationer (reveal.js HTML via slides-skillen)

Presentationer genereras som self-contained reveal.js HTML-filer med hjalp av slides-skillen. Innehallet hamtas fran NotebookLM for att sakerstalla att presentationerna ar forankrade i kallmaterialet.

## Innehallshamtning fran NotebookLM

Om en notebook ar aktiv (steg 1), hamta relevant innehall innan varje presentation genereras. Anpassa fragorna efter lektionens tema:

```bash
notebooklm ask --json "Ge mig fakta, nyckelbegrepp och konkreta exempel om [lektionens specifika tema]. Inkludera kallhanvisningar."
```
```bash
notebooklm ask --json "Finns det primorkallor, citat eller historiska dokument om [temat] som kan anvandas i en presentation?"
```
```bash
notebooklm ask --json "Vilka vanliga missforstand finns kring [temat]? Vad brukar elever ha svart att forsta?"
```

Anvand svaren som grund for:
- **`content`-slides:** Fakta, nyckelbegrepp, konkreta exempel med kallhanvisningar
- **`quote`- och `callout`-slides:** Primarkallor, citat, historiska dokument (kalla-variant av callout)
- **`discuss`- och `question`-slides:** Fragor baserade pa vanliga missforstand och centrala dilemman
- **Talarnoter:** Fordjupande information och kallreferenser for lararen

Om ingen notebook ar aktiv, generera presentationen baserat pa lektionsplanen och Claudes inbyggda kunskap. Markera osakra pastaenden med [VERIFIERA].

## Genereringsprocess

Generera presentationer for varje lektion som har ett instruktions-/presentationsmoment. Generera **en presentation i taget**.

For varje presentation:

1. **Samla innehall** fran lektionsplanen (steg 5) och NotebookLM-svaren. Matcha innehallet mot Arkivs slide-typer:
   - Nyckelbegrepp och fakta → `content`
   - Diskussionsfragor → `discuss` eller `question`
   - Primarkalla/citat → `quote` eller `callout` (variant `kalla`)
   - Jamforelser → `twocol` eller `table`
   - Kronologi → `timeline` (vertikal eller horisontell)
   - Sammanfattning → `close`

2. **Generera presentationen** i designsystemet Arkiv (se slides-skillen). Folj Arkivs principer:
   - Anvand Arkivs designtokens utan undantag — papper `#F4EDE1`, Cormorant Garamond i rubriker, bordeaux som signaturfarg
   - Rubriker bar mening: fragor som titlar, ett kursivt nyckelord per rubrik (`<em>ord</em>`)
   - Max 3 nyckelpunkter per slide
   - Diskussionspaus var 3-4:e slide (`discuss` eller `question`)
   - Talarnoter pa varje slide med lararhandledning och tidsuppskattningar
   - Inga emojis — bara typografiska tecken (`▸ ● ▪ § №`)

3. **Kvalitetskontroll** — kor slides-skillens Arkiv-checklista innan du presenterar for lararen:
   - Papperston `#F4EDE1` pa alla slides?
   - Masthead (meta_left/meta_right) + baseline (Mitt designsystem · Arkiv + sidnummer) pa varje slide?
   - Max 2 accentfarger per slide, bordeaux som primar?
   - Ett kursivt nyckelord per rubrik — max?
   - Fragor som titlar dar mojligt?
   - Max 3 nyckelpunkter per slide?
   - Brodtext max 42 em bred?
   - Diskussionspaus var 3-4:e slide?
   - Inga emojis — bara `▸ ● ▪ § №`?
   - Talarnoter pa varje slide?
   - Cormorant Garamond + Inter Tight + JetBrains Mono laddade fran Google Fonts?

4. **Presentera for lararen** och fraga om feedback innan du gar vidare till nasta presentation.

Spara till `Undervisningsmaterial/[Amne]/[Tema]/presentation-lektion-[N].html`.
