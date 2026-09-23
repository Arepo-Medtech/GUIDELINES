# Palliative care — medicines for terminal-phase symptoms at home

**Edition:** 1.0 · 2026-09-23 · **Status:** drafted and source-anchored; awaiting clinical attestation
**Scope:** the symptoms each medicine in the PBS Prescriber Bag is used for in the terminal phase of a life-limiting illness, anticipatory prescribing, and practical points for home visits (ordering, storage, subcutaneous use). The source gives no doses. Cancer pain: see `cancer-pain-adults`. PBS access for each drug is in `docs/no-guideline-pbs-listings.md`.

> ✅ **PARAPHRASED, HASH-ANCHORED.** 15 claims paraphrased from **CareSearch (including palliAGED), Flinders University; funded by the Department of Health, Disability and Ageing — *Medicines from the PBS Prescriber bag for terminal phase symptoms*** (© 2025 (PDF modified 3 June 2025; uploaded April 2026); origin: AU). **19 anchors re-checkable by machine; 5 doses.** The source's words are not reproduced: its licence is *© 2025 CareSearch. Site terms: 'We do not give permission for any use of the Information for commercial purposes. No Information authored by or on behalf of us may be copied, modified or reproduced in any way without our written permission.'*.

> ⚠️ **No doses here.** The source deliberately gives indications and product strengths only, and sends prescribers to the CareSearchgp or palliMEDS apps, Therapeutic Guidelines: Palliative Care, the Australian Medicines Handbook or a pharmacist for dosing.

> ℹ️ **Two different PBS routes.** The source is about the Prescriber Bag (doctor's emergency supply). The PBS condition below is the Palliative Care Schedule listing of clonazepam, haloperidol, hyoscine and metoclopramide for ordinary prescriptions. The clinical uses are the same; the supply route is not.

---

## Anticipatory prescribing

- **Plan ahead for a death at home.** Some people will want their care, and their death, to happen at home or in their residential aged care facility. The evidence supports prescribing all terminal-phase medicines in advance (anticipatory prescribing). The Prescriber Bag is a safety net for sudden, unexpected deterioration, not a replacement for advance planning. [S1]
- **Prescriber Bag medicines cost the prescriber nothing** and can be handed to the patient free on a home visit, for an emergency or to cover the gap until a prescription is filled. [S1]

## Which medicine for which symptom

- ⚠️ **Distressing breathlessness: morphine is first line** (it also treats pain). Avoid repeated morphine doses in serious kidney failure. [S1]
- **Clonazepam (2.5 mg/mL oral drops):** agitation, anxiety, distressing breathlessness, refractory distress and seizures. [S1]
- **Midazolam (5 mg/mL injection):** agitation, distressing breathlessness, refractory distress and seizures. [S1]
- **A benzodiazepine (clonazepam or midazolam) helps breathlessness when anxiety is part of it.** Either may also ease rigidity in end-stage Parkinson's disease once dopaminergic drugs have been stopped. [S1]
- **Haloperidol (5 mg/mL injection):** delirium, terminal restlessness, nausea and vomiting, anxiety and refractory distress. [S1]
- **Hyoscine butylbromide (20 mg/mL injection):** respiratory tract secretions and noisy breathing, and cramping pain from bowel obstruction. [S1]
- **Metoclopramide (10 mg/2 mL injection):** nausea and vomiting. [S1]
- **Hydrocortisone injection** can stand in for dexamethasone in acute severe breathlessness or spinal cord compression. [S1]
- **Adrenaline:** nebulised for airway obstruction (it may briefly relieve stridor with breathlessness), or topically for a small malignant bleed. [S1]
- **Furosemide injection** is for oedema from heart failure, and **naloxone** for reversing a life-threatening opioid overdose. [S1]

## Doses

- **For doses, use a palliative-care reference:** the CareSearchgp or palliMEDS apps, Therapeutic Guidelines: Palliative Care, or the Australian Medicines Handbook, or ask a local pharmacist. [S1]

## Practical points for home visits

- **Restock monthly:** order at the end of each month on a Prescriber Bag supply order form from Services Australia, signed and taken to a community pharmacy. [S1]
- **Store S8 drugs (especially opioids) securely under local law, carry subcutaneous equipment, keep each subcutaneous injection to 1.5 mL or less so it does not hurt, and record every dose given or discarded.** [S1]

---

## PBS listings (Australian access, schedule 4333)

Derived from PBS Public API data: counts of current restrictions, access type and listed drugs. The restriction criteria themselves are not reproduced (see `docs/no-guideline-action-agenda.md`, Decision 1).

| PBS condition | restrictions | authority / streamlined / restricted | drugs | PBS items |
|---|---:|---|---|---:|
| Use in patients receiving palliative care | 3 | 0 / 1 / 2 | Clonazepam, Metoclopramide, Haloperidol, Hyoscine | 8 |

---

## Unresolved

| # | Item | Class |
|---|---|---|
| 1 | **Doses** are not in the source by design; take them from Therapeutic Guidelines: Palliative Care or the Australian Medicines Handbook. | `input_unavailable` |
| 2 | **Which medicines are on the National Core Community Palliative Care Medicines List** is shown by shading in the source table, which does not survive text extraction. | `input_unavailable` |
| 3 | **Related PBS conditions not served by this source:** 'Terminal disease' (bromazepam, flunitrazepam), 'Terminal malignant neoplasia' (bisacodyl, enemas) and 'Chronic Breathlessness' (morphine for chronic, not terminal-phase, breathlessness). | `out_of_scope` |
| 4 | **Licence:** © CareSearch; the terms bar copying, modifying or reproducing without written permission. The claims are paraphrased and hash-anchored; the source's words are not reproduced. | `observation` |

## Sources

| id | Source | Licence | Treatment |
|---|---|---|---|
| **S1** | CareSearch (including palliAGED), Flinders University; funded by the Department of Health, Disability and Ageing. *Medicines from the PBS Prescriber bag for terminal phase symptoms*. © 2025 (PDF modified 3 June 2025; uploaded April 2026). https://www.caresearch.com.au/app/uploads/2026/04/PBS_Prescriber_Bag_Final_CS.pdf — retrieved 2026-09-23. | © 2025 CareSearch. Site terms: 'We do not give permission for any use of the Information for commercial purposes. No Information authored by or on behalf of us may be copied, modified or reproduced in any way without our written permission.' | **paraphrased, hash-anchored** |

⚠️ **`verifier_class: single_verifier_uncalibrated` — written and checked by one model, reviewed by nobody.**
