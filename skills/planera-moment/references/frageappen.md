# Steg 5b: Frågor till frågeappen (Survey Platform)

Detta steg exporterar frågor direkt till lärarens frågeapp via MCP-servern `survey-platform`. Frågeappen används för quiz och enkät i klassrummet - eleverna svarar på frågor kopplade till undervisningen.

## Förberedelse

1. Kontrollera att MCP-verktyget `mcp__survey-platform__create_quiz_from_csv` är tillgängligt. Om inte, informera läraren: "Frågeappen är inte kopplad just nu. Jag sparar frågorna som CSV istället så du kan importera dem manuellt." Generera då en CSV-fil till `output/lessons/[Ämne]/[Tema]/fragor.csv` och hoppa över resten av detta steg.

2. Hämta tillgängliga kurser via MCP-resursen `survey://courses` (kräver `ListMcpResourcesTool`/`ReadMcpResourceTool`). Om resursläsning inte är tillgänglig, be läraren ange kurs (kurserna syns i appens admin). Presentera listan och låt läraren välja vilken kurs frågorna ska kopplas till. Om kursen inte finns - informera läraren att den behöver skapas i appen först.

## Frågegenerering

Anpassa frågeprofilen efter momenttypen (momentplan.md): brottnings-moment → perspektiv-/argumentationsfrågor; färdighets-moment → tillämpningsfrågor på nya fall; översikts-moment → samband/översiktsfrågor.

Generera frågor i två kategorier:

**A. Lektionsfrågor (per lektion)**
För varje lektion, skapa 5-8 frågor:
- ~70% MULTIPLE_CHOICE med 4 svarsalternativ (ett korrekt)
- ~30% FREE_TEXT för öppna reflektioner
- Frågorna ska spegla lektionens lärandemål och innehåll
- Flervalsfrågor ska testa förståelse, inte bara faktaminne - inkludera frågor på analysera/värdera-nivå
- Distraktorer (felaktiga alternativ) ska vara rimliga, inte uppenbara
- Inkludera lektionens exit ticket som en av frågorna

**B. Momentfrågor (övergripande)**
Skapa 5-10 frågor som spänner över hela momentet:
- Syntesfrågor som kopplar ihop innehåll från flera lektioner
- Frågor på högre taxonomiska nivåer (jämföra, värdera, argumentera)
- Lämpliga som formativ avslutscheck eller repetition

