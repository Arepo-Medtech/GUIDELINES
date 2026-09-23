# GUIDELINES

Verified Australian treatment guidelines: 383 guidelines and 10,876 claims, with every claim tied to a retrieved source.

**Copied from** [`Arepo-Medtech/au-medicines-compendium`](https://github.com/Arepo-Medtech/au-medicines-compendium) at `master` `36bc939`
(2026-09-23), **with full history** for every file here (187 commits, filtered to these paths). The compendium still holds its copy
until the move is finished.

## What is here

| path | contents |
|---|---|
| `guidelines/` | one `<slug>.md` (the guideline) and one `<slug>.verification.json` (every claim, its verdict and its source) per guideline |
| `scripts/verify.py` | structural checks; with `--source`, re-checks quotes verbatim, and hash anchors for paraphrased claims |
| `scripts/number_guard.py` | flags any number in a claim that its own quote does not contain |
| `scripts/attestation.py`, `scripts/dose_queue.py`, `docs/attestation-*.md` | the clinician attestation loop for doses taken from licensed sources |
| `scripts/corpus_stats.py` | corpus totals |
| `docs/` | source decisions (Cancer Council, the STI duplication, the AMH index), audits, and `guideline-status.md` |

## Check it

```bash
python3 scripts/verify.py guidelines/*.verification.json
python3 scripts/corpus_stats.py
```

## Claim verdicts
- `pass`: quoted verbatim from the source, and machine re-checkable against it.
- `licensed_source_not_quoted`: read in a licensed source (AMH) and paraphrased. Doses go to the attestation queue.
- `pass_image_transcription`: read from a diagram by eye.
- `not_asserted`, `searched_not_found`, and the others: see `scripts/verify.py`.

⚠️ `verifier_class: single_verifier_uncalibrated`. Written and checked by one model, with no clinician review. Source licences vary.
The open questions (RCH clause 5.2, Commonwealth commercial-use terms, NC sources) are recorded in the compendium's
`docs/no-guideline-action-agenda.md`.
