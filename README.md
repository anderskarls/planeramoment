# Momentplanering — Claude Code Plugin

Plugin för att planera undervisningsmoment och lektioner i gymnasiet. Sparar tid genom att guida dig genom planeringen steg för steg och bygga vidare på dina tidigare erfarenheter i Obsidian-vaultet.

## Kommandon

### `/planera-moment`

Planera ett helt undervisningsmoment med momentplan och lektionsplaneringar.

```
/planera-moment demokrati och politik i Sh1a1, 4 lektioner
```

Kommandot:
1. Läser dina reflektioner och tidigare planeringar
2. Ställer följdfrågor om det som saknas
3. Presenterar en skiss för godkännande
4. Skapar momentplan + separata lektionsplaneringar
5. Länkar allt med wikilinks

### `/planera-lektion`

Skapa en enskild lektionsplanering utan att planera ett helt moment.

```
/planera-lektion introduktion till politiska ideologier i Sh1a1
```

## Skill: planera-moment

Aktiveras automatiskt när du diskuterar undervisning, lektionsplanering eller pedagogik. Ger Claude kunskap om:

- Dina kurser (Sh1a1, Sh3, Internationella relationer, Hi1b)
- Vaultets struktur och filformat
- Betygsnivåer (E/C/A) och kunskapskrav
- Pedagogiska metoder och lektionsstruktur
- Differentiering

## Installation

Testa lokalt:

```bash
claude --plugin-dir /home/anders/momentplanering
```

## Kurser

| Kurs | Typ |
|------|-----|
| Samhällskunskap 1a1 | Yrkesförberedande |
| Samhällskunskap 3 | Fördjupning |
| Internationella relationer | Fördjupning |
| Historia 1b | Högskoleförberedande |
