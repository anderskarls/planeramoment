# Steg 1: Ämne, kurs, system och designdialog (Ramverkets nivå Root → 1a → 1b)

Detta steg driver dialogen genom Momentplaneringsramverkets översta nivåer. Mekanismerna M-i (default + alternativ), M-ii (override-prompt) och M-iv (spårdokumentation) aktiveras vid varje val. Se `pedagogik-ramverk.md`.

### 1.1 Ämne

Om `$ARGUMENTS` angavs, använd det som ämne. Annars fråga: "Vilket ämne vill du planera för? (samhällskunskap eller historia)"

**Hoppa över 1.1 och 1.2** om ämne *och* kurs redan är kända från $ARGUMENTS eller från tidigare dialog (t.ex. när läraren startat skillen via vald ingång). Gå direkt till 1.3 och bekräfta.

### 1.2 Kurs

Läs kurslistan från `kurser.json` (i skillens rot). Presentera kurserna grupperade per system (GY11 avvecklas successivt), filtrerade efter valt ämne, med poäng. Hårdkoda aldrig kurslistan - `kurser.json` är enda källan.

### 1.3 System-detektering och referensladdning

Den valda kursens post i `kurser.json` anger `system` (GY11/GY25). Ladda systemets referensfiler enligt `referensfiler`-mappningen i samma fil. Bekräfta för läraren.

Bekräfta: "Detta moment går under [GY11 / GY25] - jag använder [kunskapskrav-modellen / betygskriterier-modellen] och kommer formulera lärandemål med [systemets värdeord]."

### 1.4 NotebookLM-koppling

Slå upp kursens `notebook_id` i `kurser.json`.

**Saknas ID:** informera läraren om att momentet planeras utan NotebookLM (wiki + `[VERIFIERA]`-taggar). Fråga inget - det finns inget att logga in på.

**Finns ID:** kontrollera att inloggningen lever *innan* du aktiverar notebooken. Kör ett skarpt kommando och läs `error`-fältet i JSON-svaret:
```bash
notebooklm list --json
```
- `"error": true` → auth är död. Ställ fallback-frågan (läge B) enligt `references/notebooklm-anvandning.md`.
- Lista med notebooks → gå vidare till notebook-valet nedan.

> **Lita aldrig på `notebooklm doctor`, `auth check` eller exit-koden** - CLI:n returnerar exit 0 även när auth är död. Fullständig motivering och fallback-protokoll: `references/notebooklm-anvandning.md`.

**Notebook-val (M-i).** `notebook_id` i `kurser.json` är kursens **default** - en bred källsamling för hela kursen. Men källor är ofta momentspecifika, och läraren bygger gärna en egen notebook per moment. Använd listan du just hämtade: leta efter en notebook vars titel matchar momentets tema eller kurs.

Presentera valet med AskUserQuestion när det finns en trolig momentnotebook, med den som default:
- **[Titel] (`[ID]`)** - momentspecifik, [N] källor, senast ändrad [datum]
- **Kursens default: [Titel] (`[ID]`)** - bred kurssamling ur `kurser.json`
- **Ingen notebook** - planera med wiki + `[VERIFIERA]`-taggar

Hittar du ingen kandidat utöver kursens default: aktivera defaulten och nämn i förbifarten att en momentspecifik notebook kan pekas ut om läraren har en.

> **Titlar räcker inte för att skilja notebooks åt** - flera kan heta samma sak (t.ex. två "Historia 1a1"). Visa alltid ID och antal källor (`notebooklm source list -n [ID] --json`) så läraren väljer rätt. Vid tveksamhet: fråga, gissa inte.

Aktivera den valda och bekräfta för läraren:
```bash
notebooklm use [NOTEBOOK_ID]
```

**Dokumentera utfallet** i momentplanens `## Grundinformation` (`**NotebookLM:** PÅ (notebook [ID] - [titel])` / `AV - kursen saknar notebook_id` / `AV - auth död [datum], lärarens val`). Beslutet gäller hela momentet och ska inte ställas om i senare steg. Skriv aldrig tillbaka ett momentval till `kurser.json` - den filen bär kursens default, inte momentets.

### 1.5 Kursminne - försörjer M-i:s defaults

Läs `output/lessons/_kursminne/[kursminne-slug].md` om den finns (sluggen står i kursens post i `kurser.json`). **Detta minne försörjer M-i:s defaults nedströms.** När skillen i 1.7-1.8 (och senare 2.x) föreslår defaults ska de vägas mot minnet.

