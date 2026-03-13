# Midterm Master Checklist (Single Source of Truth)

Last updated: 2026-03-13

Use this file as the first entry point for teammates and reviewers.
It maps assignment requirements to:

1. the authoritative repository location,
2. the evidence location that must be submitted,
3. the current completion status.

Status legend:

- `Implemented in repo`: code/config/runbook exists in repository.
- `Pending evidence`: real screenshot/log/link is still missing.
- `Pending platform action`: must be done on GitHub/GitLab/cloud platform.
- `Done`: requirement and evidence are complete.

## 1) Minimum Application Requirements

| ID | Requirement | Repository source of truth | Evidence to collect | Status | Owner |
| --- | --- | --- | --- | --- | --- |
| APP-01 | Working web interface | `src/`, `public/`, `backendSrc/main.py` | Running app screenshots in `phase2/evidence/` and `phase3/evidence/` | Implemented in repo | TBD |
| APP-02 | Database component | `backendSrc/data/conn.py`, env templates | Database connectivity proof in Phase 2/3 evidence | Implemented in repo | TBD |
| APP-03 | File upload via backend logic | `backendSrc/main.py` (`/upload-image`), `src/components/OpenNote.js` | Upload success proof in Phase 2/3 evidence | Implemented in repo | TBD |

## 2) Phase 1 - Git Workflow and Linux Automation

| ID | Requirement | Repository source of truth | Evidence to collect | Status | Owner |
| --- | --- | --- | --- | --- | --- |
| PH1-01 | Professional repository structure | `README.md`, `phase1/`, `phase2/`, `phase3/` | Repository structure screenshot in `phase1/evidence/` | Implemented in repo | TBD |
| PH1-02 | Professional technical README | `README.md` | Include in technical report references | Implemented in repo | TBD |
| PH1-03 | Correct `.gitignore` and secret hygiene | `.gitignore`, `.env.example`, `docs/SECRETS_HYGIENE_CHECKLIST.md` | Optional screenshot/notes if needed | Implemented in repo | TBD |
| PH1-04 | Ubuntu automation script | `scripts/setup.sh`, `scripts/verify.sh`, `scripts/README.md` | Setup/verify command outputs if required by report | Implemented in repo | TBD |
| PH1-05 | Branch protection on `main` | Git hosting platform settings (external) | `phase1/evidence/branch-protection-main.png` | Pending platform action | TBD |
| PH1-06 | PR-only merge workflow | Git hosting PR history (external) | `phase1/evidence/pull-request-list.png` | Pending platform action | TBD |
| PH1-07 | At least one reviewer per PR | Reviewed PR(s) on platform (external) | `phase1/evidence/reviewed-pr-example.png` | Pending platform action | TBD |
| PH1-08 | All members contribute meaningfully | Contributors/Insights page (external) | `phase1/evidence/contributors-history.png` | Pending platform action | TBD |

## 3) Phase 2 - Traditional Host Deployment

| ID | Requirement | Repository source of truth | Evidence to collect | Status | Owner |
| --- | --- | --- | --- | --- | --- |
| PH2-01 | Ubuntu server hardened (least privilege) | `phase2/runbook/deploy-host.md` | `phase2/evidence/01-server-firewall-security-group.png` | Pending evidence | TBD |
| PH2-02 | Runtime prepared using setup script | `scripts/setup.sh`, `phase2/runbook/deploy-host.md` | setup/verification terminal proof | Pending evidence | TBD |
| PH2-03 | Host-level process persistence | `phase2/config/systemd/noteweb-backend.service` | `phase2/evidence/02-systemd-service-active.png`, `03-systemd-enabled-on-boot.png` | Pending evidence | TBD |
| PH2-04 | Host reverse proxy configuration | `phase2/config/nginx/` | `phase2/evidence/04-nginx-config-enabled.png`, `05-nginx-status.png` | Pending evidence | TBD |
| PH2-05 | Domain + DNS mapping | external DNS provider | `phase2/evidence/06-dns-records.png` | Pending evidence | TBD |
| PH2-06 | HTTPS certificate active | Certbot/Nginx on host | `phase2/evidence/07-https-certificate.png` | Pending evidence | TBD |
| PH2-07 | Full app works over HTTPS | all host runtime artifacts above | `phase2/evidence/08-app-home-over-https.png`, `09-upload-feature-over-https.png`, `10-database-connectivity-proof.png` | Pending evidence | TBD |
| PH2-08 | Survives server reboot | systemd + host setup | `phase2/evidence/11-reboot-persistence-proof.png` | Pending evidence | TBD |

