---
description: >
  Planera ett komplett undervisningsmoment för gymnasiet genom en dialogdriven
  7-stegsprocess. Genererar lektionsplaner (Word/.docx), presentationer
  (reveal.js HTML) och momentöversikt (HTML) - allt förankrat i Gy11,
  Rosenshines forskning och evidensbaserad pedagogik. Använd ALLTID denna skill
  när användaren vill planera ett moment, planera undervisning, skapa
  lektionsplaner för flera lektioner, göra en momentplanering, strukturera ett
  undervisningsupplägg, eller ber om hjälp att planera lektioner i
  samhällskunskap, historia eller juridik. Triggas även av fraser som "planera
  ett moment", "planera-moment", "momentplanering", "jag vill planera", "hjälp
  mig planera", "skapa lektionsplaner", "planera undervisningen", "planera
  lektioner om [ämne]", eller när användaren beskriver ett ämne/tema och antal
  lektioner de vill ha. Denna skill ska INTE användas för enskilda dokument
  (använd docx/pptx), enskilda lektionsplaner utan momentkontext, eller
  HTML-momentöversikter från befintlig data (använd html-momentoversikt).
allowed-tools: Read, Write, Edit, Bash(node:*), Bash(npm:*), Bash(python:*), Bash(pip:*), Bash(pdftoppm:*), Bash(notebooklm:*), mcp__survey-platform__import_questions, mcp__survey-platform__create_survey, mcp__survey-platform__get_results, mcp__survey-platform__summarize_results
argument-hint: "[amne (valfritt)]"
---

Tala svenska genom hela processen. Du ar ett stod for en professionell gymnasielarare - lararen fattar alla pedagogiska beslut, du hjalper att strukturera och producera material.

Las in det pedagogiska ramverket:
@pedagogik-ramverk.md

Genomfor en 7-stegsprocess for att planera ett komplett undervisningsmoment. Ga ALDRIG vidare till nasta steg utan lararens uttryckliga godkannande. Vid varje steg: presentera konkreta forslag, invanta beslut, bekrafta beslutet genom att sammanfatta det.

Skapa output-kataloger for momentet pa tva platser:
- **Markdown (.md)** sparas i vaultet: `Undervisningsmaterial/[Amne]/[Tema]/`
- **Word (.docx)** sparas utanfor vaultet: `/home/anders/undervisningsmaterial/[Amne]/[Tema]/`

Strukturen ar identisk pa bada platser (t.ex. `Historia/Franska revolutionen/`). Amne ska ha stor bokstav, tema ska vara lasbart med mellanslag. Skapa katalogerna om de inte finns.

---

## Dialogprinciper

**Packa alltid upp principer när de nämns första gången i en dialog-turn.** Skillen refererar regelbundet till Princip 1 (Scaffoldat tolkningsslag), Princip 2 (Kontextprimat) och Princip 3 (Förberedelseintegritet) - använd aldrig en princip-referens utan att samtidigt ge en kort one-liner:

- *Princip 1 - Scaffoldat tolkningsslag: vid autonomt arbete med extern text, brief pre-teach + universell scaffold + selektiv fördjupning.*
- *Princip 2 - Kontextprimat: lärarens kontextläsning får företräde vid varje vägval - men kategori 2-5 krävs (klassobservation, mönster, struktur, ämneskunnande).*
- *Princip 3 - Förberedelseintegritet: förutsättningar levereras i förväg, elevens ansvar att tillägna sig dem.*

Inom samma dialog-turn räcker det att packa upp en gång. I nya turns: packa upp igen om läraren inte uttryckligen visat att hen har principen aktivt i huvudet.

---

## Kursminne - lärande mellan moment

Skillen har ett kursspecifikt minne som gor att den blir battre over tid. Nar lararen justerar forslag under planeringen - andrar tidsfordelning, valjer bort aktiviteter, lagger till saker - ar det signaler om preferenser. Dessa fangas upp automatiskt och anvands i framtida moment for samma kurs.

Minnesfiler lagras per kurs i `.claude/planera-moment/minne/[kursnamn-kebab-case].md`.

For fullstandigt filformat och regler for minneshantering, las:
@references/kursminne.md

### Mid-flight uppdateringar

Som default uppdateras kursminnet i Avslutningen (en samlad analys av hela momentet). Men om läraren under planeringsdialogen **explicit säger** något i stil med:
- "spara detta i kursminnet"
- "kom ihåg det här till nästa moment"
- "lägg till i kursminnet att..."

→ uppdatera kursminnesfilen **direkt** (inte vid Avslutning), bekräfta för läraren ("Sparat: [kort beskrivning]"), och notera i momentplan.md under "Tvärgående trådar > Inter-moment" att kursminnet uppdaterades vid denna plats.

Avslutningens kursminnes-uppdatering blir då en *sammanfattning + utfyllnad av det som inte fångades mid-flight*, inte enda tillfället.

---

## NotebookLM-integration (primar kallkalla)

NotebookLM ar den primara kallan for amnesinnehall. Varje kurs har en dedicerad notebook med lararens valda kallmaterial (larobocker, Skolverkets material, artiklar, primorkallor). Innehall fran NotebookLM ar kallgrundat och har inbyggda referenshanvisningar - detta minskar behovet av `[VERIFIERA]`-taggar avsevart.

### Konfiguration

Las in notebook-konfigurationen:
@notebook-config.json

Notebook-ID:n kopplar kursnamn till NotebookLM-notebooks. Om en kurs saknar notebook-ID, informera lararen och fraga om de vill fortsatta utan NotebookLM (da anvands Claudes inbyggda kunskap som fallback, med fler `[VERIFIERA]`-taggar).

### Hur NotebookLM anvands

