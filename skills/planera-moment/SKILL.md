---
description: >
  Planera ett komplett undervisningsmoment för gymnasiet genom en dialogdriven
  7-stegsprocess. Genererar lektionsplaner (Word/.docx), presentationer
  (reveal.js HTML) och momentöversikt (HTML) - allt förankrat i Gy11/Gy25,
  Momentplaneringsramverket och evidensbaserad pedagogik. Använd ALLTID denna skill
  när användaren vill planera ett moment, planera undervisning, skapa
  lektionsplaner för flera lektioner, göra en momentplanering, strukturera ett
  undervisningsupplägg, eller ber om hjälp att planera lektioner i
  samhällskunskap, historia eller juridik. Triggas även av fraser som "planera
  ett moment", "planera-moment", "momentplanering", "jag vill planera", "hjälp
  mig planera", "skapa lektionsplaner", "planera undervisningen", "planera
  lektioner om [ämne]", "snabbläge" (kör steg 1-4 som en samlad designrunda),
  eller när användaren beskriver ett ämne/tema och antal
  lektioner de vill ha. Denna skill ska INTE användas för enskilda dokument
  (använd docx/pptx), enskilda lektionsplaner utan momentkontext, eller
  HTML-momentöversikter från befintlig data (använd html-momentoversikt).
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion, Bash(node:*), Bash(npm:*), Bash(python:*), Bash(pip:*), Bash(pdftoppm:*), Bash(notebooklm:*), Bash(./resources/local-brain-search/run_search.sh:*), Bash(./resources/local-brain-search/run_connections.sh:*), ListMcpResourcesTool, ReadMcpResourceTool, mcp__survey-platform__create_quiz_from_csv, mcp__survey-platform__import_questions, mcp__survey-platform__create_survey, mcp__survey-platform__import_moment, mcp__survey-platform__get_moment_report, mcp__survey-platform__get_results, mcp__survey-platform__summarize_results
argument-hint: "[ämne (valfritt)]"
---

Tala svenska genom hela processen. Du är ett stöd för en professionell gymnasielärare - läraren fattar alla pedagogiska beslut, du hjälper att strukturera och producera material.

Läs in det pedagogiska ramverket innan du börjar: `pedagogik-ramverk.md`

Genomför en 7-stegsprocess för att planera ett komplett undervisningsmoment. Gå ALDRIG vidare till nästa steg utan lärarens uttryckliga godkännande. Vid varje steg: presentera konkreta förslag, invänta beslut, bekräfta beslutet genom att sammanfatta det.

## Så här är skillen uppbyggd (progressiv laddning)

Denna fil är en **orkestrerare**. Varje steg har en egen referensfil under `references/` med den fullständiga vägledningen. **Läs in respektive stegfil först när du når det steget** - ladda inte alla i förväg. Stegfilerna refererar i sin tur till struktur-/metodfiler (gy11/gy25, pedagogiska-metoder, lektionsplanering) som laddas vid behov.

