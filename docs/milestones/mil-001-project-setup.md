# Milestone 1: Project setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-003; autonomous, not independent | pending |

---

## Purpose

Decide whether the repository is ready to receive the README and the wiki: it is described on the git host and carries the project configuration a later Python phase needs.

## Deliverable

Repository description and topics on the git host; `.gitignore`, `pyproject.toml` and `Doxyfile` in the repository root; empty `src/` and `tests/` folders kept with a `.gitkeep`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The host API returns a non-empty description and at least 5 topics | Yes | Missing |
| 2 | `pyproject.toml` requires Python 3.13 or newer and configures pytest | Present | Missing |
| 3 | `.gitignore` ignores `.venv/`, `__pycache__/`, `.env`, `instance/` and `*.db` | Present | Missing |
| 4 | `Doxyfile` exists and `doxygen -g` style keys point at `src/` | Present | Missing |
| 5 | opengrep reports 0 findings on the branch | 0 findings | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [BC-001] accepted | The plan-first gate |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3 and 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — inside the short, documentation-only schedule in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Set a clear description and topics (for example python, flask, flask-login, authentication, sqlalchemy, gravatar, udemy, 100-days-of-code) through the git host API, reading the token from the personal `.env` outside the project. Serves S03, who judge the repository at first glance. | No | |
| 2 | Add Python .gitignore | Extend the existing Python `.gitignore` with `.venv/`, `.env`, `instance/`, `*.db`, Doxygen output and `docs/ai-prompts/` where the repository is public, so secrets and local state are never committed. | No | |
| 3 | Add pyproject.toml | Configure the project for Python 3.13 or newer with pytest as the only dev dependency and no runtime dependencies, as S03 expects. Reserve `src/` and `tests/` as the layout. | No | |
| 4 | Add Doxyfile | Create a `Doxyfile` that reads `src/` and writes to an ignored `docs/doxygen/` folder, so Doxygen comments in later code are documented. | No | |
| 5 | Reserve src and tests folders | Add `.gitkeep` files so the agreed folder structure exists while no application code is written in this project. | No | |
| 6 | Scan with opengrep before push | Run the local opengrep binary over the branch before every push and record the result in the pull request. | No | |

---

[BC-001]: ../business-case.md