Nar kursen ar vald i steg 1, aktivera notebooken:
```bash
notebooklm use [NOTEBOOK_ID]
```

Fraga notebooken med `notebooklm ask` - anvand `--json` for att fa strukturerade svar med kallhanvisningar:
```bash
notebooklm ask --json "fraga har"
```

Varje anrop utan `-c` (conversation ID) startar en ny konversation. For uppfoljningsfragor i samma kontext, anvand `-c` med konversations-ID:t fran foregaende svar (finns i JSON-output som `conversation_id`):
```bash
notebooklm ask -c [CONVERSATION_ID] --json "uppfoljningsfraga"
```

Principer for NotebookLM-fragor:
- Stall specifika, avgransade fragor - inte "beratta allt om X"
- Anvand `--json` for att fa kallhanvisningar som kan foras in i materialet
- Om svaret ar otillrackligt, stall uppfoljningsfragor eller bredda sokningen
- Presentera NotebookLM:s kallhanvisningar for lararen sa de kan verifiera

---

## Steg 1: Ämne, kurs, system och designdialog (Ramverkets nivå Root → 1a → 1b)

Detta steg driver dialogen genom Momentplaneringsramverkets översta nivåer. Mekanismerna M-i (default + alternativ), M-ii (override-prompt) och M-iv (spårdokumentation) aktiveras vid varje val. Se @pedagogik-ramverk.md.

### 1.1 Ämne

Om `$ARGUMENTS` angavs, använd det som ämne. Annars fråga: "Vilket ämne vill du planera för? (samhällskunskap eller historia)"

**Hoppa över 1.1 och 1.2** om ämne *och* kurs redan är kända från $ARGUMENTS eller från tidigare dialog (t.ex. när läraren startat skillen via vald ingång). Gå direkt till 1.3 och bekräfta.

### 1.2 Kurs

Presentera kurser per system. Filtrera efter valt ämne.

**GY11-kurser (avvecklas successivt):**
- Samhällskunskap 1a2 (50 p)
- Internationella relationer (100 p)

**GY25-kurser:**
- Samhällskunskap Nivå 1b (100 p)
- Historia Nivå 1b (100 p)

### 1.3 System-detektering och referensladdning

Baserat på kursval, identifiera system och ladda rätt referensfiler. Bekräfta för läraren.

| Kurs | System | Filer att ladda |
|---|---|---|
| Sh 1a2 | GY11 | `references/gy11/struktur.md` + `references/gy11/amnesplaner.md` |
| Internationella relationer | GY11 | (samma) |
| Sh Nivå 1b | GY25 | `references/gy25/struktur.md` + `references/gy25/amnesplaner.md` |
| Hi Nivå 1b | GY25 | (samma) |

Bekräfta: "Detta moment går under [GY11 / GY25] - jag använder [kunskapskrav-modellen / betygskriterier-modellen] och kommer formulera lärandemål med [systemets värdeord]."

### 1.4 NotebookLM-koppling

Slå upp notebook-ID i `notebook-config.json`. Om det finns, aktivera:
```bash
notebooklm use [NOTEBOOK_ID]
```
Bekräfta för läraren. Om ID saknas, informera om fallback till Claudes inbyggda kunskap med `[VERIFIERA]`-taggar.

### 1.5 Kursminne - försörjer M-i:s defaults

Läs `.claude/planera-moment/minne/[kursnamn-kebab-case].md` om den finns. **Detta minne försörjer M-i:s defaults nedströms.** När skillen i 1.7-1.8 (och senare 2.x) föreslår defaults ska de vägas mot minnet.

Presentera kort: "Tidigare moment i [kursnamn] visar mönster - t.ex. [1-2 saker som verkar relevanta för det här momentet]. Jag använder dem som **default men inte tvång** - säg till nu om något inte passar detta moment innan vi börjar, så slipper vi korrigera halvvägs in."

Tonregler för kursminnes-presentation:
- Säg "mönster" och "verkar" - undvik "vet" och "föredrar alltid"
- Lyft högst 2 saker. Hela listan finns i filen - överbelasta inte dialogen
- Inbjud aktivt till avfärdande: "säg till om något inte passar"

Om filen inte finns, säg ingenting.

### 1.6 Root: Brottningsfrågan

Fråga: "Vilken fråga ska eleverna brottas med under detta moment?"

Stöd läraren att formulera en kärnfråga som kan driva 5-10 lektioner. Om läraren behöver hjälp att fokusera, ställ:
- "Vad ska eleverna kunna säga, försvara eller överväga efter momentet som de inte kan idag?"
- "Finns det en aktuell händelse, ett dilemma eller en spänning som kan vara ingången?"

Spara frågan ordagrant.

### 1.6.5 Skärpningsfilter - innan klassificering

Innan frågan klassificeras (1.7-1.8), testa den mot tre kriterier. Varje test ska kunna besvaras "ja" - annars föreslå skärpning innan vi går vidare.

1. **Spänningstest:** Har frågan en inbyggd spänning (X *vs* Y, kontrast, värdekonflikt) eller är den öppet undersökande utan motkraft? Frågor utan inbyggd spänning ger inte brottning - eleverna kan svara "lite av varje" och få rätt.

2. **Bärighetstest:** Kan frågan driva *varje* lektion i momentet, eller bara introducera momentet? En momentintro-fråga blir tom från lektion 3 och framåt.

3. **Default-genererings-test:** Kan skillen själv ge en konkret default-Hess-klassificering med säkerhet baserat på frågans formulering? Om inte - frågan är för vag för att klassificeras.