**AI-svaghetscheck för frågor (evidensbaserad):**
- Är frågorna på varierande taxonomiska nivåer (inte bara "vad heter...")?
- Har flervalsfrågor *plausibla* distraktorer - baserade på elevers faktiska missuppfattningar, inte slumpfakta?
- Undviker distraktorer cue-ledande mönster (längsta alternativet, "alla ovan", "ingen av dem")?
- Täcker frågorna de centrala lärandemålen? (Specificitetslagen: testning är lokal - det du inte frågar om blir inte starkare)
- Inkluderar öppna frågor möjlighet till analys/reflektion?
- **Verb-kalibrering**: Använder frågorna "värdera/jämför/argumentera" för C/A-nivå, inte "beskriv/förklara"?
- **Sweet spot-kalibrering**: Sträva efter frågor där eleverna lyckas svara rätt i ~70-85% av fallen på första försöket (desirable difficulty; Bjork & Bjork). För lågt = frustration, för högt = ingen lärandeeffekt.
- **AI-genererade frågor**: Räkna med ~31% förkastningstakt (Ahmed, Kerr & O'Malley 2025). Generera ~15 frågor för att behålla 10. Kontrollera fakta mot NotebookLM-källor.
- **Format-matching**: MCQ-övning tränar bara för MCQ-prov. Om sluttestet är essä, inkludera VSAQ/fritext-frågor i banken.
- **Spacing-formel**: Planera retrieval review så att samma fråga återanvänds efter ~10% av det retentionsintervall du vill uppnå (för ett prov om 4 veckor → repetera efter ~3 dagar).

**Lämplig AI-feedbacktyp per frågeformat:**
- **MCQ**: elaborativ feedback (förklarar varför rätt/fel) - särskilt kraftfullt när eleven svarade fel (hypercorrection)
- **VSAQ/fritext**: elaborativ feedback är *nödvändig* - utan den är transfer-effekten nästan noll
- Undvik: enbart "rätt/fel" på öppna svar - minimal pedagogisk nytta
- **Inga betygsbokstäver i elevriktad feedback:** E/C/A är planeringsspråk. Elevriktad fritext-feedback (som eleven läser direkt) ska aldrig innehålla E/C/A i texten - låt nästa-steg bära nivån.

## Presentation och godkännande

Presentera frågorna grupperade per lektion i en överskådlig lista:
```
Lektion 1: [Titel]
  1. (MULTIPLE_CHOICE) [frågetext] → Korrekt: [svar]
  2. (FREE_TEXT) [frågetext]
  ...

Lektion 2: [Titel]
  ...

Momentfrågor (övergripande):
  ...
```

Fråga läraren: "Vill du ändra, lägga till eller ta bort någon fråga innan jag exporterar till appen?"

## Export till frågeappen

När läraren godkänt frågorna används MCP-verktyget `create_quiz_from_csv` - det importerar frågorna till frågeappen OCH skapar quizzen i ett enda anrop, så du behöver aldrig hålla reda på fråga-ID:n.

CSV-format (samma för alla anrop):
```
topic,type,text,option1,option2,option3,option4,correctAnswer
```
- För MULTIPLE_CHOICE med korrekt svar: fyll i `correctAnswer` (exakt samma text som rätt alternativ).
- För FREE_TEXT: lämna option- och correctAnswer-kolumnerna tomma.
- Frågornas ordning i quizzen följer raderna i CSV:n.

1. **Skapa en quiz per lektion** - Ett `create_quiz_from_csv`-anrop per lektion:
   - `course_id`: kursen läraren valde
   - `title`: `[Tema] - Lektion N: [Titel]`
   - `csv_content`: lektionens frågor, med topic-kolumnen satt till `[Tema] - Lektion N: [Titel]`
   - `mode`: `QUIZ`
   - (`lock_mode`: `true` endast om läraren vill köra lektionen som prov)

2. **Skapa momentquiz** - Ett sista `create_quiz_from_csv`-anrop med de övergripande momentfrågorna:
   - `title`: `[Tema] - Momentquiz`
   - `csv_content`: momentfrågorna, med topic-kolumnen satt till `[Tema] - Övergripande`
   - `mode`: `QUIZ`

   Verktyget returnerar `shareCode` och `url` (`/s/[kod]`) för varje skapad quiz - spara dem till nästa steg.

3. **Presentera resultat** för läraren:
   ```
   Exporterat till frågeappen:
   - [N] frågor importerade
   - Quiz skapade:
     - Lektion 1: [Titel] - delningskod: [kod]
     - Lektion 2: [Titel] - delningskod: [kod]
     - ...
     - Momentquiz: [Tema] - delningskod: [kod]
   ```

4. **Spara delningskoder** till momentplanen (`momentplan.md`) under en ny sektion:
   ```markdown
   ## Frågeapp (Survey Platform)
   | Quiz | Delningskod | Antal frågor |
   |------|------------|-------------|
   | Lektion 1: [Titel] | [kod] | [N] |
   | ... | ... | ... |
   | Momentquiz | [kod] | [N] |
   ```

## Momentexport (elevuppgifter till appen)

Utöver klassrumsquizet ovan kan hela momentet - med elevuppgifterna från steg 5a - importeras som ett sammanhållet **moment** i frågeappen. Då får eleverna en momentsida där de följer hela lektionsbågen, lämnar in uppgifterna digitalt och kan få feedback där, och läraren kan ta ut en momentrapport. Detta är skarpt verifierat på prod (verktygen `import_moment` + `get_moment_report`).

Körs efter steg 5a, när elevuppgifter finns. **Frivilligt** - fråga läraren:

> "Vill du även importera momentet med elevuppgifterna till frågeappen, så att eleverna kan lämna in och du kan ge feedback där?"

Om läraren avböjer: hoppa över detta avsnitt (quiz-exporten ovan räcker).

### Bygg import_moment-anropet

Använd MCP-verktyget `mcp__survey-platform__import_moment`. Bygg anropet från `momentplan.md` och de godkända elevuppgifterna. Anpassa exakta fältnamn efter det faktiska verktygsschemat - hitta inte på parametrar.

- `course_id`: kursen läraren valde (samma som ovan).
- `title`: momentnamnet (temat ur momentplan.md).
- `description` (valfritt): kort momentbeskrivning.
- `period` (valfritt): momentets tidsperiod, t.ex. "ca 800-300 f.Kr." (visas i elevens momenthuvud).
- `goals` (valfritt): lärandemålen på momentnivå (ur momentplan.md nivå 2) - visas för eleven.
- `lessons`: **hela** lektionsbågen, en post per lektion `{n, title, note?, date?, week?}` - även lektioner utan digital uppgift (fyll `note` med t.ex. "läsning + diskussion"). Sätt `date` (ISO `YYYY-MM-DD`) och/eller `week` om lektionsdatum är kända (driver missad/kommande-status och veckogruppering i elevvyn); annars utelämna.
- `assignments`: en post per elevuppgift, `{title, csv_content, lesson?, mode?, lock_mode?}`:
  - `title`: uppgiftens titel (t.ex. `Lektion N: [uppgiftsnamn]`).
  - `lesson`: lektionsnumret (matchar `lessons[].n`) som uppgiften hör till.
  - `csv_content`: uppgiftens frågor i samma CSV-format som ovan (`topic,type,text,option1,...,correctAnswer`). En skrivuppgift (analysuppgift/exit ticket) blir en `FREE_TEXT`-rad; ett inbäddat quiz blir `MULTIPLE_CHOICE`-rader.
  - `mode`: `QUIZ` för rättade frågor, `SURVEY` för öppna inlämningar/exit tickets.
  - `lock_mode`: `true` endast om uppgiften ska köras som prov.

Bygg en `assignment` per `elevuppgift-lektion-N` (instruktionen hämtas ur dokumentets kontextsättning). Exit tickets läggs som `SURVEY`/`FREE_TEXT` per lektion (de trycks aldrig i arbetsbladen - de görs digitalt här).

### Spara resultatet

Verktyget returnerar `unitId` (+ ev. share-koder per uppgift). Spara `unitId` och koderna i `momentplan.md` under `## Frågeapp (Survey Platform)` - utöka den befintliga tabellen med en rad/undersektion för momentet, t.ex.:

```markdown
### Moment i frågeappen
- unitId: [N] - elevmomentsida: `/student/moment/[N]`
| Uppgift | Lektion | Delningskod |
|---------|---------|-------------|
| [titel] | N | [kod] |
```

Nämn för läraren att `mcp__survey-platform__get_moment_report` kan köras när eleverna lämnat in (efter genomförandet, t.ex. i samband med `/reflektera-moment`) för att få ett aggregerat rapportunderlag per moment.
