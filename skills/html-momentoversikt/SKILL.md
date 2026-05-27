---
name: html-momentoversikt
description: >
  Genererar en visuellt tilltalande, fristående HTML-sida som ger elever
  en samlad överblick över ett undervisningsmoment — lektioner, mål,
  datum och förberedelser. Designad för att publiceras via Google Sites
  eller liknande plattform.
version: 0.1.0
---

# HTML-momentöversikt för elever

Denna skill genererar en **self-contained HTML-fil** som ger gymnasieelever en tydlig, visuellt tilltalande översikt av ett helt undervisningsmoment.

---

## 1. Design Thinking — pedagogisk kontext

### Målgrupp
Gymnasieelever (16–19 år). De är vana vid moderna, mobilanpassade gränssnitt och tappar snabbt intresset för tråkig eller rörig design. Sidan ska kännas som något de *vill* använda — inte bara ännu en PDF.

### Ton och känsla
- **Tydlig** — all information ska vara lättskummad, med tydlig hierarki
- **Modern** — ren typografi, avskalade färger, medvetna whitespace-val
- **Inbjudande** — inte steril eller "skolig", utan varm och motiverande
- **Professionell** — eleverna ska känna att momentet är genomtänkt och seriöst

### Designprinciper
1. **Innehållet först** — designen ska framhäva informationen, inte konkurrera med den
2. **Visuell hierarki** — ämne/tema > momentöversikt > individuella lektioner > detaljer
3. **Scanningsbar** — elever ska kunna hitta "vad händer nästa lektion?" på sekunder
4. **Progressionskänsla** — layouten ska visuellt förmedla att momentet rör sig framåt
5. **Minimalism med värme** — avskalat men inte kallt; använd färg och typografi medvetet

---

## 2. Struktur och innehåll

### Header-sektion
- Kursnamn och momentets titel (stort, tydligt)
- Kort beskrivning av momentet (2–3 meningar)
- Tidsperiod (startdatum – slutdatum)

### Lärandemål
- Momentets övergripande mål i kortform
- Formulerade så att elever förstår dem (inte kunskapskravsspråk)

### Lektionsöversikt
Varje lektion visas som ett visuellt kort/block med:
- **Lektionsnummer och titel**
- **Datum** (tydligt formaterat)
- **Innehåll** — kort beskrivning av vad lektionen handlar om (2–3 meningar)
- **Förberedelser** — vad eleven ska göra/ha med sig (om tillämpligt; visa bara om det finns förberedelser)
- **Fokus-mål** — vilket/vilka av momentets mål som adresseras (valfritt, kan utelämnas om läraren föredrar)

### Footer
- Lärarens namn (valfritt)
- Kursnamn
- Genererat datum

---

## 3. Estetiska riktlinjer

### Färgpalett
Välj **en** sammanhållen palett som matchar ämnet. Undvik generiska blå/grå-scheman.

| Ämne | Förslag |
|------|---------|
| Historia | Varma toner — terracotta, sand, mörkröd |
| Samhällskunskap | Moderna toner — teal, slate, vit |
| Juridik | Professionella toner — navy, guld, ljusgrå |

Paletterna ska ha:
- **En dominant bakgrundsfärg** (ljus — sidan ska vara lättläst)
- **En accentfärg** för rubriker och interaktiva element
- **En mörk textfärg** (aldrig pure black `#000` — använd `#1a1a2e` eller liknande)
- **En subtil sekundärfärg** för kort-bakgrunder, borders, och hover-effekter

### Typografi
Använd Google Fonts via `<link>`-taggar. Förslag:

| Användning | Exempel |
|------------|---------|
| Rubriker | Inter, Outfit, Plus Jakarta Sans, Sora |
| Brödtext | Inter, Source Sans 3, Nunito Sans |

Regler:
- Rubrik 1 (momenttitel): 2–2.5rem, bold
- Rubrik 2 (sektionsrubriker): 1.3–1.5rem, semibold
- Brödtext: 1rem (16px baseline), line-height 1.6
- Max radbredd: 70ch för löpande text
- Använd `font-display: swap` för att undvika FOIT

### Layout
- **CSS Grid eller Flexbox** — aldrig tabeller för layout
- **Responsiv**: fungerar på mobil (360px), tablet (768px) och desktop (1200px+)
- **Lektionskort**: visa som vertikala kort på mobil, grid (2–3 kolumner) på desktop
- **Generösa marginaler**: minst 1rem padding i containern, 1.5rem+ på desktop
- **Max-width**: 900–1000px för innehållscontainern, centrerad

