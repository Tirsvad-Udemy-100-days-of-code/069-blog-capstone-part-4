# Milestone 3: Wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [335e45c] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-005; autonomous, not independent | [335e45c] |

---

## Purpose

Decide whether the wiki explains what each lecture step taught, in English, Danish and Bahasa Malaysia, with the same page set and the step images.

## Deliverable

Flat Markdown pages in `docs/wiki/`: `Home`, one page per lecture step group, `_Sidebar`, each in `.md` (English), `-da.md` and `-ms.md`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every English page has a Danish and a Bahasa Malaysia page | Same page set | A page missing |
| 2 | Each page starts with the language switch line | Yes | No |
| 3 | Each lecture step page has its image and a "What we gained" section | 6 of 6 | Fewer |
| 4 | `_Sidebar.md` follows the framework shape and links `Home-da` and `Home-ms` | Yes | No |
| 5 | The wiki passes `QC-WIKI-001` | Pass | Fail |
| 6 | opengrep reports 0 findings on the branch | 0 findings | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | Images and the step list the wiki explains |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-16 — inside the short, documentation-only schedule in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write English wiki | Write `Home` and the six lecture step pages with the images and, for each step, a "What we gained" section. English is the authoritative text. | No | |
| 2 | Translate wiki to Danish | Write the same pages as `<Page>-da.md`, translating prose only; code, commands and file names stay in English. | No | |
| 3 | Translate wiki to Bahasa Malaysia | Write the same pages as `<Page>-ms.md`, translating prose only; code, commands and file names stay in English. | No | |
| 4 | Add wiki sidebar and check languages | Add `_Sidebar.md` in the framework shape and run `check-languages.sh` so the three languages have the same page set. | No | |

---

[BC-001]: ../business-case.md
[MIL-002]: ./mil-002-readme.md
[335e45c]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/commit/335e45c12d38b764705336eefde51af3c16930b2
