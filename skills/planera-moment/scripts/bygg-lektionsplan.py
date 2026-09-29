#!/usr/bin/env python
"""Bygg lärarens lektionsplan som HTML ur lektion-N.md.

Markdownen är sanningskällan. HTML:en är en läsvy för klassrummet och
redigeras aldrig - ändra i markdownen och kör om scriptet.

Konventioner i markdown som scriptet förstår (se references/lektionsplan-html.md):

    frontmatter      lektion, titel, kurs, moment, grupper, langd, elevaktiv
    > text           första blockcitatet före första H2 blir lektionens kärna
    ## Före lektionen / ## Efter lektionen   checklistor med "- [ ]"
    ## Genom hela lektionen                  repliker och regler som gäller hela passet
    ## Förlopp       text före första H3 blir en "om tiden inte räcker"-ruta
    ### 0-4 · Titel  ett tidsblock; tiderna styr tidslinjen och klockan
    #### Rubrik      fördjupning inom ett tidsblock, hopfälld
    ## Bakgrund      hopfälld; allt om varför (roll, mål, overrides, källor)
    Säg: "..."       ordagrann replik, valfritt följd av " - not"
    Eleverna: ...    vad eleverna gör i blocket

Inline: **fet**, *kursiv*, `kod`, [[wikilänk]].

Användning:
    python bygg-lektionsplan.py <lektion-N.md> [--ut <fil.html>]
"""
from __future__ import annotations

import html as htmlmod
import re
import sys
from pathlib import Path


def die(msg: str) -> None:
    print(f"FEL: {msg}", file=sys.stderr)
    sys.exit(2)


# ------------------------------------------------------------------ parsning

def frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm = {}
    for line in parts[1].splitlines():
        m = re.match(r"^\s*([\w_]+)\s*:\s*(.*?)\s*$", line)
        if m:
            fm[m.group(1).lower()] = m.group(2).strip().strip('"\'')
    return fm, parts[2]


def dela(text: str, niva: int) -> tuple[str, list[tuple[str, str]]]:
    """Dela på rubriker av given nivå. Returnerar (text före första, [(rubrik, innehåll)])."""
    mönster = re.compile(r"^" + "#" * niva + r"\s+(?!#)(.+?)\s*$")
    före, delar, rubrik, buf = [], [], None, []
    for line in text.splitlines():
        m = mönster.match(line)
        if m:
            if rubrik is None:
                före = buf
            else:
                delar.append((rubrik, "\n".join(buf).strip()))
            rubrik, buf = m.group(1).strip(), []
        else:
            buf.append(line)
    if rubrik is None:
        före = buf
    else:
        delar.append((rubrik, "\n".join(buf).strip()))
    return "\n".join(före).strip(), delar


# ------------------------------------------------------------------ inline

def inline(s: str) -> str:
    s = htmlmod.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]",
               lambda m: f'<span class="wiki">{m.group(2) or m.group(1)}</span>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\*\w])\*([^*\n]+?)\*(?![\*\w])", r"<em>\1</em>", s)
    return s


# ------------------------------------------------------------------ block

LISTRAD = re.compile(r"^(\s*)(-|\d+\.)\s+(\[[ xX]\]\s+)?(.*)$")


def lista(rader: list[str], nyckel: str) -> str:
    """Rendera en lista. Checkboxar blir avbockningsbara och minns per läsare."""
    poster: list[tuple[str, bool, str]] = []   # (typ, check, text)
    for r in rader:
        m = LISTRAD.match(r)
        if m:
            typ = "ol" if m.group(2)[0].isdigit() else "ul"
            poster.append((typ, bool(m.group(3)), m.group(4).strip()))
        elif poster:
            t, c, txt = poster[-1]
            poster[-1] = (t, c, txt + " " + r.strip())
    if not poster:
        return ""
    tagg = poster[0][0]
    ut = []
    for i, (_, check, txt) in enumerate(poster):
        kropp = inline(txt)
        if check:
            ut.append(f'<li class="check"><label><input type="checkbox" '
                      f'data-nyckel="{nyckel}-{i}"><span>{kropp}</span></label></li>')
        else:
            klass = ' class="ratt"' if kropp.startswith("<strong>Rätt") else ""
            ut.append(f"<li{klass}>{kropp}</li>")
    klass = ' class="checklista"' if any(c for _, c, _ in poster) else ""
    return f"<{tagg}{klass}>" + "".join(ut) + f"</{tagg}>"


