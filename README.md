# GUIDELINES

Verified Australian treatment guidelines: 404 guidelines and 11,326 claims, with every claim tied to a retrieved source.

**Copied from** [`Arepo-Medtech/au-medicines-compendium`](https://github.com/Arepo-Medtech/au-medicines-compendium) at `master` `36bc939`
(2026-09-23), **with full history** for every file here (187 commits, filtered to these paths). The compendium still holds its copy
until the move is finished.

**Wave 1 (21 guidelines) added 2026-09-23** from the compendium branch `no-guideline-agenda`: guidelines for PBS conditions that
had none (rheumatology, respiratory, blood cancers, endocrine, neuro, eye, schizophrenia). History is carried as 7 path-limited commits.

## What is here

| path | contents |
|---|---|
| `guidelines/` | one `<slug>.md` per guideline: the guideline itself |
| `verification/` | one `<slug>.verification.json` per guideline: every claim, its verdict and its source (split from `guidelines/` on 2026-09-25 so each folder stays under GitHub's 1,000-file listing limit) |
| `scripts/verify.py` | structural checks; with `--source`, re-checks quotes verbatim, and hash anchors for paraphrased claims |
| `scripts/anchor.py`, `scripts/test_anchor_verify.py` | hash anchors: paraphrased claims stay machine re-checkable without storing the source's words |
| `scripts/number_guard.py` | flags any number in a claim that its own quote does not contain |
| `scripts/attestation.py`, `scripts/dose_queue.py`, `docs/attestation-*.md` | the clinician attestation loop for doses taken from licensed sources |
| `scripts/corpus_stats.py` | corpus totals |
| `docs/` | source decisions (Cancer Council, the STI duplication, the AMH index), audits, and `guideline-status.md` |

## Check it

```bash
python3 scripts/verify.py verification/*.verification.json
python3 scripts/corpus_stats.py
```

## Claim verdicts
- `pass`: quoted verbatim from the source, and machine re-checkable against it.
- `pass_paraphrase_anchored`: paraphrase of a source that can be read but not reproduced. Backed by hash anchors, it is re-checked by
  `verify.py --source` (anchor found, numbers match, no copying of 8+ words).
- `licensed_source_not_quoted`: read in a licensed source (AMH) and paraphrased. Doses go to the attestation queue.
- `pass_image_transcription`: read from a diagram by eye.
- `not_asserted`, `searched_not_found`, and the others: see `scripts/verify.py`.

⚠️ `verifier_class: single_verifier_uncalibrated`. Written and checked by one model, with no clinician review. Source licences vary.
The open questions (RCH clause 5.2, Commonwealth commercial-use terms, NC sources) are recorded in the compendium's
`docs/no-guideline-action-agenda.md`.
