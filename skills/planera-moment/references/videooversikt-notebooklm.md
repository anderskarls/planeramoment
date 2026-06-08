# Steg 5c: Videoöversikter för elever (NotebookLM)

Detta steg genererar **pedagogiska videor** via NotebookLM som eleverna kan använda för att lära sig - dels en samlad momentöversikt, dels förförståelse-videor inför de lektioner som har förberedelsematerial. Videorna är källgrundade i kursens notebook (samma källor som resten av momentet) och blir den konkreta leveransvehikeln för **Princip 3 - Förberedelseintegritet** (*förutsättningar levereras i förväg och det är elevens ansvar att ha tagit del av dem*).

Videorna laddas ner som `.mp4`-filer. Läraren lägger upp dem där eleverna når dem (Google Drive, Classroom, YouTube olistad) och länkar dem från momentöversikten (Steg 7). **Dela aldrig hela notebooken publikt** för att ge eleverna åtkomst - det exponerar allt källmaterial (läromedel, upphovsrättsskyddat material) för vem som helst med länken.

---

## Förutsättningar (gate innan steget körs)

1. **Aktiv notebook (från Steg 1).** Videor genereras ur notebookens källor. Saknas notebook-ID för kursen kan steget inte köras - informera läraren: "Det finns ingen NotebookLM-notebook kopplad till den här kursen, så jag kan inte generera videor. Vill du hoppa över videosteget?" och hoppa över resten.

2. **CLI:n måste vara inloggad.** Kontrollera:
   ```bash
   notebooklm doctor
   ```
   Om raden `Auth` visar `fail`/`not authenticated`: be läraren köra inloggningen själv (den öppnar en webbläsare och kan inte köras automatiskt):
   > "NotebookLM-CLI:n är inte inloggad. Kör `! notebooklm login` här i chatten - en webbläsare öppnas där du loggar in med ditt Google-konto. Säg till när det är klart, så fortsätter jag."

   Fortsätt inte förrän auth är `pass`. Aktivera rätt notebook:
   ```bash
   notebooklm use [NOTEBOOK_ID]
   ```

---

## Vad som ska genereras (M-i: default + läraren justerar)

### 1. Momentöversikt-video (alltid)

En video som täcker hela momentet - tänkt som introduktion i början och repetition inför prov. En per moment.

### 2. Förförståelse-videor (per lektion, villkorat)

En video per lektion **vars lektionsplan (Steg 5) flaggar elevriktat förberedelsematerial som levereras i förväg** - dvs. ett förförståelsepaket / Princip 3-leverans. Så hittar du dem:

- Gå igenom varje lektions `Förberedelse`-sektion (och momentplanens leveransplan under Nivå 3).
- Slå till en förförståelse-video för de lektioner där förberedelsen är **elevriktad och levereras innan lektionen** - kännetecken: formuleringar som *"förförståelsepaket"*, *"levereras i förväg"*, *"Princip 3"*, *"elevens ansvar att ha tittat på"*, *"dela ut några dagar innan"*.
- Räkna **inte** in ren lärarförberedelse ("förbered en populärkulturbild", "skriv ut domänkort") - bara material eleven själv ska ta del av i förväg.

> Exempel (Den mörka medeltiden): Lektion 1:s Förberedelse-sektion säger *"Förförståelsepaket (I1) levereras i förväg ... det är elevens ansvar att ha tittat på det"*. Den lektionen får en förförståelse-video. Videon ersätter/kompletterar tidslinjepaketet - eleverna tittar före L1.

**Presentera den föreslagna videolistan för läraren innan generering** (M-i):
```
Föreslagna videor:
  - Momentöversikt: [Tema]            (hela momentet, intro + repetition)
  - Förförståelse inför Lektion [N]: [Titel]   (förförståelsepaket levereras i förväg)
  - ...
```
Fråga: "Vill du lägga till eller ta bort någon video innan jag genererar? (Generering tar några minuter per video.)" Läs lärarens justering som signal till kursminnet (Avslutning).

---

## Genereringsparametrar

| Parameter | Default | Not |
|---|---|---|
| `--format` | `explainer` | Längre förklarande video. `brief` för kort recap. **`cinematic` uteslutet** (Veo 3, 30-40 min, kräver AI Ultra). |
| `--language` | `sv` | Svenska. Om CLI:n inte stöder `sv` för video, fall tillbaka på `en` och flagga `[VERIFIERA]` att språk blev rätt. |
| `--style` | ämnesanpassad | Historia: `heritage` eller `classic`. Samhällskunskap: `classic` eller `whiteboard`. Juridik: `classic`. Osäker: `auto`. |

### Fokusprompt (styr innehållet)

Fokusprompten är det positionella argumentet till `generate video`. Skriv den på svenska och scoppa den mot innehållet.

