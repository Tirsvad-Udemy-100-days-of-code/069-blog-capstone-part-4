# Milestone 4: Blog foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [3028e2d] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-011; autonomous, not independent | [3028e2d] |

---

## Purpose

Decide whether the blog the lecture starts from exists: posts stored in a database and shown on the home page and a post page, with create, edit and delete, built on a documented architecture.

## Deliverable

A runnable Flask blog under `src/blog/` with tests under `tests/`, and the architecture ADR.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The architecture ADR (Clean Architecture, presentation pattern, persistence) is `Accepted` with a `Go` review | Yes | No |
| 2 | A fresh clone runs `python -m blog` and serves the home page with posts from the SQLite database | Yes | No |
| 3 | The routes `get_all_posts`, `show_post`, `add_new_post`, `edit_post`, `delete_post`, `about` and `contact` work | Yes | No |
| 4 | Constants live in `constants.py` and the source has Doxygen comments | Yes | No |
| 5 | The code passes `python -m pytest` and its review against the programming checklist is a Go | Pass | Fail |
| 6 | opengrep reports 0 findings on the branch | 0 findings | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Configuration the code uses |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 4, 6 and 7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-17 — inside the 2026-11-30 end date in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Record the architecture ADR | Write ADR-0001: Clean Architecture layers, MVVM-style presentation for the server-rendered user interface, Flask with Flask-SQLAlchemy as the persistence adapter; review it. The lecture screens, in the Clean Blog look of the Day 59 project, are the wireframes. | No | |
| 2 | Domain and persistence for posts | Add the `BlogPost` domain model, the port and the SQLAlchemy repository with a seeded `blog.db`, plus unit tests. | No | |
| 3 | Home, post, about and contact pages | Add the Flask app factory, the routes `get_all_posts`, `show_post`, `about`, `contact` and the Clean Blog templates and static files (reused from the Day 59 project, with its licence notice). | No | |
| 4 | Create, edit and delete posts | Add `add_new_post`, `edit_post` and `delete_post` with a `PostForm` (Flask-WTF) and the CKEditor body field, using Bootstrap-Flask `render_form()`; tests for each route. | No | |
| 5 | Add runtime dependencies and run docs | Declare Flask, Flask-SQLAlchemy, Flask-WTF, Flask-CKEditor and Bootstrap-Flask in `pyproject.toml` and document the run command. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-project-setup.md
[3028e2d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/commit/3028e2d2f42bac50beb12082513c6319e62eca74
