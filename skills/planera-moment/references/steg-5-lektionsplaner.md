# Steg 5: Detaljerade lektionsplaner (HTML-läsvy för klassrummet)

Läs in lektionsplaneringsreferensen (ramprinciper, rollvägledning och mallen): `references/lektionsplanering.md`. **Avsnitt 5 är formatet** - läs det och exemplet `exempel/lektionsplan-exempel.md` innan första lektionen skrivs.

Lektionsplanen skrivs för läraren, som läser den **på skärm i klassrummet**. Markdownen är källan; en HTML-sida byggs ur den med tidslinje, lektionsklocka, checklistor och hopfällda fördjupningar. Det finns ingen Word-version av lektionsplaner (elevuppgifter i steg 5a görs fortfarande i Word).

Generera **en lektion i taget**, rollbaserat. Varje lektion realiserar de roller den tilldelades i Steg 4 - lektionens inre förlopp formas av rollen/rollerna och (för Brottning) diskursmålet + formen från 3.2. **Ingen fast fassekvens.**

*I snabbläge: generera alla lektionsplaner i följd, presentera en samlad översikt, invänta en godkännanderunda. Kvalitetskontrollen nedan körs ändå per lektion.*

**NotebookLM-innehållshämtning:** Endast om momentplanen anger `**NotebookLM:** PÅ` (steg 1.4). Står det `AV`, hoppa tyst över uppslaget, tagga faktapåståenden `[VERIFIERA]` och fråga inte om igen. Hämta annars relevant innehåll från notebooken innan varje lektion genereras - läs `error`-fältet i varje svar, ett fel betyder att auth dött (läge C i `references/notebooklm-anvandning.md`), inte att notebooken saknade material. Anpassa frågorna efter lektionens tema:
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
- **Tidsblockens lärarpunkter och `Säg:`-rader**: nyckelformuleringar, fördjupningsfrågor, vanliga missförstånd att korrigera
- **Differentiering**: fördjupningsmaterial (mot A) från notebookens källor
Notebookens källhänvisningar skrivs under `### Källor` i lektionsplanens `## Bakgrund` - inte i klassrumsvyn.

**Wiki-uppslag per lektion:** Innan lektionen genereras, slå även upp lärarens kunskapsbas (protokoll i `references/wiki-anvandning.md`):
```bash
./resources/local-brain-search/run_search.sh "[lektionens roll/metod] [lektionens tema]" --limit 5 --json
```
Komplettera med ämnes-MOC:en från steg 1.5.5 om en sådan finns (den pekar ofta på sidor om just denna lektions delområde). Wikifynden matar **lärarens sida** av lektionsplanen, där NotebookLM matar **elevens**:
- **Tidsblockens lärarpunkter**: didaktiska fynd om rollens aktivitet (t.ex. vanliga fallgropar i formen, kalibrering, frågeteknik)
- **Öppning och exit ticket**: kalibrering mot kunskapsbasens evidens (svårighetsgrad, frågeverb)
- **Differentiering**: tekniker och stödstrukturer kunskapsbasen dokumenterat
- **Ämnesvinklar**: synteser och perspektiv från ingestade källor som skärper innehållet

Fyndet omsätts i handling i klassrumsvyn; `[[länken]]` skrivs under `### Källor` i `## Bakgrund` och läggs till i momentplanens `## Kunskapsunderlag (wiki)`. Hittas inget relevant: gå vidare utan kommentar.

### Lektionens ram (tre evidensprinciper, inte faser)

Varje lektion ramas av tre principer, ortogonala mot rollinnehållet (full motivering: `lektionsplanering.md` avsnitt 1 - kanonisk):

1. **Öppna med retrieval** (spaced practice; första lektionen: aktivera förkunskaper istället).
2. **Elevaktiv tid: norm > 50% (sikta 60%+), golv 30%** - mellan 30 och 50% krävs en M-ii-motivering, under 30% säger skillen ifrån (`lektionsplanering.md` avsnitt 1 - kanonisk).
3. **Avsluta med exit ticket + framåtkoppling** som mäter rollens exit.

**Kärnan mellan öppning och avslut formas av lektionens roll** (se `lektionsplanering.md` för rollspecifik kärnvägledning). Kort:

- **Begreppsbygge / Perspektivbygge:** explicit instruktion med worked examples + guidad bearbetning (Frayer, begreppskartor, perspektivanalys).
- **Brottning:** kärnan *är* den valda formen (sokratiskt seminarium / debatt / fishbowl / SAC) med diskursmålet som styr samtalsstrukturen och gruppmekanismen från 3.2. Formens faser blir egna tidsblock. Ingen lärargenomgång ska tränga ut brottningstiden.
- **Syntes:** integrationsaktivitet där eleven väver ihop positioner/perspektiv till en helhet.
- **Metareflektion / Applikation / Återbesök:** struktureras mot sina respektive exits.

