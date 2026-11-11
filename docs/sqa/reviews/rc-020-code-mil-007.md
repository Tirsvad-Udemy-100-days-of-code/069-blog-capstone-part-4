# Review of the code of MIL-007

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-020 |
| CrossReference | [PY-MIL-007], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [PY-MIL-007]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: not applicable (this artifact type is written in English, outside the PO-language types)
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing | Pass | `ruff check` (pep8-naming selected) reports no finding. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names such as `CreatePost`, `HtmlSanitizer`, `format_post_date`; the assignment's route names are kept. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check src tests` and `ruff check .` are clean; the `noqa: S105` constants, the `noqa: SLF001` that unwraps the Flask-Login proxy and the `type: ignore[misc]` are explained in the code and `pyproject.toml`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict` passes on 36 source files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept | Pass | `PostNotFoundError`, `UnknownEmailError`, `InvalidCredentialsError` and `EmailAlreadyRegisteredError` are specific and mapped to responses; no bare except found by ruff. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | `ruff` B and A rules report nothing. |
| 7 | Files, locks and connections are managed with context managers | Pass | Database sessions are handled by Flask-SQLAlchemy and passwords only by the hasher; no file handles are opened by hand. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class and function has a Doxygen docstring (`@brief`, `@param`, `@return`). |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` in `src/`; the secret key and passwords are never logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | The project has no DCD; the classes follow ADR-0001, which records the layers and the decision. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 120 tests (unit and integration), each builds a fresh app on in-memory SQLite; 99% coverage with branches. The earlier unclosed-connection ResourceWarning is fixed (the CSRF test now disposes its engine). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` clean; ignored missing stubs are commented in `pyproject.toml`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Declared with lower bounds only (no lock file); none unused. Optional criterion, recorded as an action item. |
| 14 | Each piece of knowledge is defined in one place | Pass | Constants (labels, allowed tags, ports) live in `constants.py`; the sanitising rule is in one adapter. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` and `application` import only the standard library and each other (checked with grep for flask, sqlalchemy, bleach, werkzeug). |
| 16 | SOLID holds | Pass | Use cases are single-purpose classes; the repository, clock and sanitiser are ports with one adapter each. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/blog`; `unit` and `integration` under `tests/`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.` | Pass | Checked in the file list. |

## Overall Verdict

No-Go — a Mandatory criterion fails.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Pin or lock the dependency versions (criterion 13, Optional) | S01 | 2026-11-30 |
| Accounts stored with mixed-case emails are not migrated; none exist in a fresh database | S01 | n/a |

---

[PY-MIL-007]: ../../../src/blog/
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
