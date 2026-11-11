# Milestone 2: README

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-004; autonomous, not independent | pending |

---

## Purpose

Decide whether the README explains the Day 69 lecture to a newcomer: every lecture step with its image, and how to set up and run a local `.venv`.

## Deliverable

`README.md` built from the framework template, and the step images under `docs/images/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The README follows the framework template and `check-readme.sh` passes | Passes | Fails |
| 2 | Each of the 6 lecture steps has a heading, a short explanation and an image | 6 of 6 | Fewer |
| 3 | The README documents creating and using `.venv` and `python -m pip install --upgrade pip` | Present | Missing |
| 4 | The README says how to run the tests and states that the project has no runtime dependencies | Present | Missing |
| 5 | Images show example data only, are labelled as illustrations, and show no credentials | Yes | No |
| 6 | opengrep reports 0 findings on the branch | 0 findings | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Configuration and repository metadata the README refers to |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-13 — inside the short, documentation-only schedule in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Draw lecture step images | Draw one illustration per lecture step with example data (register form, login, admin-only buttons and 403, users/posts/comments schema, comment form and list, Gravatar avatars), label each as an illustration, store them in `docs/images/` and record each source. No application is run. | No | |
| 2 | Write README lecture walkthrough | Write the README from the framework template: the 6 steps (register new users, log in, protect routes, relational database, comments, Gravatar), each with its image. | No | |
| 3 | Document venv, run and tests | Add Requirements, Setup, Run and Tests sections: create `.venv`, upgrade pip with `python -m pip install --upgrade pip`, run pytest, and state that there are no runtime dependencies. Serves S02. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-project-setup.md
