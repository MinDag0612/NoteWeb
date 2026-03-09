# Requirements Traceability Matrix (Repository + Manual Evidence)

This document maps assignment requirements to current repository assets and explicitly separates local completion from manual external completion.

## A. Minimum Application Requirements

| Requirement | Status | Evidence |
| --- | --- | --- |
| Working web interface | Implemented in code | `src/`, `public/` |
| Database component | Implemented in code | `backendSrc/data/conn.py` |
| File upload processed by backend | Implemented in code | `backendSrc/main.py`, `src/components/OpenNote.js` |

## B. Phase 1 (Git Workflow + Automation)

| Requirement | Status | Evidence |
| --- | --- | --- |
| Professional repo structure | Implemented | root tree + phase directories |
| Comprehensive README | Implemented | `README.md` |
| Correct `.gitignore` | Implemented | `.gitignore` |
| Automation script for Ubuntu setup | Implemented | `scripts/setup.sh` |
| Verification script | Implemented | `scripts/verify.sh` |
| Branch protection and PR discipline | Manual platform action required | `phase1/evidence/README.md` |

## C. Phase 2 (Traditional Deployment)

| Requirement | Status | Evidence |
| --- | --- | --- |
| Reverse proxy templates | Implemented in repo | `phase2/config/nginx/` |
| Process manager template | Implemented in repo | `phase2/config/systemd/` |
| Host env template | Implemented in repo | `phase2/env/phase2.env.example` |
| Deployment runbook + validation checklist | Implemented in repo | `phase2/runbook/` |
| DNS/HTTPS/running-app evidence | Manual cloud action required | `phase2/evidence/` |

## D. Phase 3 (Docker + Compose)

| Requirement | Status | Evidence |
| --- | --- | --- |
| Production Dockerfiles | Implemented in repo | `phase3/docker/` |
| Compose project using published images | Implemented in repo | `phase3/compose/docker-compose.prod.yml` |
| DB + upload persistent volumes | Implemented in repo | compose `volumes` |
| Build/push/pull/deploy runbooks | Implemented in repo | `phase3/runbook/` |
| Docker runtime evidence | Manual cloud action required | `phase3/evidence/` |

## E. Technical Report Requirements

| Requirement | Status | Evidence |
| --- | --- | --- |
| Formal report structure by 3 phases | Implemented as template | `docs/TECHNICAL_REPORT_TEMPLATE.md` |
| Comparative analysis section | Implemented as template | same report template |
| Diagram placeholders | Implemented | `docs/diagrams/README.md` |
| Team contribution matrix | Implemented as template | report template section |

## Final Note

Repository artifacts are now prepared for strict submission, but real deployment/governance evidence must still be captured from actual infrastructure and Git platform activity.
