# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted on a Go review, RC-002; autonomous, not independent | pending |

---

## Purpose

Identify who is involved in the Day 69 documentation project and what each needs from it. The analysis uses the power/interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct, reviewed record of what the lecture teaches |
| S02 | Udemy coursists | Course participants who share code and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable instructions with the assignment's function names |
| S03 | GitHub viewers | Readers who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and reviews every artifact.
- **Keep Informed (S02):** cannot change the project but depends on the README instructions and wiki.
- **Monitor (S03):** casual readers; served by the repository description, topics and README.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every artifact is reviewed before the next step | Supportability |
| CN-002 | S02 | Instructions that run as written (local `.venv`, tests) | Usability |
| CN-003 | S02 | Wiki readable in their own language | Usability |
| CN-004 | S03 | Clear description, topics and README at first glance | Usability |
| CN-005 | S03 | No runtime dependencies to install | Functionality |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| COM-001 | Chat and pull request | Per milestone | Pull request with closed issues | All milestones |
| COM-002 | Repository README and wiki | On merge | Published documentation | MIL-002, MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants runnable code; the project delivers documentation only | S02, S01 | The README states the scope and how to set up a local `.venv` |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | Objective 5 in [BC-001] |
| S02 | CN-002, CN-003 | Objectives 1 and 2 in [BC-001] |
| S03 | CN-004, CN-005 | Objectives 3 and 4 in [BC-001] |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Accepted by stand-in on RC-002 (Go); open to challenge | 2026-11-11 |

---

[BC-001]: ./business-case.md
