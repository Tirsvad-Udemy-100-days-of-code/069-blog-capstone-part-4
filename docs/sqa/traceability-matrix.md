# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [335e45c] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Rows for MIL-004 to MIL-008 and RC-008 to RC-015 | [3028e2d] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-008] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-009] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007], [MIL-008] | [RC-010] |
| [MIL-001] | MIL | en | it | [PP-001] | - | [RC-003] |
| [MIL-002] | MIL | en | it | [MIL-001] | - | [RC-004] |
| [MIL-003] | MIL | en | it | [MIL-002] | - | [RC-005] |
| [MIL-004] | MIL | en | it | [MIL-001] | - | [RC-011] |
| [MIL-005] | MIL | en | it | [MIL-004] | - | [RC-012] |
| [MIL-006] | MIL | en | it | [MIL-005] | - | [RC-013] |
| [MIL-007] | MIL | en | it | [MIL-006] | - | [RC-014] |
| [MIL-008] | MIL | en | it | [MIL-007] | - | [RC-015] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [PP-001] | - | - | Covered |
| CN-002 | [MIL-002] | - | - | Covered |
| CN-003 | [MIL-003] | - | - | Covered |
| CN-004 | [MIL-001] | - | - | Covered |
| CN-005 | [MIL-001] | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | - | None found | - | Closed | - |

## Coverage Notes

Types with no instance yet have no row. `-` in Upstream means foundational, in Downstream that nothing is built on it yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-readme.md
[MIL-003]: ../milestones/mil-003-wiki.md
[MIL-004]: ../milestones/mil-004-blog-foundation.md
[MIL-005]: ../milestones/mil-005-users-and-login.md
[MIL-006]: ../milestones/mil-006-authorisation-and-relations.md
[MIL-007]: ../milestones/mil-007-comments-and-gravatar.md
[MIL-008]: ../milestones/mil-008-screenshots-and-docs.md
[RC-008]: ./reviews/reviews\rc-008-bc-v2.md
[RC-009]: ./reviews/reviews\rc-009-sa-v2.md
[RC-010]: ./reviews/reviews\rc-010-pp-v2.md
[RC-011]: ./reviews/reviews\rc-011-mil-004.md
[RC-012]: ./reviews/reviews\rc-012-mil-005.md
[RC-013]: ./reviews/reviews\rc-013-mil-006.md
[RC-014]: ./reviews/reviews\rc-014-mil-007.md
[RC-015]: ./reviews/reviews\rc-015-mil-008.md
[RC-001]: ./reviews/rc-001-bc.md
[RC-002]: ./reviews/rc-002-sa.md
[RC-003]: ./reviews/rc-003-mil-001.md
[RC-004]: ./reviews/rc-004-mil-002.md
[RC-005]: ./reviews/rc-005-mil-003.md
[RC-006]: ./reviews/rc-006-pp.md
[335e45c]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/commit/335e45c12d38b764705336eefde51af3c16930b2
[3028e2d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/commit/3028e2d2f42bac50beb12082513c6319e62eca74
