# Wikin - användning (lärarens kunskapsbas)

Wikin i vaultet (`wiki/`) är lärarens ackumulerade kunskapsbas: pedagogisk evidens, didaktiska synteser och ämnessynteser från ingestade källor. Den konsulteras genom hela planeringen, parallellt med NotebookLM.

## Arbetsfördelning: wiki vs NotebookLM

| | **Wikin** | **NotebookLM** |
|---|---|---|
| Innehåll | Lärarens kunskapsbas: pedagogisk evidens, didaktik, ämnessynteser, reflektionslärdomar | Källgrundat ämnesinnehåll (läromedel, källor) med referenshänvisningar |
| Svarar på | "Hur undervisar jag detta bra? Vad vet jag redan? Vad har jag lärt mig tidigare?" | "Vad ska eleverna lära sig om X? Vilka fakta, citat och källor finns?" |
| Matar främst | Designval (steg 1-3), didaktiska val och lärarinstruktioner (steg 5) | Elevriktat innehåll: lektionsstoff, elevuppgifter, presentationer, videor (steg 5-6) |

Båda kan träffa samma fråga - då är wikin lärarens röst (vägval) och NotebookLM källans röst (stoff).

## Uppslagsprotokoll

1. **Läs `index.md`** (vaultets rot) - innehållskatalogen över alla wiki-sidor. Identifiera relevanta MOC:ar och concepts för temat. Ämnes-MOC:ar förekommer (t.ex. en MOC byggd inför ett specifikt moment) - de är guld när de finns.
2. **Läs de mest relevanta sidorna** (topics före concepts före sources - MOC:arna pekar vidare).
3. **Semantisk sökning** när index inte räcker eller för att hitta oväntade kopplingar:
   ```bash
   ./resources/local-brain-search/run_search.sh "[sökfråga]" --limit 5 --json
   ```
4. **Kopplingar runt en träffad sida** (valfritt, när en sida visar sig central):
   ```bash
   ./resources/local-brain-search/run_connections.sh "[Sidnamn]" --json
   ```

**Fallback:** om sökskripten inte finns på maskinen - använd `index.md` + Grep över `wiki/`. Protokollet fungerar utan FAISS, bara långsammare.

## Presentationsregler (samma ton som kursminnet)

- Lyft högst 2-3 fynd per uppslag - wikin ska informera dialogen, inte översvämma den
- Citera alltid med `[[wikilänkar]]` så läraren kan gå till källan
- Säg "wikin föreslår" / "enligt [[sidan]]" - wikifynd är input till M-i-defaults, inte tvång
- Hittas inget relevant: säg ingenting och gå vidare

## Spårbarhet: Kunskapsunderlag i momentplan.md

Wiki-sidor som faktiskt påverkat ett designval eller en lektion dokumenteras löpande i momentplanens sektion `## Kunskapsunderlag (wiki)` med `[[länk]]` + en rad om vad sidan bidrog med. Det ger spårbarhet (M-iv-anda) och gör momentplanen till en ingång tillbaka till kunskapsbasen.

## Var i processen wikin konsulteras

| Steg | Uppslag |
|---|---|
| **1** (designdialog) | Tema-uppslag: ämnes-MOC, relevanta concepts, tidigare reflektioner om temat/kursen. Informerar brottningsfråga, skärpningsfilter och Hess-default. |
| **3** (roller/form) | Metod- och didaktikuppslag: vad säger kunskapsbasen om kandidatformerna och rollernas aktiviteter? Tidigare reflektioner från liknande moment. |
| **5** (lektionsplaner) | Per lektion: didaktiska fynd för lektionens roll/metod (missuppfattningar, tekniker, kalibrering) + ämnessynteser som skärper lärarinstruktionerna. |
| **Avslutning** | Slingan sluts: lärarens reflektion efter momentet ingestas till wikin och stärker nästa planering. |

## Wiki-slingan (varför detta ackumulerar)

Wikin blir bättre av varje moment: planeringen läser wikin → momentet genomförs → läraren reflekterar → reflektionen ingestas → nya wiki-sidor → nästa planering läser dem. Skillen läser wikin men skriver ALDRIG till den (output skriver inte tillbaka till wikin - den växer via ingest).
