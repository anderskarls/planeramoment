---
name: planera-lektion
description: Skapa en enskild lektionsplanering. Användaren beskriver lektionen fritt, och du ställer följdfrågor för att fylla luckor. Rollbaserad - lektionen realiserar en roll ur Momentplaneringsramverket.
argument-hint: "[beskriv lektionen, t.ex. 'introduktion till politiska ideologier i Sh Nivå 1b']"
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - AskUserQuestion
  - Bash(./resources/local-brain-search/run_search.sh:*)
---

# Skapa enskild lektionsplanering

Guida användaren genom att skapa en enskild lektionsplanering. Används när man vill skapa en lektion utan att planera ett helt moment.

Detta kommando är den lätta, fristående vägen. Vill användaren planera ett **helt moment** (5-10 lektioner med övergripande momentplan, ramverksdriven designdialog, .docx/presentationer) - hänvisa till skillen `planera-moment`.

## Steg 1: Läs format och vault-kontext

Läs den rollbaserade formatreferensen och kurslistan:
- `${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/references/lektionsformat.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/kurser.json` (enda källan för kurser, system och ämnesmappar)

Sök och läs relevant kontext i vaultet:

1. Använd Glob för att hitta reflektioner i `raw/reflections/` - läs de senaste och mest relevanta
2. Sök efter befintliga planeringar i `output/lessons/[Ämne]/`
3. Sök i `raw/personal-notes/` efter relevanta planer eller idéer
4. **Wiki-uppslag:** läs `index.md` (vaultets rot) och sök kunskapsbasen på lektionens tema + roll:
   ```bash
   ./resources/local-brain-search/run_search.sh "[tema] [roll/metod]" --limit 5 --json
   ```
   Läs de 2-3 mest relevanta wiki-sidorna. Wikifynd matar lärarinstruktioner, differentiering och exit ticket-kalibrering - citera med `[[länkar]]` i lektionsplanen. Hittas inget: gå vidare utan kommentar.

Sammanfatta kort om du hittade något relevant.

## Steg 2: Tolka beskrivning och ställ följdfrågor

Tolka vad användaren angett och identifiera vad som saknas.

Obligatorisk information:
- **Kurs** - en av kurserna i `kurser.json`
- **Tema** - vad lektionen handlar om
- **Roll** - vilken roll lektionen spelar (se nedan)
- **Lektionslängd** - default 60 minuter

**Roll (Momentplaneringsramverkets nivå 4):** en lektion realiserar en roll, definierad av vad eleven exit:ar med. Föreslå en default utifrån beskrivningen och låt användaren bekräfta:

| Roll | Eleven exit:ar med |
|------|--------------------|
| Frågeförankring | Förståelse av en fråga värd att brottas med |
| Provokation | En produktiv kognitiv dissonans |
| Begreppsbygge | Begreppslig precision |
| Perspektivbygge | En perspektivinventering, utan egen position |
| Brottning | En försvarad/prövad position (kräver diskursmål + form) |
| Syntes | En integrerad helhetsförståelse |
| Metareflektion | Insikt om sitt eget tänkande |
| Applikation | Förmåga att tillämpa på ett nytt fall |
| Återbesök | Befäst, spaced retrieval av tidigare kärna |

Är rollen **Brottning**, fråga också om diskursmål (Övertyga / Syntes / Utforska / Klargöra / Pröva) och gruppstorlek - formen härleds därifrån (se lektionsformat.md).

Fråga alltid om **detaljnivå**:
- **Detaljerad** - fullständiga lärarinstruktioner, lektionsförlopp, differentiering, bilagor
- **Kortfattad** - grundstruktur som läraren fyller i själv

Samla alla frågor i ett AskUserQuestion-anrop.

## Steg 3: Skapa lektionsplanering

Bestäm rätt ämnesmapp via kursens `amnesmapp`-fält i `kurser.json`: `output/lessons/[amnesmapp]/`

Skapa filen med ett beskrivande namn: `[Lektionsnamn].md`. Tillhör lektionen ett befintligt moment, lägg den i momentets temamapp och länka till momentplanen och övriga lektioner.

Följ formatet i `${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/references/lektionsformat.md` - detaljerad eller kortfattad variant baserat på användarens val. Lektionsförloppet ska formas av rollen, inte av en fast fassekvens.

## Steg 4: Sammanfatta

Avsluta med:
- Vilken fil som skapades (med sökväg)
- Lektionens roll och vad eleven exit:ar med
- Förslag på kopplingar (reflektioner, relaterade lektioner)

## Viktiga principer

- Skriv alltid på **svenska**
- Bygg vidare på vault-kontexten - referera till reflektioner och tidigare erfarenheter
- **Rollbaserad ram:** öppna med retrieval (spaced practice) → rollkärna (formas av rollen) → avsluta med exit ticket som mäter rollens exit. Ingen fast fassekvens
- Sikta på minst 60% elevaktiv tid i detaljerade planeringar
- Inkludera differentiering (stöd mot E, utmaning mot A) i detaljerade planeringar
- Inkludera bilagor (sorteringskort, tabeller etc.) direkt i lektionsfilen för detaljerade planeringar
- Anpassa språk och nivå efter kursen
- Datumet i frontmatter ska vara dagens datum
