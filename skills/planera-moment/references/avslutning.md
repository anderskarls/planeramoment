# Avslutning

När alla steg är klara:

1. Presentera en **översikt** av allt genererat material med fillista:

   **I vaultet** (`output/lessons/[Ämne]/[Tema]/`):
   - `momentplan.md` - översiktsplanering
   - `lektion-N.md` - detaljerade lektionsplaner (Markdown)
   - `elevuppgift-lektion-N.md` - elevuppgifter, arbetsblad och källmaterial (Markdown)
   - `presentation-lektion-N.html` - klassrumspresentationer (reveal.js HTML)
   - `momentoversikt.html` - momentöversikt för elever (HTML)

   **Utanför vaultet** (`[Word-mappen]\[Ämne]\[Tema]\` - se Sökvägar i SKILL.md):
   - `lektion-N.docx` - detaljerade lektionsplaner (Word)
   - `elevuppgift-lektion-N.docx` - elevuppgifter, arbetsblad och källmaterial (Word)
   - `video/video-moment-oversikt.mp4` - momentöversikt-video för elever (NotebookLM)
   - `video/video-forforstaelse-lektion-N.mp4` - förförståelse-videor inför lektioner med förberedelsematerial (NotebookLM)
2. Fråga om läraren vill justera något.
3. **Wiki-slingan (H4):** Föreslå att läraren skriver en reflektion efter momentet med hjälp av mallen i `templates/Lektionsreflektion.md` (om den finns). Påminn om slingan: reflektionen ingestas till wikin (`/ingest`) och blir en del av kunskapsbasen som nästa moments planering läser i steg 1.5.5, 3 och 5. Peka på momentplanens `## Kunskapsunderlag (wiki)` - den visar vilka wiki-sidor som bar detta moment och är en naturlig startpunkt för reflektionen ("stämde kunskapsbasens råd i klassrummet?").
4. Nämn kort vad som kan byggas vidare i framtiden: flashcards, elevmaterial, formativa bedömningsuppgifter.
5. Tipsa om att `momentoversikt.html` kan publiceras via Google Sites: skapa en ny sida, välj "Bädda in" > "Embed code" och klistra in HTML-koden, eller ladda upp filen och länka till den.

6. **Uppdatera kursminnet:** Analysera hela konversationen och identifiera justeringar läraren gjorde under processen. Fokusera på:
   - Förslag som läraren ändrade (pedagogisk ansats, tidsfördelning, aktiviteter)
   - Saker läraren lade till eller tog bort
   - Explicit feedback ("jag vill alltid ha...", "det här fungerar inte för den här gruppen")
   - Mönster i differentieringen

   Generalisera lärdomarna - spara inte detaljer specifika för just detta moment, utan det som troligen gäller för framtida moment i samma kurs. Skriv/uppdatera minnesfilen i `output/lessons/_kursminne/[kursminne-slug].md` (sluggen står i `kurser.json`) enligt formatet i `references/kursminne.md`. Skapa katalogen om den inte finns.

   Presentera kort vad som sparades: "Jag har uppdaterat kursminnet för [kursnamn] med följande lärdomar: [kort lista]. Nästa gång du planerar ett moment i denna kurs tar jag hänsyn till detta från start."

   *Obs: detta är planeringspreferenser (vad du ville medan vi planerade). Utfallet - vad som faktiskt hände i klassrummet - fångas separat.*

7. **Peka på slingans andra halva:** Påminn läraren om att köra `/reflektera-moment` **efter** att momentet undervisats. Då förs utfallet (höll frågan, nådde rollerna sina exit, satt förutsättningarna, var dina overrides rätt) tillbaka till kursminnets `## Utfall`-sektion och försörjer framtida defaults med det som faktiskt fungerade - inte bara det du föredrog vid planeringsbordet. Det är så systemet blir bättre över tid på riktigt.

Avsluta med: "Ditt moment är klart! Markdown-filerna finns i vaultet under `output/lessons/[Ämne]/[Tema]/` och Word-dokumenten finns i Word-mappen (`[Word-mappen]\[Ämne]\[Tema]\` - ange den resolvade sökvägen). Presentationerna är HTML-filer (öppna i webbläsaren och tryck S för talarnoter) och momentöversikten är en HTML-sida som du kan dela med eleverna via Google Sites - redo att använda direkt. Lycka till med undervisningen!"
