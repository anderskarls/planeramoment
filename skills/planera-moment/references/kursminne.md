# Kursminne - format och regler

## Lagringsformat

En fil per kurs i vaultet under `output/lessons/_kursminne/`:
```
output/lessons/_kursminne/historia-niva-1b.md
output/lessons/_kursminne/samhallskunskap-1a2.md
output/lessons/_kursminne/internationella-relationer.md
```

Filnamnet är kursens `kursminne`-slug från `kurser.json`. Minnet ligger i vaultet (inte i `.claude/`) så att det syncas mellan maskiner via Obsidian Sync och är synligt i Obsidian.

Varje minnesfil har denna struktur:

```markdown
---
kurs: [Kursens fullständiga namn]
senast_uppdaterad: YYYY-MM-DD
antal_moment: [N]
---

# Kursminne: [Kursnamn]

## Pedagogiska preferenser
- [Lärdom från justering, t.ex. "Föredrar EPA framför traditionella genomgångar"]
- [...]

## Tidsfördelning
- [T.ex. "Kortar lärargenomgången till förmån för elevaktivt arbete i rollkärnan"]
- [...]

## Aktiviteter och metoder
- [T.ex. "Gillar debattövningar, använder dem ofta som brottningsform"]
- [T.ex. "Väljer alltid bort rollspel för denna grupp"]
- [...]

## Differentiering
- [T.ex. "Lägger alltid till meningsstartare som stöd mot E"]
- [...]

## Innehållspreferenser
- [T.ex. "Vill alltid ha primärkällor med, inte bara lärobokstexter"]
- [...]

## Övrigt
- [Andra mönster som inte passar ovan]
- [...]

## Tvärgående trådar mellan moment
- [T.ex. "Antikens arv-momentet - väck tillbaka i renässans-momentet, upplysnings-momentet, fascism-momentet"]
- [Format: när X-moment kommer, väck koppling till Y-moment med fråga/verktyg Z]
- [...]

## Historik
| Datum | Moment | Nyckellärdom |
|-------|--------|-------------|
| YYYY-MM-DD | [Temanamn] | [Kort sammanfattning] |
```

## Regler för minneshantering

- **Skriv aldrig över** - lägg till nya lärdomar, ta inte bort gamla
- **Generalisera** - spara inte "ändrade tid i lektion 3 från 10 till 15 min" utan "föredrar längre guidad övning, kortar explicit instruktion"
- **Undvik redundans** - om en lärdom redan finns, förstärk den med en notering istället för att duplicera
- **Max 5 punkter per kategori** - om det blir fler, slå ihop eller ersätt de minst specifika
- **Var ärlig** - om det inte finns tydliga mönster efter bara ett moment, skriv få punkter. Minnet växer organiskt.

## När minnet uppdateras

Som default uppdateras kursminnet i **Avslutningen** (en samlad analys av hela momentet - se `references/avslutning.md`).

### Mid-flight uppdateringar

Om läraren under planeringsdialogen **explicit säger** något i stil med:
- "spara detta i kursminnet"
- "kom ihåg det här till nästa moment"
- "lägg till i kursminnet att..."

→ uppdatera kursminnesfilen **direkt** (inte vid Avslutning), bekräfta för läraren ("Sparat: [kort beskrivning]"), och notera i momentplan.md under "Tvärgående trådar > Inter-moment" att kursminnet uppdaterades vid denna plats.

Avslutningens kursminnes-uppdatering blir då en *sammanfattning + utfyllnad av det som inte fångades mid-flight*, inte enda tillfället.