### Visuella detaljer
- Subtila `box-shadow` på lektionskort (inte flat, inte overdone)
- Rundade hörn (`border-radius: 8–12px`) på kort
- Mjuka färgövergångar om bakgrundsfärger används
- Lektionsnummer som visuellt element (t.ex. stor siffra eller badge)
- Datum tydligt markerat (t.ex. liten badge eller etikett)
- Ikonliknande visuella markörer för förberedelser (t.ex. en bok-emoji eller liknande) — håll det minimalt

---

## 4. Tekniska krav

### Self-contained HTML
- **En enda `.html`-fil** — all CSS och JS ska vara inline (`<style>` och `<script>`)
- **Inga externa beroenden** förutom Google Fonts (laddas via `<link>` i `<head>`)
- Filen ska fungera om man öppnar den direkt i en webbläsare
- Filen ska fungera inbäddad via Google Sites "Embed code"-funktion

### HTML-standard
- Korrekt `<!DOCTYPE html>` och `<html lang="sv">`
- Semantisk HTML: `<header>`, `<main>`, `<section>`, `<article>`, `<footer>`
- Korrekt `<meta charset="UTF-8">` och `<meta name="viewport" ...>`
- Tillgänglig: kontrastvärden uppfyller WCAG AA (4.5:1 för text)

### Responsiv design
- Mobile-first media queries
- Testa mentalt mot tre breakpoints: 360px, 768px, 1200px
- Lektionskort staplas vertikalt på mobil, grid på större skärmar
- Rubriker skalas ner på mobil (clamp() eller media queries)

### Google Sites-kompatibilitet
- Filen ska kunna klistras in i Google Sites via "Bädda in" > "Embed code"
- Undvik JavaScript som kräver extern data (fetch, AJAX)
- All interaktivitet ska vara enkel och fristående (CSS-only eller minimal JS)

---

## 5. Anti-patterns — undvik dessa

### Generisk AI-estetik
- **Ingen gradient-overload** — max en subtil gradient, och bara om det verkligen behövs
- **Inga generiska hero-sektioner** med enorm text och knappar som inte leder någonstans
- **Inget "startup-template-utseende"** — sidan ska se ut som den designats *för detta moment*, inte som en mallanpassning
- **Inga onödiga animationer** — subtila transitions är OK, men inget ska "bouncas" eller "floata" in

### Rörig design
- **Inte för mycket färg** — begränsa paletten till 3–4 färger
- **Inte för många typsnitt** — max 2 (ett för rubriker, ett för brödtext)
- **Inte för tätt** — generöst med whitespace, speciellt mellan lektionskort
- **Inte för litet** — brödtext aldrig under 16px, rubriker aldrig under 18px

### Dålig informationsarkitektur
- **Ingen information overload** — bara det eleven behöver veta, inte lärarens interna planering
- **Inga kunskapskravsformuleringar** — skriv om mål till elevvänligt språk
- **Ingen duplicering** — visa inte samma information på flera ställen

---

## 6. Genereringsprocess

1. **Samla data** från momentplanen (steg 1–4 i planera-moment):
   - Ämne, kurs, tema
   - Lärandemål (omformulera till elevspråk)
   - Lektionsstruktur med titlar och innehållsbeskrivningar
   - Pedagogiska metoder (nämn bara de som är relevanta för eleven)

2. **Fråga läraren** om kompletterande information:
   - Datum för varje lektion
   - Förberedelser som eleverna behöver göra inför specifika lektioner
   - Om lärarens namn ska visas
   - Om det finns något extra läraren vill kommunicera till eleverna

3. **Välj färgpalett och typografi** baserat på ämne — presentera valet för läraren

4. **Generera HTML-filen**:
   - Skriv HTML-koden direkt (ingen templating-motor behövs)
   - All CSS inline i `<style>`-block
   - Eventuell JS inline i `<script>`-block (minimalt)
   - Validera mentalt mot tekniska krav och estetiska riktlinjer

5. **Presentera för läraren**:
   - Visa en kort beskrivning av vad sidan innehåller
   - Öppna filen i webbläsare om möjligt, annars beskriv layouten
   - Fråga om justeringar (färg, formuleringar, ordning)

6. **Spara** till `moment-[ämne]-[tema]/momentoversikt.html`
