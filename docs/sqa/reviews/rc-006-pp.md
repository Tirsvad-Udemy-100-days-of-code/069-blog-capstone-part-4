# x

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-006 |
| CrossReference | [PP-001], [QC-PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [335e45c] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] (and [QC-LANG-001])
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-11, end 2026-11-16, constraint cited from BC-001. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Three gateways each with document, decision date and owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates 11-12, 11-13, 11-16 match the MIL target dates and lie inside the window. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Every BC in-scope item maps to a gateway in Scope Coverage. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001, MIL-002, MIL-003 is acyclic and matches the schedule. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | No-Go moves later gateways; S01 decides the end date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owners use S01. The project has no governance document, so no RACI to match. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions list their source; no re-baseline yet. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | One plan risk with mitigation, traced to BC-001 risk 1. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | One open issue, consistent with the rest of the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Deliverables match the MIL deliverables. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says none (documentation tasks). |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars and table dates agree; chain agrees with Dependencies. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column says not yet synced. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Single plan, Version History kept. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language | en` and `Domain | it` present, no placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English; no mixed language. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Executive documents use IT Executive English, others IT Professional English, per registry. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No project dictionary (DICT) exists; terms used consistently (e.g. `.venv`, `route`, `comment`) with no synonyms. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No `*.en.md` twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change since a previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Reviewer (AI as stand-in for S01) reads English and knows the IT domain; S01 is the PO for this language and domain. Terms used correctly. Open to challenge by S01. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (SA, BC, MIL) are defined by their document names on first use. |

## Overall Verdict

Go — every Mandatory criterion passes in both tables. Stand-in decision: criteria 3, 5 and 9 of QC-LANG-001 are judged by the stand-in because the language (English) and domain (IT) are the reviewer's own; S01 may challenge this.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[335e45c]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/commit/335e45c12d38b764705336eefde51af3c16930b2
