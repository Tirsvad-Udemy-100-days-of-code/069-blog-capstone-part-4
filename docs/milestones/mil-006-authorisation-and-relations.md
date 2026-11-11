# Milestone 6: Authorisation and relations

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-013; autonomous, not independent | pending |

---

## Purpose

Decide whether only the admin can manage posts and whether posts are linked to their authors: Requirement 3 and the relational database of the lecture.

## Deliverable

The `admin_only` decorator, hidden admin buttons, the `author_id` foreign key and bidirectional `User`/`BlogPost` relationship, with tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | User id 1 is the admin; the buttons "Create New Post", "Edit Post" and delete are hidden from everyone else | Yes | No |
| 2 | A non-admin or anonymous request to `/new-post`, `/edit-post/<id>` or `/delete/<id>` gets HTTP 403 | Yes | No |
| 3 | `User.posts` and `BlogPost.author` are a bidirectional one-to-many relationship using `author_id` | Yes | No |
| 4 | The post author name shown on the home and post pages comes from the `User` object | Yes | No |
| 5 | The code passes `python -m pytest` and its review against the programming checklist is a Go | Pass | Fail |
| 6 | opengrep reports 0 findings on the branch | 0 findings | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-005] | Users and login |

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

2026-11-24 — inside the 2026-11-30 end date in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the admin_only decorator | Implement `admin_only` with `functools.wraps` and `abort(403)`, and apply it to the three post routes; tests for admin, other user and anonymous. | No | |
| 2 | Hide admin buttons in templates | Use `current_user.id == 1` in `index.html` and `post.html`; template tests. | No | |
| 3 | Relate users and posts | Add `author_id` and the `relationship()` pair with `back_populates`; recreate the database and the seed; the `add_new_post` route sets the author to `current_user`. | No | |
| 4 | Show the author name | Show `post.author.name` on the home and post pages; tests. | No | |

---

[BC-001]: ../business-case.md
[MIL-005]: ./mil-005-users-and-login.md
