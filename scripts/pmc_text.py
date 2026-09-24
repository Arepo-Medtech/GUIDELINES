"""JATS XML (Europe PMC fullTextXML) -> plain text: tables removed, citation markers dropped, tags stripped BEFORE unescaping.

  python3 pmc_text.py in.xml out.txt            body text only (tables replaced by '[table omitted]')
  python3 pmc_text.py in.xml out.txt --tables   same body, then every CLEAN table appended row by row
  python3 pmc_text.py in.xml existing.txt --append-tables
                                                 leave an existing source file as it is (it may have a hand-added abstract)
                                                 and append the clean tables once; running it again changes nothing
  python3 pmc_text.py --selftest

--tables keeps the body byte-identical, so anchors made on the body still resolve. Each clean table row is written as one
self-describing line, "[Table 2 row 3] Drug: imatinib · Dose: 400 mg daily", so a claim can anchor to a single row with its
column headings. A table is CLEAN only if no cell spans rows or columns, and every body row has as many cells as the header;
anything else is listed as '[Table N not extracted: ...]' and stays an input_unavailable gap.
Known limit: an unlabelled table is named by its position ('Table 3'), which can repeat a real label; cite such rows by
their text, not the label. A table with no header row has its first data row read as headings; cite such rows by the cell
text. Both are left as they are so that existing anchors stay reproducible.
"""
import html, re, sys


def _txt(frag):
    frag = re.sub(r"<xref[^>]*ref-type=\"(?:bibr|ref)\"[^>]*>.*?</xref>", "", frag, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", " ", frag))
    return re.sub(r"\s+", " ", t).strip()


def jats_text(x):
    body = x[x.find("<body"):x.find("</body>")]
    body = re.sub(r"<table-wrap.*?</table-wrap>", "\n[table omitted]\n", body, flags=re.S)
    body = re.sub(r"<xref[^>]*ref-type=\"bibr\"[^>]*>.*?</xref>", "", body, flags=re.S)   # [12] citation markers
    body = re.sub(r"<sup>\s*</sup>", "", body)
    body = re.sub(r"<(p|title|sec|list-item|boxed-text)[^>]*>", "\n", body)
    t = html.unescape(re.sub(r"<[^>]+>", "", body))          # strip tags FIRST, then unescape (keeps '<0.001')
    t = re.sub(r"\s*,\s*(?=[,.;])", "", t)                    # leftover commas between removed citations
    t = re.sub(r"[ \t]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()


def jats_tables(x):
    """Clean tables as self-describing row lines; unclean ones named, not extracted."""
    out = []
    for n, tw in enumerate(re.findall(r"<table-wrap\b.*?</table-wrap>", x, flags=re.S), 1):
        label = _txt((re.findall(r"<label>(.*?)</label>", tw, flags=re.S) or [f"Table {n}"])[0]) or f"Table {n}"
        cap = _txt((re.findall(r"<caption>(.*?)</caption>", tw, flags=re.S) or [""])[0])
        tab = (re.findall(r"<table\b.*?</table>", tw, flags=re.S) or [""])[0]
        if not tab:
            out.append(f"[{label} not extracted: no table markup (image only)]"); continue
        if re.search(r"(?:row|col)span=\"(?!1\")\d+\"", tab):
            out.append(f"[{label} not extracted: merged cells]"); continue
        rows = [[_txt(c) for c in re.findall(r"<t[hd]\b[^>]*>(.*?)</t[hd]>", tr, flags=re.S)]
                for tr in re.findall(r"<tr\b.*?</tr>", tab, flags=re.S)]
        rows = [r for r in rows if any(r)]
        head_block = re.findall(r"<thead\b.*?</thead>", tab, flags=re.S)
        nhead = len(re.findall(r"<tr\b", head_block[0])) if head_block else 1
        if not rows or nhead != 1 or len(rows) < 2:
            out.append(f"[{label} not extracted: {'multi-row header' if nhead > 1 else 'no header row'}]"); continue
        head, body = rows[0], rows[1:]
        if any(len(r) != len(head) for r in body):
            out.append(f"[{label} not extracted: ragged rows]"); continue
        out.append(f"[{label}] {cap}".rstrip())
        for i, r in enumerate(body, 1):
            out.append(f"[{label} row {i}] " + " · ".join(f"{h}: {c}" if h else c for h, c in zip(head, r) if c))
        for foot in re.findall(r"<table-wrap-foot\b[^>]*>(.*?)</table-wrap-foot>", tw, flags=re.S):
            if _txt(foot):
                out.append(f"[{label} footnote] {_txt(foot)}")
    return "\n".join(out)


def selftest():
    x = ("<article><body><p>Start imatinib.</p><table-wrap><label>Table 1</label><caption><p>Doses</p></caption><table>"
         "<thead><tr><th>Drug</th><th>Dose</th></tr></thead><tbody><tr><td>Imatinib</td><td>400 mg daily</td></tr>"
         "<tr><td>Dasatinib</td><td>100 mg &lt;daily&gt;</td></tr></tbody></table><table-wrap-foot><p>Adults only.</p>"
         "</table-wrap-foot></table-wrap><table-wrap><label>Table 2</label><table><tr><th colspan=\"2\">X</th></tr>"
         "<tr><td>a</td><td>b</td></tr></table></table-wrap></body></article>")
    assert jats_text(x) == "Start imatinib.\n[table omitted]\n[table omitted]"
    t = jats_tables(x).splitlines()
    assert t[0] == "[Table 1] Doses" and t[1] == "[Table 1 row 1] Drug: Imatinib · Dose: 400 mg daily", t
    assert t[2] == "[Table 1 row 2] Drug: Dasatinib · Dose: 100 mg <daily>" and t[3] == "[Table 1 footnote] Adults only.", t
    assert t[4] == "[Table 2 not extracted: merged cells]", t
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest(); raise SystemExit(0)
    src, out = sys.argv[1:3]
    xml = open(src).read()
    MARK = "\n\n[TABLES — extracted by pmc_text.py --tables]\n"
    if "--append-tables" in sys.argv:
        cur = open(out).read()
        tabs = jats_tables(xml)
        if MARK in cur or not tabs:
            print("unchanged:", "tables already appended" if MARK in cur else "no tables"); raise SystemExit(0)
        open(out, "w").write(cur + MARK + tabs)
        print(tabs.count(" row 1]"), "clean tables appended;", tabs.count("not extracted"), "not extracted"); raise SystemExit(0)
    t = jats_text(xml)
    if "--tables" in sys.argv:
        tabs = jats_tables(xml)
        if tabs:
            t += MARK + tabs
    open(out, "w").write(t)
    print(len(t), "chars", t.count("[table omitted]"), "tables in body,", t.count(" row 1]"), "extracted")
