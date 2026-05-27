# Lektionsplanering — Format och mallar

Två varianter: **detaljerad** och **kortfattad**.

---

## Variant 1: Detaljerad lektionsplanering

Fullständig planering med lärarinstruktioner, tidsschema, differentiering och bilagor. Passar när läraren vill ha allt färdigt och kunna gå rakt in i klassrummet.

### Frontmatter

```yaml
---
tags:
  - lektionsplanering
  - [ämne: samhällskunskap eller historia]
ämne: [Ämne]
kurs: [Kursnamn]
område: [Tema/område]
datum: "[YYYY-MM-DD]"
status: utkast
---
```

### Struktur

```markdown
# Lektion [N]: [Lektionstitel]

**Kurs:** [Kurs]
**Moment:** [Moment/område]
**Lektionslängd:** [t.ex. 60 minuter]

## Lärandemål för lektionen

[Vad ska eleven kunna efter lektionen?]

- **E-nivå:** [Översiktligt mål]
- **C-nivå:** [Utförligt mål]
- **A-nivå:** [Utförligt och nyanserat mål]

## Centralt innehåll (Gy11)

- [Relevant centralt innehåll]

## Förberedelse

- [Vad behöver läraren förbereda innan lektionen?]
- [Material att skriva ut, projicera, etc.]

## Tidsplanering

| Tid | Fas | Aktivitet | Beskrivning |
|-----|-----|-----------|-------------|
| 0–5 min | Uppstart | [Namn] | [Kort beskrivning] |
| 5–20 min | Instruktion | [Namn] | [Kort beskrivning] |
| 20–45 min | Bearbetning | [Namn] | [Kort beskrivning] |
| 45–55 min | Summering | [Namn] | [Kort beskrivning] |
| 55–60 min | Koppling framåt | [Namn] | [Kort beskrivning] |

## Lärarinstruktioner

### Uppstart (0–5 min)
[Detaljerade instruktioner med exakta formuleringar läraren kan använda, markerade med kursiv stil.]

### Instruktion (5–20 min)
[Innehåll att presentera, med inbäddade EPA-stopp och snabbfrågor var femte minut.]

### Bearbetning (20–45 min)
[Steg-för-steg-instruktioner för elevaktiviteter. Scaffolding-tips. Frågor att ställa vid cirkulering.]

### Summering (45–55 min)
[Utgångsbiljett eller annan formativ bedömning. Fråga + scaffolding.]

### Koppling framåt (55–60 min)
[Kort intro till nästa lektion. Exakt formulering.]

## Elevaktiviteter

- **[Aktivitet 1]** ([form], [tid]): [Beskrivning]
- **[Aktivitet 2]** ([form], [tid]): [Beskrivning]
- ...

**Elevaktiv tid: ca [X] av [Y] minuter ([Z]%)**

## Differentiering

- **Stöd (mot E):** [Scaffolding: meningsstartare, hjälpfrågor, ifyllda exempel, ordbank]
- **Utmaning (mot A):** [Öppnare uppgifter, perspektivbyte, gråzoner, extra analys]

## Material

- [Lista allt material som behövs]

## Koppling till kunskapskrav

[Vilka förmågor tränas? Hur kopplar lektionen till kursplanens kunskapskrav?]

## Kopplingar

- Momentplan: [[Momentnamn — momentplan]]
- Föregående lektion: [[Momentnamn — Lektion N-1]]
- Nästa lektion: [[Momentnamn — Lektion N+1]]

---

## Bilaga: [Namn]

[Bilagor som sorteringskort, jämförelsetabeller, etc. inkluderas direkt i filen.]
```

### Riktlinjer för detaljerad planering

- **Lärarinstruktioner**: Skriv exakta formuleringar som läraren kan använda ordagrant (kursiverade). Inkludera övergångar mellan faserna.
- **EPA-stopp**: Bädda in minst ett EPA-stopp var femte minut under instruktionsfasen.
- **Cirkuleringstips**: Under bearbetningsfasen — ange frågor läraren kan ställa till enskilda grupper/par.
- **Bilagor**: Inkludera allt utdelbart material direkt i filen (sorteringskort, tabeller, arbetsblad).
- **Elevaktiv tid**: Beräkna och ange procentuell elevaktiv tid. Sikta på 60%+.
- **Tidsangivelser**: Var realistisk — hellre lite marginal än för tajt.

---

## Variant 2: Kortfattad lektionsplanering

Grundstruktur som läraren fyller i och anpassar själv. Passar för erfarna lärare som vill ha en stomme att utgå ifrån.

### Struktur

```markdown
# Lektion [N]: [Lektionstitel]

**Kurs:** [Kurs]
**Moment:** [Moment]
**Lektionslängd:** [Längd]

## Lärandemål

[Kortfattat mål — vad ska eleven kunna?]

## Centralt innehåll

- [Relevant innehåll]

## Tidsplanering

| Tid | Aktivitet | Beskrivning |
|-----|-----------|-------------|
| 0–5 min | Uppstart | [Kort beskrivning] |
| 5–20 min | Genomgång | [Kort beskrivning] |
| 20–45 min | Elevarbete | [Kort beskrivning] |
| 45–55 min | Avslutning | [Kort beskrivning] |

## Material

- [Material som behövs]

## Kopplingar

- [[Momentnamn — momentplan]]
- [[Eventuell nästa lektion]]
```

### Riktlinjer för kortfattad planering

- **Lärandemål**: Ett mål räcker — formulera det tydligt utan betygsnivåer.
- **Tidsplanering**: Ange aktiviteter utan detaljerade instruktioner.
- **Hoppa över**: Differentiering, bilagor, lärarinstruktioner, elevaktivitetslista — läraren hanterar detta själv.
- **Fokus**: Ge en tydlig stomme, inte en färdig produkt.
