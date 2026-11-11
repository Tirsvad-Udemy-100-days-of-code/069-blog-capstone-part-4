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
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-001; autonomous, not independent | pending |

---

## Executive Summary

Day 69 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" finishes the blog capstone by adding users: registering and logging in with Flask-Login, protecting routes with an `admin_only` decorator, a one-to-many relational database (users, posts and comments), comments for logged-in users and Gravatar profile pictures. This project turns that lecture into a public learning reference: a README and a three-language wiki (English, Danish, Bahasa Malaysia) that explain each lecture step with an image and say what was learned. No application code is delivered; the project holds documentation and project configuration only.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/` (plan first, review every artifact against its QC checklist, record each review as an `RC-*`). Quality attributes follow ISO/IEC 25010:2023. Documentation follows the framework's README template and wiki process (`framework/process/wiki.md`).

## Problem Statement

A course participant's notes on a lecture are scattered and lose value once the course is finished. Other course participants and GitHub readers who look for a worked example of blog authentication find code without explanation, or explanation without the visual result of each step.

## Business Opportunity

A single repository can show what each lecture step produces (an image) and what it teaches (a short explanation), in English and in two further languages, so the lecture can be revisited and shared.

## Objectives

1. Publish a README that walks through every Day 69 lecture step (six step groups) with an image and instructions to set up a local `.venv`.
2. Publish a wiki in English, Danish and Bahasa Malaysia that explains what each step teaches.
3. Describe the repository on the git host with a description and topics.
4. Provide project configuration (`pyproject.toml`, Python `.gitignore`, `Doxyfile`) that a later coding phase can use unchanged.
5. Keep a traceable history: one branch and pull request per milestone.

## Scope

### In Scope

- README (framework template) for the Day 69 lecture steps, with images.
- Wiki pages in `docs/wiki/` in English, Danish (`-da`) and Bahasa Malaysia (`-ms`), with images and "what we gained" sections.
- One illustration per lecture step, drawn for this repository from the lecture description and labelled as an illustration.
- Repository description and topics on the git host.
- `pyproject.toml` (Python 3.13 or newer, pytest), Python `.gitignore`, `Doxyfile`, documented `.venv` setup with `python -m pip install --upgrade pip`.
- A local opengrep scan before each push.

### Out of Scope

- Writing application source code or tests under `src/` and `tests/` (the folders are reserved for a later phase).
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
| 1 | Lecture steps covered | All 6 steps in README and wiki | Count of steps with text and image |
| 2 | Wiki languages | 3 (en, da, ms) with the same page set | `check-languages.sh` and page list |
| 3 | Repository metadata | Description and at least 5 topics set | Host API response |
| 4 | Review | Every artifact `Accepted` with a `Go` review | `RC-*` records |
| 5 | Security scan | 0 opengrep findings before each push | opengrep output |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The course end project is not available to this repository, and no code is written | Real screenshots cannot be captured | Draw illustrations with example data, label each as an illustration, record the source of each, and ask S01 to confirm at plan acceptance (precedent: Day 67) |
| The lecture material is copyrighted by the course author | Legal exposure | Summarise in own words; never reproduce solution code or the course archive |
| A token leaks into the repository | Credential exposure | Tokens are read from `.env` outside the repository, never printed, never committed |
| Translations drift from English | Inconsistent wiki | English is authoritative; same page set; `check-languages.sh` |
| Screenshots show personal data | Privacy loss | Use test data only |

## Assumptions

- S01 is Product Owner, developer and reviewer.
- The Product Owner domain language is English, domain IT.
- The git host wiki is enabled and the organisation holds `TOKEN_FOR_GITEA_WIKI`.
- The images are illustrations with example data, because no application code is run.

## Constraints

- Duration: the whole project is complete by 2026-11-16 (start 2026-11-11).
- Python 3.13 or newer; a local `.venv`; pytest for tests; constants in `constants.py` when code is written.
- Doxygen comments in any source code.
- Documents live under `docs/`; `src/` and `tests/` stay empty in this project.
- No GUI is run on the host desktop.

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
