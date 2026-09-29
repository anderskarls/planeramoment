# Lektionsplanering - format och mallar (fristående lektioner)

Mallar för **fristående lektioner** (kommandot `planera-lektion`). Rollbaserade: en lektion realiserar en roll ur Momentplaneringsramverket (nivå 4), och lektionskärnan formas av rollen - inte av en fast fassekvens.

**Ram, rollvägledning och detaljerad mall: se `lektionsplanering.md`** - den är kanonisk. Där finns de tre evidensprinciperna (ram), den rollspecifika kärnvägledningen för de 9 rollerna, brottningsformen och formatet för lektionsplanen med dess skrivregler (Variant 1 = `lektionsplanering.md` avsnitt 5). Nedan endast det fristående-specifika: frontmatter, den kortfattade varianten (Variant 2) och riktlinjer.

Båda varianterna byggs till en HTML-läsvy för klassrummet med `scripts/bygg-lektionsplan.py`. Scriptet läser tidsblocken (`### start-slut · Titel`), så även den kortfattade varianten skrivs med dem.

En fristående lektion saknar föregående lektions exit ticket-data. Öppna då med **förkunskapsaktivering** i stället för spaced retrieval, och skriv "Fristående lektion" i `moment`-fältet.

---

## Frontmatter (läggs överst i lektionsfilen)

```yaml
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: lektionsplan
tags:
  - lektionsplanering
  - [ämne: samhällskunskap eller historia]
lektion: [N, eller tomt]
titel: [Lektionstitel]
kurs: [Kursnamn]
grupper: [Grupp (antal), eller tomt]
moment: [Momentets titel, eller "Fristående lektion"]
langd: [minuter]
elevaktiv: [elevaktiva minuter]
roll: [lektionens roll]
status: utkast
---
```

För den **detaljerade** varianten: lägg frontmattern överst och följ sedan mallen i `lektionsplanering.md` avsnitt 5 (med de fristående-anpassningar som beskrivs ovan).

---

## Variant 2: Kortfattad lektionsplanering

Grundstruktur som läraren fyller i och anpassar själv. Passar för erfarna lärare som vill ha en stomme att utgå ifrån.

### Struktur

```markdown
# Lektion [N]: [Lektionstitel]

> [Vad eleverna går ut med, i en mening]

## Före lektionen

- [ ] [Förberedelse]

## Förlopp

### 0-X · Öppning: [förkunskapsaktivering eller retrieval]

Eleverna: [kort]

### X-Y · [Rollkärna]

Eleverna: [kort]

### Y-Z · Exit ticket och avslut

Eleverna: [kort]

## Material

- [Material som behövs]

## Bakgrund

**Roll:** [roll] - eleven exit:ar med [...].
**Lärandemål:** [ett mål]
**Centralt innehåll:** [relevant innehåll]
**Kopplingar:** [[Momentnamn - momentplan]], [[Eventuell nästa lektion]]
```

### Riktlinjer för kortfattad planering

- **Kärnan (`>`)** och **roll** i Bakgrund styr lektionen även i den korta varianten.
- **Lärandemål:** ett mål räcker - formulera det tydligt utan betygsnivåer.
- **Förlopp:** ett tidsblock per del med en `Eleverna:`-rad, utan lärarpunkter och `Säg:`-rader, men behåll ramen (öppning → kärna → avslut).
- **Hoppa över:** differentiering, bilagor, exit ticket-sektion, Genom hela lektionen - läraren hanterar detta själv.
- **Fokus:** ge en tydlig stomme, inte en färdig produkt.
