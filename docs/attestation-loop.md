# The attestation loop

**Before this, 621 dose claims sat in a queue that was printed to stdout and thrown away.**
There was nowhere to record a sign-off, nothing read one, and no number moved if you did the work.
`reference/attestations.json` held exactly one attestation and `verify.py` never looked at it.

## How it works now

**One file is the record: [`docs/attestation-queue.md`](attestation-queue.md).** You tick it in place.

| you write in the ✓ cell | means |
|---|---|
| *(empty)* | not yet attested |
| `KL 2026-09-23` | **CONFIRMED** against the subscription |
| `! KL 2026-09-23 AMH says 400 mg` | ⚠️ **REJECTED** — ***`verify.py` fails until the guideline is fixed*** |
| `~ owner 2026-09-24` | **OWNER-ACCEPTED, not individually checked** — the owner accepts the dose for use without having read it against the subscription. Counted separately and **never reported as confirmed**; overwrite with initials and date once checked |

There is deliberately **no second JSON to keep in sync**, because two copies drift.

## What makes it safe

Every row carries `ref` (`guideline#claim-index`) **and `sha`** — the first 8 hex of sha256 over the
claim text.

> ⚠️ **A tick is honoured only when the sha still matches.** If a claim is reworded after sign-off, the
> sha changes and the attestation is **not** carried onto text nobody read. The row returns to the queue.

That is the whole reason for the sha. A positional key alone would silently transfer a clinician's
sign-off onto different words the next time a build script renumbered a file.

## The four behaviours, all tested

| You do | What happens |
|---|---|
| **Confirm a row** | `verify.py` notes `N/M queued dose(s) ATTESTED`; `corpus_stats.py` reports `N of 621 ATTESTED` |
| **Reject a row** | ⚠️ `verify.py` **FAILS** that guideline, naming the attestor and reason. `corpus_stats.py` appends **"build is FAILING"** so the corpus line cannot read clean while a rejected dose stands |
| **Reword a claim, then regenerate** | Tick dropped, row returns to the queue, and the header reports **"N previously attested row(s) returned"** |
| **Reword a claim, don't regenerate** | `verify.py` refuses the sign-off: *"attested earlier, but the claim text has CHANGED since"* |

## Commands

```bash
python3 scripts/dose_queue.py            # rewrite the queue, preserving your ticks
python3 scripts/dose_queue.py --stdout   # print, change nothing
python3 scripts/verify.py guidelines/*.verification.json
python3 scripts/corpus_stats.py
python3 scripts/attestation.py           # self-check of the parser
```

**Run `dose_queue.py` after any change to the guidelines.** It is the step that returns reworded claims
to the queue.

## Owner acceptance (2026-09-24)

On 2026-09-24 the owner accepted all 621 queued doses for use **without** checking each against the AMH
subscription (`~ owner 2026-09-24` on every row). `verify.py` and `corpus_stats.py` report these as
**OWNER-ACCEPTED, not individually checked**, and keep the ATTESTED count at the number of doses a person has
actually read against the source. The sha rule applies to acceptance too: a reworded claim loses it.

## ⚠️ What this does NOT do

- **It does not attest anything.** 621 rows are outstanding and only a person can close them.
- **It does not review the prose.** All 145 guidelines still carry `verifier_class:
  single_verifier_uncalibrated` — one model wrote them and the same model checked them. **Dose
  attestation and guideline review are two different passes**; this closes the loop on the first only.
- **It does not check open-source doses.** The 177 quoted doses are machine re-checkable already and are
  correctly not in this queue.