SAG = re.compile(r'^Säg:\s*["“”](.+?)["“”]\s*(?:[-–]\s*(.*))?$', re.S)


def block(text: str, nyckel: str = "x") -> str:
    ut = []
    for i, stycke in enumerate(re.split(r"\n\s*\n", text.strip())):
        stycke = stycke.strip()
        if not stycke:
            continue
        rader = stycke.splitlines()
        if LISTRAD.match(rader[0]):
            ut.append(lista(rader, f"{nyckel}-{i}"))
            continue
        # Rader som var för sig börjar med fetstil ("**Roll:** ...") är egna
        # uppgifter, inte ett stycke som råkat brytas - håll isär dem.
        if len(rader) > 1 and all(r.strip().startswith("**") for r in rader):
            ut.extend(f"<p>{inline(r.strip())}</p>" for r in rader)
            continue
        platt = " ".join(r.strip() for r in rader)
        if platt.startswith(">"):
            citat = re.sub(r"^>\s*", "", platt).replace(" > ", " ")
            ut.append(f'<p class="karna">{inline(citat)}</p>')
        elif platt.startswith("Säg:"):
            m = SAG.match(platt)
            if m:
                not_ = f'<span class="sagnot">{inline(m.group(2))}</span>' if m.group(2) else ""
                ut.append(f'<blockquote class="sag"><span class="etikett">Säg</span>'
                          f'<p>{inline(m.group(1))}</p>{not_}</blockquote>')
            else:
                ut.append(f'<blockquote class="sag"><span class="etikett">Säg</span>'
                          f'<p>{inline(platt[4:].strip())}</p></blockquote>')
        elif platt.startswith("Eleverna:"):
            ut.append(f'<p class="elever"><span class="etikett">Eleverna</span>'
                      f'{inline(platt[9:].strip())}</p>')
        else:
            ut.append(f"<p>{inline(platt)}</p>")
    return "\n".join(ut)


# ------------------------------------------------------------------ montering

TIDSBLOCK = re.compile(r"^(\d+)\s*[-–]\s*(\d+)\s*(?:min)?\s*[·|:]\s*(.+)$")


