# Steg 5b: Fragor till frageappen (Survey Platform)

Detta steg exporterar fragor direkt till lararens frageapp via MCP-servern `survey-platform`. Frageappen anvands for quiz och enkat i klassrummet - eleverna svarar pa fragor kopplade till undervisningen.

## Forberedelse

1. Kontrollera att MCP-verktyget `mcp__survey-platform__create_quiz_from_csv` ar tillgangligt. Om inte, informera lararen: "Frageappen ar inte kopplad just nu. Jag sparar fragorna som CSV istallet sa du kan importera dem manuellt." Generera da en CSV-fil till `Undervisningsmaterial/[Amne]/[Tema]/fragor.csv` och hoppa over resten av detta steg.

2. Hamta tillgangliga kurser via MCP-resursen `survey://courses`. Presentera listan och lat lararen valja vilken kurs fragorna ska kopplas till. Om kursen inte finns - informera lararen att den behover skapas i appen forst.

## Fragegenerering

Generera fragor i tva kategorier:

**A. Lektionsfragor (per lektion)**
For varje lektion, skapa 5-8 fragor:
- ~70% MULTIPLE_CHOICE med 4 svarsalternativ (ett korrekt)
- ~30% FREE_TEXT for oppna reflektioner
- Fragorna ska spegla lektionens larandemal och innehall
- Flervalsfragor ska testa forstaelse, inte bara faktaminne - inkludera fragor pa analysera/vardera-niva
- Distraktorer (felaktiga alternativ) ska vara rimliga, inte uppenbara
- Inkludera lektionens exit ticket som en av fragorna

**B. Momentfragor (overgripande)**
Skapa 5-10 fragor som spanner over hela momentet:
- Syntesfragor som kopplar ihop innehall fran flera lektioner
- Fragor pa hogre taxonomiska nivaer (jamfora, vardera, argumentera)
- Lampliga som formativ avslutscheck eller repetition

**AI-svaghetscheck for fragor (evidensbaserad):**
- Ar fragorna pa varierande taxonomiska nivaer (inte bara "vad heter...")?
- Har flervalsfragar *plausibla* distraktorer - baserade pa elevers faktiska missuppfattningar, inte slumpfakta?
- Undviker distraktorer cue-ledande monster (langsta alternativet, "alla ovan", "ingen av dem")?
- Tacker fragorna de centrala larandemalen? (Specificitetslagen: testning ar lokal - det du inte fragar om blir inte starkare)
- Inkluderar oppna fragor mojlighet till analys/reflektion?
- **Verb-kalibrering**: Anvander fragorna "vardera/jamfor/argumentera" for C/A-niva, inte "beskriv/forklara"?
- **Sweet spot-kalibrering**: Strava efter fragor dar eleverna lyckas svara ratt i 60-85% av fallen pa forsta forsoket (Pyke et al. 2025). Under 60% = frustration, over 85% = ingen larandeeffekt.
- **AI-genererade fragor**: Rakna med ~31% forkastningstakt (Ahmed, Kerr & O'Malley 2025). Generera ~15 fragor for att behalla 10. Kontrollera fakta mot NotebookLM-kallor.
- **Format-matching**: MCQ-ovning tranar bara for MCQ-prov. Om sluttestet ar essa, inkludera VSAQ/fritext-fragor i banken.
- **Spacing-formel**: Planera retrieval review sa att samma fraga ateranvands efter ~10% av det retentionsintervall du vill uppnaa (for ett prov om 4 veckor → repetera efter ~3 dagar).

**Lamplig AI-feedbacktyp per frageformat:**
- **MCQ**: elaborativ feedback (forklarar varfor ratt/fel) - sarskilt kraftfullt nar eleven svarade fel (hypercorrection)
- **VSAQ/fritext**: elaborativ feedback ar *nodvandig* - utan den ar transfer-effekten nastan noll
- Undvik: enbart "ratt/fel" pa oppna svar - minimal pedagogisk nytta

## Presentation och godkannande

Presentera fragorna grupperade per lektion i en oversiktlig lista:
```
Lektion 1: [Titel]
  1. (MULTIPLE_CHOICE) [fragetext] → Korrekt: [svar]
  2. (FREE_TEXT) [fragetext]
  ...

Lektion 2: [Titel]
  ...

Momentfragor (overgripande):
  ...
```

Fraga lararen: "Vill du andra, lagga till eller ta bort nagon fraga innan jag exporterar till appen?"

## Export till frageappen

Nar lararen godkant fragorna anvands MCP-verktyget `create_quiz_from_csv` - det importerar fragorna till frageappen OCH skapar quizzen i ett enda anrop, sa du behover aldrig halla reda pa fraga-ID:n.

CSV-format (samma for alla anrop):
```
topic,type,text,option1,option2,option3,option4,correctAnswer
```
- For MULTIPLE_CHOICE med korrekt svar: fyll i `correctAnswer` (exakt samma text som ratt alternativ).
- For FREE_TEXT: lamna option- och correctAnswer-kolumnerna tomma.
- Fragornas ordning i quizzen foljer raderna i CSV:n.

1. **Skapa en quiz per lektion** - Ett `create_quiz_from_csv`-anrop per lektion:
   - `course_id`: kursen lararen valde
   - `title`: `[Tema] - Lektion N: [Titel]`
   - `csv_content`: lektionens fragor, med topic-kolumnen satt till `[Tema] - Lektion N: [Titel]`
   - `mode`: `QUIZ`
   - (`lock_mode`: `true` endast om lararen vill kora lektionen som prov)

2. **Skapa momentquiz** - Ett sista `create_quiz_from_csv`-anrop med de overgripande momentfragorna:
   - `title`: `[Tema] - Momentquiz`
   - `csv_content`: momentfragorna, med topic-kolumnen satt till `[Tema] - Overgripande`
   - `mode`: `QUIZ`

   Verktyget returnerar `shareCode` och `url` (`/s/[kod]`) for varje skapad quiz - spara dem till nasta steg.

3. **Presentera resultat** for lararen:
   ```
   Exporterat till frageappen:
   - [N] fragor importerade
   - Quiz skapade:
     - Lektion 1: [Titel] - delningskod: [kod]
     - Lektion 2: [Titel] - delningskod: [kod]
     - ...
     - Momentquiz: [Tema] - delningskod: [kod]
   ```

4. **Spara delningskoder** till momentplanen (`momentplan.md`) under en ny sektion:
   ```markdown
   ## Frageapp (Survey Platform)
   | Quiz | Delningskod | Antal fragor |
   |------|------------|-------------|
   | Lektion 1: [Titel] | [kod] | [N] |
   | ... | ... | ... |
   | Momentquiz | [kod] | [N] |
   ```
