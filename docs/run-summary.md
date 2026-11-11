# Run summary (autonomous mode)

Runs of 2026-11-11 for the Day 69 project: first documentation only, then, after S01 corrected the first prompt, the blog application itself.

## Pull requests merged

| PR | Milestone | Closes |
| --- | --- | --- |
| 1 | Baseline (BC-001, SA-001, PP-001, MIL-001..003, TM-001, RC-001..006, framework submodule) | none |
| 16 | MIL-001 project setup | issues 2 to 7 |
| 17 | MIL-002 README | issues 8 to 10 |
| 18 | MIL-003 wiki | issues 11 to 14 |
| 19 | Close-out of the documentation run | none |
| 20 | Plan amendment: code in scope, MIL-004..008, RC-008..015 | none |
| 42 | MIL-004 blog foundation, ADR-0001 | issues 21 to 25 |
| 43 | MIL-005 users and login | issues 26 to 29 |
| 44 | MIL-006 authorisation and relations | issues 30 to 33 |
| 45 | MIL-007 comments and Gravatar | issues 34 to 37 |
| this PR | MIL-008 real screenshots, README and wiki | issues 38 to 41 |

Pull request 15 was opened by mistake with no changes (the plan gate rejected my first commit, because I used issue numbers instead of task numbers in the `Task:` trailers) and closed unmerged.

## Reviews

| Record | Instance | Verdict | Mode |
| --- | --- | --- | --- |
| RC-001 to RC-006 | BC-001, SA-001, MIL-001..003, PP-001 (first version) | Go | autonomous, not independent |
| RC-007 | Wiki (QC-WIKI-001), first version | Go | autonomous, not independent |
| RC-008 to RC-010 | BC-001, SA-001, PP-001 (code in scope) | Go | autonomous, not independent |
| RC-011 to RC-015 | MIL-004 to MIL-008 | Go | autonomous, not independent |
| RC-016 | ADR-0001 | Go | autonomous, not independent |
| RC-017 to RC-021 | Code of MIL-004 to MIL-008 against QC-PY-001 | Go | autonomous, not independent |
| RC-022 | Wiki after the real screenshots (QC-WIKI-001) | Go, after the published-wiki check | autonomous, not independent |

## Stand-in decisions (open to challenge by S01)

- The AI acted as stand-in for S01 as reviewer of every artifact and of the code. A subagent wrote the Python code; the review ran the tools (pytest, ruff, mypy --strict, opengrep) and checked the layer rule with grep.
- **Scope change.** The first prompt said "No programming"; S01 corrected it ("We are doing programming"). The plan was amended, accepted again, and the first run's README and wiki were rewritten with real screenshots.
- The course starter and solution were not available (the Day 67 repository holds no code), so the blog was written from the lecture description with the assignment's route and function names.
- `bleach` (HTML sanitising) and `email-validator` are runtime dependencies the lecture does not name. bleach was added because stored HTML from CKEditor is otherwise an XSS risk; email-validator because WTForms needs it.
- Delete is a POST with a CSRF token (the lecture uses a GET link); logout stays a GET as in the lecture. Emails are trimmed and lower-cased.
- Criteria 3, 5 and 9 of QC-LANG-001 were judged by the stand-in because English and IT are the reviewer's own language and domain.
- Two opengrep findings are suppressed with a reason in the code: the Django CSRF rule on the Jinja delete forms (false positive, the form carries the token).

## Notes for the reader

- I once ran `git checkout` on uncommitted plan edits and lost them; I re-applied them from a saved script before any commit, so nothing reached the history.
- The screenshots come from `bash scripts/screenshots/capture_screenshot.sh --all`, which runs a headless browser only inside Docker with example data (Jane Doe, John Doe, Mary Roe).
- The Gravatar images in the screenshots load from gravatar.com during the capture.
- Pull request status cannot be bound to the desktop app for Gitea, so no CI monitor was set; each pull request was merged through the API after its three required checks passed.
- Repository description and topics were set through the host API with the token from the personal `.env`, which was not read into any file or printed.
- opengrep ran locally before every push: 0 findings each time.

## Stopped on

Nothing: no stop rule was triggered. The scope change was handled as the rules require (stop, amend the plan, get it accepted).
