# Steg 5: Detaljerade lektionsplaner (Word-dokument)

Läs in docx-skillen (bundlad i pluginen): `${CLAUDE_PLUGIN_ROOT}/skills/docx/SKILL.md`

Säkerställ att `docx`-paketet är installerat: `npm install -g docx`

Läs in lektionsplaneringsreferensen (rollbaserad mall + ramprinciper): `references/lektionsplanering.md`

Generera **en lektion i taget**, rollbaserat. Varje lektion realiserar de roller den tilldelades i Steg 4 - lektionens inre förlopp formas av rollen/rollerna och (för Brottning) diskursmålet + formen från 3.2. **Ingen fast fassekvens.**

**NotebookLM-innehållshämtning:** Innan varje lektion genereras, hämta relevant innehåll från notebooken. Anpassa frågorna efter lektionens tema:
```bash
notebooklm ask --json "Ge mig fakta, nyckelbegrepp och konkreta exempel om [lektionens specifika tema]. Inkludera källhänvisningar."
```
```bash
notebooklm ask --json "Vilka vanliga missförstånd eller svårigheter finns kring [temat]? Vad brukar elever ha svårt att förstå?"
```
```bash
notebooklm ask --json "Finns det primärkällor, citat eller historiska dokument om [temat] som kan användas som undervisningsmaterial?"
```
Använd svaren som grund för (mappat mot lektionens roll, inte fasta faser):
- **Kunskapsöverförande roller** (Begreppsbygge/Perspektivbygge): worked examples, faktainnehåll, begreppsdefinitioner
- **Brottning/Syntes**: källmaterial, analysuppgifter, positionsunderlag
- **Lärarinstruktioner**: nyckelformuleringar och fördjupningsfrågor
- **Differentiering**: fördjupningsmaterial (mot A) från notebookens källor
Inkludera NotebookLM:s källhänvisningar i lektionsplanens materialsektion.

**Wiki-uppslag per lektion:** Innan lektionen genereras, slå även upp lärarens kunskapsbas (protokoll i `references/wiki-anvandning.md`):
```bash
./resources/local-brain-search/run_search.sh "[lektionens roll/metod] [lektionens tema]" --limit 5 --json
```
Komplettera med ämnes-MOC:en från steg 1.5.5 om en sådan finns (den pekar ofta på sidor om just denna lektions delområde). Wikifynden matar **lärarens sida** av lektionsplanen, där NotebookLM matar **elevens**:
- **Lärarinstruktioner**: didaktiska fynd om rollens aktivitet (t.ex. vanliga fallgropar i formen, kalibrering, frågeteknik)
- **Retrieval-öppning och exit ticket**: kalibrering mot kunskapsbasens evidens (svårighetsgrad, frågeverb)
- **Differentiering**: tekniker och stödstrukturer kunskapsbasen dokumenterat
- **Ämnesvinklar**: synteser och perspektiv från ingestade källor som skärper innehållet

Citera använda sidor med `[[länk]]` i lektionsplanens materialsektion och lägg till dem i momentplanens `## Kunskapsunderlag (wiki)`. Hittas inget relevant: gå vidare utan kommentar.

### Lektionens ram (tre evidensprinciper, inte faser)

Varje lektion ramas av tre principer som är ortogonala mot rollinnehållet - de gäller oavsett roll:

1. **Öppna med retrieval** (spaced practice): aktiv återkallelse från tidigare lektioner, styrd av föregående lektions exit ticket-data. (Momentets första lektion: aktivera förkunskaper istället.)
2. **Elevaktiv tid > 50%** av lektionen. Rosenshines fynd att framgångsrika lärare lägger ~57% av tiden på guidad övning gäller fortfarande - men som **teknik inom de roller där eleven arbetar mot en exit**, inte som en universell, tvingande fas.
3. **Avsluta med exit ticket + framåtkoppling**: en fråga som mäter rollens exit + en preview av nästa lektion.

**Kärnan mellan öppning och avslut formas av lektionens roll** (se `lektionsplanering.md` för rollspecifik kärnvägledning). Kort:

