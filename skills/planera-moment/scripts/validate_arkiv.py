#!/usr/bin/env python3
"""Mekanisk validering av en Arkiv v2.1-presentation (reveal.js HTML).

Kontrollerar de saker som kan avgoras rent mekaniskt - designtokens, struktur,
emojis, typsnitt. De icke-mekaniska punkterna (frageformulering, pedagogisk
progression, talarnoternas kvalitet) maste fortfarande granskas for hand enligt
checklistan i references/presentationer-notebooklm.md.

Anvandning:
    python validate_arkiv.py <presentation.html>

Windows: satt PYTHONUTF8=1 sa svenska tecken lases ratt.

Exit 0 om alla hardkontroller passerar (VARNING tillats), annars exit 1.
"""

import re
import sys


# Kodpunkter som ar TILLATNA typografiska tecken i Arkiv (inte emojis):
#   § U+00A7, · U+00B7, — U+2014, ▸ U+25B8, ● U+25CF, ▪ U+25AA, № U+2116, " " citattecken
# Emoji-detektion: astrala tecken (> U+FFFF) samt kanda emoji-block i BMP,
# medvetet UTAN U+2500-U+25FF (geometriska former: ▸ ● ▪) och vanliga skiljetecken.
_EMOJI_RANGES = [
    (0x1F000, 0x1FAFF),   # emoji-block (astral)
    (0x2600, 0x26FF),     # Miscellaneous Symbols
    (0x2700, 0x27BF),     # Dingbats
    (0x2B00, 0x2BFF),     # Miscellaneous Symbols and Arrows
    (0x1F1E6, 0x1F1FF),   # Regional indicators
    (0xFE00, 0xFE0F),     # Variation selectors (emoji-presentation)
    (0x200D, 0x200D),     # Zero-width joiner (emoji-sekvenser)
]


def _is_emoji(cp: int) -> bool:
    return any(lo <= cp <= hi for lo, hi in _EMOJI_RANGES)


def main(argv):
    if len(argv) != 2:
        print("Anvandning: python validate_arkiv.py <presentation.html>")
        return 2

    path = argv[1]
    try:
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
    except OSError as exc:
        print(f"FAIL  Kunde inte lasa filen: {exc}")
        return 1

    results = []  # (status, text)   status in {"PASS", "FAIL", "VARNING"}

    # 1. Papperston
    if "#F4EDE1" in html.upper():
        results.append(("PASS", "Papperston #F4EDE1 forekommer"))
    else:
        results.append(("FAIL", "Papperston #F4EDE1 saknas (--paper-tokenen)"))

    # 2. De tre typsnitten
    for font in ("Cormorant Garamond", "Inter Tight", "JetBrains Mono"):
        if font in html:
            results.append(("PASS", f"Typsnitt refereras: {font}"))
        else:
            results.append(("FAIL", f"Typsnitt saknas: {font}"))

    # 3. Struktur: talarnoter pa varje slide (<section> == <aside class="notes">)
    n_sections = len(re.findall(r"<section\b", html, re.IGNORECASE))
    n_notes = len(re.findall(r'<aside\s+class="notes"', html, re.IGNORECASE))
    if n_sections == 0:
        results.append(("FAIL", "Inga <section>-slides hittades"))
    elif n_sections == n_notes:
        results.append(("PASS", f"Talarnoter pa varje slide ({n_notes}/{n_sections})"))
    else:
        results.append(("FAIL", f"Talarnoter saknas pa nagon slide (<aside class=\"notes\">: {n_notes}, <section>: {n_sections})"))

    # 4. Chrome-tackning (masthead). Cover, callout och content-highlight har
    #    egen ram utan .masthead, sa detta ar en VARNING, inte ett FAIL.
    n_masthead = len(re.findall(r'class="masthead"', html, re.IGNORECASE))
    if n_masthead == 0 and n_sections > 0:
        results.append(("VARNING", "Ingen .masthead alls - kontrollera att standardslides har chrome-ram"))
    else:
        results.append(("PASS", f"Masthead-ram forekommer ({n_masthead} st; cover/callout/content-highlight saknar den avsiktligt)"))

    # 5. Inga emojis
    emojis = sorted({ch for ch in html if _is_emoji(ord(ch))})
    if emojis:
        joined = " ".join(f"U+{ord(ch):04X}" for ch in emojis)
        results.append(("FAIL", f"Emoji(s) hittade: {joined} - anvand typografiska tecken (▸ ● ▪ § №)"))
    else:
        results.append(("PASS", "Inga emojis"))

    # 6. Heuristik (VARNING): slide-sektion med fler an 3 <li> pa toppniva.
    #    Rakna <li> per <section>-block.
    section_blocks = re.split(r"(?=<section\b)", html, flags=re.IGNORECASE)
    overfull = 0
    for block in section_blocks:
        if not re.match(r"\s*<section\b", block, re.IGNORECASE):
            continue
        n_li = len(re.findall(r"<li\b", block, re.IGNORECASE))
        if n_li > 3:
            overfull += 1
    if overfull:
        results.append(("VARNING", f"{overfull} slide(s) har fler an 3 <li> - kontrollera regeln 'max 3 nyckelpunkter'"))
    else:
        results.append(("PASS", "Ingen slide overskrider 3 <li> (max 3 nyckelpunkter)"))

    # Utskrift
    print(f"Arkiv-validering: {path}\n")
    for status, text in results:
        print(f"  {status:<8}{text}")

    has_fail = any(status == "FAIL" for status, _ in results)
    n_warn = sum(1 for status, _ in results if status == "VARNING")
    print()
    if has_fail:
        print("Resultat: FAIL - atgarda punkterna ovan.")
        return 1
    if n_warn:
        print(f"Resultat: PASS med {n_warn} varning(ar) - granska dem manuellt.")
    else:
        print("Resultat: PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
