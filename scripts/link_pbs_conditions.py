#!/usr/bin/env python3
"""Attach owner-approved PBS conditions to an existing guideline (reference/pbs_condition_links.json).

A link says a PBS condition with no guideline of its own is covered by an existing one. The script adds
(or refreshes) a "## PBS listings — linked conditions" section in the target guideline, rendered from
reference/no_guideline_pbs.json (derived data only: counts, access type, drug names; no restriction text).
Conditions already listed in the guideline's own generated PBS table are skipped. Idempotent.

  python3 scripts/link_pbs_conditions.py
  python3 scripts/link_pbs_conditions.py --selftest
"""
import json, re, sys

HEAD = "## PBS listings — linked conditions"
SECTION = re.compile(r"\n---\n\n" + re.escape(HEAD) + r".*?(?=\n---\n|\n## |\Z)", re.S)
ROW = re.compile(r"^\| ([^|]+?) \| \d+ \|", re.M)


def row(r):
    a = r["access"]
    drugs = ", ".join(r["drugs"][:8]) + (f" +{len(r['drugs']) - 8}" if len(r["drugs"]) > 8 else "")
    return (f"| {r['condition']} | {r['restrictions_current']} | {a.get('authority', 0)} / {a.get('streamlined', 0)} / "
            f"{a.get('restricted', 0)} | {drugs} | {len(r['pbs_codes'])} |")


def apply(md, conditions, rows, sched, decided):
    md = SECTION.sub("", md)
    listed = set(ROW.findall(md))
    todo = [c for c in conditions if c not in listed]
    if not todo:
        return md
    sec = ["", "---", "", f"{HEAD} (schedule {sched})", "",
           f"These PBS conditions have no guideline of their own; the owner linked them to this one on {decided}. "
           "Derived from PBS Public API data; the restriction criteria themselves are not reproduced.", "",
           "| PBS condition | restrictions | authority / streamlined / restricted | drugs | PBS items |",
           "|---|---:|---|---|---:|"] + [row(rows[c]) for c in todo]
    at = md.find("\n---\n\n## Unresolved")
    if at < 0:
        at = md.find("\n## Unresolved")
    if at < 0:
        at = md.find("\n## Sources")
    return (md.rstrip("\n") + "\n" + "\n".join(sec) + "\n") if at < 0 else md[:at] + "\n".join(sec) + "\n" + md[at:]


def main():
    links = json.load(open("reference/pbs_condition_links.json"))
    d = json.load(open("reference/no_guideline_pbs.json"))
    rows = {r["condition"]: r for r in d["conditions"]}
    by_target = {}
    for l in links["approved"]:
        assert l["condition"] in rows, f"not a no-guideline PBS condition: {l['condition']!r}"
        by_target.setdefault(l["guideline"], []).append(l["condition"])
    for g, conds in sorted(by_target.items()):
        p = f"guidelines/{g}.md"
        md = open(p).read()
        new = apply(md, conds, rows, d["schedule_code"], links["decided"])
        if new != md:
            open(p, "w").write(new)
        print(f"  {g:45} {len(conds)} linked")


def selftest():
    rows = {"A": {"condition": "A", "restrictions_current": 2, "access": {"authority": 1}, "drugs": ["X"], "pbs_codes": ["1"]},
            "B": {"condition": "B", "restrictions_current": 1, "access": {}, "drugs": [], "pbs_codes": []}}
    md = "# T\n\n## Treat\n- x\n\n---\n\n## Unresolved\n\n| a |\n\n## Sources\n"
    once = apply(md, ["A"], rows, "4333", "2026-09-24")
    assert once.index(HEAD) < once.index("## Unresolved") and "| A | 2 | 1 / 0 / 0 | X | 1 |" in once
    assert apply(once, ["A"], rows, "4333", "2026-09-24") == once, "not idempotent"
    gen = "# T\n\n## PBS listings\n\n| A | 2 | 1 / 0 / 0 | X | 1 |\n"
    assert apply(gen, ["A"], rows, "4333", "2026-09-24") == gen, "should skip a condition already in the generated table"
    assert HEAD in apply("# T\n", ["B"], rows, "4333", "2026-09-24")
    print("selftest ok")


if __name__ == "__main__":
    selftest() if "--selftest" in sys.argv else main()
