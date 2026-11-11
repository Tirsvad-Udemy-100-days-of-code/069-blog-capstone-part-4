# Milestone 8: Real screenshots and docs

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-008 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [3028e2d] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-015; autonomous, not independent | [3028e2d] |

---

## Purpose

Decide whether the README and the wiki show the real blog: one screenshot per lecture step taken in a container, and the documents updated to match the code.

## Deliverable

Screenshots in `docs/images/` that replace the illustrations, and the README and the wiki in en, da and ms updated.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Each of the 6 lecture steps has a real screenshot, taken from the blog in a Docker container with example data | Yes | No |
| 2 | The README no longer calls the images illustrations, and says how to run the blog and its tests | Yes | No |
| 3 | The three-language wiki shows the new screenshots and the code the project really contains; `check-languages.sh` passes | Yes | No |
| 4 | No screenshot shows a credential or personal data | Yes | No |
| 5 | The code passes `python -m pytest` and its review against the programming checklist is a Go | Pass | Fail |
| 6 | opengrep reports 0 findings on the branch | 0 findings | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-007] | The finished blog |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2 and 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-30 — inside the 2026-11-30 end date in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Container screenshot tooling | Reuse the Docker approach of the Day 63 project: an image that starts the blog and a headless browser that captures the pages with example data; the browser never runs on the host desktop. | No | |
| 2 | Capture one screenshot per step | Capture register, login, admin buttons, 403, comments and avatars, and the database relations view; store them in `docs/images/`. | No | |
| 3 | Update the README | Replace the illustrations, add "Run the blog" and update Requirements for the runtime dependencies. | No | |
| 4 | Update the wiki in three languages | Update the six step pages in en, da and ms with the screenshots and the code that is really in `src/`; run `check-languages.sh`. | No | |

---

[BC-001]: ../business-case.md
[MIL-007]: ./mil-007-comments-and-gravatar.md
[3028e2d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/commit/3028e2d2f42bac50beb12082513c6319e62eca74
