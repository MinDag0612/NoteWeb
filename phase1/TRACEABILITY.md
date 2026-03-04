# Phase 1 Requirements Traceability

This document maps the repository state to the Phase 1-related requirements in the midterm specification. It distinguishes between items that can be satisfied directly in the repository and items that must be completed manually on GitHub or GitLab.

## Section 2: Application Requirements

| Requirement | Status | Evidence |
| --- | --- | --- |
| Fully working web interface | Satisfied in codebase | React SPA under `src/` and FastAPI backend under `backendSrc/` |
| Database component | Satisfied in codebase | MongoDB connection in `backendSrc/data/conn.py` |
| File upload processed by backend logic | Satisfied in codebase | Upload endpoint in `backendSrc/main.py` and frontend upload flow in `src/components/OpenNote.js` |
| Application must run locally before deployment | Documented; runtime verification remains manual | Local setup instructions in root `README.md` |

## Section 3: Git/GitHub Collaboration Requirements

| Requirement | Status | Evidence |
| --- | --- | --- |
| All members appear in commit history with meaningful contributions | Manual platform activity required | Must be demonstrated through real team commits and contributor history |
| Branch protection on `main` with PR requirement | Manual platform configuration required | `phase1/evidence/README.md` lists the screenshots to collect |
| At least one reviewer per PR | Manual platform configuration required | Must be enabled and demonstrated in reviewed PRs |
| All merges into `main` via PRs only | Manual workflow enforcement required | Must be visible in PR history |
| PRs contain clear titles, descriptions, and review evidence | Manual workflow enforcement required | Must be captured from actual PRs |
| Technical report includes Git workflow screenshots or links | Prepared with evidence placeholders | Store real artifacts under `phase1/evidence/` |

## Section 4.1: Repository Structure and Documentation Standards

| Requirement | Status | Evidence |
| --- | --- | --- |
| Professional repository organization | Satisfied in repository | Root README, `scripts/`, `phase1/`, `phase2/`, and `phase3/` |
| Comprehensive README in technical English | Satisfied in repository | Root `README.md` |
| Local run instructions | Satisfied in repository | Root `README.md` local setup section |
| Environment variables documented safely | Satisfied in repository | `.env.example` and environment variable table in `README.md` |
| High-level later deployment approach | Satisfied in repository | Phase 2 and Phase 3 overview in `README.md` |
| Automation scripts documented | Satisfied in repository | `scripts/README.md` |
| Correct `.gitignore` excluding generated files and secrets | Satisfied in repository | Root `.gitignore` |
| Dedicated scripts folder exists | Satisfied in repository | `scripts/` |
| Supplementary documentation directory available | Satisfied in repository | `phase1/docs/` |

## Section 4.2: Collaborative Git Workflow and Branch Protection Policies

| Requirement | Status | Evidence |
| --- | --- | --- |
| Work occurs in feature branches | Manual team workflow required | Must be demonstrated in branch and PR history |
| Merges to `main` occur exclusively via PRs | Manual team workflow required | Must be demonstrated in PR history |
| Main branch blocks direct commits and force pushes | Manual platform configuration required | Must be demonstrated with branch protection screenshots |
| Pull requests include reviewer approval | Manual team workflow required | Must be demonstrated with reviewed PR screenshots |
| Contribution patterns show participation from all members | Manual team workflow required | Must be demonstrated in contributor history |

## Section 4.3: Linux Automation Script Requirements

| Requirement | Status | Evidence |
| --- | --- | --- |
| Functional setup script exists | Satisfied in repository | `scripts/setup.sh` |
| Installs system dependencies for project stack | Satisfied in repository | `scripts/setup.sh` installs Ubuntu packages for Node.js and Python |
| Prepares runtime environment for application execution | Satisfied in repository | `scripts/setup.sh` prepares the backend virtual environment and frontend dependencies |
| Creates required directory structures | Satisfied in repository | `scripts/setup.sh` creates `logs/`, `uploads/`, and `data/` |
| No hard-coded credentials in script | Satisfied in repository | `scripts/setup.sh` contains no secrets |
| Includes concise explanatory comments | Satisfied in repository | Comments added at major setup steps in `scripts/setup.sh` |

## Section 4.4: Summary of Expected Outcomes

### Repository-Level Outcome

The repository now satisfies the structural expectations of Phase 1:

- documented in professional English
- organized with explicit phase deliverable directories
- equipped with reusable setup and verification scripts
- protected from accidental secret and artifact commits through `.gitignore`
- prepared with evidence placeholders for the technical report

### Manual Outcome Still Required

The following items cannot be manufactured inside the repository and must be completed by the actual team:

1. configure branch protection on the hosting platform
2. use feature branches and pull requests for real work
3. collect reviewer approvals
4. capture screenshots or links for the report
5. ensure all team members have meaningful contribution history
