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