## 4) Phase 3 - Docker + Docker Compose

| ID | Requirement | Repository source of truth | Evidence to collect | Status | Owner |
| --- | --- | --- | --- | --- | --- |
| PH3-01 | Docker and Compose installed on same host | `phase3/runbook/deploy-compose.md` | `phase3/evidence/01-docker-version.png`, `02-compose-version.png` | Pending evidence | TBD |
| PH3-02 | Production Dockerfiles | `phase3/docker/backend/Dockerfile`, `phase3/docker/frontend/Dockerfile` | build screenshots in `phase3/evidence/` | Implemented in repo | TBD |
| PH3-03 | Image registry workflow (build/push/pull) | `phase3/runbook/build-and-publish.md`, `phase3/compose/.env.compose.example` | `03/04/05/06` images in `phase3/evidence/` | Pending evidence | TBD |
| PH3-04 | Compose pulls published image (no server-side build) | `phase3/compose/docker-compose.prod.yml` (`image:` only) | pull/up logs in `phase3/evidence/` | Implemented in repo | TBD |
| PH3-05 | MongoDB runs in Docker | `phase3/compose/docker-compose.prod.yml` (`mongodb` service) | `phase3/evidence/07-docker-ps.png` | Implemented in repo | TBD |
| PH3-06 | Persistent volumes for MongoDB and uploads | `phase3/compose/docker-compose.prod.yml` (`mongo_data`, `uploads_data`) | `phase3/evidence/09-docker-volumes.png` | Implemented in repo | TBD |
| PH3-07 | Restart policy and reboot behavior | compose `restart: unless-stopped`, runbook reboot step | `phase3/evidence/11-restart-persistence-after-reboot.png` | Pending evidence | TBD |
| PH3-08 | Host HTTPS proxy kept, upstream moved to containers | `phase3/runbook/deploy-compose.md`, host nginx config from Phase 2 | `phase3/evidence/10-https-app-container-runtime.png` | Pending evidence | TBD |
| PH3-09 | No PM2/systemd for app runtime in Phase 3 | `phase3/runbook/validation-checklist.md` | logs/screenshots proving container-only runtime | Pending evidence | TBD |

## 5) Final Deliverables Checklist

| ID | Deliverable | Repository location | Status | Owner |
| --- | --- | --- | --- | --- |
| DLV-01 | Structured repo with phase1/phase2/phase3 artifacts | root + phase folders | In progress | TBD |
| DLV-02 | Technical report in official template | `docs/TECHNICAL_REPORT_TEMPLATE.md` (fill with real data) | In progress | TBD |
| DLV-03 | Slides (3 phases + comparison) | store in `docs/` or external link in report | Pending | TBD |
| DLV-04 | Video demo (Phase 2 + Phase 3 + evidence) | store link in report and/or `docs/` | Pending | TBD |
| DLV-05 | Live demo readiness (Phase 3 HTTPS domain) | runtime environment + `phase3/` runbooks | Pending | TBD |

## 6) Quick Navigation (Who Should Read What)

- New teammate: read `README.md` then this file, then phase readmes.
- DevOps implementer: follow `phase2/runbook/deploy-host.md` and `phase3/runbook/deploy-compose.md`.
- Evidence collector: follow `phase1/evidence/`, `phase2/evidence/`, `phase3/evidence/` checklists.
- Report writer: use `docs/TECHNICAL_REPORT_TEMPLATE.md` and link each section to evidence files.
