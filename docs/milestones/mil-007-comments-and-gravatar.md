# Milestone 7: Comments and Gravatar

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-007 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [3028e2d] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-014; autonomous, not independent | [3028e2d] |

---

## Purpose

Decide whether logged-in users can comment on posts and see avatars: Requirement 4 and the Gravatar section of the lecture.

## Deliverable

The `CommentForm`, the `Comment` table with its relationships, comments shown on the post page, and Gravatar avatars, with tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A logged-in user can submit a comment on a post and it is saved with its author and post | Yes | No |
| 2 | A logged-out user who submits a comment is flashed a message and redirected to `/login` | Yes | No |
| 3 | All comments of a post are shown with their author name and the CKEditor HTML | Yes | No |
| 4 | Each comment shows a Gravatar avatar built from the SHA-256 hash of the lowercased email | Yes | No |
| 5 | The code passes `python -m pytest` and its review against the programming checklist is a Go | Pass | Fail |
| 6 | opengrep reports 0 findings on the branch | 0 findings | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-006] | Users, posts and the relationship |

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

2026-11-27 — inside the 2026-11-30 end date in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Comment model and relationships | Add the `Comment` table (`id`, `text`) with one-to-many links from `User` and from `BlogPost`; recreate the seed. | No | |
| 2 | CommentForm and the post route | Add `CommentForm` (one CKEditor field) and make `show_post` accept `GET` and `POST`; redirect anonymous users to `login` with a flash message. | No | |
| 3 | Show comments and avatars | Loop over `post.comments` in `post.html`, render the HTML text with `|safe`, and add a small tested `gravatar_url()` helper. | No | |
| 4 | Comment tests | Route and unit tests for commenting, the anonymous redirect, the comment list and the avatar URL. | No | |

---

[BC-001]: ../business-case.md
[MIL-006]: ./mil-006-authorisation-and-relations.md
[3028e2d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/commit/3028e2d2f42bac50beb12082513c6319e62eca74
