# Review of the wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-007 |
| CrossReference | [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [c0a8375] |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Criterion 14 closed after publishing: verdict Go | [c0a8375] |

---

## Artifact Under Review

- Instance reviewed: the wiki in `docs/wiki/` (no ID; documentation, not an artifact)
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: n/a (a wiki is not a PO-language artifact type)
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Starts with bold title, then one English list, `Home` first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Home and the six step pages are listed; a link check found no dead link. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No related wikis, so no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages section is last; one line each for English, Dansk, Bahasa Malaysia. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is not produced by a generator that the wiki publishes with, so there is no generator comment to carry. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English, Danish (da) and Bahasa Malaysia (ms). |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 7 English pages (Home and 6 steps) each exist in da and ms; a script found no missing page. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | All 21 pages start with the language line, current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Files are `<Page>-da.md` and `<Page>-ms.md`; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Code blocks and commands are the same in all languages. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | On 2026-11-11 the host returned HTTP 200 for Home in each language, `_Sidebar` and a step page, and for a screenshot (`raw` URL); the sidebar and page links point to existing pages. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | Pass | No layout rule changed. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All 22 files are directly in `docs/wiki/`. |

## Overall Verdict

Go — every Mandatory criterion passes; criterion 14 was closed after the merge by checking the published wiki. Criterion 7 is N-A because no generator produces the sidebar.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None (the published-wiki check is done) | S01 | |

---

[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[c0a8375]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/069-blog-capstone-part-4/commit/c0a837560baf15f352e796e434b69537364f51b6
