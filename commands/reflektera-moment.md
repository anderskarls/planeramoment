---
name: reflektera-moment
description: Reflektera över ett GENOMFÖRT moment och mata tillbaka utfallet till kursminnet. Stänger återkopplingsslingan - fångar vad som faktiskt hände i klassrummet (höll frågan, nådde rollerna sina exit, satt förutsättningarna, var overrides rätt), inte planeringspreferenser. Kör efter att momentet undervisats.
argument-hint: "[ämne/tema, t.ex. 'franska revolutionen i Hi Nivå 1b' - valfritt]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - AskUserQuestion
---

# Reflektera över ett genomfört moment (F3)

Detta kommando stänger återkopplingsslingan i Momentplaneringsramverket. `/planera-moment` bygger momentet och kursminnet fångar lärarens **planeringspreferenser**. Detta kommando fångar något annat och starkare: **vad som faktiskt hände när momentet undervisades** - höll den drivande frågan, nådde rollerna sina exit, satt förutsättningarna, visade sig lärarens overrides vara rätt eller fel i klassrummet.

Utfallsdata är ett starkare signalvärde än preferenser eftersom det är validerat mot verkligheten. Det matas in i kursminnet och försörjer därmed M-i:s defaults nästa gång ett liknande moment planeras (se steg 1.5 i `planera-moment`).

Kör detta kommando **efter** att momentet undervisats.

## Genomförande

Läs och följ hela protokollet i:
`${CLAUDE_PLUGIN_ROOT}/skills/planera-moment/references/reflektera-moment.md`

Kort översikt (fullständig vägledning i referensfilen):

1. **Lokalisera momentet** - från `$ARGUMENTS` eller lista befintliga `output/lessons/*/*/momentplan.md`. Läs momentplanen: drivande fråga, momenttyp, rollsekvens, brottningsform, förutsättningar (nivå 3), lärandemål och Override-räknare.
2. **Utfallsintervju** - strukturerad kring ramverkets egna begrepp (bärighet, roll-exit, form, förutsättningsverifikation, diskursmål, override-utfall, differentiering, elevaktiv tid). Utgå från momentets faktiska val - fråga inte generiskt.
3. **Skriv till kursminnet** under sektionen `## Utfall (från genomförda moment)` (håll den skild från preferenssektionerna) + uppdatera Historik-tabellen.
4. **Skriv till momentplan.md** en `## Utfall`-sektion - spårbart per moment (fullbordar M-iv).
5. **Bekräfta** kort vad som sparades och hur det påverkar framtida planering.

Skriv på **svenska** genom hela dialogen. Läraren äger tolkningen av vad som hände - du strukturerar och bokför.
