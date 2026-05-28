# Kursminne - format och regler

## Lagringsformat

En fil per kurs i `.claude/planera-moment/minne/`:
```
.claude/planera-moment/minne/historia-1b.md
.claude/planera-moment/minne/samhallskunskap-1a1.md
.claude/planera-moment/minne/internationella-relationer.md
```

Filnamnet ar kursnamnet i kebab-case (gemener, bindestreck).

Varje minnesfil har denna struktur:

```markdown
---
kurs: [Kursens fullstandiga namn]
senast_uppdaterad: YYYY-MM-DD
antal_moment: [N]
---

# Kursminne: [Kursnamn]

## Pedagogiska preferenser
- [Lardom fran justering, t.ex. "Foredrar EPA framfor traditionella genomgangar"]
- [...]

## Tidsfordelning
- [T.ex. "Kortar larargenomgangen till forman for elevaktivt arbete i rollkarnan"]
- [...]

## Aktiviteter och metoder
- [T.ex. "Gillar debattovningar, anvander dem ofta som brottningsform"]
- [T.ex. "Valjer alltid bort rollspel for denna grupp"]
- [...]

## Differentiering
- [T.ex. "Lagger alltid till meningsstartar som stod mot E"]
- [...]

## Innehallspreferenser
- [T.ex. "Vill alltid ha primorkallor med, inte bara larobokstexter"]
- [...]

## Ovrigt
- [Andra monster som inte passar ovan]
- [...]

## Tvargaende tradar mellan moment
- [T.ex. "Antikens arv-momentet - vack tillbaka i renässans-momentet, upplysnings-momentet, fascism-momentet"]
- [Format: nar X-moment kommer, vack koppling till Y-moment med fraga/verktyg Z]
- [...]

## Historik
| Datum | Moment | Nyckellardom |
|-------|--------|-------------|
| YYYY-MM-DD | [Temanamn] | [Kort sammanfattning] |
```

## Regler for minneshantering

- **Skriv aldrig over** - lagg till nya lardomar, ta inte bort gamla
- **Generalisera** - spara inte "andrade tid i lektion 3 fran 10 till 15 min" utan "foredrar langre guidad ovning, kortar explicit instruktion"
- **Undvik redundans** - om en lardom redan finns, forstark den med en notering istallet for att duplicera
- **Max 5 punkter per kategori** - om det blir fler, sla ihop eller ersatt de minst specifika
- **Var arlig** - om det inte finns tydliga monster efter bara ett moment, skriv fa punkter. Minnet vaxer organiskt.
