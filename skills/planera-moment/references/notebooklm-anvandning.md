# NotebookLM - användning (CLI)

NotebookLM är den primära källan för ämnesinnehåll. Innehåll därifrån är källgrundat med inbyggda referenshänvisningar - det minskar behovet av `[VERIFIERA]`-taggar avsevärt.

Men NotebookLM är en **extern tjänst med en inloggning som dör tyst**. Därför gäller: kontrollera en gång, fatta beslutet en gång, och låt beslutet följa med genom hela momentet. Kontrollen ligger i steg 1.4 och beskrivs nedan.

---

## Auth-kontrollen (steg 1.4) - gör den EN gång per session

### Så här kontrollerar du INTE

Dessa tre ger **falska positiva** - de kan rapportera att allt är bra medan CLI:n i själva verket är utloggad:

- `notebooklm doctor`
- `notebooklm auth check`
- MCP-verktyget `refresh_auth`

Och den viktigaste fällan: **CLI:n returnerar exit-kod 0 även när auth är död.** Verifierat 2026-08-18:

```bash
$ notebooklm list --json
{"error": true, "code": "UNEXPECTED_ERROR",
 "message": "Unexpected error: Authentication expired or invalid. ...
             Run 'notebooklm login' to re-authenticate."}
$ echo $?
0
```

Lita därför **aldrig** på att kommandot "gick igenom". Ett tomt eller misslyckat NotebookLM-svar som tolkas som ett giltigt svar är värre än inget svar alls - då förs auth-felet in i lektionsmaterialet som "notebooken innehöll inget om detta".

### Så här kontrollerar du

Kör ett skarpt kommando och **läs JSON-svarets `error`-fält**:

```bash
notebooklm list --json
```

- Innehåller svaret `"error": true` → NotebookLM är **DÖD**. Gå till Fallback-beslutet nedan.
- Får du en lista med notebooks → NotebookLM är **LEVANDE**. Aktivera kursens notebook:
  ```bash
  notebooklm use [NOTEBOOK_ID]
  ```

Samma regel gäller varje senare anrop: **läs alltid `error`-fältet i svaret**, aldrig exit-koden.

---

## Vilken notebook? Kursdefault och momentnotebook

`notebook_id` i `kurser.json` är kursens **default** - en bred källsamling som gäller hela kursen. Ett enskilt moment har ofta egna källor, och läraren bygger då en egen notebook för momentet. Skillen stödjer båda:

- **Kursens default** används när inget annat pekas ut.
- **En momentnotebook** väljs i steg 1.4 ur `notebooklm list --json` och skrivs i momentplanen. Den gäller hela momentet.

`kurser.json` uppdateras **aldrig** från ett momentval - byter kursen sin breda notebook är det en egen, medveten ändring.

Titlar är inte unika (två notebooks kan heta "Historia 1a1"). Skilj dem åt på ID, antal källor och ändringsdatum:
```bash
notebooklm source list -n [NOTEBOOK_ID] --json
```

---

## Fallback-beslutet - fattas en gång, i steg 1.4

Tre lägen kan uppstå. Alla tre ska landa i ett dokumenterat beslut innan planeringen går vidare.

**Läge A - kursen saknar `notebook_id` i `kurser.json`.** Informera läraren och kör utan NotebookLM. Fråga inte - det finns inget att logga in på. (Gäller idag Sh 1a2, IR och Sh Nivå 1b.)

**Läge B - notebook_id finns, men auth är död.** Ställ frågan till läraren med AskUserQuestion, en gång:

> "NotebookLM-inloggningen har gått ut. Vill du logga in nu, eller ska jag planera utan NotebookLM?"
>
> - **Kör utan NotebookLM (rekommenderad)** - jag använder wikin och min egen kunskap, och taggar faktapåståenden med `[VERIFIERA]` så du kan kontrollera dem. Planeringen fortsätter direkt.
> - **Jag loggar in nu** - kör `! notebooklm login` här i chatten (en webbläsare öppnas, kan inte automatiseras). Säg till när det är klart, så kontrollerar jag om och fortsätter.

Defaulten är att fortsätta. Skälet: en död inloggning ska inte kosta läraren ett helt planeringspass, och `[VERIFIERA]`-taggarna gör bortfallet synligt och åtgärdbart i efterhand.

Om läraren loggar in: kör om kontrollen (`notebooklm list --json`) innan du går vidare. Rapportera aldrig att inloggningen lyckades utan att ha sett en faktisk notebook-lista.

**Läge C - auth dör mitt i körningen** (ett `ask`-svar innehåller `"error": true` i steg 3, 5, 5a, 5c eller 6). Tolka det ALDRIG som att notebooken saknade material. Säg till läraren att inloggningen dog, och ställ frågan från läge B en gång. Läraren väljer; beslutet skrivs om i momentplanen och gäller resten av momentet.

### Dokumentera beslutet i momentplan.md

Skriv in resultatet under `## Grundinformation` så att beslutet överlever ett sessionsavbrott och läses av Återupptagande-kontrollen:

```markdown
**NotebookLM:** AV - auth död 2026-08-18, läraren valde att fortsätta med [VERIFIERA]-taggning
```

Möjliga värden: `PÅ (notebook [ID])` · `AV - kursen saknar notebook_id` · `AV - auth död [datum], lärarens val`

**Fråga aldrig om igen** när beslutet står i momentplanen. Är NotebookLM markerad AV: hoppa tyst över alla notebook-uppslag i steg 3, 5, 5a och 6, och hoppa över steg 5c (videor kan inte genereras utan notebook).

---

## Att planera utan NotebookLM

Bortfallet ska vara synligt, inte dolt. Konkret:

- Faktapåståenden som annars hade varit källgrundade taggas `[VERIFIERA]` i lektionsplanen (lärarens sida, aldrig i elevmaterialet).
- Wikin bär fortfarande **lärarens** sida - didaktik, metoder, ämnessynteser. Den påverkas inte av att NotebookLM är nere. Se `references/wiki-anvandning.md`.
- Primärkällor och citat: föreslå dem, men markera dem som overifierade. Hitta aldrig på sidhänvisningar eller citat som ser källgrundade ut.
- Nämn bortfallet i Avslutningens materiallista, så läraren vet vad som behöver granskas innan materialet möter elever.

---

## Fråga notebooken

Fråga med `notebooklm ask` - använd `--json` för strukturerade svar med källhänvisningar:
```bash
notebooklm ask --json "fråga här"
```

Varje anrop utan `-c` (conversation ID) startar en ny konversation. För uppföljningsfrågor i samma kontext, använd `-c` med konversations-ID:t från föregående svar (finns i JSON-output som `conversation_id`):
```bash
notebooklm ask -c [CONVERSATION_ID] --json "uppföljningsfråga"
```

## Principer för NotebookLM-frågor

- Kontrollera `error`-fältet i varje svar innan du använder innehållet (läge C ovan)
- Ställ specifika, avgränsade frågor - inte "berätta allt om X"
- Använd `--json` för att få källhänvisningar som kan föras in i materialet
- Om svaret är otillräckligt, ställ uppföljningsfrågor eller bredda sökningen
- Presentera NotebookLM:s källhänvisningar för läraren så de kan verifiera

## Videogenerering

För elevriktade videoöversikter (momentöversikt + förförståelse-videor), se Steg 5c och `references/videooversikt-notebooklm.md`.