Presentera kort: "Tidigare moment i [kursnamn] visar mönster - t.ex. [1-2 saker som verkar relevanta för det här momentet]. Jag använder dem som **default men inte tvång** - säg till nu om något inte passar detta moment innan vi börjar, så slipper vi korrigera halvvägs in."

Tonregler för kursminnes-presentation:
- Säg "mönster" och "verkar" - undvik "vet" och "föredrar alltid"
- Lyft högst 2 saker. Hela listan finns i filen - överbelasta inte dialogen
- Inbjud aktivt till avfärdande: "säg till om något inte passar"

Om filen inte finns, säg ingenting.

### 1.5.5 Wiki-uppslag på temat

När ämne/tema är känt (från $ARGUMENTS eller 1.1): slå upp temat i wikin enligt protokollet i `references/wiki-anvandning.md`:

1. Läs `index.md` (vaultets rot) och identifiera relevanta sidor - särskilt en eventuell **ämnes-MOC** för temat (t.ex. en MOC byggd inför just detta moment), relevanta concepts och tidigare reflektioner.
2. Komplettera med semantisk sökning:
   ```bash
   ./resources/local-brain-search/run_search.sh "[temat] [kursen]" --limit 5 --json
   ```
3. Läs de 2-3 mest relevanta sidorna.

Presentera kort (samma ton som kursminnet): "Wikin har material om temat - t.ex. [[sida]] som [en rad om bidraget]. Jag använder det som underlag för förslagen framåt." Lyft högst 2-3 fynd. Hittas inget relevant: säg ingenting.

Fynden informerar nedströms: förslag på brottningsfråga (1.6), skärpningsfilter (1.6.5), Hess-default (1.7) och CI-urval (1.9). Sidor som faktiskt påverkar val dokumenteras i momentplanens `## Kunskapsunderlag (wiki)` (1.11).

### 1.5.7 Nivå 0 - Momenttyp

Innan roten: fastställ **momenttypen**. Inte varje moment drivs av en omtvistad fråga - att tvinga in en kontrovers där innehållet inte bär en är lika inautentiskt som att brotta över en sluten fråga. Se `pedagogik-ramverk.md`, nivå 0.

**Default-rekommendation (M-i):** Föreslå typ utifrån ämne/tema + ev. kursminne, presentera alla tre med en rad var, be om val:

| Momenttyp | Roten är | Signal |
|---|---|---|
| **Brottnings-moment** | En omtvistad fråga | Läraren kan formulera en "bör / är det rätt att"-fråga med två försvarbara sidor |
| **Färdighets-moment** | En förmåga att utveckla | Målet är att kunna göra något (värdera källor, läsa statistik, skriva analys) |
| **Översikts-moment** | Ett skeende/område att förstå i bredd | Målet är att förstå en epok/ett förlopp, ingen tvingande motkraft |

Momenttypen styr nedströms: vad roten är (1.6), om spänningstestet gäller (1.6.5), om Hess-gaten aktiveras (1.7), och vilka core-roller som krävs (steg 3.1). Bekräfta valet och spara det - det är första fältet i momentplanen (1.11).

**Blandtyp:** om momentet genuint är både-och, välj den typ vars rot driver flest lektioner och notera den andra som sekundär inriktning.

**Override-prompt (M-ii):** momenttyp är ett lärarval, inte en ramverksdefault med golv - ingen kategori-2-5-prompt behövs här. Men om läraren väljer brottnings-moment och sedan i 1.6 inte kan formulera en fråga som passerar spänningstestet, återvänd hit och pröva om en annan typ passar bättre.

### 1.6 Root: Den drivande frågan

Vad roten är beror på momenttypen (1.5.7):

- **Brottnings-moment:** "Vilken fråga ska eleverna brottas med under detta moment?" - en kontroversiell/öppen kärnfråga.
- **Färdighets-moment:** "Vilken förmåga ska momentet bygga?" - formulera som ett kunna-göra-mål (t.ex. "eleven ska kunna källkritiskt värdera en historisk primärkälla").
- **Översikts-moment:** "Vilken öppen fråga organiserar undersökningen?" - en bred undersökande fråga (t.ex. "hur och varför spreds reformationen genom Europa?").