**Om ett test fallerar:** Presentera 2-3 skärpningar enligt M-i (default + alternativ med pedagogisk motivering). Be läraren välja eller forma något eget. Acceptera *inte* den ursprungliga vaga frågan om något test fallerade - det är skillens jobb att skydda momentet från luddigheten, inte tvärtom.

**Om alla tre tester passerar:** Gå direkt till 1.7.

### 1.7 Nivå 1a - Hess-gate

Klassificera frågan (Hess 2009): **sluten | tippande | öppen**.

**Default-rekommendation (M-i):** Skillen föreslår klassificering baserat på frågan + ev. kursminne. T.ex. "Frågan 'Bör Sverige ha straffrabatt för unga?' är öppen policyfråga - naturlig brottningskandidat."

#### Vid SLUTEN fråga

Förklara: "Detta är en sluten fråga - det finns ett etablerat rätt svar. Att brotta över den är inautentiskt pedagogiskt. Den kan tas in i Begreppsbygge eller Perspektivbygge istället."

Erbjud tre vägar:
1. **Omformulera** frågan till en öppen/tippande variant - föreslå konkret omformulering
2. **Behåll** frågan men placera den i Begreppsbygge i Steg 4 (då är det inte brottningsfråga)
3. **Avbryt** och välj ny fråga

Återgå till 1.6 om läraren väljer 1 eller 3.

#### Vid TIPPANDE fråga

Förklara: "Detta är en tippande fråga - bred samhällskonsensus men inte universellt. Vi lägger på position-tilldelning som default i Steg 5 (Formvalsprincip 3) för att skydda elever med minoritetsposition."

#### Vid ÖPPEN fråga

"Naturlig brottningskandidat. Fortsätt."

**Override-prompt (M-ii):** Om läraren går emot defaulten, fråga: *"Vilken kontextläsning motiverar avvikelsen? Kategori 2-5 (specifik klassobservation | mönster över tid | strukturella faktorer | ämneskunnande)."*

Magkänsla utan stöd avvisas - defaulten vinner.

### 1.8 Nivå 1b - Frågetypologi (ämnesspecifik)

Gäller bara öppna och tippande frågor.

**Historia:** Disciplinär | Etisk | Existentiell
**Samhällskunskap:** Hess-fråga | Värdefråga | Analysfråga | Existentiell

**Default-rekommendation (M-i):** Baserat på frågans formulering + kursminne. T.ex. "Frågan 'Bör Sverige ha straffrabatt för unga?' är en Värdefråga (normativ - vad bör gälla)."

Visa övriga alternativ med kort förklaring. Be om val.

**Sekundär frågetyp (valbar):** Om frågan har en tydlig andra-axel utöver den primära, dokumentera den som sekundär typ. Sekundär typ är inte ett separat val utan en *flagga* om vad som lever vidare nedströms. Skillen ska aktivt fråga: "Har frågan en sekundär dimension? Om ja - vilken av de övriga typerna?"

Sekundär typ påverkar:
- **Bedömningsmål (2.2):** kan väva in båda dimensionerna i prövningsverben
- **Lärandemål (2.3):** kan inkludera mål som primärt adresserar sekundär-axeln
- **Nivå 4 (parkerad - roller):** Syntes/metareflektion-roller adresserar ofta sekundär-axeln

**Override-prompt (M-ii):** Samma form som 1.7.

### 1.9 Centralt innehåll

Presentera CI från laddad amnesplaner-fil (gy11 eller gy25), organiserat efter dess rubriker. Be läraren välja vilka punkter momentet ska täcka.

**NotebookLM:** Om aktiv, sök efter material om de valda punkterna:
```bash
notebooklm ask --json "Vilka centrala begrepp och perspektiv finns kring [valda CI-punkter]?"
```

### 1.10 Antal lektioner och tema/vinkel

Fråga: "Hur många lektioner (och hur långa)? Finns det ett specifikt tema eller vinkel?"

### 1.10.5 Tvärgående trådar (valbar)

Fråga: "Finns det en bivinkel/överlagring som ska löpa genom momentet, eller en koppling till andra moment i kursen som ska väckas senare?"

Två sub-fält:

- **Intra-moment** (bivinkel som vävs in i flera lektioner inom momentet): T.ex. "kontinuitet/förändring som genomgående analyslins", eller "historiebruks-perspektiv aktiveras vid varje brytpunkt". Dokumenteras i momentplan.md och informerar lektionsstrukturen.

- **Inter-moment** (framtida koppling som väcks i senare moment): T.ex. "när kursen senare når renässansen, väck tråden tillbaka till detta moment". Sparas i **kursminnet** (under sektionen "Tvärgående trådar mellan moment") så att framtida moment kan plocka upp den.

Om läraren inte har någon tvärgående tråd, hoppa över - det är frivilligt.

### 1.11 Sammanfattning och momentplan.md (M-iv)

Sammanfatta valen och be läraren bekräfta. Skapa `Undervisningsmaterial/[Ämne]/[Tema]/momentplan.md`:

```markdown
# Momentplan: [Tema]

## Grundinformation
- **Ämne/Kurs:** [val]
- **System:** GY11 | GY25
- **Centralt innehåll:** [valda punkter]
- **Antal lektioner:** [N] × [X] minuter
- **Tema/vinkel:** [ev.]

## Designval (Momentplaneringsramverket)

### Root: Brottningsfråga
> [frågan ordagrant]

### Nivå 1a - Hess-gate
- **Klassificering:** [sluten | tippande | öppen]
- **Default:** [systemets rekommendation]
- **Valt:** [lärarens val]
- **Override:** [Nej | Ja - kategori X kontextläsning: "..."]

### Nivå 1b - Frågetypologi
- **Primär typ:** [...]
- **Sekundär typ:** [... eller "ingen"]
- **Default:** [...]
- **Valt:** [...]
- **Override:** [Nej | Ja - kategori X: "..."]

### Tvärgående trådar (valbart)
- **Intra-moment:** [bivinkel eller "ingen"]
- **Inter-moment:** [framtida koppling sparad i kursminne, eller "ingen"]

## Override-räknare
- **Antal overrides hittills:** [N]
- **Mönsterlarm:** [Inte triggat | Triggat på princip X - motivering: "..."]
```