def bygg(md_path: Path) -> str:
    fm, body = frontmatter(md_path.read_text(encoding="utf-8"))
    före_h2, sektioner = dela(body, 2)

    h1 = re.search(r"^#\s+(.+)$", före_h2, re.M)
    titel = fm.get("titel") or (h1.group(1).split(":", 1)[-1].strip() if h1 else md_path.stem)
    lektion = fm.get("lektion", "")
    def tal(v: str) -> int:        # "70", "70 min" och "ca 53" ska alla gå
        m = re.search(r"\d+", v or "")
        return int(m.group()) if m else 0

    langd = tal(fm.get("langd", ""))
    elevaktiv = tal(fm.get("elevaktiv", ""))
    karna_m = re.search(r"^>\s*(.+(?:\n>.*)*)", före_h2, re.M)
    karna = re.sub(r"\n>\s*", " ", karna_m.group(1)).strip() if karna_m else ""

    sek = {r.lower(): (r, t) for r, t in sektioner}
    använda: set[str] = set()

    def ta(namn: str) -> tuple[str, str] | None:
        for k, v in sek.items():
            if k.startswith(namn):
                använda.add(k)
                return v
        return None

    # --- förloppet
    förlopp_html, remsa_html, block_data = "", "", []
    f = ta("förlopp")
    if f:
        intro, delar = dela(f[1], 3)
        if intro:
            förlopp_html += f'<div class="ruta obs">{block(intro, "intro")}</div>'
        for n, (rubrik, innehåll) in enumerate(delar):
            m = TIDSBLOCK.match(rubrik)
            start, slut, namn = (int(m.group(1)), int(m.group(2)), m.group(3)) if m else (0, 0, rubrik)
            block_data.append((start, slut, namn))
            huvud, fördjup = dela(innehåll, 4)
            detaljer = "".join(
                f'<details class="fordjup"><summary>{inline(r)}</summary>{block(t, f"m{n}-{j}")}</details>'
                for j, (r, t) in enumerate(fördjup))
            längd = f'<span class="langd">{slut - start} min</span>' if m else ""
            förlopp_html += (
                f'<section class="moment" id="m{n}" data-start="{start}" data-slut="{slut}">'
                f'<header><span class="tid">{start}-{slut}</span>'
                f'<h3>{inline(namn)}</h3>{längd}<span class="nu-etikett">Nu</span></header>'
                f'{block(huvud, f"m{n}")}{detaljer}</section>')
        total = max((s for _, s, _ in block_data), default=langd) or 1
        for n, (start, slut, namn) in enumerate(block_data):
            bredd = (slut - start) / total * 100
            kort = namn.split(":")[0]
            remsa_html += (f'<a class="seg" href="#m{n}" data-n="{n}" style="flex:{bredd:.2f}" '
                           f'title="{htmlmod.escape(namn)}"><span class="segtid">{start}</span>'
                           f'<span class="segnamn">{htmlmod.escape(kort)}</span></a>')

    def sektion(namn: str, klass: str = "", oppen: bool = True, rubrik: str | None = None) -> str:
        s = ta(namn)
        if not s:
            return ""
        r, t = s
        intro, under = dela(t, 3)
        kropp = block(intro, namn[:6])
        kropp += "".join(f'<h4>{inline(ur)}</h4>{block(ut_, f"{namn[:6]}{j}")}'
                         for j, (ur, ut_) in enumerate(under))
        return (f'<details class="sektion {klass}"{" open" if oppen else ""}>'
                f'<summary><h2>{inline(rubrik or r)}</h2></summary>'
                f'<div class="sektionskropp">{kropp}</div></details>')

    fore = sektion("före lektionen", "checkavsnitt")
    genom = ta("genom hela lektionen")
    genom_html = (f'<div class="ruta genom"><h3 class="rubrik">Genom hela lektionen</h3>'
                  f'{block(genom[1], "genom")}</div>') if genom else ""
    exit_ = sektion("exit ticket", "exit")
    efter = sektion("efter lektionen", "checkavsnitt")
    diff = sektion("differentiering", oppen=False)
    material = sektion("material", oppen=False)
    bakgrund = sektion("bakgrund", "bakgrund", oppen=False, rubrik="Bakgrund och motiveringar")
    ta("förlopp")
    övriga = "".join(sektion(k, oppen=False) for k in list(sek) if k not in använda)

    procent = round(elevaktiv / langd * 100) if langd and elevaktiv else 0
    meta = []
    if langd:
        meta.append(f"{langd} min")
    if fm.get("grupper"):
        meta.append(htmlmod.escape(fm["grupper"]))
    elevaktiv_html = (
        f'<div class="elevaktiv" title="Elevaktiv tid"><span>Elevaktiv tid {elevaktiv} av {langd} min</span>'
        f'<span class="stapel"><span style="width:{procent}%"></span></span><b>{procent} %</b></div>'
    ) if procent else ""

    nyckel = re.sub(r"\W+", "-", f"{fm.get('moment', '')}-{lektion}").strip("-").lower()

    return f"""<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>L{htmlmod.escape(lektion)} {htmlmod.escape(titel)} - lektionsplan</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Inter+Tight:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet" />
<style>
{CSS}
</style>
<script>
(function(){{try{{var t=localStorage.getItem('lektionsplan-tema');
if(t==='ljus'||t==='mork')document.documentElement.setAttribute('data-tema',t);}}catch(e){{}}}})();
</script>
</head>
<body data-nyckel="{nyckel}" data-langd="{langd}">

<header class="omslag">
  <div class="rad">
    <span class="etikett">{htmlmod.escape(fm.get('kurs', ''))}</span>
    <span class="etikett">{htmlmod.escape(fm.get('moment', ''))}</span>
    <span class="etikett">Lektion {htmlmod.escape(lektion)}</span>
  </div>
  <h1>{inline(titel)}</h1>
  {f'<p class="karna">{inline(karna)}</p>' if karna else ''}
  <div class="meta"><span>{' · '.join(meta)}</span>{elevaktiv_html}</div>
</header>

<nav class="klocka" aria-label="Lektionens tidslinje">
  <div class="remsa">{remsa_html}<span class="nal" hidden></span></div>
  <div class="kontroller">
    <span class="tidvisning" aria-live="polite">Klockan står still</span>
    <button type="button" id="btn-start">Starta</button>
    <button type="button" id="btn-nu" hidden>Gå till nu</button>
    <button type="button" id="btn-noll" hidden>Nollställ</button>
    <button type="button" id="btn-tema" class="tema"><span class="tema-mork">Mörkt</span><span class="tema-ljus">Ljust</span></button>
  </div>
</nav>

<main>
{fore}
{genom_html}
<section class="forlopp" aria-label="Förlopp">
{förlopp_html}
</section>
{exit_}
{efter}
{diff}
{material}
{övriga}
{bakgrund}
</main>

<footer>Genererad ur {htmlmod.escape(md_path.name)}. Ändra i markdownen och bygg om - inte här.</footer>

<script>
{JS}
</script>
</body>
</html>
"""