**Momentöversikt:**
> "Skapa en pedagogisk översiktsvideo för gymnasieelever om [tema]. Utgå från momentets brottningsfråga: '[frågan ordagrant]'. Täck de centrala innehållspunkterna [lista] så att eleverna får en helhetsbild de kan använda för att förbereda sig och repetera. Gymnasienivå, på svenska."

**Förförståelse (per lektion):**
> "Skapa en kort förberedelsevideo för gymnasieelever inför en lektion om [lektionens tema]. Efter videon ska eleven kunna [förförståelsepaketets/förutsättningarnas innehåll, t.ex. medeltidens grova tidsindelning tidig/hög/sen och vad periodisering betyder]. Detta är material eleven tittar på före lektionen. Gymnasienivå, på svenska."

---

## Genereringsflöde (parallellt, sedan hämta)

Starta alla videor utan att blockera (de genereras parallellt server-side), vänta sedan in och ladda ner var och en.

1. **Starta varje video** med `--no-wait` och `--json`, fånga ID ur svaret:
   ```bash
   notebooklm generate video "[fokusprompt]" --format explainer --style [stil] --language sv --no-wait --json
   ```
   Svaret ser ut så här: `{"task_id": "<UUID>", "status": "pending"}`. **`task_id` är samma UUID som artefaktens `id`** - använd det rakt av i `artifact wait`, `download` och `rename`. Spara det per startad video.

2. **Vänta in** varje video (blockerar tills klar). Tar några minuter - kör gärna som bakgrundskommando så du får besked när den är klar:
   ```bash
   notebooklm artifact wait [ID] --timeout 1800 --json
   ```

3. **Döp om artefakten** (annars får den notebookens namn som titel, vilket gör den svår att hitta i NotebookLM):
   ```bash
   notebooklm artifact rename [ID] "Momentöversikt - [Tema]"
   notebooklm artifact rename [ID] "Förförståelse inför Lektion [N] - [Titel]"
   ```

4. **Ladda ner** till `.mp4`:
   ```bash
   notebooklm download video -a [ID] "[output]/video/video-moment-oversikt.mp4" --json
   notebooklm download video -a [ID] "[output]/video/video-forforstaelse-lektion-[N].mp4" --json
   ```

**Enklare alternativ** (en i taget, långsammare): hoppa över `--no-wait` och kör `generate video "..." --wait --timeout 1800 --json`, ladda sedan ner direkt.

**Spara filerna** i samma katalog som lektionernas `.docx` (se Steg 5), i undermappen `video/`:
- `video/video-moment-oversikt.mp4`
- `video/video-forforstaelse-lektion-[N].mp4`

---

## Loggning i momentplan.md

Lägg till en sektion (artefakt-ID:n behövs för att kunna ladda ner/retry:a igen; elevlänken fyller läraren i efter uppladdning):

```markdown
## Videoöversikter (NotebookLM)
| Video | Typ | Artefakt-ID | Fil | Status | Elevlänk (klistras in) |
|---|---|---|---|---|---|
| Momentöversikt: [Tema] | Momentöversikt | [ID] | video/video-moment-oversikt.mp4 | klar | [Drive/Classroom-URL] |
| Lektion [N]: [Titel] | Förförståelse | [ID] | video/video-forforstaelse-lektion-[N].mp4 | klar | [URL] |
```

---

## Leverans till elever (matar Steg 7)

Skillen kan inte ladda upp filer åt läraren. Berätta därför för läraren:

> "Videorna är nedladdade som `.mp4`. Ladda upp dem där eleverna når dem - enklast Google Drive (dela 'alla med länken kan se') eller Google Classroom. Klistra in länken i momentplanens 'Elevlänk'-kolumn, så länkar jag dem från momentöversikten."

I **Steg 7 (momentöversikt)**:
- **Momentöversikt-videon** länkas högst upp (i headern/introduktionen) som "Se hela momentet i kort form".
- **Förförståelse-videorna** länkas i respektive lektions **Förberedelser**-fält, med ramning: *"Titta på denna video före lektionen (förberedelse)."*

Om läraren ännu inte laddat upp när Steg 7 körs: lämna en tydlig platshållare ("[videolänk läggs till när du laddat upp]") så att den är lätt att fylla i senare.

---

## Kvalitetskontroll

- **Förväntningsstyrning:** säg antalet videor och grov tidsuppskattning *innan* generering startar (explainer = några minuter styck).
- **Granska före delning:** be läraren titta igenom varje video innan den delas med elever - kontrollera saklighet, språk (svenska) och att tonen passar målgruppen. Videor är källgrundade (lågt `[VERIFIERA]`-behov) men ska ändå förhandsgranskas.
- **Förförståelse-matchning:** levererar förförståelse-videon faktiskt de förutsättningar lektionens Förberedelse-sektion pekar ut (inte ett bredare ämnessvep)?
- **Språkkontroll:** blev videon på svenska? Om CLI:n föll tillbaka på engelska - flagga för läraren.
- **Retry vid fel:** om en artefakt failar, `notebooklm artifact retry [ARTIFACT_ID]` och vänta in på nytt.