---

## Steg 2: Bedömningsmål, lärandemål och förutsättningar (Ramverkets nivå 2 → 3)

Detta steg fortsätter designdialogen genom Momentplaneringsramverkets nivå 2 (Vad är lyckad brottning?) och nivå 3 (Förutsättningar för brottning). M-i, M-ii, M-iii och M-iv aktiveras.

### 2.1 Ladda systemets struktur-fil

Baserat på system från Steg 1.3, läs:
- **GY11:** `references/gy11/struktur.md`
- **GY25:** `references/gy25/struktur.md`

### 2.2 Nivå 2 - Bedömningsmål: Vad är lyckad brottning?

Fråga: "Vad ska 'lyckad brottning' innebära för eleverna i detta moment?"

**Default-rekommendation (M-i):** Skillen föreslår bedömningsmål baserat på frågetypen från 1.8 + kursminne. Exempel-mappning:

| Frågetyp (1.8) | Default-bedömningsmål |
|---|---|
| Värdefråga / Hess-fråga | Eleven kan formulera och försvara en egen ståndpunkt med motargument |
| Etisk fråga (historia) | Eleven kan väga aktörers ansvar mot tidens villkor |
| Disciplinär fråga | Eleven kan formulera en historiskt välgrundad tolkning |
| Analysfråga | Eleven kan identifiera flera orsaker och konsekvenser med teorianvändning |
| Existentiell fråga | Eleven kan formulera sitt eget förhållande till frågan med begreppsstöd |

Visa default + alternativ. Be om val.

**Viktigt:** Vissa bedömningsmål låser diskursmålet (Steg 5 nivå 5 - byggs senare). T.ex. "kan formulera motståndarens starkaste position" → låser syntes-DNA.

**Override-prompt (M-ii):** Vid avvikelse från default - fråga om kontextläsningskategori.

### 2.3 Lärandemål med E/C/A-progression

Föreslå **3-5 konkreta lärandemål** som operationaliserar bedömningsmålet mot det centrala innehållet. Varje mål ska:

- Använda verb från **rätt system:**
  - **GY11:** verb från kunskapskraven (redogöra, analysera, resonera, jämföra, diskutera)
  - **GY25:** verb från betygskriterierna + GY25:s värdeord (godtagbara/goda/mycket goda; enkla/utvecklade/välutvecklade)
- Visa E/C/A-progression explicit
- Koppla till valt CI

**Default-rekommendation (M-i):** Skillen genererar förslag baserat på (a) bedömningsmål från 2.2, (b) CI från 1.9, (c) kursminnesdata.

Presentera med E/C/A-progressionen synlig. Fråga om läraren vill ändra/lägga till/ta bort.

**Override-prompt (M-ii):** Vid avvikelse - fråga om kontextläsningskategori.

### 2.4 Nivå 3 - Förutsättningar för brottning

Identifiera **två kategorier**:

1. **Innehåll** - fakta, händelser, kontext eleven måste känna till
2. **Begrepp** - fackbegrepp eleven måste kunna använda

*Argumentation och disciplinära färdigheter hör INTE hit - de är utvecklingsbåge över moment (bedöms via 2.2-2.3).*

**Default-rekommendation (M-i):** Skillen genererar lista baserat på bedömningsmål + CI + (om aktiv) NotebookLM-uppslag på "vad måste eleven känna till för att kunna brottas med [frågan]?".

**För varje förutsättning ska skillen peka ut leveransplan** - fyra kategorier:

| Leveransstatus | Innebörd | Princip 3-status |
|---|---|---|
| **Ärvd** | Från tidigare moment/kurs | Uppfyller helt |
| **Förförståelse** | Levereras i förförståelsepaket innan momentet | Uppfyller |
| **L1 etablerar** | Introduceras i momentets första lektion | Mjuk (uppfyller om L1 ligger innan första brottnings-lektion) |
| **Bygg-upp-under-momentet** | Levereras i samma lektion eller efter att den används | **Override mot Princip 3 - kräv motivering (M-ii)** |

**Cirkularitetskontroll:** Om en förutsättning får leveransstatus "Bygg-upp-under-momentet" *och* förutsättningen behövs för att den lektionens huvudaktivitet ska fungera → **flagga intern konflikt** och be läraren välja:
- (a) Flytta förutsättningen till Förförståelse eller en tidigare lektion
- (b) Acceptera override mot Princip 3 (M-ii triggas, motivering krävs)
- (c) Omformulera lektionsstrukturen så förutsättningen levereras tidigare

Presentera leveranstabellen för läraren, be hen justera. Acceptera inte en förutsättning utan utpekad leveransplan.

#### Verifikationsregel (mjuk + spårbar)

Innan brottning släpps lös, bedöm mot **tre dimensioner** - be läraren resonera kring varje:

1. **Andel + spridning:** Hur stor del av klassen har förutsättningarna? Finns elever totalt utan?
2. **Konsekvens av luckan:** Räcker det att tappa nyans, eller blir brottningen meningslös?
3. **Frågetypens tolerans:** Hess-frågor tål okunnigt deltagande bättre än disciplinära källfrågor.

Inga hårda tröskelvärden. Lärarens bedömning står i centrum.

### 2.5 Princip 3 - Förberedelseintegritet

