# After Wave 3: proposed links and evidence gaps

**As of 2026-09-23 (branch `wave-3`).** The corpus has 481 guidelines, and all 481 pass verification. Of the 393 true-gap rows in `reference/no_guideline_triage.json`, 156 now appear in a guideline's PBS listings table. That leaves **237**.

- **164** have a usable source recorded in `research/*.json`. They are Wave 4 candidates.
- **20** have a researched source that isn't usable (paywalled, login-only or bot-challenged).
- **53** have no source recorded. They are sorted below.

Nothing below has been applied. Each link needs the owner's confirmation before it becomes a binding.

## 1. Proposed links to an existing guideline (confirm or reject)

These rows most likely don't need a new guideline, only a link to one that already exists.

| PBS condition | Proposed guideline | Confidence |
|---|---|---|
| Major depressive disorders; Depression | `major-depressive-disorder` | high |
| Acute coronary syndrome | `acute-coronary-syndromes` | high |
| Urothelial carcinoma | `urothelial-carcinoma` | high |
| Gastro-oesophageal / oesophageal cancer | `gastric-and-gojunction-cancer` | high |
| Alcohol dependence | `alcohol-problems` | high |
| Bronchospasm | `asthma` | high |
| Staphylococcal infection | `drug-choice-for-selected-infections` | high |
| Functional carcinoid; non-functional GEP-NET | `neuroendocrine-neoplasms` | high |
| VIPoma | `neuroendocrine-neoplasms` | weak |
| Eradication of Helicobacter pylori | `peptic-ulcer-disease` | high |
| Idiopathic menorrhagia; Menorrhagia | `heavy-menstrual-bleeding` | high |
| Chronic renal failure; Chronic renal disease | `chronic-kidney-disease` | high |
| Haemodialysis | `chronic-kidney-disease` | weak |
| Ulcerative proctitis; Proctitis | `inflammatory-bowel-disease` | high |
| Faecal impaction | `constipation` | high |
| Megacolon | `constipation` | weak |
| Chronic bronchitis | `copd` | high |
| Chronic stable atherosclerotic disease | `cardiovascular-disease-risk` | medium |
| Preservation of bone mineral density | `osteoporosis` | high |
| Chronic granulomatous disease | `primary-immunodeficiencies` | medium |
| Dynamic equinus foot deformity | `spasticity` | medium |
| Terminal malignant neoplasia | `palliative-care-terminal-phase-medicines` | high |
| Stimulation of follicular development; Patients undergoing in-vitro fertilisation | `infertility` | high |
| The onset of lactation | `lactation-suppression-and-stimulation` | high |
| Acute bacterial enterocolitis | `diarrhoea` | medium |
| Zollinger-Ellison syndrome; Pathological hypersecretory conditions | `peptic-ulcer-disease` | weak |
| Corticosteroid-responsive dermatoses | `eczema` | weak |
| Chronic arthropathies | `osteoarthritis-knee-and-hip` | weak |
| Secondarily infected traumatic skin lesions | `cellulitis-and-skin-infections-children` | weak (paediatric only) |
| Hypogonadism (chorionic gonadotrophin) | `androgen-deficiency-in-men` | partial |

## 2. PBS listing text read as a condition (not a disease)

The triage `ADMIN` pattern misses the phrasing "Patients requiring …". These rows are listing policy, so no guideline is needed:

- Patients requiring administration of fluorouracil by intravenous infusion
- Patients requiring administration of fluorouracil by intravenous injection
- Patients requiring doses greater than 20 mg per week
- Use in a hospital
- Local intra-articular or peri-articular infiltration
- Malignant neoplasia
- Urinary symptoms

Fix to consider: add `^patients? requiring|^use in a hospital` to `ADMIN` in `scripts/no_guideline_triage.py`, on the retained Graph-Ontology branch `no-guideline-agenda`.

## 3. Evidence gaps: no source recorded yet

This list means the research pass recorded no source for these rows. It does not mean no source exists. Paget disease and hyperhidrosis almost certainly have free guidance, so these rows are Wave 4 research targets.

| Area | Conditions |
|---|---|
| Paediatric / congenital GI and liver | Progressive familial intrahepatic cholestasis · Biliary atresia · Anorectal congenital abnormalities · Enterokinase deficiency |
| Intestinal failure and malabsorption | Intestinal malabsorption including short bowel syndrome · Type III short bowel syndrome with intestinal failure · Rehydration in intestinal failure · Fat malabsorption · Calcium malabsorption · Chronic liver failure with fat malabsorption · Chylous ascites · Thiamine deficiency · Dietary management of conditions requiring a highly restrictive therapeutic diet |
| Bone | Paget disease of bone · Tumour-induced osteomalacia |
| Skin | Primary axillary hyperhidrosis · Disorders of keratinisation · Facial lipoatrophy |
| Eye | Corneal grafts |
| Infection | Chronic pulmonary histoplasmosis · Disseminated pulmonary histoplasmosis |