CSS = r"""
:root{
  color-scheme:light;
  --papper:#F4EDE1; --papper2:#EBE1CF; --black:#1F1A15; --black2:#4A3F33;
  --linje:#2A221A; --bordeaux:#7A2E2E; --marin:#2C3E55; --oliv:#5A6A3A;
  --ocker:#B8862F; --harfin:rgba(42,34,26,.14); --nu:rgba(184,134,47,.16);
  --m-papper:#191512; --m-papper2:#231E18; --m-black:#EFE6D8; --m-black2:#B6A895;
  --m-linje:#7A6B5C; --m-bordeaux:#E2907E; --m-marin:#89A8CB; --m-oliv:#A3B872;
  --m-ocker:#D8A94D; --m-harfin:rgba(239,230,216,.14); --m-nu:rgba(216,169,77,.14);
  --serif:'Cormorant Garamond',Georgia,serif;
  --sans:'Inter Tight',system-ui,-apple-system,'Segoe UI',sans-serif;
  --mono:'JetBrains Mono',ui-monospace,Menlo,monospace;
  --matt:780px; --kant:28px;
}
@media (prefers-color-scheme:dark){
  :root:not([data-tema]){color-scheme:dark;
    --papper:var(--m-papper); --papper2:var(--m-papper2); --black:var(--m-black); --black2:var(--m-black2);
    --linje:var(--m-linje); --bordeaux:var(--m-bordeaux); --marin:var(--m-marin); --oliv:var(--m-oliv);
    --ocker:var(--m-ocker); --harfin:var(--m-harfin); --nu:var(--m-nu)}
}
:root[data-tema="mork"]{color-scheme:dark;
  --papper:var(--m-papper); --papper2:var(--m-papper2); --black:var(--m-black); --black2:var(--m-black2);
  --linje:var(--m-linje); --bordeaux:var(--m-bordeaux); --marin:var(--m-marin); --oliv:var(--m-oliv);
  --ocker:var(--m-ocker); --harfin:var(--m-harfin); --nu:var(--m-nu)}
*{box-sizing:border-box}
html{scroll-padding-top:120px}
body{margin:0; background:var(--papper); color:var(--black); font-family:var(--sans);
  font-size:18px; line-height:1.6}
.omslag,main,footer,.klocka>*{max-width:var(--matt); margin-left:auto; margin-right:auto}
.omslag,main,footer{padding:0 var(--kant)}
.etikett{font-family:var(--mono); font-size:11.5px; font-weight:600; letter-spacing:.14em;
  text-transform:uppercase; color:var(--black2)}
code{font-family:var(--mono); font-size:.82em; background:var(--harfin); padding:1px 5px}
.wiki{border-bottom:1px dotted var(--black2)}
strong{font-weight:600}

/* omslag */
.omslag{padding-top:40px}
.omslag .rad{display:flex; gap:16px; flex-wrap:wrap; border-bottom:1.5px solid var(--linje); padding-bottom:12px}
.omslag .rad span+span::before{content:"▸ "; color:var(--bordeaux)}
h1{font-family:var(--serif); font-weight:600; color:var(--bordeaux); font-size:clamp(2.1rem,5.5vw,3.3rem);
  line-height:1.05; margin:22px 0 0}
.omslag .karna{font-family:var(--serif); font-style:italic; font-size:1.35rem; line-height:1.42;
  color:var(--black2); margin:14px 0 0; max-width:48ch}
.meta{display:flex; flex-wrap:wrap; gap:10px 28px; align-items:center; margin:20px 0 0;
  font-family:var(--mono); font-size:12px; letter-spacing:.06em; color:var(--black2)}
.elevaktiv{display:flex; align-items:center; gap:10px}
.stapel{display:inline-block; width:110px; height:7px; background:var(--harfin)}
.stapel span{display:block; height:100%; background:var(--oliv)}

/* klocka och tidslinje */
.klocka{position:sticky; top:0; z-index:30; background:var(--papper); margin-top:26px;
  border-top:1.5px solid var(--linje); border-bottom:1.5px solid var(--linje); padding:10px var(--kant)}
.remsa{position:relative; display:flex; gap:3px; height:46px}
.seg{position:relative; min-width:0; display:flex; flex-direction:column; justify-content:space-between;
  padding:5px 7px; background:var(--papper2); border-top:3px solid var(--marin);
  color:var(--black); text-decoration:none; overflow:hidden}
.seg:hover{border-top-color:var(--bordeaux)}
.seg.aktiv{border-top-color:var(--ocker); background:var(--nu)}
.segtid{font-family:var(--mono); font-size:10.5px; color:var(--black2)}
.segnamn{font-size:12.5px; font-weight:600; white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
.nal{position:absolute; top:-4px; bottom:-4px; width:2px; background:var(--bordeaux); pointer-events:none}
.kontroller{display:flex; gap:10px; align-items:center; margin-top:9px; flex-wrap:wrap}
.tidvisning{font-family:var(--mono); font-size:12px; letter-spacing:.05em; color:var(--black2); margin-right:auto}
.kontroller button{font-family:var(--mono); font-size:11.5px; font-weight:600; letter-spacing:.1em;
  text-transform:uppercase; padding:6px 12px; border:1.5px solid var(--linje); background:transparent;
  color:var(--black); cursor:pointer}
.kontroller button:hover{background:var(--papper2)}
#btn-start.gar{background:var(--bordeaux); color:var(--papper); border-color:var(--bordeaux)}
button:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid var(--bordeaux); outline-offset:2px}
.tema-ljus{display:none}
@media (prefers-color-scheme:dark){:root:not([data-tema]) .tema-mork{display:none} :root:not([data-tema]) .tema-ljus{display:inline}}
:root[data-tema="mork"] .tema-mork{display:none} :root[data-tema="mork"] .tema-ljus{display:inline}

/* sektioner */
main{padding-top:10px; padding-bottom:60px}
details.sektion{margin-top:34px; border-top:1.5px solid var(--linje)}
details.sektion>summary{list-style:none; cursor:pointer; display:flex; align-items:baseline; gap:12px; padding-top:14px}
details.sektion>summary::-webkit-details-marker{display:none}
details.sektion>summary::after{content:"+"; font-family:var(--mono); color:var(--black2); margin-left:auto}
details.sektion[open]>summary::after{content:"–"}
h2{font-family:var(--serif); font-weight:600; font-size:1.75rem; margin:0; line-height:1.15}
.sektionskropp{padding-top:12px}
.sektionskropp h4{font-family:var(--mono); font-size:12px; letter-spacing:.14em; text-transform:uppercase;
  color:var(--marin); margin:24px 0 8px}
details.bakgrund .sektionskropp{font-size:16.5px; color:var(--black2)}
p{margin:0 0 12px}
ul,ol{margin:0 0 12px; padding-left:1.25em}
li{margin:0 0 7px}
li.ratt::marker{color:var(--oliv)}
li.ratt strong{color:var(--oliv)}

/* checklistor */
ul.checklista{list-style:none; padding:0}
li.check label{display:flex; gap:12px; align-items:flex-start; cursor:pointer; padding:6px 0;
  border-bottom:1px solid var(--harfin)}
li.check input{width:20px; height:20px; margin:4px 0 0; flex:none; accent-color:var(--oliv)}
li.check input:checked+span{opacity:.45; text-decoration:line-through; text-decoration-color:var(--black2)}

/* rutor */
.ruta{background:var(--papper2); border-left:5px solid var(--marin); padding:18px 22px; margin:28px 0 0}
.ruta p:last-child,.ruta ul:last-child{margin-bottom:0}
.ruta.obs{border-left-color:var(--ocker); margin:0 0 18px; font-size:16.5px}
.ruta.genom{border-left-color:var(--bordeaux)}
.rubrik{font-family:var(--mono); font-size:12px; font-weight:600; letter-spacing:.14em;
  text-transform:uppercase; color:var(--bordeaux); margin:0 0 10px}

/* förloppet */
.forlopp{margin-top:34px; border-top:1.5px solid var(--linje); padding-top:22px}
.moment{position:relative; padding:18px 0 14px 22px; margin:0 0 18px; border-left:3px solid var(--harfin)}
.moment>header{display:flex; align-items:baseline; gap:14px; margin:0 0 12px; flex-wrap:wrap}
.moment .tid{font-family:var(--mono); font-size:13px; font-weight:600; color:var(--marin); min-width:52px}
.moment h3{font-family:var(--serif); font-weight:600; font-size:1.55rem; line-height:1.15; margin:0}
.moment .langd{font-family:var(--mono); font-size:11px; color:var(--black2); letter-spacing:.06em}
.nu-etikett{display:none; font-family:var(--mono); font-size:11px; font-weight:600; letter-spacing:.14em;
  text-transform:uppercase; background:var(--ocker); color:var(--papper); padding:2px 8px}
.moment.nu{border-left-color:var(--ocker); background:linear-gradient(90deg,var(--nu),transparent 70%)}
.moment.nu .nu-etikett{display:inline-block}
.moment.passerad>*{opacity:.55}
.elever{font-size:17px; padding:8px 0 8px 0; border-bottom:1px solid var(--harfin); margin-bottom:14px}
.elever .etikett,.sag .etikett{display:inline-block; margin-right:10px; color:var(--oliv)}
.sag{margin:14px 0; padding:2px 0 2px 18px; border-left:3px solid var(--bordeaux)}
.sag .etikett{color:var(--bordeaux); display:block; margin-bottom:2px}
.sag p{font-family:var(--serif); font-style:italic; font-size:1.36rem; line-height:1.4; margin:0}
.sagnot{display:block; font-size:14.5px; color:var(--black2); margin-top:4px}
details.fordjup{margin:12px 0 0; border:1px solid var(--harfin); background:var(--papper2)}
details.fordjup>summary{cursor:pointer; padding:10px 14px; font-weight:600; font-size:16px}
details.fordjup>summary::marker{color:var(--marin)}
details.fordjup[open]>summary{border-bottom:1px solid var(--harfin)}
details.fordjup>:not(summary){margin-left:14px; margin-right:14px}
details.fordjup>:nth-child(2){margin-top:12px}
details.fordjup>:last-child{margin-bottom:14px}

footer{border-top:1.5px solid var(--linje); padding-top:16px; padding-bottom:50px;
  font-family:var(--mono); font-size:11.5px; color:var(--black2)}

@media (max-width:640px){
  :root{--kant:16px} body{font-size:17px}
  .segnamn{display:none} .remsa{height:30px}
  .moment{padding-left:14px}
  .sag p{font-size:1.22rem}
}
@media print{
  .klocka{display:none} details{display:block} details>summary::after{display:none}
  details:not([open])>*:not(summary){display:block}
  body{background:#fff; color:#000; font-size:11pt}
  .moment{break-inside:avoid-page}
}
"""


