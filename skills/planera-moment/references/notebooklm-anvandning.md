# NotebookLM - användning (CLI)

NotebookLM är den primära källan för ämnesinnehåll. Innehåll därifrån är källgrundat med inbyggda referenshänvisningar - det minskar behovet av `[VERIFIERA]`-taggar avsevärt.

## Aktivera notebooken

När kursen är vald i steg 1, aktivera notebooken (ID slås upp i `notebook-config.json`):
```bash
notebooklm use [NOTEBOOK_ID]
```
Om kursen saknar notebook-ID: informera läraren och fråga om de vill fortsätta utan NotebookLM (då används Claudes inbyggda kunskap som fallback, med fler `[VERIFIERA]`-taggar).

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

- Ställ specifika, avgränsade frågor - inte "berätta allt om X"
- Använd `--json` för att få källhänvisningar som kan föras in i materialet
- Om svaret är otillräckligt, ställ uppföljningsfrågor eller bredda sökningen
- Presentera NotebookLM:s källhänvisningar för läraren så de kan verifiera

## Videogenerering

För elevriktade videoöversikter (momentöversikt + förförståelse-videor), se Steg 5c och `references/videooversikt-notebooklm.md`.
