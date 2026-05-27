---
name: planera-moment
description: Planera ett helt undervisningsmoment med övergripande momentplan och lektionsplaneringar. Användaren beskriver momentet fritt, och du ställer följdfrågor för att fylla luckor.
argument-hint: "[beskriv momentet fritt, t.ex. 'demokrati i Sh1a1, 5 lektioner']"
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - AskUserQuestion
---

# Planera undervisningsmoment

Guida användaren genom att planera ett komplett undervisningsmoment. Arbetsflödet är blandat: användaren beskriver fritt, du ställer följdfrågor för det som saknas.

## Steg 1: Läs vault-kontext

Innan något annat — läs befintligt material i vaultet för att bygga vidare på tidigare erfarenheter.

Läs referensfilerna för format:
- `${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/references/momentformat.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/references/lektionsformat.md`

Sök och läs relevant kontext:

1. Använd Glob för att hitta reflektioner i `Reflektioner/` — läs de senaste och mest relevanta
2. Sök efter befintliga planeringar i relevant ämnesmapp under `Lektionsplaneringar/`
3. Sök i `Tankar och planer/` efter relevanta idéer

Sammanfatta kort för användaren vad du hittade av relevans (t.ex. "Jag såg att du reflekterade över X i din senaste reflektion — jag tar med det.").

## Steg 2: Tolka användarens beskrivning

Användaren kan ge allt från en kort mening till en detaljerad beskrivning. Tolka vad som angetts och identifiera vad som saknas.

Obligatorisk information:
- **Kurs** — Sh1a1, Sh3, Internationella relationer, eller Hi1b
- **Tema/område** — vad momentet handlar om
- **Antal lektioner** — hur många lektioner momentet ska bestå av
- **Lektionslängd** — default 60 minuter om ej angivet

Valfri information som berikar planeringen:
- Specifika mål eller centralt innehåll
- Önskade metoder eller aktiviteter
- Bedömningsform
- Särskilda behov eller anpassningar

## Steg 3: Ställ följdfrågor

Använd AskUserQuestion för att samla in information som saknas. Samla flera frågor i ett anrop om möjligt — undvik att ställa en fråga i taget.

Fråga alltid om **detaljnivå**:
- **Detaljerad** — fullständiga lärarinstruktioner, tidsplanering, differentiering, bilagor
- **Kortfattad** — grundstruktur som läraren fyller i själv

Om användaren gett tillräcklig information i sin beskrivning, bekräfta bara och fråga om detaljnivå.

## Steg 4: Presentera momentskiss

Innan filer skapas — presentera en kort skiss av momentet:

1. Övergripande mål
2. Röd tråd genom momentet
3. Lektionsöversikt (en rad per lektion med fokus och huvudaktivitet)
4. Bedömningsstrategi

Presentera skissen i chatten och fråga: "Ser det här bra ut, eller vill du justera något?"

Vänta på bekräftelse innan du skapar filer.

## Steg 5: Skapa filer

Bestäm rätt ämnesmapp:
- Sh1a1, Sh3, Internationella relationer → `Lektionsplaneringar/Samhällskunskap/`
- Hi1b → `Lektionsplaneringar/Historia/`

Skapa filerna i denna ordning:

### 5a: Momentplan
Skapa `[Momentnamn] — momentplan.md` i rätt ämnesmapp.
Följ formatet i `${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/references/momentformat.md`.

### 5b: Lektionsplaneringar
Skapa `[Momentnamn] — Lektion [N].md` för varje lektion.
Följ formatet i `${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/references/lektionsformat.md`.
Välj detaljerad eller kortfattad variant baserat på användarens val.

### 5c: Wikilinks
Säkerställ att alla filer är korrekt länkade:
- Momentplan → varje lektion
- Varje lektion → momentplan
- Varje lektion → nästa lektion
- Kopplingar till relevanta reflektioner eller tankar

## Steg 6: Sammanfatta

Avsluta med en sammanfattning:

- Vilka filer som skapades (med sökvägar)
- Kort om momentets upplägg
- Tips på nästa steg (t.ex. "Kör momentet och skapa en reflektion efteråt!")

Använd detta format:
```
Klart! Jag skapade följande filer:
- 📋 [[Momentnamn — momentplan]] — övergripande plan
- 📝 [[Momentnamn — Lektion 1]] — [kort beskrivning]
- 📝 [[Momentnamn — Lektion 2]] — [kort beskrivning]
- ...
```

## Viktiga principer

- Skriv alltid på **svenska**
- Bygg vidare på vault-kontexten — referera till reflektioner och tidigare erfarenheter
- Var pedagogiskt genomtänkt — följ lektionsstrukturen (uppstart → instruktion → bearbetning → summering → koppling framåt)
- Sikta på minst 60% elevaktiv tid i detaljerade planeringar
- Inkludera differentiering (stöd mot E, utmaning mot A) i detaljerade planeringar
- Inkludera bilagor (sorteringskort, tabeller etc.) direkt i lektionsfilen för detaljerade planeringar
- Anpassa språk och nivå efter kursen (Sh1a1 kräver mer scaffolding än Sh3)
- Datumet i frontmatter ska vara dagens datum
