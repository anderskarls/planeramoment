# Steg 6: Presentationer (reveal.js HTML i designsystemet Arkiv)

Presentationer genereras som self-contained reveal.js HTML-filer i designsystemet Arkiv v2.1. Innehållet hämtas från NotebookLM för att säkerställa att presentationerna är förankrade i källmaterialet.

Läs in innan du börjar:
- `references/arkiv-presentationer.md` - Arkiv v2.1: boilerplate (komplett CSS), slide-katalog och konventioner
- `references/presentationsteknik.md` - pedagogiska principer för klassrumspresentationer

Generera presentationer för varje lektion som har ett instruktions-/presentationsmoment. Generera **en presentation i taget**. Spara till `output/lessons/[Ämne]/[Tema]/presentation-lektion-[N].html`.

*I snabbläge: generera alla presentationer i följd, presentera en samlad översikt, invänta en godkännanderunda. Kvalitetskontrollen (Arkiv-checklistan) körs ändå per presentation.*

## Innehållshämtning från NotebookLM

Endast om momentplanen anger `**NotebookLM:** PÅ` (steg 1.4). Står det `AV`, hoppa tyst över uppslaget, bygg presentationen på lektionsplanen och wikin, och fråga inte om igen. Hämta annars relevant innehåll innan varje presentation genereras - läs `error`-fältet i varje svar, ett fel betyder att auth dött (läge C i `references/notebooklm-anvandning.md`), inte att notebooken saknade material. Anpassa frågorna efter lektionens tema:

```bash
notebooklm ask --json "Ge mig fakta, nyckelbegrepp och konkreta exempel om [lektionens specifika tema]. Inkludera källhänvisningar."
```
```bash
notebooklm ask --json "Finns det primärkällor, citat eller historiska dokument om [temat] som kan användas i en presentation?"
```
```bash
notebooklm ask --json "Vilka vanliga missförstånd finns kring [temat]? Vad brukar elever ha svårt att förstå?"
```

Använd svaren som grund för:
- **`content`-slides:** Fakta, nyckelbegrepp, konkreta exempel med källhänvisningar
- **`quote`- och `callout`-slides:** Primärkällor, citat, historiska dokument (källa-variant av callout)
- **`discuss`- och `question`-slides:** Frågor baserade på vanliga missförstånd och centrala dilemman
- **Talarnoter:** Fördjupande information och källreferenser för läraren

Om ingen notebook är aktiv, generera presentationen baserat på lektionsplanen och Claudes inbyggda kunskap. Markera osäkra påståenden med [VERIFIERA].

## Genereringsprocess

Generera presentationer för varje lektion som har ett instruktions-/presentationsmoment. Generera **en presentation i taget**.

För varje presentation:

1. **Samla innehåll** från lektionsplanen (steg 5) och NotebookLM-svaren. Matcha innehållet mot Arkivs slide-typer (full katalog i `arkiv-presentationer.md`):
   - Nyckelbegrepp och fakta → `content`
   - Diskussionsfrågor → `discuss` eller `question`
   - Primärkälla/citat → `quote` eller `callout` (variant `kalla`)
   - Jämförelser → `twocol` eller `table`
   - Kronologi → `timeline` (vertikal eller horisontell)
   - Sammanfattning → `close`

2. **Generera presentationen** i designsystemet Arkiv (boilerplate och markup-mönster i `arkiv-presentationer.md`). Följ Arkivs principer:
   - Använd Arkivs designtokens utan undantag - papper `#F4EDE1`, Cormorant Garamond i rubriker, bordeaux som signaturfärg
   - Rubriker bär mening: frågor som titlar, ett kursivt nyckelord per rubrik (`<em>ord</em>`)
   - Max 3 nyckelpunkter per slide
   - Diskussionspaus var 3-4:e slide (`discuss` eller `question`)
   - Talarnoter på varje slide med lärarhandledning och tidsuppskattningar
   - Inga emojis - bara typografiska tecken (`▸ ● ▪ § №`)

3. **Kvalitetskontroll** - kör först den mekaniska validatorn, gå därefter igenom de icke-mekaniska punkterna:

   Kör först (på Windows: `PYTHONUTF8=1`):
   ```bash
   python ${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/scripts/validate_arkiv.py [fil]
   ```
   Den täcker papperston `#F4EDE1`, de tre typsnitten, talarnoter på varje slide, emoji-frihet, masthead-täckning och en heuristik för max 3 nyckelpunkter. Åtgärda alla FAIL innan du går vidare.

   Gå sedan igenom de icke-mekaniska punkterna för hand:
   - Baseline (Arkiv · v2.1 + sidnummer) på varje standardslide?
   - Max 2 accentfärger per slide, bordeaux som primär?
   - Ett kursivt nyckelord per rubrik - max?
   - Frågor som titlar där möjligt?
   - Brödtext max 42 em bred?
   - Diskussionspaus var 3-4:e slide?

4. **Presentera för läraren** och fråga om feedback innan du går vidare till nästa presentation.

Spara till `output/lessons/[Ämne]/[Tema]/presentation-lektion-[N].html`.
