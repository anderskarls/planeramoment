# Steg 2: Bedömningsmål, lärandemål och förutsättningar (Ramverkets nivå 2 → 3)

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
