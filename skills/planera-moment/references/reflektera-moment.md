# Reflektera över ett genomfört moment (F3) - protokoll

Detta protokoll stänger återkopplingsslingan. Där `/planera-moment` fångar **planeringspreferenser** (vad läraren ville medan ni planerade) fångar detta **utfall** (vad som hände i klassrummet). Skillnaden är hela poängen: utfall är validerat mot verkligheten och är ett starkare underlag för framtida defaults än en preferens.

Håll dialogen på **svenska**. Läraren äger tolkningen av vad som hände; du strukturerar, speglar mot momentets designval och bokför.

---

## 1. Lokalisera momentet

1. Om `$ARGUMENTS` anger ämne/tema: leta upp `output/lessons/[Ämne]/[Tema]/momentplan.md`.
2. Annars: lista befintliga momentplaner (`output/lessons/*/*/momentplan.md`), visa tema + kurs + datum, och fråga vilket moment reflektionen gäller.
3. **Läs momentplanen i sin helhet.** Extrahera det som utfallsintervjun ska speglas mot:
   - **Momenttyp** (brottnings- / färdighets- / översikts-moment) och **drivande fråga** (ordagrant)
   - **Rollsekvens** (nivå 4) - vilka roller, i vilken ordning, med vilken exit per roll
   - **Brottningsform** (nivå 5) - diskursmål, form, gruppstruktur, ev. position-tilldelning (endast om momentet hade en Brottning-roll)
   - **Förutsättningar** (nivå 3) - innehåll + begrepp + leveransplan, och verifikationsregelns tre bedömningar
   - **Lärandemål** (E/C/A)
   - **Override-räknare** - vilka avvikelser från defaults läraren gjorde, med kontextläsningskategori och motivering
   - **Kunskapsunderlag (wiki)** - vilka wiki-sidor som bar momentet

Om ingen momentplan finns: säg det, och erbjud en fri reflektion som ändå kan skrivas till kursminnet (utan spegling mot designval).

---

## 2. Utfallsintervju - förankrad i momentets faktiska val

Ställ frågorna **mot momentets egna designval**, inte generiskt. Gruppera i rimliga AskUserQuestion-omgångar (2-4 frågor åt gången) eller för en öppen dialog om läraren föredrar det. Läraren kan hoppa över vad som helst.

Anpassa efter momenttyp: en Brottning-fråga (2.3) är bara relevant om momentet hade en Brottning-roll. För färdighets-/översikts-moment: fokusera på 2.1, 2.2, 2.4, 2.6-2.8.

### 2.1 Bärighet - höll den drivande frågan?

> "Höll frågan *'[frågan ordagrant]'* hela momentet, eller tappade den kraft efter någon lektion?"

Detta trycktestar skärpningsfiltrets **bärighetstest** (steg 1.6.5) mot verkligheten. Om frågan dog tidigt: notera det - det är ett skarpt lärdomstillfälle för hur frågor formuleras i denna kurs.

### 2.2 Rollutfall - nådde eleverna rollernas exit?

För **varje roll** i sekvensen (eller de mest bärande): 

> "Rollen [roll] skulle sluta med att eleven exit:ar med [rollens exit]. Visade exit ticket-datan att de nådde dit? Vilken roll fungerade bäst, vilken sämst?"

Fråga konkret efter **exit ticket-utfallet** (de tre högarna: nådde exit / osäker / nådde inte). Det är den mätpunkt ramverket redan bygger in - här flödar den tillbaka.

### 2.3 Brottningsform - höll formen? (endast Brottning-moment)

> "Brottningen kördes som [form] med [gruppstruktur/strukturmekanism] mot diskursmålet [diskursmål]. Höll strukturen talutrymmet, eller dominerade några få trots mekanismen? Uppnåddes diskursmålet (t.ex. för Syntes: formulerade de motståndarens position lika starkt)? Skulle du byta form nästa gång?"

Spegla mot Larsson-risken (3-5 elever dominerar utan strukturerade talturer) och Felton/Crowell/Liu (diskursmålet, inte formatet, avgör my-side-bias).

### 2.4 Förutsättningsverifikation - satt grunden? (nivå 3)

> "När kärnaktiviteten släpptes lös - satt förutsättningarna ([innehåll/begrepp från 2.4]), eller blev det luckor? Höll Princip 3-leveransen (levererat i förväg, elevens ansvar), eller fick du stötta mer än planerat?"

Om luckor: var verifikationsregelns bedömning (andel/spridning, konsekvens, frågetypens tolerans) för optimistisk? Det kalibrerar nästa moments verifikation.

### 2.5 Override-utfall - var avvikelserna rätt?