The rows noted in earlier waves as having no free source at all are still open: rare inborn errors, T-cell lymphomas, MDS, the neutropenias and rare GI conditions.

## 4. Wave 3 source problems

| Guideline | Problem | Next step |
|---|---|---|
| `hypertrophic-cardiomyopathy` | Built on the CSANZ guideline, which predates mavacamten. The agent skipped ESC 2023 because of its AI-use clause. **That breaks the owner's decision that AI-use clauses are recorded, not excluding.** | ESC 2023 is free to read and © ESC. Paraphrase it in, adding mavacamten. |
| `herpes-simplex-keratitis` | Built on AAO 2014, which has an AI-use clause | The owner's decision covers it. No action. |
| `non-infectious-uveitis` | The CC BY source (Singh 2024) was behind a bot challenge | Used the CC BY-NC Taiwan consensus instead. Retry Singh 2024 later. |
| `dry-eye-disease` | TFOS DEWS III (CC BY) was behind a bot challenge | Used Messmer 2023 (CC BY-NC; writing funded by Santen, which is disclosed). Retry TFOS DEWS III later. |
| `polycystic-ovary-syndrome` | The MJA 2024 summary (Wiley, 403) and the Monash guideline (bot challenge) were unreadable. Table 4 was stripped. | Retry. There are no grades or doses yet. |
| `venous-leg-ulcer` | The source covers assessment only, with no compression section | Find a management source |
| `neovascular-age-related-macular-degeneration` | Optometry Australia 2019 predates faricimab and brolucizumab, which are both PBS-listed | Find a newer source |
| `androgen-deficiency-in-men` | ESA 2016 predates TRAVERSE. The dose table came out interleaved. | Find a newer source |

---

## 5. After Wave 4 (2026-09-24)

The corpus has 525 guidelines, and all 525 pass. Of the 393 true-gap rows, 216 are now covered, which leaves **177**.

Three planned guidelines weren't written, all for the same reason: every usable copy was behind a bot challenge, paywall or login.

| Item | Blocked sources | Status |
|---|---|---|
| `chemotherapy-induced-neutropenia` (adult G-CSF) | AGIHO 2026 (CC BY), ASCO 2026. eviQ has no G-CSF page. | Gap. Nearest coverage is one line in `anticancer-drugs-general-principles`. |
| `hypertrophic-cardiomyopathy` rebuild on ESC 2023 (mavacamten) | OUP plus four repository copies | Unchanged. It still has no mavacamten content. |
| `central-precocious-puberty` | Endocrine Society 2026 is paywalled. The 2019 consortium paper's licence is unclear. | Gap |

New link: *Chronic eosinophilic leukaemia*, *Hypereosinophilic syndrome* and the three imatinib *Myelodysplastic/Myeloproliferative disorder* rows now sit with `hypereosinophilic-syndrome`. That settles Unresolved #3 in `myeloproliferative-neoplasms`.

These PBS rows were deliberately not attached, because their source doesn't support them:
- *Megaloblastic anaemias* (folinic acid)
- *Constitutional delay of growth or puberty*
- *Central precocious puberty*
- the two paediatric glioma rows

Sources that were blocked and should be retried: the 2024 ANZ cardiac amyloidosis consensus, the NIH/CDC opportunistic-infection guidelines, the international TSC consensus 2021, ERS 2024 chronic breathlessness, and the NLA 2025 chylomicronaemia management review.

---

## 6. After Wave 5 (2026-09-24)

The corpus has 561 guidelines, and all 561 pass. Of the 393 true-gap rows, 265 are now covered, which leaves **128**.

New proposed links. As with section 1, the owner needs to confirm each one:

| PBS condition | Proposed guideline | Confidence |
|---|---|---|
| Detrusor overactivity | `urinary-incontinence` | high (it covers oxybutynin and propantheline) |
| Pubertal induction | `disorders-of-puberty` | high |
| Micropenis | none | the pairing with `disorders-of-puberty` does **not** hold |

