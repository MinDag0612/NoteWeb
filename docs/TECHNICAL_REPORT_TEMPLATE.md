# Technical Report Template - DevOps Midterm

> Replace all placeholders with real project data. Do not fabricate evidence.

## Cover Information

- Project title:
- Team name:
- Course / class:
- Submission date:
- Repository URL:
- Public domain used for deployment:

## Executive Summary

- Problem statement
- Proposed architecture
- Final deployment outcomes

## Phase 1 - Git Workflow and Linux Automation

### Objective

### Method

### Implemented Artifacts

- Repository structure
- README and `.gitignore`
- Setup/verification scripts
- Branching strategy and branch protection settings

### Evidence

Reference files under `phase1/evidence/`:

- branch protection screenshots
- PR list and reviewed PR examples
- contributor history screenshots

### System Behavior

- How setup script prepares Ubuntu runtime
- Security controls for secrets management

## Phase 2 - Traditional Host-Based Deployment

### Objective

### Method

### Implemented Artifacts

Reference files under `phase2/`:

- nginx config
- systemd service template
- env template
- deployment runbook and validation checklist

### Evidence

Reference files under `phase2/evidence/`:

- DNS mapping
- HTTPS certificate
- running app over HTTPS
- backend persistence across reboot
- upload and database operation proof

### System Behavior

- Request flow from HTTPS endpoint to backend
- Runtime persistence and failure recovery behavior

## Phase 3 - Docker + Docker Compose Deployment

### Objective

### Method

### Implemented Artifacts

Reference files under `phase3/`:

- backend/frontend Dockerfiles
- compose deployment definitions
- build/push/pull runbooks
- validation checklist

### Evidence

Reference files under `phase3/evidence/`:

- Docker build and push outputs
- Docker Hub tag screenshots
- compose pull and container runtime status
- volume persistence and restart behavior

### System Behavior

- Host reverse proxy path after container migration
- data and upload persistence with Docker volumes

## Comparative Analysis - Phase 2 vs Phase 3

| Criterion | Phase 2 (Host Runtime) | Phase 3 (Compose Runtime) | Conclusion |
| --- | --- | --- | --- |
| Deployment speed |  |  |  |
| Operational complexity |  |  |  |
| Isolation and reproducibility |  |  |  |
| Rollback approach |  |  |  |
| Data persistence model |  |  |  |
| Security posture |  |  |  |

## Architecture Diagrams

Add or link diagrams from `docs/diagrams/`:

- high-level architecture
- Phase 2 runtime topology
- Phase 3 runtime topology

## Team Contribution Evidence

| Member | Main Contributions | Related Commits/PRs | Evidence Link |
| --- | --- | --- | --- |
| Member 1 |  |  |  |
| Member 2 |  |  |  |
| Member 3 |  |  |  |

## Risks and Limitations

- unresolved constraints
- assumptions and impacts

## Conclusion and Future Improvements

- summary of achieved compliance
- recommended next improvements