Bekräfta principen: *"Brottning väntar inte på att alla ska vara redo. Förutsättningar levereras i förväg och det är elevens ansvar att ha tillägnat sig dem. Differentierad tillämpning för elever med dokumenterat stöd."*

Be läraren bekräfta att förutsättningarna i 2.4 kommer levereras innan brottning. Om läraren vill avvika (t.ex. "denna gång scaffoldas brottningen för alla") - det är override mot Princip 3 → M-ii utlöses.

### 2.6 Mönsterlarms-check (M-iii)

Räkna overrides från Steg 1-2 (1.7, 1.8, 2.2, 2.3, 2.4, 2.5). Två triggers:

1. **Antal:** 3+ overrides totalt i momentet
2. **Typ-mönster:** 3+ overrides i samma kategori (2-5) inom samma moment, även om totalantalet är lägre

**Vid antal-trigger, pausa med medium friktion:**
> "Mönsterlarm: du har överridit defaults 3+ gånger i detta moment. Antingen är ramverkets defaults fel formulerade för din kontext, eller du har glidit in i en vana. Skriv en kort motivering innan vi fortsätter - vad ser du i kontexten som gör att defaults inte passar?"

**Vid typ-mönster-trigger, pausa med medium friktion (anpassad prompt):**
> "Mönsterlarm: du har överridit defaults 3+ gånger i kategori [N: namn] inom detta moment. Antingen är ramverkets defaults systematiskt fel kalibrerade för din kontext (i den kategorin), eller du har glidit in i ett vanemönster. Skriv en kort motivering innan vi fortsätter."

Kräv skriftlig motivering. Spara i momentplan.md → Override-räknare → Mönsterlarm.

Om ingen trigger: gå vidare utan paus.

### 2.7 Sammanfattning och uppdatering av momentplan.md (M-iv)

Sammanfatta nivå 2-3-besluten. Uppdatera `momentplan.md` med:

```markdown
## Designval (Momentplaneringsramverket) - forts.

### Nivå 2 - Bedömningsmål
- **"Lyckad brottning" innebär:** [...]
- **Default:** [...]
- **Valt:** [...]
- **Override:** [...]

### Nivå 3 - Förutsättningar
- **Innehåll:** [...]
- **Begrepp:** [...]
- **Verifikationsregel:**
  - Andel/spridning: [bedömning]
  - Konsekvens av lucka: [bedömning]
  - Frågetypens tolerans: [bedömning]
- **Princip 3 bekräftad:** [Ja | Override - motivering: "..."]

## Lärandemål (E/C/A-progression)
[3-5 mål]
```

Uppdatera även Override-räknare.

*Behåller "Grundinformation"-sektionen så Steg 3-7 inte bryts. Designval läggs till som ny sektion.*

---

## Steg 3: Rollsekvens (nivå 4) och brottningsform (nivå 5)

Detta steg fortsätter designdialogen genom Momentplaneringsramverkets nivå 4 (sekvenslogik - 9 roller) och nivå 5 (brottningsform - diskursmål + formvalsprinciper). Här komponeras momentet av **roller**, inte av en generell pedagogisk ansats. M-i, M-ii, M-iii och M-iv aktiveras. Se @pedagogik-ramverk.md.

Läs in metodreferensen (metodbibliotek organiserat efter funktion - försörjer rollernas konkreta aktiviteter):
@references/pedagogiska-metoder.md

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

---

## Steg 4: Lektionssekvens - rollerna mappas på lektioner

Här mappas rollsekvensen från Steg 3.1 på det faktiska antalet lektioner. En roll kan spänna över flera lektioner; en lektion kan bära en eller flera roller (eller en del av en roll). Det är **rollerna**, inte en generisk progression, som driver ordningen.

Läs in lektionsplaneringsreferensen:
@references/lektionsplanering.md

1. **Föreslå en lektion-för-lektion-mappning** av rollsekvensen. För varje lektion:
   - Nummer och arbetstitel
   - **Vilken/vilka roller** lektionen realiserar (från 3.1)
   - **Rollens exit** - vad eleven exit:ar med i just denna lektion
   - **Primär form/metod** - för en Brottning-lektion: diskursmålet + formen från 3.2. För övriga roller: lämplig metod från `pedagogiska-metoder.md`
   - Vilka lärandemål den adresserar
   - **Exit ticket-fråga** (H2) - en specifik fråga som mäter rollens exit, inte bara "vad lärde du dig"

2. **Gör progressionen explicit i rolltermer.** Förklara varför lektionerna kommer i denna ordning utifrån rollsekvensens logik (typiskt Begreppsbygge/Perspektivbygge → Brottning → Syntes) och de hårda ordningsreglerna (Frågeförankring först, Brottning före Syntes, Metareflektion sist). Visa hur det analytiska kravet stiger mot Brottning och hur Syntes integrerar.

3. **Identifiera:**
   - Var retrieval/spaced practice återkopplar till tidigare lektioner (särskilt Återbesök-rollen)
   - **Hur varje lektions exit ticket-data informerar nästa lektions retrieval-öppning** (H2) - och särskilt: verifierar exit ticket-data inför Brottning-lektionen att förutsättningarna (2.4) sitter?
   - Var den mest kognitivt krävande lektionen ligger (ofta Brottning) - är placeringen rätt, och ligger förutsättningarna före?
   - Var det finns naturliga stoppunkter om läraren behöver anpassa

4. **Presentera mappningen som en numrerad lista** (lektion → roll(er) → exit → form) och fråga läraren om de vill ändra ordning, slå ihop/dela roller över lektioner, lägga till eller ta bort.

**Sammanfatta** den godkända lektionssekvensen och uppdatera momentplanen med en lektionsöversikt där **roll** är en egen kolumn:

