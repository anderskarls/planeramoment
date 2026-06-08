# Steg 7: Momentöversikt för elever (HTML)

**OBS:** Om frågor exporterades till frågeappen i steg 5b, inkludera delningskoderna i momentöversikten så eleverna enkelt kan nå sina quiz.

**OBS (video):** Om videor genererades i steg 5c, länka dem i momentöversikten - momentöversikt-videon högst upp (intro/repetition) och varje förförståelse-video i respektive lektions Förberedelser-fält ("Titta på denna video före lektionen"). Hämta elevlänkarna från momentplanens "Videoöversikter"-tabell. Om en länk ännu saknas (läraren inte laddat upp .mp4:n), lämna en tydlig platshållare.

Läs in HTML-momentöversikt-skillen: `.claude/skills/html-momentoversikt/SKILL.md`

Momentöversikten är en fristående HTML-sida som ger eleverna en samlad överblick av hela momentet - datum, innehåll, förberedelser och mål. Sidan kan publiceras via Google Sites eller liknande.

### 7a: Samla kompletterande information

Du har redan all pedagogisk data från steg 1-4. Fråga läraren om:

1. **Datum för varje lektion** - presentera lektionslistan och be läraren ange datum (t.ex. "Lektion 1: ?, Lektion 2: ?, ..."). Acceptera valfritt datumformat.
2. **Förberedelser** - "Finns det något eleverna ska förbereda eller ha med sig inför någon specifik lektion? (t.ex. läsa en text, ta med dator, repetera begrepp)"
3. **Lärarens namn** - "Vill du att ditt namn ska visas på sidan?" (valfritt)
4. **Övrigt meddelande** - "Finns det något extra du vill kommunicera till eleverna på sidan?" (valfritt)

### 7b: Generera HTML

Baserat på data från steg 1-4 och kompletteringarna ovan:

1. Välj en färgpalett och typografi som matchar ämnet (se skillen). Presentera valet kort för läraren.
2. Omformulera lärandemålen till **elevnära språk** - inga kunskapskravsformuleringar, utan konkreta beskrivningar av vad eleven ska kunna.
3. Generera en **self-contained HTML-fil** enligt skillens specifikation:
   - All CSS inline i `<style>`-block
   - Semantisk HTML med korrekt `lang="sv"`
   - Responsiv design (mobil, tablet, desktop)
   - Google Fonts via `<link>` (enda tillåtna externa resursen)
   - Lektionskort med nummer, titel, datum, innehåll och ev. förberedelser
   - Header med kursnamn, momenttitel och tidsperiod
   - Lärandemål i elevnära formulering
4. Presentera resultatet för läraren och fråga om justeringar.

Spara till `Undervisningsmaterial/[Ämne]/[Tema]/momentoversikt.html`.