Skapa output-kataloger för momentet på två platser:
- **Markdown (.md)** sparas i vaultet: `output/lessons/[Ämne]/[Tema]/`
- **Word (.docx)** sparas utanför vaultet: `[Word-mappen]\[Ämne]\[Tema]\` (se **Sökvägar** nedan)

Strukturen är identisk på båda platser (t.ex. `Historia/Franska revolutionen/`). Ämne ska ha stor bokstav, tema ska vara läsbart med mellanslag. Skapa katalogerna om de inte finns. Vilken ämnesmapp en kurs hör till anges i `kurser.json` (fältet `amnesmapp`).

## Sökvägar

Skillen använder tre platser. Resolva dem i början av arbetet:

- **Vaultrot.** Läs `$VAULT_BASE_PATH` från `.claude/settings.md` i arbetskatalogen om filen finns; annars anta att cwd är vaultroten. Alla `output/lessons/...`-sökvägar är relativa vaultroten.
- **Word-mappen** (`[Word-mappen]` i stegfilerna). Läs nyckeln `WORD_OUTPUT_PATH` från samma `.claude/settings.md`; om nyckeln saknas är defaulten `C:\Undervisningsmaterial`. Under den läggs `[Ämne]\[Tema]\` (samma struktur som i vaultet). Här sparas .docx-filer och videor - stora binärer hålls utanför vaultet.
- **Sökskripten.** `[vaultrot]/resources/local-brain-search/run_search.sh` (och `run_connections.sh`). Faller de bort finns en fallback beskriven i `references/wiki-anvandning.md` (index.md + Grep över `wiki/`). Sökskripts-anropen förutsätter att cwd = vaultroten (normalfallet när sessionen startar där).

---

## Återupptagande - kör ALLTID denna kontroll först

Ett moment spänner ofta över flera sessioner. Innan du startar steg 1: ta reda på om detta är ett **nytt moment eller en fortsättning**.

1. Om tema/ämne framgår av `$ARGUMENTS` eller dialogen: kontrollera om `output/lessons/[Ämne]/[Tema]/momentplan.md` redan finns. Om tema är okänt: fråga läraren "Nytt moment, eller fortsätter vi på ett påbörjat?" och lista ev. befintliga momentmappar med momentplan.md.
2. **Om en momentplan.md finns:** läs den. Sektionerna speglar stegen - identifiera senaste avklarade steg:
   - `Nivå 0 - Momenttyp` + `Root: Drivande fråga` (+ 1a-1b för brottnings-moment) → steg 1 klart
   - `Nivå 2 - Bedömningsmål` + `Lärandemål` → steg 2 klart
   - `Nivå 4 - Rollsekvens` + `Nivå 5 - Brottningsform` → steg 3 klart
   - `Lektionssekvens (rollmappning)` → steg 4 klart
   - `Frågeapp (Survey Platform)` → steg 5b klart; `Videoöversikter` → steg 5c klart
3. **Inventera artefakter på disk** mot Completion Checklist: vilka `lektion-N.md`/`.docx`, `elevuppgift-lektion-N.*`, `presentation-lektion-N.html`, `video/*.mp4`, `momentoversikt.html` finns redan? (`.docx` och `video/*.mp4` ligger i Word-mappen, inte i vaultmappen - se Sökvägar.)
4. **Återställ arbetskontexten** utan att ställa om designfrågorna: ladda rätt referensfiler för systemet (steg 1.3), läs kursminnet (steg 1.5) och återställ NotebookLM-läget (steg 1.4). Står `**NotebookLM:** AV` i Grundinformationen gäller det beslutet vidare - fråga inte om igen. Står det `PÅ`, kontrollera om att inloggningen lever (`notebooklm list --json`, läs `error`-fältet) och aktivera notebooken; en ny session betyder ofta ny auth-status.
5. **Sammanfatta läget** för läraren ("Steg 1-4 klara, lektion 1-2 av 6 genererade, inga presentationer ännu") och föreslå att fortsätta från nästa ogjorda punkt. Läraren kan välja att backa.

Skapa ALDRIG om befintliga godkända artefakter utan att fråga. Om läraren bekräftar nytt moment: fortsätt till steg 1 som vanligt.

---

## Dialogprinciper

**Packa alltid upp principer när de nämns första gången i en dialog-turn.** Skillen refererar regelbundet till Princip 1 (Scaffoldat tolkningsslag), Princip 2 (Kontextprimat) och Princip 3 (Förberedelseintegritet) - använd aldrig en princip-referens utan att samtidigt ge en kort one-liner:

- *Princip 1 - Scaffoldat tolkningsslag: vid autonomt arbete med extern text, brief pre-teach + universell scaffold + selektiv fördjupning.*
- *Princip 2 - Kontextprimat: lärarens kontextläsning får företräde vid varje vägval - men kategori 2-5 krävs (klassobservation, mönster, struktur, ämneskunnande).*
- *Princip 3 - Förberedelseintegritet: förutsättningar levereras i förväg, elevens ansvar att tillägna sig dem.*

Inom samma dialog-turn räcker det att packa upp en gång. I nya turns: packa upp igen om läraren inte uttryckligen visat att hen har principen aktivt i huvudet.

Mekanismerna **M-i** (default + alternativ), **M-ii** (override-prompt), **M-iii** (mönsterlarm) och **M-iv** (spårdokumentation i momentplan.md) aktiveras genom hela steg 1-3. Full beskrivning i `pedagogik-ramverk.md`.

**Använd AskUserQuestion för M-i-val med slutna alternativ** (momenttyp, Hess-klassificering, frågetyp, diskursmål, form): defaulten som första alternativ märkt "(Rekommenderad)", övriga med en rads beskrivning. Öppna val (frågeformulering, lärandemål) förblir fri dialog. M-ii:s turn-disciplin gäller oförändrat: blanda aldrig en override-kategorisering och ett nytt val i samma fråga.

---

## Kursminne - lärande mellan moment

Skillen har ett kursspecifikt minne (en fil per kurs i vaultet: `output/lessons/_kursminne/[kursminne-slug].md`, där sluggen anges per kurs i `kurser.json`) som gör att den blir bättre över tid. Lärarens justeringar under planeringen fångas upp och används i framtida moment för samma kurs. Minnet ligger i vaultet så att det syncas mellan maskiner via Obsidian Sync.

För filformat, regler för minneshantering och när minnet uppdateras (default vid Avslutning + mid-flight när läraren explicit ber om det), läs: `references/kursminne.md`

---

## Två kunskapskällor: NotebookLM och wikin

Planeringen lutar sig mot två källor med tydlig arbetsfördelning:

**NotebookLM (primär källa för ämnesinnehåll).** Källgrundat material med inbyggda referenshänvisningar - svarar på "vad ska eleverna lära sig om X?". Varje kurs har en bred default-notebook via fältet `notebook_id` i `kurser.json`, och ett moment kan välja en egen momentnotebook i steg 1.4 (den skrivs i momentplanen, aldrig tillbaka till `kurser.json`). Notebooken aktiveras i steg 1 och frågas genom steg 1, 3, 5 och 6.

NotebookLM är en extern tjänst vars inloggning dör tyst, och **CLI:n returnerar exit 0 även när auth är död** - använd aldrig `notebooklm doctor`, `auth check` eller exit-koden som test. Auth kontrolleras en gång i steg 1.4 (skarpt anrop + läs `error`-fältet), fallback-beslutet fattas en gång, och utfallet skrivs som `**NotebookLM:** PÅ/AV` i momentplanens Grundinformation. Är den AV hoppas alla notebook-uppslag över tyst och steg 5c utgår. För kontrollen, fallback-protokollet, CLI-kommandon och frågeprinciper, läs: `references/notebooklm-anvandning.md`

**Wikin (lärarens kunskapsbas).** Vaultets `wiki/` (index.md → topics/concepts/sources) bär lärarens ackumulerade pedagogiska evidens, didaktiska synteser och ämnessynteser - svarar på "hur undervisar jag detta bra, och vad vet jag redan?". Konsulteras i steg 1, 3 och 5; fynd som påverkar designval dokumenteras med `[[wikilänkar]]` i momentplanens sektion `## Kunskapsunderlag (wiki)`. För uppslagsprotokoll, arbetsfördelning och presentationsregler, läs: `references/wiki-anvandning.md`

---

## De sju stegen (orkestrering)

Varje steg nedan: läs stegfilen, följ den, invänta lärarens godkännande innan nästa steg.

### Steg 1: Ämne, kurs, system och designdialog (Momenttyp → Root → 1a → 1b)

Driver dialogen genom ramverkets översta nivåer: ämne/kurs/system + referensladdning, NotebookLM-koppling, kursminne, **momenttyp (nivå 0: brottnings- / färdighets- / översikts-moment)**, drivande fråga, skärpningsfilter, Hess-gate (1a - endast brottnings-moment), frågetypologi (1b - endast brottnings-moment), centralt innehåll och tvärgående trådar. **Läs och följ `references/steg-1-designdialog.md`.**
Output: skapar `momentplan.md` (Grundinformation inkl. momenttyp + Designval nivå 0-1b + Override-räknare).

### Steg 2: Bedömningsmål, lärandemål och förutsättningar (nivå 2 → 3)

Bedömningsmål ("vad är lyckat utfall?" - momenttyp-relativt: lyckad brottning / behärskad förmåga / fullgod helhetsförståelse), 3-5 lärandemål med E/C/A-progression, förutsättningar (innehåll + begrepp) med leveransplan, verifikationsregel och mönsterlarms-check. **Läs och följ `references/steg-2-mal-forutsattningar.md`.**
Output: uppdaterar `momentplan.md` (nivå 2-3 + lärandemål).

### Steg 3: Rollsekvens (nivå 4) och brottningsform (nivå 5)

Komponera momentet av roller (de 9 rollerna, core + ordningsregler), härled diskursmål → brottningsform, differentiering/UDL och formativa avstämningar. **Läs och följ `references/steg-3-roller-brottningsform.md`.**
Output: uppdaterar `momentplan.md` (rollsekvens + brottningsform + differentiering).

### Steg 4: Lektionssekvens - rollerna mappas på lektioner

Mappa rollsekvensen på det faktiska antalet lektioner med exit och form per lektion, exit ticket-slinga och progression i rolltermer. **Läs och följ `references/steg-4-lektionssekvens.md`.**
Output: uppdaterar `momentplan.md` (lektionssekvens/rollmappning).

### Steg 5: Detaljerade lektionsplaner (Word-dokument)

Generera en lektion i taget, rollbaserat, med NotebookLM-innehåll, tre evidensprinciper (retrieval/elevaktiv tid/exit ticket), kvalitetskontroll och .docx-generering. **Läs och följ `references/steg-5-lektionsplaner.md`.**
Output: `lektion-N.md` (vault) + `lektion-N.docx`.

### Steg 5a: Elevuppgifter (separata Word-dokument)

Efter varje godkänd lektionsplan: generera elevmaterial för lektionens rollkärna (arbetsblad, källmaterial, analysuppgifter) med inbyggd differentiering. **Läs och följ `references/steg-5a-elevuppgifter.md`.**
Output: `elevuppgift-lektion-N.md` + `.docx` (samma mönster för `kallmaterial-lektion-N`).

### Steg 5b: Frågor till frågeappen (Survey Platform)

Exportera klassrumsquiz till lärarens frågeapp via MCP. Om elevuppgifter genererats (steg 5a) kan hela momentet även importeras som ett sammanhållet moment (`import_moment`), så eleverna följer lektionsbågen, lämnar in digitalt och läraren kan ta ut en momentrapport (`get_moment_report`). **Läs och följ `references/frageappen.md`.**
Output: frågor + ev. moment med elevuppgifter i databasen + delningskoder i `momentplan.md`.

### Steg 5c: Videoöversikter för elever (NotebookLM)

Generera elevriktade videor: en momentöversikt-video + förförståelse-videor inför de lektioner som har elevriktat förberedelsematerial levererat i förväg (Princip 3). Laddas ner som `.mp4`, länkas från momentöversikten (steg 7). Kräver aktiv notebook och inloggad CLI. **Läs och följ `references/videooversikt-notebooklm.md`.**
Output: `video/video-*.mp4` + Videoöversikter-tabell i `momentplan.md`.

### Steg 6: Presentationer (reveal.js HTML i designsystemet Arkiv)

Generera presentationer för lektioner med instruktionsmoment, i designsystemet Arkiv, med NotebookLM-förankrat innehåll. **Läs och följ `references/presentationer-notebooklm.md`.**
Output: `presentation-lektion-N.html`.

### Steg 7: Momentöversikt för elever (HTML)

Self-contained HTML-översikt för eleverna (datum, innehåll, förberedelser, mål) - inkl. ev. delningskoder (5b) och videolänkar (5c). **Läs och följ `references/steg-7-momentoversikt.md`.**
Output: `momentoversikt.html`.

### Avslutning

Materiallista, reflektionsförslag, publiceringstips och uppdatering av kursminnet. **Läs och följ `references/avslutning.md`.**

---

## Tillval: Enskild lektion (M2)

Om `$ARGUMENTS` innehåller "enskild-lektion" eller om läraren specifikt ber om att planera en enstaka lektion:
1. Hoppa över steg 4, 6 och 7
2. Acceptera en befintlig `momentplan.md` som input
3. Fokusera på steg 5 (detaljerad lektionsplan) för en enda lektion
4. Fråga vilken lektion i momentet det gäller (eller om det är fristående)

---

## Tillval: Snabbläge

Om `$ARGUMENTS` innehåller "snabb"/"express", eller läraren ber om det: kör steg 1-4 som EN samlad designrunda i stället för fyra godkännanderundor. Skillen tar fram defaults för hela kedjan (momenttyp → fråga → Hess/typologi → bedömningsmål → lärandemål → förutsättningar → roller → form → lektionssekvens), presenterar allt som en enda sammanhållen designöversikt och ber läraren godkänna eller peka ut vad som ska ändras. M-ii (override-prompt) och M-iii (mönsterlarm) gäller fortfarande fullt ut för de val läraren ändrar. Kursminne och wiki-uppslag körs som vanligt och matar defaults.

I steg 5/5a/6 erbjuds batchgenerering: generera alla lektionsplaner (eller alla presentationer) i följd och presentera en samlad ändringslista, i stället för godkännande per artefakt. Kvalitetskontrollerna körs per artefakt precis som i normalläget.

## State Dependencies

| Steg | Input från | Output till |
|------|-----------|-------------|
| 1 | Användare + kurser.json + amnesplaner.md + **kursminne** + **wiki** (tema-uppslag) | momentplan.md |
| 2 | Steg 1 + gy11/struktur.md eller gy25/struktur.md (rätt system per kurs) | momentplan.md (uppdaterad) |
| 3 | Steg 1-2 + pedagogik-ramverk.md (nivå 4-5) + pedagogiska-metoder.md + **wiki** (metoder + reflektioner) + **NotebookLM** | momentplan.md (rollsekvens + brottningsform) |
| 4 | Steg 1-3 (rollsekvens) + lektionsplanering.md | momentplan.md (lektionssekvens/rollmappning) |
| 5 | Steg 1-4 + lektionsplanering.md + docx SKILL.md + **NotebookLM** + **wiki** (didaktik per lektion) | lektion-N.md (vault) + lektion-N.docx ([Word-mappen]\) |
| 5a | Steg 5 (godkänd lektionsplan) + docx SKILL.md | elevuppgift-lektion-N.md + .docx, kallmaterial-lektion-N.md + .docx |
| 5b | Steg 1-5 + Steg 5a (elevuppgifter) + **MCP survey-platform** | frågor + ev. moment med elevuppgifter i databasen + momentplan.md (uppdaterad) |
| 5c | Steg 1 (notebook) + Steg 4-5 (lektionsteman + förberedelsematerial) + **NotebookLM-CLI** | video-moment-oversikt.mp4 + video-forforstaelse-lektion-N.mp4 + momentplan.md (uppdaterad) |
| 6 | Steg 1-4 + arkiv-presentationer.md + presentationsteknik.md + **NotebookLM** (innehåll) | presentation-lektion-N.html |
| 7 | Steg 1-4 + html-momentoversikt SKILL.md + lärar-input + ev. delningskoder + ev. videolänkar | momentoversikt.html |

## Completion Checklist

- [ ] momentplan.md skapad med alla steg dokumenterade (inkl. momenttyp, nivå 0)
- [ ] Rollsekvens (nivå 4) dokumenterad; core-roller för momenttypen finns (brottnings-moment: Frågeförankring+Brottning+Syntes; färdighet: +Begreppsbygge+Applikation; översikt: +Perspektiv-/Begreppsbygge+Syntes)
- [ ] Brottningsform (nivå 5) dokumenterad *om momentet har en Brottning-roll* (annars ej tillämpligt)
- [ ] Varje lektion realiserar sin tilldelade roll; exit ticket mäter rollens exit
- [ ] Alla lektionsplaner genererade som .md (vault) och .docx ([Word-mappen]\)
- [ ] Elevuppgifter genererade som .md (vault) och .docx ([Word-mappen]\) för varje lektion
- [ ] Frågor genererade och exporterade till frågeappen (eller sparade som CSV om MCP ej tillgängligt)
- [ ] Moment med elevuppgifter exporterat till frågeappen (om läraren valde det)
- [ ] Videoöversikter genererade (momentöversikt + förförståelse-videor för lektioner med förberedelsematerial), nedladdade som .mp4 och loggade i momentplan.md (om notebook aktiv)
- [ ] Presentationer genererade som reveal.js HTML för lektioner med instruktionsmoment
- [ ] Momentöversikt genererad som .html (med delningskoder om frågor exporterades, och videolänkar om videor genererades)
- [ ] .md-filer sparade i vaultet (`output/lessons/[Ämne]/[Tema]/`), .docx-filer i `[Word-mappen]\[Ämne]\[Tema]\`
- [ ] Kunskapsunderlag (wiki) dokumenterat i momentplan.md med [[länkar]] (eller markerat tomt)
- [ ] AI-svaghetscheck genomförd på alla lektionsplaner
- [ ] Exit ticket-slinga verifierad (varje exit ticket mäter rollens exit och informerar nästa retrieval-öppning)
- [ ] Kursminne uppdaterat med lärdomar från detta moment
