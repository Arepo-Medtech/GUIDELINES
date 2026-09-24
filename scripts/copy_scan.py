#!/usr/bin/env python3
"""Find text on a guideline page that copies a source it may only paraphrase.

Reports every run of MIN (default 8) or more consecutive words that the rendered page shares with the source
(case- and punctuation-insensitive, same tokeniser as scripts/anchor.py). Use it as the final gate for sources
licensed for personal use only (e.g. RCH): verify.py checks each claim against its own anchors, this checks the
whole page, including banners, tables and prose.

  python3 scripts/copy_scan.py guidelines/croup.md --source /path/to/rch-Croup.txt [--min 8] [--allow "<citation text>" ...]

Each line is scanned on its own, so a heading followed by a bullet never counts as one run. --allow removes a phrase
(e.g. the cited title or URL of the source) before scanning, because citing a source is not copying it.
  python3 scripts/copy_scan.py --selftest
"""
import re, sys

tok = lambda t: re.findall(r"[a-z0-9]+(?:\.[0-9]+)?", t.lower())


def runs(page, source, limit=8):
    """Maximal shared runs of >= limit words, as strings, in page order."""
    a, b = tok(page), tok(source)
    grams = {tuple(b[i:i + limit]) for i in range(len(b) - limit + 1)}
    out, i = [], 0
    while i <= len(a) - limit:
        if tuple(a[i:i + limit]) in grams:
            j = i + limit
            while j < len(a) and tuple(a[j - limit + 1:j + 1]) in grams:
                j += 1
            out.append(" ".join(a[i:j])); i = j
        else:
            i += 1
    return out


def selftest():
    src = "Most children will have a muscular torticollis and can be managed with simple analgesia."
    assert runs("Most kids: muscular torticollis; simple pain relief works.", src) == []
    r = runs("Note: most children will have a muscular torticollis and can be managed at home.", src)
    assert r == ["most children will have a muscular torticollis and can be managed"], r
    assert [r for l in "## Key points\n- cns respiratory".splitlines() for r in runs(l, "key points cns respiratory and cardiac effects are common in overdose", 4)] == []
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest(); raise SystemExit(0)
    lim = int(sys.argv[sys.argv.index("--min") + 1]) if "--min" in sys.argv else 8
    page = open(sys.argv[1]).read()
    src = open(sys.argv[sys.argv.index("--source") + 1]).read()
    for i, a in enumerate(sys.argv):
        if a == "--allow":
            page = page.replace(sys.argv[i + 1], " ")
    found = [r for line in page.splitlines() for r in runs(line, src, lim)]
    for r in found:
        print(f"  COPIES ({len(r.split())} words): {r[:140]}")
    print(f"{len(found)} copied run(s) of {lim}+ words")
    raise SystemExit(1 if found else 0)