```markdown
## Lektionssekvens (rollmappning)

| Lektion | Roll(er) | Eleven exit:ar med | Form/metod | Lärandemål |
|---|---|---|---|---|
| 1 | Frågeförankring (+ ...) | [...] | [...] | [...] |
| ... | | | | |

**Röd tråd (rolltermer):** [hur rollsekvensen bär momentet från fråga till syntes]
```

---

## Steg 5: Detaljerade lektionsplaner (Word-dokument)

Las in docx-skillen:
@.claude/skills/docx/SKILL.md

Sakerstall att `docx`-paketet ar installerat: `npm install -g docx`

Läs in lektionsplaneringsreferensen (rollbaserad mall + ramprinciper):
@references/lektionsplanering.md

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


Presentera lektionsplanen och fraga: "Vill du justera nagot i denna lektionsplan, eller ska jag ga vidare till nasta?"

**Generera som Word-dokument (.docx):**
Skapa varje godkand lektionsplan som ett professionellt Word-dokument med `docx-js`. Anvand:
- A4-format (11906 x 16838 DXA) med 1"-marginaler
- Rubrik: "Lektion N: [Titel]" som Heading 1
- Underrubriker (Larandemal, Forberedelse, Tidsplanering, etc.) som Heading 2
- Tidsplaneringen som en formaterad tabell med kolumnerna: Tid, Fas, Aktivitet, Beskrivning
- Bullet-listor med `LevelFormat.BULLET` (aldrig unicode-bullets)
- Sidfot med kursnamn och momentets titel
- Teckensnitt: Arial, 12pt brodtext

Skriv ett Node.js-script som genererar .docx-filen och kor det.
Validera filen med `python resources/office-scripts/validate.py`.

**Spara i bada format:**
- **Markdown:** `Undervisningsmaterial/[Amne]/[Tema]/lektion-[N].md` (i vaultet)
- **Word:** `/home/anders/undervisningsmaterial/[Amne]/[Tema]/lektion-[N].docx`

Markdown-versionen ska innehalla samma innehall som Word-dokumentet men formaterat som ren markdown (rubriker, tabeller, listor).

---

## Steg 5a: Elevuppgifter (separata Word-dokument)

Eleverna behover konkret material att arbeta med under lektionen - inte bara instruktioner i lararens lektionsplan. Efter att varje lektionsplan godkants, generera separata elevuppgifter for lektionens **rollkärna** (det guidade och sjalvstandiga elevarbetet som realiserar rollens exit).

### Vad ska genereras

Ga igenom den godkanda lektionsplanen och identifiera vilka elevmaterial som behovs. Typiska exempel:

- **Arbetsblad/uppgiftsblad** - strukturerade fragor, analysuppgifter, jamforelseovningar med tydliga instruktioner och utrymme for elevsvar
- **Kallmaterial** - sammanstallda kalltexter, utdrag, citat, bilder eller data som eleverna ska arbeta med. Inkludera kallhanvisningar. Om NotebookLM ar aktivt, anvand kallor darifraan
- **Analysuppgifter** - konkreta uppgifter med stegvisa instruktioner, fragestallningar som stiger i komplexitet (E-C-A-progression)

Ibland racker ett dokument per lektion, ibland behovs flera (t.ex. ett kallkompendium + ett arbetsblad). Anpassa efter lektionens innehall.

### Innehall och struktur

Varje elevuppgift ska:
- Ha en tydlig rubrik som kopplar till lektionen ("Lektion N: [Uppgiftstitel]")
- Borja med en kort kontextsattning - vad ska eleven gora och varfor
- Ha numrerade instruktioner/fragor
- **Inkludera differentieringsstod direkt i dokumentet** - t.ex. stodrutor ("Tips: ...") for elever som behover hjalp, och fordjupningsfragor markerade med stjarna for elever som vill utmanas
- Inkludera eventuellt kallmaterial direkt i dokumentet, eller hanvisa till ett separat kalldokument om det ar omfattande

### Kvalitetskontroll

- Matchar uppgiften lektionens rollkärna (det guidade/sjalvstandiga elevarbetet)?
- Ar instruktionerna tillrackligt tydliga for att eleven ska kunna borja arbeta utan ytterligare forklaring?
- Finns bade stod (mot E) och utmaning (mot A) inbyggt?
- Ar sprakniavan anpassad for gymnasieelever (inte lararsprak)?

### Generera som Word-dokument (.docx)

Anvand samma docx-metod som lektionsplanerna. Format:
- A4-format med 1"-marginaler
- Rubrik som Heading 1, underrubriker som Heading 2
- Numrerade listor for fragor/instruktioner
- Tabeller vid behov (t.ex. jamforelseuppgifter, kallsammanstallningar)
- Teckensnitt: Arial, 12pt brodtext
- Sidfot med kursnamn och lektionstitel

**Spara i bada format:**
- **Markdown:** `Undervisningsmaterial/[Amne]/[Tema]/elevuppgift-lektion-[N].md` (i vaultet)
- **Word:** `/home/anders/undervisningsmaterial/[Amne]/[Tema]/elevuppgift-lektion-[N].docx`

(Samma monster for kallmaterial: `kallmaterial-lektion-[N].md` / `.docx`)

Presentera en kort beskrivning av de genererade elevuppgifterna och fraga: "Vill du justera elevuppgifterna, eller ska jag ga vidare?"

---

## Steg 5b: Fragor till frageappen (Survey Platform)

Exportera fragor till lararens frageapp for klassrumsquiz. Las in den fullstandiga guiden:
@references/frageappen.md

---

## Steg 6: Presentationer (reveal.js HTML via slides-skillen)

