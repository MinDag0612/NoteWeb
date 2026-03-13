# NoteWeb Midterm Repository (Compliance-Oriented)

## 0. Start Here (Team + Reviewer)

Use this reading order so anyone can understand scope, status, and intent quickly:

1. `CHECKLIST_MASTER.md` (master mapping from assignment checklist to repo evidence and status)
2. `README.md` (architecture, local run instructions, repository conventions)
3. `phase1/README_PHASE1.md`, `phase2/README.md`, `phase3/README.md`
4. `phase1/evidence/`, `phase2/evidence/`, `phase3/evidence/` checklists

Single source of truth for graded deployment artifacts:

- Phase 1 governance and automation: `phase1/`
- Phase 2 host deployment: `phase2/`
- Phase 3 Docker deployment: `phase3/`
- Deprecated compatibility references: `legacy/` (not primary grading artifacts)

## 1. Project Overview

This repository contains a note management web application prepared for a DevOps midterm submission.
The stack is:

- Frontend: React (Create React App)
- Backend: FastAPI (Python)
- Database: MongoDB

Core user flows include authentication, notes CRUD, and image upload handled by backend logic.

## 2. Architecture Summary

- Frontend runs as a single-page application.
- Backend exposes REST endpoints for login, note operations, and uploads.
- MongoDB stores user and note documents.
- Uploads support hybrid storage:
  - local filesystem (default, required for volume persistence)
  - Cloudinary fallback (optional)

## 3. Repository Structure

```text
.
|-- backendSrc/                    # FastAPI app, DB access, schemas
|-- public/                        # Frontend public assets
|-- src/                           # Frontend source
|-- scripts/                       # Ubuntu setup + verification scripts
|-- phase1/                        # Git workflow, traceability, and phase-1 evidence scaffolding
|-- phase2/                        # Host-based deployment configs/runbooks/evidence checklist
|-- phase3/                        # Docker + Compose configs/runbooks/evidence checklist
|-- docs/                          # Technical report and diagram templates
|-- legacy/                        # Deprecated compatibility references
|-- CHECKLIST_MASTER.md            # Master assignment traceability and status
|-- .env.example                   # Safe config template
|-- .gitignore
`-- package.json
```

## 4. Local Development Setup

### Prerequisites

- Node.js 20+
- Python 3.10+
- MongoDB (local or remote)

### Steps

```bash
git clone <your-repository-url>
cd NoteWeb
cp .env.example .env
```

Configure `.env` values before running the app.

Backend:

```bash
python -m venv backendSrc/.venv
# Linux/macOS
source backendSrc/.venv/bin/activate
# PowerShell
# .\backendSrc\.venv\Scripts\Activate.ps1
pip install -r backendSrc/requirements.txt
uvicorn backendSrc.main:app --reload --host 127.0.0.1 --port 8000
```

Frontend (second terminal):

```bash
npm install
npm start
```

## 5. Environment Variables

Use `.env.example` as the only committed template.

| Variable | Purpose |
| --- | --- |
| `REACT_APP_API_PROCESS_LOGIN` | Frontend login endpoint |
| `REACT_APP_API_PROCESS_LOGIN_GG` | Frontend Google login endpoint |
| `REACT_APP_API_NOTES` | Frontend notes listing endpoint |
| `REACT_APP_API_ADD_NOTE` | Frontend create-note endpoint |
| `REACT_APP_API_DELETE_NOTE` | Frontend delete-note endpoint |
| `REACT_APP_API_UPDATE_NOTE` | Frontend update-note endpoint |
| `REACT_APP_API_IMAGE_UPLOAD` | Frontend upload endpoint |
| `REACT_APP_GOOGLE_CLIENT_ID` | Google client ID used by frontend |
| `MONGODB_URI` | MongoDB connection URI |
| `JWT_SECRET_KEY` | JWT signing secret |
| `GOOGLE_CLIENT_ID` | Google client ID used by backend verification |
| `BACKEND_CORS_ORIGINS` | Comma-separated allowed origins for backend CORS |
| `API_ROOT_PATH` | FastAPI root path (default `/api`) |
| `UPLOAD_STORAGE_MODE` | `local`, `cloudinary`, or `hybrid` |
| `UPLOAD_LOCAL_DIR` | Local upload directory path |
| `PUBLIC_BASE_URL` | Public base URL used to generate upload links |
| `UPLOAD_CLOUDINARY_FOLDER` | Cloudinary folder name |
| `CLOUDY_NAME` | Cloudinary cloud name (optional unless cloud mode used) |
| `CLOUDY_API_KEY` | Cloudinary API key |
| `CLOUDY_SECRET` | Cloudinary API secret |

## 6. Upload Storage Behavior

- `UPLOAD_STORAGE_MODE=local`: store uploads on server filesystem only.
- `UPLOAD_STORAGE_MODE=cloudinary`: store uploads on Cloudinary only.
- `UPLOAD_STORAGE_MODE=hybrid` (default): try local storage first, then Cloudinary fallback.

The `/upload-image` API response format remains unchanged (`{"url": "..."}`).

## 7. DevOps Phase Assets

Assignment-level traceability starts at `CHECKLIST_MASTER.md`.

### Phase 1

See `phase1/` for repository governance traceability and Git workflow evidence scaffolding.

### Phase 2 (Traditional Host-Based Deployment)

See:

- `phase2/config/nginx/`
- `phase2/config/systemd/`
- `phase2/env/phase2.env.example`
- `phase2/runbook/deploy-host.md`
- `phase2/runbook/validation-checklist.md`

### Phase 3 (Docker + Docker Compose)

See:

- `phase3/docker/`
- `phase3/compose/docker-compose.prod.yml`
- `phase3/runbook/build-and-publish.md`
- `phase3/runbook/deploy-compose.md`
- `phase3/runbook/validation-checklist.md`

## 8. Git and Collaboration Requirements

This assignment requires real workflow evidence on your Git hosting platform:

- protected `main` branch
- pull-request-only merges
- reviewer approval requirement
- no direct commits to `main`
- visible meaningful contributions from all team members

Capture those artifacts under `phase1/evidence/`.

## 9. Technical Report Scaffolding

- `docs/TECHNICAL_REPORT_TEMPLATE.md`
- `docs/diagrams/README.md`

These templates are provided to structure a formal report by Phase 1/2/3, including comparative analysis and contribution evidence.

## 10. Security and Repository Hygiene

- Never commit `.env` or live secrets.
- Keep certificate/private key files out of git.
- Do not fabricate screenshots, PR history, DNS, HTTPS, or Docker registry evidence.
- Store only real artifacts collected from actual environments.
- Use `docs/SECRETS_HYGIENE_CHECKLIST.md` if credentials were exposed in git history before cleanup.

## 11. Legacy References

Deprecated compatibility files are stored under `legacy/`:

- `legacy/nginx.conf`
- `legacy/backend.service`
- `legacy/Deploy-step.md`

Primary, graded deployment artifacts are under `phase2/` and `phase3/`.