Rows that were deliberately not attached: *Isovaleric acidaemia* (the source doesn't cover it; a candidate is PMC12551068).

Notes for the reviewer:
- **Obesity:** PBS item 4570M (orlistat) is in program **R1, which is RPBS only**. So the "Obesity" row reflects repatriation benefits, not the general PBS. GLP-1 agonists are PBS-listed only for type 2 diabetes.
- **Two probable typos in quoted sources:** the verbatim text is kept, and the claims leave these figures out. They are flagged in Unresolved.
  - `hypoparathyroidism`: calcium "> 2 mg/day"
  - `cushing-syndrome`: pasireotide "every 28 months"
- **HCM rebuild on ESC 2023:** still blocked.
- **Shared-folder rule:** it was broken again. One agent's cleanup glob deleted five 128-byte 404 files belonging to another agent. The agent recreated them, and no real source was lost.

---

## 7. After Wave 6 (2026-09-24)

The corpus has 578 guidelines, and all 578 pass. Of the 393 true-gap rows, 284 are now covered, leaving **109**. Most of those need a link, not a new guideline:

- **Links to confirm.** Each one needs the owner's confirmation:
  - The rows in sections 1 and 6.
  - Cancer subtypes that go to an existing tumour guideline:
    - NSCLC rows → `non-small-cell-lung-cancer`
    - breast rows → `breast-cancer-*`
    - urothelial and BCG → `urothelial-carcinoma`
    - gastric and GOJ → `gastric-and-gojunction-cancer`
    - NET rows → `neuroendocrine-neoplasms`
    - BCC and cSCC → `keratinocyte-cancer`
    - medullary and thyroid → `thyroid-cancer-systemic-therapy`
    - clear-cell RCC → `renal-cell-carcinoma`
    - endometrial → `endometrial-cancer-advanced`
    - PV → `myeloproliferative-neoplasms`
  - Antibiotic rows (the septicaemia, susceptible-organism and staphylococcal rows) → `drug-choice-for-selected-infections`
  - STI rows → `sti-syndromes-and-screening`
  - Worm rows → `worm-infections`
  - Mood rows:
    - bipolar mixed episodes → `bipolar-disorder`
    - depression rows → `major-depressive-disorder`
  - Spasticity and equinus rows → `spasticity`
  - Hypsarrhythmia → `infantile-spasms`
  - Pseudomonas in CF → `cystic-fibrosis`
  - Enthesitis-related JIA → `juvenile-idiopathic-arthritis`
  - Megacolon → `hirschsprung-enterocolitis` (weak)
- **PBS listing text** (no guideline needed):
  - section 2 rows
  - *Local intra-articular or peri-articular infiltration*
  - *Use in a hospital*
  - *Terminal disease* and *Malignant neoplasia* (the benzodiazepine rows)
- **Still no guideline:**
  - adult diabetic ketoacidosis. It isn't a PBS row, but it came up as a corpus gap.
  - micropenis
  - enterokinase deficiency
  - corneal grafts and postoperative eye inflammation
  - neurogenic urinary retention
  - perichondritis of the pinna
  - the dietary "highly restrictive therapeutic diet" row
  - the HCM ESC 2023 rebuild, which is still blocked

Notes for the reviewer:
- **`type-1-diabetes`, unresolved items 4–5.** These are Australian context written from model knowledge, not from the source. They are marked `observation` and "check" and are not claims:
  - no SGLT inhibitor is TGA- or PBS-approved for T1D
  - CGM is supplied through the NDSS
- **`status-epilepticus-adults` has no doses.** NICE defers to the BNF and AMH defers to local protocol, so the guideline sends readers to their hospital protocol.
- **eviQ licence.** The eviQ copyright page, fetched 2026-09-24, now reads CC BY-NC 4.0 and says the content is not to be hosted on external sites. We still paraphrase it.

---

## 8. After Wave 7 (2026-09-24)

The corpus has 585 guidelines, and all 585 pass. Of the 393 true-gap rows, 290 are now covered, leaving **103**. Those are almost all links for the owner to confirm (sections 1, 6 and 7) or PBS listing text, not conditions.

- **New link to confirm:** *Eye inflammation* (prednisolone with phenylephrine) → `cataract`.
- **Not written:** `enterokinase-deficiency`. Only case reports exist.
- **HCM rebuilt** on Sanghvi 2025 (CC BY 4.0), a systematic review of ESC 2023, AHA/ACC 2024 and JCS 2018. It now covers mavacamten's place in treatment and its pregnancy contraindication, and CSANZ 2016 appears as the Australian counterpart banner. The page lost two things:
  - The CSANZ family-screening intervals. The Wave 3 version, commit `0c3f49e`, still has them.
  - Mavacamten monitoring was never covered. BSE 2025 (CC BY, PMC12128337) could support a companion page.
- **`neurogenic-bladder`: attached on class-level support only.** EAU recommends α-blockers but never names phenoxybenzamine, the PBS drug. A banner says so. To drop the row, remove it from `pbs_conditions`.
- **Weaker sources, each bannered:**
  - corneal graft: narrative review
  - perichondritis: single-centre retrospective study
  - CGD: expert "How I Treat"
  - micropenis: narrative review with no dose
