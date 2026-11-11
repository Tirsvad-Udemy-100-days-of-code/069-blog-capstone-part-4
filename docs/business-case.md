# Business Case: Blog Capstone Part 4 (Day 69)

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Scope amended: the application code is in scope (S01 corrected the first prompt) | [3028e2d] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-008; autonomous, not independent | [3028e2d] |

---

## Executive Summary

Day 69 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" finishes the blog capstone by adding users: registering and logging in with Flask-Login, protecting routes with an `admin_only` decorator, a one-to-many relational database (users, posts and comments), comments for logged-in users and Gravatar profile pictures. This project builds the blog the lecture describes and turns the lecture into a public learning reference: a runnable Flask application written from scratch under `src/` with tests under `tests/`, a README and a three-language wiki (English, Danish, Bahasa Malaysia) that explain each lecture step with a real screenshot and say what was learned. The course's own starter and solution are not used; the blog is written for this repository, with the assignment's route and function names.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/` (plan first, review every artifact against its QC checklist, record each review as an `RC-*`). Quality attributes follow ISO/IEC 25010:2023. Documentation follows the framework's README template and wiki process (`framework/process/wiki.md`).

## Problem Statement

A course participant's notes on a lecture are scattered and lose value once the course is finished. Other course participants and GitHub readers who look for a worked example of blog authentication find code without explanation, or explanation without the visual result of each step.

## Business Opportunity

A single repository can show what each lecture step produces (an image) and what it teaches (a short explanation), in English and in two further languages, so the lecture can be revisited and shared.

## Objectives

1. Publish a README that walks through every Day 69 lecture step (six step groups) with a screenshot and instructions to set up a local `.venv`, run the blog and run its tests.
2. Publish a wiki in English, Danish and Bahasa Malaysia that explains what each step teaches.
3. Describe the repository on the git host with a description and topics.
4. Provide project configuration (`pyproject.toml`, Python `.gitignore`, `Doxyfile`) for the code.
5. Keep a traceable history: one branch and pull request per milestone.
6. Build a working Flask blog: posts (read, create, edit, delete), user registration and login, an admin-only authorisation rule, a one-to-many relational database (users, posts, comments), comments for logged-in users and Gravatar pictures.
7. Cover the logic with pytest tests and review the code against the programming checklist before each pull request.

## Scope

### In Scope

- README (framework template) for the Day 69 lecture steps, with images.
- Wiki pages in `docs/wiki/` in English, Danish (`-da`) and Bahasa Malaysia (`-ms`), with images and "what we gained" sections.
- The blog application in `src/` (Python 3.13 or newer, Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, Flask-CKEditor, Bootstrap-Flask), with its pytest tests in `tests/`.
- A real screenshot of each lecture step, taken from this blog running in a Docker container.
- Architecture and design: Clean Architecture with the presentation pattern recorded in an ADR.
- Repository description and topics on the git host.
- `pyproject.toml` (Python 3.13 or newer, pytest), Python `.gitignore`, `Doxyfile`, documented `.venv` setup with `python -m pip install --upgrade pip`.
- A local opengrep scan before each push.

### Out of Scope

- Hosting or deploying the blog, and any copy of the course starter or solution.
- Reproducing the lecture's video or course material beyond short descriptions and own illustrations.
- Publishing the course starting or end archive in the repository.

## Expected Benefits

### Tangible Benefits

- A README and a three-language wiki that a reader can follow without watching the lecture.
- One image per lecture step as visual evidence.

### Intangible Benefits

- Consolidated learning of authentication, authorisation, relational data and avatars.
- A repository other participants can compare their solutions with.

## Strategic Alignment

The project supports the participant's learning goal in the bootcamp and the practice of the SQA and QC framework on a small, complete project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Lecture steps covered | All 6 steps in README and wiki, each with a real screenshot | Count of steps with text and screenshot |
| 2 | Wiki languages | 3 (en, da, ms) with the same page set | `check-languages.sh` and page list |
| 3 | Repository metadata | Description and at least 5 topics set | Host API response |
| 4 | Review | Every artifact `Accepted` with a `Go` review | `RC-*` records |
| 5 | Security scan | 0 opengrep findings before each push | opengrep output |
| 6 | Working blog | All four lecture requirements implemented; tests pass | `python -m pytest` result and the screenshots |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The course starter and end project are not available, and the Day 67 repository holds no code | The blog must be written from scratch | Build it from the lecture description with the assignment's names; S01 confirmed that code is in scope |
| The blog needs runtime dependencies | S03 expected none | Keep them to the packages the lecture names, list them in `pyproject.toml` and the README |
| The lecture material is copyrighted by the course author | Legal exposure | Summarise in own words; never reproduce solution code or the course archive |
| A token leaks into the repository | Credential exposure | Tokens are read from `.env` outside the repository, never printed, never committed |
| Translations drift from English | Inconsistent wiki | English is authoritative; same page set; `check-languages.sh` |
| Screenshots show personal data | Privacy loss | Use test data only |

## Assumptions

- S01 is Product Owner, developer and reviewer.
- The Product Owner domain language is English, domain IT.
- The git host wiki is enabled and the organisation holds `TOKEN_FOR_GITEA_WIKI`.
- Screenshots come from the blog itself, run in a Docker container with example data.

## Constraints

- Duration: the whole project is complete by 2026-11-30 (start 2026-11-11; the first end date, 2026-11-16, covered documentation only).
- Python 3.13 or newer; a local `.venv`; pytest for tests; constants in `constants.py`.
- Doxygen comments in the source code.
- Folder structure `src/`, `tests/`, `docs/`.
- No GUI or browser test runs on the host desktop; it runs in a Docker container.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| Author time for writing, translating and drawing the step images. The assessment is qualitative because the project has no monetary cost or revenue. | A reusable reference for S01, S02 and S03 |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns the project, writes and reviews it |
| S02 | Reads and runs the README to compare solutions |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, documentation only, and the lecture description is available.

---

[SA-001]: ./stakeholder-analysis.md
[335e45c]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/commit/335e45c12d38b764705336eefde51af3c16930b2
[3028e2d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/commit/3028e2d2f42bac50beb12082513c6319e62eca74