- **Begreppsbygge / Perspektivbygge:** explicit instruktion med worked examples + guidad bearbetning (Frayer, begreppskartor, perspektivanalys). Det här är hemvisten för de tekniker som tidigare låg i "fas 3-4".
- **Brottning:** kärnan *är* den valda formen (sokratiskt seminarium / debatt / fishbowl / SAC) med diskursmålet som styr samtalsstrukturen och gruppmekanismen från 3.2. Ingen lärargenomgång ska tränga ut brottningstiden.
- **Syntes:** integrationsaktivitet där eleven väver ihop positioner/perspektiv till en helhet.
- **Metareflektion / Applikation / Återbesök:** struktureras mot sina respektive exits.

### Lektionsplanens innehåll

Varje lektionsplan ska innehålla:

- **Lektion N: [Titel]**
- **Roll(er)** - vilken/vilka roller lektionen realiserar + rollens exit (vad eleven exit:ar med)
- **Lärandemål för lektionen** - vilka av momentets mål som adresseras
- **Förberedelse** - vad läraren behöver göra innan; för förutsättningar: notera Princip 3-leverans (levereras i förväg, elevens ansvar)
- **Retrieval-öppning** (H2) - "Baserat på exit ticket från lektion N-1: [specifik koppling]"
- **Lektionsförlopp** - minut-för-minut: öppning (retrieval) → rollkärna → avslut (exit ticket). Tidsuppskattningar, inte fasta fasandelar
- **Brottningsform** (endast Brottning-lektioner) - diskursmål, form, gruppstorlek + strukturmekanism, ev. position-tilldelning
- **Lärarinstruktioner** - vad läraren säger/gör vid nyckelmoment, diskussionsfrågor, hur formen/gruppen faciliteras
- **Elevaktiviteter** - specifika instruktioner med tydliga steg
- **Differentiering** - konkreta stödstrukturer (mot E) och utmaningar (mot A)
- **Material som behövs** - allt som krävs
- **Exit ticket** (H2) - en specifik fråga som mäter rollens exit + instruktion för hur resultaten informerar nästa lektion
- **Koppling till bedömningsmål/kunskapskrav** - hur lektionen bidrar till E/C/A-progressionen

### Kvalitetskontroll (obligatorisk) - kör innan du presenterar varje lektionsplan

**Standardkontroller:**
- Realiserar lektionen sin tilldelade roll, och mäter exit ticket den rollens exit?
- Öppnar lektionen med retrieval kopplad till föregående lektion (utom momentets första)?
- Överstiger elevaktiv tid 50% av total tid?
- För Brottning-lektioner: matchar förloppet diskursmålet + formen från 3.2 (inte en generisk genomgång)?
- Är differentieringen konkret (inte "stöd svagare elever")?
- Finns [VERIFIERA]-taggar vid osäkra faktapåståenden?
- Kopplar lektionen framåt till nästa?


Presentera lektionsplanen och fråga: "Vill du justera något i denna lektionsplan, eller ska jag gå vidare till nästa?"

**Generera som Word-dokument (.docx):**
Skapa varje godkänd lektionsplan som ett professionellt Word-dokument med `docx-js`. Använd:
- A4-format (11906 x 16838 DXA) med 1"-marginaler
- Rubrik: "Lektion N: [Titel]" som Heading 1
- Underrubriker (Lärandemål, Förberedelse, Tidsplanering, etc.) som Heading 2
- Tidsplaneringen som en formaterad tabell med kolumnerna: Tid, Fas, Aktivitet, Beskrivning
- Bullet-listor med `LevelFormat.BULLET` (aldrig unicode-bullets)
- Sidfot med kursnamn och momentets titel
- Teckensnitt: Arial, 12pt brödtext

Skriv ett Node.js-script som genererar .docx-filen och kör det.
Validera filen med `python ${CLAUDE_PLUGIN_ROOT}/skills/docx/scripts/office/validate.py` (på Windows: sätt `PYTHONUTF8=1` i miljön, annars fallerar valideringen på svenska tecken).

**Spara i bada format:**
- **Markdown:** `output/lessons/[Ämne]/[Tema]/lektion-[N].md` (i vaultet)
- **Word:** `C:\Undervisningsmaterial\[Ämne]\[Tema]\lektion-[N].docx`

Markdown-versionen ska innehålla samma innehåll som Word-dokumentet men formaterat som ren markdown (rubriker, tabeller, listor).
