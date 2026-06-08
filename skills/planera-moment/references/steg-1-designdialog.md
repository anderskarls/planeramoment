# Steg 1: Ämne, kurs, system och designdialog (Ramverkets nivå Root → 1a → 1b)

Detta steg driver dialogen genom Momentplaneringsramverkets översta nivåer. Mekanismerna M-i (default + alternativ), M-ii (override-prompt) och M-iv (spårdokumentation) aktiveras vid varje val. Se `pedagogik-ramverk.md`.

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