Stöd läraren att formulera något som kan driva 5-10 lektioner. Om hjälp behövs:
- "Vad ska eleverna kunna säga, försvara, göra eller överväga efter momentet som de inte kan idag?"
- (Brottning:) "Finns det en aktuell händelse, ett dilemma eller en spänning som kan vara ingången?"

Spara frågan/målet ordagrant. Nedströms kallas detta **den drivande frågan** oavsett typ.

### 1.6.5 Skärpningsfilter - innan klassificering

Testa den drivande frågan/målet mot kriterierna nedan. Vilka som gäller beror på momenttypen (1.5.7).

**Gäller alla momenttyper:**

1. **Bärighetstest:** Kan frågan/målet driva *varje* lektion i momentet, eller bara introducera det? En momentintro-fråga blir tom från lektion 3 och framåt.

**Gäller endast brottnings-moment:**

2. **Spänningstest:** Har frågan en inbyggd spänning (X *vs* Y, kontrast, värdekonflikt) eller är den öppet undersökande utan motkraft? En brottningsfråga utan inbyggd spänning ger inte brottning - eleverna kan svara "lite av varje" och få rätt. *(Översikts-moment ska tvärtom vara öppet undersökande - för dem är avsaknad av motkraft rätt, inte fel.)*

3. **Default-genererings-test:** Kan skillen själv ge en konkret default-Hess-klassificering (1.7) med säkerhet? Om inte - frågan är för vag för att klassificeras.

**Om ett tillämpligt test fallerar:** Presentera 2-3 skärpningar enligt M-i (default + alternativ med pedagogisk motivering). Be läraren välja eller forma något eget. Acceptera *inte* den ursprungliga vaga frågan - det är skillens jobb att skydda momentet från luddigheten. Om en brottningsfråga upprepat fallerar spänningstestet: återvänd till 1.5.7 och pröva om momentet egentligen är ett översikts- eller färdighets-moment.

**Om tillämpliga tester passerar:** brottnings-moment → gå till 1.7. Färdighets-/översikts-moment → hoppa 1.7-1.8 (Hess-gate och frågetypologi gäller inte) och gå direkt till 1.9.

### 1.7 Nivå 1a - Hess-gate (endast brottnings-moment)

*Hoppa över detta steg och 1.8 för färdighets- och översikts-moment - gå till 1.9.*

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

Sammanfatta valen och be läraren bekräfta. Skapa `output/lessons/[Ämne]/[Tema]/momentplan.md`:

```markdown
# Momentplan: [Tema]

## Grundinformation
- **Ämne/Kurs:** [val]
- **System:** GY11 | GY25
- **Momenttyp:** [brottnings-moment | färdighets-moment | översikts-moment] (ev. sekundär inriktning: [...])
- **Centralt innehåll:** [valda punkter]
- **Antal lektioner:** [N] × [X] minuter
- **Tema/vinkel:** [ev.]

## Designval (Momentplaneringsramverket)

### Nivå 0 - Momenttyp
- **Vald typ:** [brottnings- | färdighets- | översikts-moment]
- **Motivering:** [varför denna typ passar temat]

### Root: Drivande fråga
> [frågan/målet ordagrant]

### Nivå 1a - Hess-gate *(endast brottnings-moment)*
- **Klassificering:** [sluten | tippande | öppen | *ej tillämpligt - ej brottnings-moment*]
- **Default:** [systemets rekommendation]
- **Valt:** [lärarens val]
- **Override:** [Nej | Ja - kategori X kontextläsning: "..."]

### Nivå 1b - Frågetypologi *(endast brottnings-moment)*
- **Primär typ:** [... | *ej tillämpligt*]
- **Sekundär typ:** [... eller "ingen"]
- **Default:** [...]
- **Valt:** [...]
- **Override:** [Nej | Ja - kategori X: "..."]

### Tvärgående trådar (valbart)
- **Intra-moment:** [bivinkel eller "ingen"]
- **Inter-moment:** [framtida koppling sparad i kursminne, eller "ingen"]

## Kunskapsunderlag (wiki)
- [[sida]] - [vad sidan bidrog med till vilket val]
- *(fylls på löpande genom steg 1-5; tom sektion om wikin inte gav något)*

## Override-räknare
- **Antal overrides hittills:** [N]
- **Mönsterlarm:** [Inte triggat | Triggat på princip X - motivering: "..."]
```
