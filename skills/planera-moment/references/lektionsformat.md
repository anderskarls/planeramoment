# Lektionsplanering - format och mallar (fristående lektioner)

Mallar för **fristående lektioner** (kommandot `planera-lektion`). Rollbaserade: en lektion realiserar en roll ur Momentplaneringsramverket (nivå 4), och lektionskärnan formas av rollen - inte av en fast fassekvens.

**Ram, rollvägledning och detaljerad mall: se `lektionsplanering.md`** - den är kanonisk. Där finns de tre evidensprinciperna (ram), den rollspecifika kärnvägledningen för de 9 rollerna, brottningsformen och den detaljerade lektionsmallen (Variant 1 = `lektionsplanering.md` avsnitt 5). Nedan endast det fristående-specifika: frontmatter, den kortfattade varianten (Variant 2) och riktlinjer.

En fristående lektion saknar föregående lektions exit ticket-data. Öppna då med **förkunskapsaktivering** i stället för spaced retrieval, och ersätt "Moment"-fältet med "Fristående lektion" i mallen.

---

## Frontmatter (läggs överst i lektionsfilen)

```yaml
---
tags:
  - lektionsplanering
  - [ämne: samhällskunskap eller historia]
ämne: [Ämne]
kurs: [Kursnamn]
område: [Tema/område]
roll: [lektionens roll]
datum: "[YYYY-MM-DD]"
status: utkast
---
```

För den **detaljerade** varianten: lägg frontmattern överst och följ sedan den detaljerade mallen i `lektionsplanering.md` avsnitt 5 (med de fristående-anpassningar som beskrivs ovan).

---

## Variant 2: Kortfattad lektionsplanering

Grundstruktur som läraren fyller i och anpassar själv. Passar för erfarna lärare som vill ha en stomme att utgå ifrån.

### Struktur

```markdown
# Lektion [N]: [Lektionstitel]

**Kurs:** [Kurs]
**Moment:** [Moment, eller "Fristående lektion"]
**Lektionslängd:** [Längd]

## Roll
- [Vilken roll lektionen realiserar + vad eleven exit:ar med]

## Lärandemål

[Kortfattat mål - vad ska eleven kunna?]

## Centralt innehåll

- [Relevant innehåll]

## Lektionsförlopp

| Tid | Moment | Beskrivning |
|-----|--------|-------------|
| 0-X min | Öppning (retrieval) | [Kort beskrivning] |
| X-Y min | Rollkärna | [Kort beskrivning] |
| Y-Z min | Avslut (exit ticket) | [Kort beskrivning] |

## Material

- [Material som behövs]

## Kopplingar

- [[Momentnamn - momentplan]]
- [[Eventuell nästa lektion]]
```

### Riktlinjer för kortfattad planering

- **Roll:** ange rollen och exit - det styr kärnan även i den korta varianten.
- **Lärandemål:** ett mål räcker - formulera det tydligt utan betygsnivåer.
- **Lektionsförlopp:** ange moment utan detaljerade instruktioner, men behåll ramen (öppning → kärna → avslut).
- **Hoppa över:** differentiering, bilagor, lärarinstruktioner, elevaktivitetslista - läraren hanterar detta själv.
- **Fokus:** ge en tydlig stomme, inte en färdig produkt.