JS = r"""
(function(){
  var rot=document.documentElement, body=document.body;
  var nyckel='lektionsplan:'+body.dataset.nyckel;
  function las(k){try{return JSON.parse(localStorage.getItem(k));}catch(e){return null;}}
  function skriv(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}

  // Checklistor minns per läsare och lektion.
  var bockar=las(nyckel+':bockar')||{};
  document.querySelectorAll('input[data-nyckel]').forEach(function(cb){
    cb.checked=!!bockar[cb.dataset.nyckel];
    cb.addEventListener('change',function(){bockar[cb.dataset.nyckel]=cb.checked; skriv(nyckel+':bockar',bockar);});
  });

  // Tema.
  var bT=document.getElementById('btn-tema');
  function tema(){var v=rot.getAttribute('data-tema'); if(v) return v;
    return (window.matchMedia&&matchMedia('(prefers-color-scheme:dark)').matches)?'mork':'ljus';}
  bT.addEventListener('click',function(){var ny=tema()==='mork'?'ljus':'mork';
    rot.setAttribute('data-tema',ny); try{localStorage.setItem('lektionsplan-tema',ny);}catch(e){}});

  // Lektionsklockan. Tillståndet sparas, så att en omladdning mitt i passet
  // inte nollställer den.
  var moment=[].slice.call(document.querySelectorAll('.moment'));
  var segment=[].slice.call(document.querySelectorAll('.seg'));
  var remsa=document.querySelector('.remsa'), nal=document.querySelector('.nal');
  var visning=document.querySelector('.tidvisning');
  var bS=document.getElementById('btn-start'), bN=document.getElementById('btn-nu'), bR=document.getElementById('btn-noll');
  var total=moment.reduce(function(m,el){return Math.max(m,+el.dataset.slut);},0)||+body.dataset.langd||1;
  var k=las(nyckel+':klocka')||{samlat:0,sedan:null};

  function minuter(){return (k.samlat+(k.sedan?Date.now()-k.sedan:0))/60000;}
  function rita(){
    var min=minuter(), igang=k.sedan!==null, startad=igang||k.samlat>0;
    bS.textContent=igang?'Pausa':(startad?'Fortsätt':'Starta');
    bS.classList.toggle('gar',igang);
    bN.hidden=!startad; bR.hidden=!startad; nal.hidden=!startad;
    var aktiv=-1;
    moment.forEach(function(el,i){
      var s=+el.dataset.start, e=+el.dataset.slut;
      var nu=startad&&min>=s&&min<e; if(nu) aktiv=i;
      el.classList.toggle('nu',nu);
      el.classList.toggle('passerad',startad&&min>=e);
      if(segment[i]) segment[i].classList.toggle('aktiv',nu);
    });
    if(!startad){visning.textContent='Klockan står still'; return;}
    nal.style.left=Math.min(100,min/total*100)+'%';
    var hel=Math.floor(min);
    var kvar=aktiv>=0?Math.ceil(+moment[aktiv].dataset.slut-min):0;
    visning.textContent=hel+' av '+total+' min'+(aktiv>=0?' · '+kvar+' min kvar i blocket':(min>=total?' · lektionen slut':''))+(igang?'':' · pausad');
  }
  bS.addEventListener('click',function(){
    if(k.sedan!==null){k.samlat+=Date.now()-k.sedan; k.sedan=null;} else {k.sedan=Date.now();}
    skriv(nyckel+':klocka',k); rita();
  });
  bR.addEventListener('click',function(){k={samlat:0,sedan:null}; skriv(nyckel+':klocka',k); rita();});
  bN.addEventListener('click',function(){var el=document.querySelector('.moment.nu'); if(el) el.scrollIntoView({behavior:'smooth'});});
  rita(); setInterval(rita,10000);
})();
"""


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    argv = sys.argv[1:]
    args = [a for i, a in enumerate(argv) if not a.startswith("--") and (i == 0 or argv[i - 1] != "--ut")]
    if not args:
        die("Användning: bygg-lektionsplan.py <lektion-N.md> [--ut <fil.html>]")
    md = Path(args[0]).resolve()
    if not md.exists():
        die(f"hittar inte {md}")
    ut = Path(argv[argv.index("--ut") + 1]) if "--ut" in argv else md.with_suffix(".html")
    ut.write_text(bygg(md), encoding="utf-8", newline="\n")
    print(f"✓ {ut}")


if __name__ == "__main__":
    main()
