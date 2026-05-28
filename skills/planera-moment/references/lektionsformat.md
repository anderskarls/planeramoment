# Lektionsplanering - format och mallar (rollbaserad)

Mallar för **fristående lektioner** (kommandot `planera-lektion`). Rollbaserade: en lektion realiserar en roll ur Momentplaneringsramverket (nivå 4), och lektionskärnan formas av rollen - inte av en fast fassekvens.

Två varianter: **detaljerad** och **kortfattad**.

För full roll-för-roll-vägledning och brottningsformer, se `lektionsplanering.md`. Denna fil är den praktiska mallen.

---

## Ram (gäller båda varianter)

Varje lektion ramas av tre evidensprinciper, ortogonala mot rollinnehållet:

1. **Öppna med retrieval** (spaced practice) - aktiv återkallelse från tidigare lektioner. Fristående lektion utan föregångare: aktivera förkunskaper istället.
2. **Elevaktiv tid > 50%** (sikta 60%+).
3. **Avsluta med exit ticket** som mäter rollens exit + kort framåtkoppling.

Kärnan mellan öppning och avslut formas av lektionens roll (Frågeförankring, Provokation, Begreppsbygge, Perspektivbygge, Brottning, Syntes, Metareflektion, Applikation, Återbesök).

---

## Variant 1: Detaljerad lektionsplanering

Fullständig planering med lärarinstruktioner, lektionsförlopp, differentiering och bilagor. Passar när läraren vill ha allt färdigt och kunna gå rakt in i klassrummet.

### Frontmatter

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

### Struktur

```markdown
# Lektion [N]: [Lektionstitel]

**Kurs:** [Kurs]
**Moment:** [Moment/område, eller "Fristående lektion"]
**Lektionslängd:** [t.ex. 60 minuter]

## Roll
- **Roll:** [vilken av de 9 rollerna lektionen realiserar]
- **Eleven exit:ar med:** [rollens exit, konkretiserad mot temat]

## Lärandemål för lektionen

[Vad ska eleven kunna efter lektionen?]

- **E-nivå:** [Översiktligt mål]
- **C-nivå:** [Utförligt mål]
- **A-nivå:** [Utförligt och nyanserat mål]

## Centralt innehåll

- [Relevant centralt innehåll från kursplanen]

## Förberedelse

- [Vad behöver läraren förbereda innan lektionen?]
- [Material att skriva ut, projicera, etc.]

## Lektionsförlopp

| Tid | Moment | Aktivitet | Beskrivning |
|-----|--------|-----------|-------------|
| 0-X min | Öppning (retrieval) | [Namn] | [Kort beskrivning] |
| X-Y min | Rollkärna: [roll] | [Namn] | [Kort beskrivning] |
| Y-Z min | Avslut (exit ticket) | [Namn] | [Kort beskrivning] |

(Tidsuppskattningar, inte fasta fasandelar. Elevaktiv tid > 50%.)

## Brottningsform (endast Brottning-lektioner)

- **Diskursmål:** [Övertyga / Syntes / Utforska / Klargöra / Pröva]
- **Form:** [sokratiskt seminarium / debatt / fishbowl / SAC ...]
- **Gruppstorlek + strukturmekanism:** [t.ex. talkort, roterande roller]
- **Position-tilldelning:** [Ja, tippande fråga | Ej tillämpligt]

## Lärarinstruktioner

### Öppning (retrieval)
[Specifika återkallelsefrågor, kopplade till tidigare lektion om sådan finns.]

### Rollkärna
[Detaljerade instruktioner för rollens aktivitet. Worked examples vid Begreppsbygge/Perspektivbygge; samtalsstruktur och facilitering vid Brottning. Inbäddade EPA-stopp och scaffolding-tips. Frågor att ställa vid cirkulering.]

### Avslut (exit ticket)
[Exit ticket-fråga som mäter rollens exit + kort framåtkoppling.]

## Elevaktiviteter

- **[Aktivitet 1]** ([form], [tid]): [Beskrivning]
- **[Aktivitet 2]** ([form], [tid]): [Beskrivning]

**Elevaktiv tid: ca [X] av [Y] minuter ([Z]%)**

## Differentiering

- **Stöd (mot E):** [Scaffolding: meningsstartare, hjälpfrågor, ifyllda exempel, ordbank]
- **Utmaning (mot A):** [Öppnare uppgifter, perspektivbyte, gråzoner, extra analys]

## Material

- [Lista allt material som behövs]

## Koppling till bedömningsmål/kunskapskrav

[Vilka förmågor tränas? Hur kopplar lektionen till kursplanens kunskapskrav (GY11) / betygskriterier (GY25)?]

## Kopplingar

- Momentplan: [[Momentnamn - momentplan]] (om lektionen tillhör ett moment)
- Föregående lektion: [[Momentnamn - Lektion N-1]]
- Nästa lektion: [[Momentnamn - Lektion N+1]]

---

## Bilaga: [Namn]

[Bilagor som sorteringskort, jämförelsetabeller, etc. inkluderas direkt i filen.]
```

### Riktlinjer för detaljerad planering

- **Roll först:** lektionskärnan ska realisera den valda rollen. En Brottning-lektion låter formen och diskursmålet styra förloppet; en Begreppsbygge-lektion bygger på worked examples + guidad bearbetning.
- **Lärarinstruktioner:** skriv exakta formuleringar som läraren kan använda ordagrant (kursiverade). Inkludera övergångar mellan öppning, kärna och avslut.
- **EPA-stopp:** bädda in minst ett EPA-stopp vid kunskapsöverförande kärnor.
- **Cirkuleringstips:** under elevarbetet - ange frågor läraren kan ställa till enskilda grupper/par.
- **Bilagor:** inkludera allt utdelbart material direkt i filen (sorteringskort, tabeller, arbetsblad).
- **Elevaktiv tid:** beräkna och ange procentuell elevaktiv tid. Sikta på 60%+.
- **Tidsangivelser:** var realistisk - hellre lite marginal än för tajt.

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