Gå igenom Override-räknaren. För varje override:

> "Du avvek från defaulten på [nod] med motiveringen [kontextläsning]. Visade sig det vara rätt i klassrummet, eller hade ramverkets default varit bättre?"

Detta är Kontextprimatets självkorrigering sluten mot utfall: en override som konsekvent visar sig rätt betyder att defaulten är fel kalibrerad *för denna kurs* (skriv in i kursminnet så defaulten justeras); en override som visar sig fel är en vana att vara vaksam på.

### 2.6 Differentiering - höll golvet och taket?

> "Höll stödet mot E (eleverna kunde brottas/arbeta på grundläggande nivå)? Fick A-eleverna gå på djupet, eller bromsades de? (Meta-mönstret: skydda golvet, släpp taket.)"

### 2.7 Elevaktiv tid och tid

> "Landade elevaktiv tid över 50% i praktiken, eller åt genomgångar/logistik upp arbetstiden? Höll tidsplaneringen?"

### 2.8 Fritt - vad ändrar du nästa gång?

> "Om du kör ett liknande moment i denna kurs igen - vad gör du annorlunda?"

---

## 3. Skriv till kursminnet - sektionen `## Utfall (från genomförda moment)`

Öppna kursens minnesfil (`output/lessons/_kursminne/[kursminne-slug].md`, sluggen i `kurser.json`). Skapa den om den saknas enligt formatet i `references/kursminne.md`.

**Håll utfall skilt från preferenser.** Skriv utfallslärdomar under sektionen `## Utfall (från genomförda moment)` - inte i preferenssektionerna. Skälet: en preferens är vad läraren vill; ett utfall är vad som fungerade. Att blanda dem gör att man inte kan se vilket råd som är validerat mot klassrummet.

Regler (utöver de allmänna i `references/kursminne.md`):
- **Generalisera till kursnivå** - inte "lektion 3 drog över" utan "sokratiskt seminarium med hela klassen kollapsade i talutrymme - använd fishbowl eller mindre grupper i denna klass".
- **Tagga varje utfallspunkt med vilket ramverkselement det gäller** (roll / form / förutsättning / override / differentiering / bärighet) så det kan matcha rätt default nästa gång.
- **Koppla override-utfall explicit:** om en override visade sig rätt tre gånger → notera "default för [nod] är fel kalibrerad för denna kurs, föredra [lärarens val]". Det är så defaulten faktiskt lär sig.
- **Max 5 punkter** även här; slå ihop de minst specifika när det svämmar över.

Format för sektionen:

```markdown
## Utfall (från genomförda moment)
- **[Ramverkselement]:** [generaliserad lärdom validerad mot klassrummet] (moment: [tema], [datum])
- ...
```

Uppdatera även **Historik**-tabellen med en rad: `| [datum] | [tema] | [nyckellärdom från utfallet] |`. Bumpa `senast_uppdaterad` och `antal_moment` i frontmatter.

---

## 4. Skriv till momentplan.md - sektionen `## Utfall`

Lägg till (eller uppdatera) en `## Utfall`-sektion sist i momentplanen. Detta fullbordar M-iv: designvalen dokumenterades vid planering, utfallet dokumenteras här - tillsammans blir momentplanen en fullständig post av *val → resultat*.

```markdown
## Utfall (reflektion efter genomförande)
- **Reflekterat:** [datum]
- **Bärighet (drivande fråga):** [höll / dog efter lektion N - kommentar]
- **Rollutfall:** [vilka roller nådde exit enligt exit tickets, vilken fallerade]
- **Brottningsform:** [höll formen / diskursmålet uppnått? - eller "ej tillämpligt"]
- **Förutsättningar (nivå 3):** [satt / luckor - verifikationsregeln träffsäker?]
- **Override-utfall:** [per override: rätt / fel i klassrummet]
- **Differentiering:** [golv höll? tak släppt?]
- **Elevaktiv tid:** [>50% i praktiken? ja/nej]
- **Till nästa gång:** [lärarens konkreta ändring]
```

---

## 5. Bekräfta

Sammanfatta kort:

> "Jag har fört tillbaka utfallet från [tema] till kursminnet för [kurs] under *Utfall* - bl.a. [1-2 skarpaste lärdomar]. Nästa gång du planerar ett liknande moment i den här kursen väger jag in det när jag föreslår defaults (roll, form, förutsättningar), så förslagen bygger på vad som faktiskt fungerade och inte bara på vad ramverket antar. Momentplanen har nu en Utfall-sektion så valen och resultatet står tillsammans."

Om någon override visade sig systematiskt rätt: nämn att defaulten för den noden nu är omkalibrerad för kursen.