Generera presentationer for lektioner med instruktions-/presentationsmoment. Presentationerna skapas som self-contained reveal.js HTML-filer med hjalp av slides-skillen - detta ger visuellt tilltalande, interaktiva presentationer som fungerar direkt i webblasaren.

Las in slides-skillen:
@.claude/skills/slides/SKILL.md

### Innehallshamtning fran NotebookLM

Om en notebook ar aktiv (steg 1), hamta relevant innehall innan varje presentation genereras. Anpassa fragorna efter lektionens tema:
```bash
notebooklm ask --json "Ge mig fakta, nyckelbegrepp och konkreta exempel om [lektionens specifika tema]. Inkludera kallhanvisningar."
```
```bash
notebooklm ask --json "Finns det primorkallor, citat eller historiska dokument om [temat] som kan anvandas i en presentation?"
```
Anvand svaren som grund for presentationens innehall - fakta, citat, kallhanvisningar och diskussionsfragor. Inkludera NotebookLM:s kallhanvisningar pa relevanta slides.

Om ingen notebook ar aktiv, generera presentationen baserat pa lektionsplanen och Claudes inbyggda kunskap. Markera osakra pastaenden med [VERIFIERA].

### Genereringsprocess

Generera presentationer for varje lektion som har ett instruktions-/presentationsmoment. Generera **en presentation i taget**.

For varje presentation:

1. **Samla innehall** fran lektionsplanen (steg 5) och NotebookLM-svaren. Identifiera:
   - Nyckelbegrepp och fakta for innehallsslides
   - Diskussionsfragor for diskussionsslides
   - Kallmaterial for kallanalysslides
   - Jamforelser, tidslinjer eller statistik som passar specialiserade slide-typer

2. **Generera presentationen** i designsystemet Arkiv (se slides-skillen). Folj Arkivs principer:
   - Anvand Arkivs designtokens utan undantag - papper `#F4EDE1`, Cormorant Garamond i rubriker, bordeaux som signaturfarg
   - Rubriker bar mening: fragor som titlar, ett kursivt nyckelord per rubrik (`<em>ord</em>`)
   - Max 3 nyckelpunkter per slide
   - Diskussionspaus var 3-4:e slide (`discuss` eller `question`)
   - Talarnoter pa varje slide med lararhandledning och tidsuppskattningar
   - Valj slide-typ efter innehall - Arkiv har 11 typer: `cover`, `section`, `question`, `content`, `twocol`, `timeline`, `quote`, `callout` (fakta/tips/varning/kalla), `table`, `discuss`, `close`
   - Inga emojis - bara typografiska tecken (`▸ ● ▪ § №`)

3. **Kvalitetskontroll** - kor slides-skillens checklista innan du presenterar for lararen.

4. **Presentera for lararen** och fraga om feedback innan du gar vidare till nasta presentation.

Spara till `Undervisningsmaterial/[Amne]/[Tema]/presentation-lektion-[N].html`.

---

## Steg 7: Momentoversikt for elever (HTML)

**OBS:** Om fragor exporterades till frageappen i steg 5b, inkludera delningskoderna i momentoversikten sa eleverna enkelt kan naa sina quiz.

Las in HTML-momentoversikt-skillen:
@.claude/skills/html-momentoversikt/SKILL.md

Momentoversikten ar en fristaende HTML-sida som ger eleverna en samlad overblick av hela momentet - datum, innehall, forberedelser och mal. Sidan kan publiceras via Google Sites eller liknande.

### 7a: Samla kompletterande information

Du har redan all pedagogisk data fran steg 1-4. Fraga lararen om:

1. **Datum for varje lektion** - presentera lektionslistan och be lararen ange datum (t.ex. "Lektion 1: ?, Lektion 2: ?, ..."). Acceptera valfritt datumformat.
2. **Forberedelser** - "Finns det nagot eleverna ska forbereda eller ha med sig infor nagon specifik lektion? (t.ex. lasa en text, ta med dator, repetera begrepp)"
3. **Lararens namn** - "Vill du att ditt namn ska visas pa sidan?" (valfritt)
4. **Ovrigt meddelande** - "Finns det nagot extra du vill kommunicera till eleverna pa sidan?" (valfritt)

### 7b: Generera HTML

Baserat pa data fran steg 1-4 och kompletteringarna ovan:

1. Valj en fargpalett och typografi som matchar amnet (se skillen). Presentera valet kort for lararen.
2. Omformulera larandemalen till **elevanligt sprak** - inga kunskapskravsformuleringar, utan konkreta beskrivningar av vad eleven ska kunna.
3. Generera en **self-contained HTML-fil** enligt skillens specifikation:
   - All CSS inline i `<style>`-block
   - Semantisk HTML med korrekt `lang="sv"`
   - Responsiv design (mobil, tablet, desktop)
   - Google Fonts via `<link>` (enda tilliatna externa resursen)
   - Lektionskort med nummer, titel, datum, innehall och ev. forberedelser
   - Header med kursnamn, momenttitel och tidsperiod
   - Larandemal i elevanlig formulering
4. Presentera resultatet for lararen och fraga om justeringar.

Spara till `Undervisningsmaterial/[Amne]/[Tema]/momentoversikt.html`.

---

## Avslutning

Nar alla steg ar klara:

1. Presentera en **oversikt** av allt genererat material med fillista:

   **I vaultet** (`Undervisningsmaterial/[Amne]/[Tema]/`):
   - `momentplan.md` - oversiktsplanering
   - `lektion-N.md` - detaljerade lektionsplaner (Markdown)
   - `elevuppgift-lektion-N.md` - elevuppgifter, arbetsblad och kallmaterial (Markdown)
   - `presentation-lektion-N.html` - klassrumspresentationer (reveal.js HTML)
   - `momentoversikt.html` - momentoversikt for elever (HTML)

   **Utanfor vaultet** (`/home/anders/undervisningsmaterial/[Amne]/[Tema]/`):
   - `lektion-N.docx` - detaljerade lektionsplaner (Word)
   - `elevuppgift-lektion-N.docx` - elevuppgifter, arbetsblad och kallmaterial (Word)