### Lektionsplanens innehåll

Följ mallen i `lektionsplanering.md` avsnitt 5. I korthet:

- **Klassrumsvyn:** kärnan i en mening (`>`), `## Före lektionen` (checklista), ev. `## Genom hela lektionen`, `## Förlopp` med ett `### start-slut · Titel`-block per tidsavsnitt (varje block: `Eleverna:`, lärarpunkter, `Säg:`-rader, ev. `####`-fördjupningar), `## Exit ticket`, `## Efter lektionen` (checklista), `## Differentiering`, `## Material`.
- **`## Bakgrund`:** roll och exit, lärandemål, koppling till bedömningsmål, ev. brottningsform, elevaktiv tid med uppdelning och ev. M-ii-motivering, ändringar/overrides, källor och wikilänkar.
- **Frontmatter:** `lektion`, `titel`, `kurs`, `grupper`, `moment`, `langd`, `elevaktiv` - HTML:en läser dem.

Retrieval-öppningen är det första tidsblocket och ska säga hur föregående lektions exit ticket-högar används. Förutsättningar som levereras i förväg (Princip 3 - förutsättningar levereras i förväg, elevens ansvar att tillägna sig dem) står som punkter under `## Före lektionen`, formulerade som vad som ska levereras till vem och när.

### AI-svaghetscheck och kvalitetskontroll (obligatorisk) - kör innan du presenterar varje lektionsplan

- Realiserar lektionen sin tilldelade roll, och mäter exit ticket den rollens exit?
- Öppnar lektionen med retrieval kopplad till föregående lektion (utom momentets första)?
- Beräkna elevaktiv tid ur tidsblocken och skriv den i frontmattern (`elevaktiv`) och under `### Elevaktiv tid` i Bakgrund som "Ca X av Y min (Z %)". Norm >50% (sikta 60%+), golv 30%. Hantera utfallet så här:
   - **Z > 50:** normalläge, gå vidare utan kommentar.
   - **30 ≤ Z ≤ 50:** presentera lektionsplanen som vanligt, men ställ M-ii-prompten i **egen turn** innan du frågar om justeringar: *"Lektionen landar på Z% elevaktiv tid, under normen 50%. Vilken kontextläsning motiverar det? Kategori 2-5."* Skriv lärarens svar under `### Elevaktiv tid` och räkna upp momentplanens Override-räknare. Har läraren redan motiverat samma sak för en tidigare lektion i momentet: hänvisa till det beslutet i stället för att fråga om igen.
   - **Z < 30:** stanna. Säg att lektionen ligger under golvet, peka ut var i förloppet elevarbete kan återtas, och fråga om läraren vill att du justerar eller vill gå vidare ändå. Går läraren vidare: dokumentera som override med kategori 2-5.
   - Är det **tiden** som tagit slut snarare än ett medvetet val - korta lärargenomgången, aldrig elevarbetet. Skriv prioriteringen i `## Förlopp`:s "Om tiden inte räcker"-rad.
- För Brottning-lektioner: matchar tidsblocken diskursmålet + formen från 3.2 (inte en generisk genomgång)?
- Är differentieringen konkret (inte "stöd svagare elever")?
- Är faktapåståenden källgrundade (NotebookLM) eller [VERIFIERA]-taggade?
- Är exemplen konkreta och ämnesspecifika (inte generiska AI-exempel)?
- Kopplar lektionen framåt till nästa (sista blockets `Säg:`)?
- **Formatkontroll:** täcker tidsblocken hela lektionen utan luckor, med sista slut = `langd`? Beskrivs varje minut en gång? Står allt som är motivering, ramverksvokabulär, källor och ändringshistorik i `## Bakgrund` och inte i klassrumsvyn? Är varje `Säg:`-rad något läraren faktiskt säger?

Presentera lektionsplanen och fråga: "Vill du justera något i denna lektionsplan, eller ska jag gå vidare till nästa?"

### Spara och bygg

- **Markdown:** `output/lessons/[Ämne]/[Tema]/lektion-[N].md` (i vaultet) - källan.
- **HTML:** byggs ur markdownen bredvid den, som `lektion-[N].html`:

```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/scripts/bygg-lektionsplan.py" "output/lessons/[Ämne]/[Tema]/lektion-[N].md"
```

(På Windows: sätt `PYTHONUTF8=1` om konsolen klagar på svenska tecken.) Bygg om efter varje ändring av markdownen - redigera aldrig HTML:en. Kontrollera efter bygget att scriptet rapporterat en fil, och att `Säg:`, `**` och `[[` inte finns kvar som råtext i den byggda sidan (det betyder en rad som inte följde konventionen).

Ge läraren sökvägen till HTML-filen och öppna den i webbläsaren.
