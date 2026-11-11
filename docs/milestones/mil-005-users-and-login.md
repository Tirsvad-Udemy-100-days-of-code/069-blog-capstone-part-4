# Milestone 5: Users and login

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-012; autonomous, not independent | pending |

---

## Purpose

Decide whether people can register, log in and log out: Requirements 1 and 2 of the lecture.

## Deliverable

A `User` table, `RegisterForm` and `LoginForm`, the routes `register`, `login` and `logout`, Flask-Login wired in, with tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A new user is stored with a salted and hashed password (never the plain text) | Yes | No |
| 2 | A registered user can log in with the right password and gets a flash message for an unknown email or a wrong password | Yes | No |
| 3 | After registering, the user is logged in and sent to the home page | Yes | No |
| 4 | The navigation shows Login and Register to a logged-out user and Log Out to a logged-in user | Yes | No |
| 5 | The code passes `python -m pytest` and its review against the programming checklist is a Go | Pass | Fail |
| 6 | opengrep reports 0 findings on the branch | 0 findings | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] | The blog and its database |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-20 — inside the 2026-11-30 end date in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | User model and RegisterForm | Add the `User` table (with `UserMixin`) and `RegisterForm`; render it with Bootstrap-Flask `render_form()`; unit tests for the model and form. | No | |
| 2 | Register route with hashing | Implement `register` with `generate_password_hash(method="pbkdf2:sha256", salt_length=8)`, reject an already registered email, and log the new user in with `login_user()`. | No | |
| 3 | Login and logout | Add `LoginForm`, `LoginManager` with `user_loader`, and the routes `login` and `logout`; look the user up with a `where()` clause and use `check_password_hash()`; flash messages for the failure cases. | No | |
| 4 | Navigation state and tests | Show the right links in `header.html` with `current_user.is_authenticated`; route tests for register, login, logout and the flash messages. | No | |

---

[BC-001]: ../business-case.md
[MIL-004]: ./mil-004-blog-foundation.md
