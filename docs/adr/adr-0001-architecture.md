# ADR-0001: Architecture of the blog

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-016; autonomous, not independent | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The Day 69 blog must be written from scratch (BC-001 risk 1), keep the assignment's route and function names (S02), and use only the packages the lecture names (S03). The lecture's own code puts routes, models and logic in one `main.py`. Forces: the code is also a teaching reference, it needs pytest tests, it must follow the framework's Clean Architecture rules, and it must stay small.

Options evaluated:

1. **One `main.py`** as in the lecture. Smallest, but the business rules (who is admin, who may comment, the hashing rule) can only be tested through Flask, and it ignores the framework's layer rules.
2. **Clean Architecture** with `domain`, `application`, `infrastructure` and `presentation` packages; Flask and SQLAlchemy only in the outer layers. More files, but the rules are tested without Flask or a database.
3. **Flask blueprints only** (feature folders, no ports). Less ceremony than option 2, but the rules still import Flask-SQLAlchemy.

For the presentation layer the framework's default is MVVM for a user interface and MVC for an API. The blog is a server-rendered user interface, so each route builds a view model (a plain object holding what the Jinja template shows) and passes it to the template.

## Decision

We use option 2: Clean Architecture in `src/blog/` with `domain`, `application`, `infrastructure` and `presentation` packages, a Flask app factory and the composition root in `presentation`, and an MVVM-style presentation in which route functions (with the assignment's names) call a use case and render a template from a view model. Persistence is Flask-SQLAlchemy with SQLite in `infrastructure`; Flask-Login, Flask-WTF, Flask-CKEditor and Bootstrap-Flask are used only in `presentation`.

## Consequences

**Positive:**

- The business rules (admin, comment permission, password hashing through a port, Gravatar URL) are unit-tested without Flask or a database.
- The layer rules of `clean-architecture` are met, so the code review has a clear target.
- The route and function names of the assignment stay in one readable module.

**Negative:**

- More files and some mapping code between domain objects and SQLAlchemy models than the lecture's single file.
- A course participant comparing with the lecture's `main.py` must find the equivalent code in `presentation/routes.py`.

Quality attributes: maintainability and testability improve; the mapping adds a small performance cost that does not matter for a blog of this size.

## Affected Artifacts

- [BC-001] — the decision realises objectives 6 and 7 and answers risk 1.

---

[BC-001]: ../business-case.md
