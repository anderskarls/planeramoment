# Avslutning

När alla steg är klara:

1. Presentera en **översikt** av allt genererat material med fillista:

   **I vaultet** (`Undervisningsmaterial/[Ämne]/[Tema]/`):
   - `momentplan.md` - översiktsplanering
   - `lektion-N.md` - detaljerade lektionsplaner (Markdown)
   - `elevuppgift-lektion-N.md` - elevuppgifter, arbetsblad och källmaterial (Markdown)
   - `presentation-lektion-N.html` - klassrumspresentationer (reveal.js HTML)
   - `momentoversikt.html` - momentöversikt för elever (HTML)

   **Utanför vaultet** (`C:\Undervisningsmaterial\[Ämne]\[Tema]\`):
   - `lektion-N.docx` - detaljerade lektionsplaner (Word)
   - `elevuppgift-lektion-N.docx` - elevuppgifter, arbetsblad och källmaterial (Word)
   - `video/video-moment-oversikt.mp4` - momentöversikt-video för elever (NotebookLM)
   - `video/video-forforstaelse-lektion-N.mp4` - förförståelse-videor inför lektioner med förberedelsematerial (NotebookLM)
2. Fråga om läraren vill justera något.
3. **Kunskapsbasintegration (H4):** Föreslå att läraren skriver en reflektion efter momentet med hjälp av mallen i `Mallar/Lektionsreflektion.md` (om den finns). Reflektionen kan sedan användas för att förbättra framtida moment.
4. Nämn kort vad som kan byggas vidare i framtiden: flashcards, elevmaterial, formativa bedömningsuppgifter.
5. Tipsa om att `momentoversikt.html` kan publiceras via Google Sites: skapa en ny sida, välj "Bädda in" > "Embed code" och klistra in HTML-koden, eller ladda upp filen och länka till den.

6. **Uppdatera kursminnet:** Analysera hela konversationen och identifiera justeringar läraren gjorde under processen. Fokusera på:
   - Förslag som läraren ändrade (pedagogisk ansats, tidsfördelning, aktiviteter)
   - Saker läraren lade till eller tog bort
   - Explicit feedback ("jag vill alltid ha...", "det här fungerar inte för den här gruppen")
   - Mönster i differentieringen

   Generalisera lärdomarna - spara inte detaljer specifika för just detta moment, utan det som troligen gäller för framtida moment i samma kurs. Skriv/uppdatera minnesfilen i `.claude/planera-moment/minne/[kursnamn-kebab-case].md` enligt formatet i sektionen "Kursminne" (se `references/kursminne.md`). Skapa katalogen om den inte finns.

   Presentera kort vad som sparades: "Jag har uppdaterat kursminnet för [kursnamn] med följande lärdomar: [kort lista]. Nästa gång du planerar ett moment i denna kurs tar jag hänsyn till detta från start."

Avsluta med: "Ditt moment är klart! Markdown-filerna finns i vaultet under `Undervisningsmaterial/[Ämne]/[Tema]/` och Word-dokumenten finns i `C:\Undervisningsmaterial\[Ämne]\[Tema]\`. Presentationerna är HTML-filer (öppna i webbläsaren och tryck S för talarnoter) och momentöversikten är en HTML-sida som du kan dela med eleverna via Google Sites - redo att använda direkt. Lycka till med undervisningen!"
