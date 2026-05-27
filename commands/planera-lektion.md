---
name: planera-lektion
description: Skapa en enskild lektionsplanering. Användaren beskriver lektionen fritt, och du ställer följdfrågor för att fylla luckor.
argument-hint: "[beskriv lektionen, t.ex. 'introduktion till politiska ideologier i Sh1a1']"
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - AskUserQuestion
---

# Skapa enskild lektionsplanering

Guida användaren genom att skapa en enskild lektionsplanering. Används när man vill skapa en lektion utan att planera ett helt moment.

## Steg 1: Läs vault-kontext

Läs referensfilen för format:
- `${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/references/lektionsformat.md`

Sök och läs relevant kontext:

1. Använd Glob för att hitta reflektioner i `Reflektioner/` — läs de senaste
2. Sök efter befintliga planeringar i relevant ämnesmapp under `Lektionsplaneringar/`

Sammanfatta kort om du hittade något relevant.

## Steg 2: Tolka beskrivning och ställ följdfrågor

Tolka vad användaren angett och identifiera vad som saknas.

Obligatorisk information:
- **Kurs** — Sh1a1, Sh3, Internationella relationer, eller Hi1b
- **Tema** — vad lektionen handlar om
- **Lektionslängd** — default 60 minuter

Fråga alltid om **detaljnivå**:
- **Detaljerad** — fullständiga lärarinstruktioner, tidsplanering, differentiering, bilagor
- **Kortfattad** — grundstruktur som läraren fyller i själv

Samla alla frågor i ett AskUserQuestion-anrop.

## Steg 3: Skapa lektionsplanering

Bestäm rätt ämnesmapp:
- Sh1a1, Sh3, Internationella relationer → `Lektionsplaneringar/Samhällskunskap/`
- Hi1b → `Lektionsplaneringar/Historia/`

Skapa filen med ett beskrivande namn: `[Lektionsnamn].md`

Följ formatet i `${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/references/lektionsformat.md` — detaljerad eller kortfattad variant baserat på användarens val.

Om lektionen tillhör ett befintligt moment, länka till momentplanen och övriga lektioner.

## Steg 4: Sammanfatta

Avsluta med:
- Vilken fil som skapades (med sökväg)
- Kort om lektionens upplägg
- Förslag på kopplingar (reflektioner, relaterade lektioner)

## Viktiga principer

- Skriv alltid på **svenska**
- Bygg vidare på vault-kontexten
- Följ lektionsstrukturen (uppstart → instruktion → bearbetning → summering → koppling framåt)
- Sikta på minst 60% elevaktiv tid i detaljerade planeringar
- Inkludera differentiering i detaljerade planeringar
- Anpassa nivå efter kurs (Sh1a1 = mer scaffolding, Sh3 = högre krav)
- Datumet i frontmatter ska vara dagens datum
