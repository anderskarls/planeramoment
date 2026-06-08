# Steg 5a: Elevuppgifter (separata Word-dokument)

Eleverna behöver konkret material att arbeta med under lektionen - inte bara instruktioner i lärarens lektionsplan. Efter att varje lektionsplan godkänts, generera separata elevuppgifter för lektionens **rollkärna** (det guidade och självständiga elevarbetet som realiserar rollens exit).

### Vad ska genereras

Gå igenom den godkända lektionsplanen och identifiera vilka elevmaterial som behövs. Typiska exempel:

- **Arbetsblad/uppgiftsblad** - strukturerade frågor, analysuppgifter, jämförelseövningar med tydliga instruktioner och utrymme för elevsvar
- **Källmaterial** - sammanställda källtexter, utdrag, citat, bilder eller data som eleverna ska arbeta med. Inkludera källhänvisningar. Om NotebookLM är aktivt, använd källor därifrån
- **Analysuppgifter** - konkreta uppgifter med stegvisa instruktioner, frågeställningar som stiger i komplexitet (E-C-A-progression)

Ibland räcker ett dokument per lektion, ibland behövs flera (t.ex. ett källkompendium + ett arbetsblad). Anpassa efter lektionens innehåll.

### Innehåll och struktur

Varje elevuppgift ska:
- Ha en tydlig rubrik som kopplar till lektionen ("Lektion N: [Uppgiftstitel]")
- Börja med en kort kontextsättning - vad ska eleven göra och varför
- Ha numrerade instruktioner/frågor
- **Inkludera differentieringsstöd direkt i dokumentet** - t.ex. stödrutor ("Tips: ...") för elever som behöver hjälp, och fördjupningsfrågor markerade med stjärna för elever som vill utmanas
- Inkludera eventuellt källmaterial direkt i dokumentet, eller hänvisa till ett separat källdokument om det är omfattande

### Kvalitetskontroll

- Matchar uppgiften lektionens rollkärna (det guidade/självständiga elevarbetet)?
- Är instruktionerna tillräckligt tydliga för att eleven ska kunna börja arbeta utan ytterligare förklaring?
- Finns både stöd (mot E) och utmaning (mot A) inbyggt?
- Är språknivån anpassad för gymnasieelever (inte lärarspråk)?

### Generera som Word-dokument (.docx)

Använd samma docx-metod som lektionsplanerna. Format:
- A4-format med 1"-marginaler
- Rubrik som Heading 1, underrubriker som Heading 2
- Numrerade listor för frågor/instruktioner
- Tabeller vid behov (t.ex. jämförelseuppgifter, källsammanställningar)
- Teckensnitt: Arial, 12pt brödtext
- Sidfot med kursnamn och lektionstitel

**Spara i båda format:**
- **Markdown:** `Undervisningsmaterial/[Ämne]/[Tema]/elevuppgift-lektion-[N].md` (i vaultet)
- **Word:** `C:\Undervisningsmaterial\[Ämne]\[Tema]\elevuppgift-lektion-[N].docx`

(Samma mönster för källmaterial: `kallmaterial-lektion-[N].md` / `.docx`)

Presentera en kort beskrivning av de genererade elevuppgifterna och fråga: "Vill du justera elevuppgifterna, eller ska jag gå vidare?"