2. Fraga om lararen vill justera nagot.
3. **Kunskapsbasintegration (H4):** Foresla att lararen skriver en reflektion efter momentet med hjalp av mallen i `Mallar/Lektionsreflektion.md` (om den finns). Reflektionen kan sedan anvandas for att forbattra framtida moment.
4. Namnt kort vad som kan byggas vidare i framtiden: flashcards, elevmaterial, formativa bedomningsuppgifter.
5. Tipsa om att `momentoversikt.html` kan publiceras via Google Sites: skapa en ny sida, valj "Badda in" > "Embed code" och klistra in HTML-koden, eller ladda upp filen och lanka till den.

6. **Uppdatera kursminnet:** Analysera hela konversationen och identifiera justeringar lararen gjorde under processen. Fokusera pa:
   - Forslag som lararen andrade (pedagogisk ansats, tidsfordelning, aktiviteter)
   - Saker lararen lade till eller tog bort
   - Explicit feedback ("jag vill alltid ha...", "det har fungerar inte for den har gruppen")
   - Monster i differentieringen

   Generalisera lärdomarna - spara inte detaljer specifika for just detta moment, utan det som troligen galler for framtida moment i samma kurs. Skriv/uppdatera minnesfilen i `.claude/planera-moment/minne/[kursnamn-kebab-case].md` enligt formatet i sektionen "Kursminne". Skapa katalogen om den inte finns.

   Presentera kort vad som sparades: "Jag har uppdaterat kursminnet for [kursnamn] med foljande lardomar: [kort lista]. Nasta gang du planerar ett moment i denna kurs tar jag hansyn till detta fran start."

Avsluta med: "Ditt moment ar klart! Markdown-filerna finns i vaultet under `Undervisningsmaterial/[Amne]/[Tema]/` och Word-dokumenten finns i `/home/anders/undervisningsmaterial/[Amne]/[Tema]/`. Presentationerna ar HTML-filer (oppna i webblasaren och tryck S for talarnoter) och momentoversikten ar en HTML-sida som du kan dela med eleverna via Google Sites - redo att anvanda direkt. Lycka till med undervisningen!"

---

## Tillval: Enskild lektion (M2)

Om `$ARGUMENTS` innehaller "enskild-lektion" eller om lararen specifikt ber om att planera en enstaka lektion:
1. Hoppa over steg 4, 6 och 7
2. Acceptera en befintlig `momentplan.md` som input
3. Fokusera pa steg 5 (detaljerad lektionsplan) for en enda lektion
4. Fraga vilken lektion i momentet det galler (eller om det ar fristaende)

---

## State Dependencies

| Steg | Input fran | Output till |
|------|-----------|-------------|
| 1 | Anvandare + amnesplaner.md + notebook-config.json + **kursminne** | momentplan.md |
| 2 | Steg 1 + gy11-struktur.md | momentplan.md (uppdaterad) |
| 3 | Steg 1-2 + pedagogik-ramverk.md (nivå 4-5) + pedagogiska-metoder.md + vault-sok + **NotebookLM** | momentplan.md (rollsekvens + brottningsform) |
| 4 | Steg 1-3 (rollsekvens) + lektionsplanering.md | momentplan.md (lektionssekvens/rollmappning) |
| 5 | Steg 1-4 + lektionsplanering.md + docx SKILL.md + **NotebookLM** | lektion-N.md (vault) + lektion-N.docx (/home/anders/undervisningsmaterial/) |
| 5a | Steg 5 (godkand lektionsplan) + docx SKILL.md | elevuppgift-lektion-N.md + .docx, kallmaterial-lektion-N.md + .docx |
| 5b | Steg 1-5 + **MCP survey-platform** | fragor i databasen + momentplan.md (uppdaterad) |
| 6 | Steg 1-4 + slides SKILL.md + **NotebookLM** (innehall) | presentation-lektion-N.html |
| 7 | Steg 1-4 + html-momentoversikt SKILL.md + larar-input + ev. delningskoder | momentoversikt.html |

## Completion Checklist

- [ ] momentplan.md skapad med alla steg dokumenterade
- [ ] Rollsekvens (nivå 4) + brottningsform (nivå 5) dokumenterade i momentplan.md
- [ ] Varje lektion realiserar sin tilldelade roll; exit ticket mäter rollens exit
- [ ] Alla lektionsplaner genererade som .md (vault) och .docx (/home/anders/undervisningsmaterial/)
- [ ] Elevuppgifter genererade som .md (vault) och .docx (/home/anders/undervisningsmaterial/) for varje lektion
- [ ] Fragor genererade och exporterade till frageappen (eller sparade som CSV om MCP ej tillgangligt)
- [ ] Presentationer genererade som reveal.js HTML for lektioner med instruktionsmoment
- [ ] Momentoversikt genererad som .html (med delningskoder om fragor exporterades)
- [ ] .md-filer sparade i vaultet (`Undervisningsmaterial/[Amne]/[Tema]/`), .docx-filer i `/home/anders/undervisningsmaterial/[Amne]/[Tema]/`
- [ ] AI-svaghetscheck genomford pa alla lektionsplaner
- [ ] Exit ticket-slinga verifierad (varje exit ticket mäter rollens exit och informerar nästa retrieval-öppning)
- [ ] Kursminne uppdaterat med lardomar fran detta moment
