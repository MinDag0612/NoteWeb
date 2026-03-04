# NoteWeb Midterm Project

## Overview

This repository contains a note management web application prepared for a DevOps-oriented midterm project. The system consists of a React single-page frontend and a FastAPI backend backed by MongoDB. Users can authenticate, create and manage notes, and upload note images through backend logic.

The repository is organized to satisfy Phase 1 expectations of the midterm specification: clear documentation, safe environment management, reproducible Ubuntu setup scripts, and a structured place for later deployment evidence.

## Features

- Web user interface implemented as a React SPA
- FastAPI backend for authentication and note management
- MongoDB persistence for users and notes
- File upload flow handled by the backend and stored through Cloudinary
- Local authentication and Google Sign-In support
- Phase-based repository layout for later deployment deliverables

## Tech Stack

### Frontend

- React 19
- Create React App
- React Router
- Bootstrap 5

### Backend

- Python 3
- FastAPI
- PyMongo
- `python-jose` for JWT handling
- `bcrypt` for password verification
- Cloudinary SDK
- Google authentication libraries

### Data and Infrastructure

- MongoDB
- Shell automation for Ubuntu host preparation
- Nginx and systemd placeholders for later deployment phases

## Repository Structure

```text
.
|-- backendSrc/           # FastAPI application, schemas, MongoDB helpers
|-- public/               # CRA public assets
|-- src/                  # React application source
|-- scripts/              # Phase 1 automation and verification scripts
|-- phase1/               # Phase 1 deliverables, checklist, and evidence placeholders
|-- phase2/               # Phase 2 placeholder for traditional deployment artifacts
|-- phase3/               # Phase 3 placeholder for Docker artifacts
|-- .env.example          # Safe environment template
|-- package.json          # Frontend dependencies and scripts
`-- backendSrc/requirements.txt
```

Generated output such as `build/` is intentionally excluded from version control and must be recreated locally with `npm run build`.

## Local Setup

### Assumptions

- Local development uses Node.js 20 LTS or newer.
- Local development uses Python 3.10 or newer.
- The example environment file assumes the backend is started directly on `http://127.0.0.1:8000` without a reverse proxy.

### 1. Clone the repository

```bash
git clone https://github.com/MinDag0612/NoteWeb.git
cd NoteWeb
```

### 2. Create the local environment file

```bash
cp .env.example .env
```

Update `.env` with real credentials before starting the application. Never commit `.env`.

### 3. Install and run the backend

From the repository root:

```bash
python -m venv backendSrc/.venv
```

Linux or macOS:

```bash
source backendSrc/.venv/bin/activate
pip install -r backendSrc/requirements.txt
uvicorn backendSrc.main:app --reload --host 127.0.0.1 --port 8000
```

PowerShell:

```powershell
.\backendSrc\.venv\Scripts\Activate.ps1
pip install -r backendSrc\requirements.txt
uvicorn backendSrc.main:app --reload --host 127.0.0.1 --port 8000
```

### 4. Install and run the frontend

Open a second terminal in the repository root:

```bash
npm install
npm start
```

The frontend is served by Create React App at `http://localhost:3000`.

### 5. Optional local build verification

```bash
npm run build
```

## Environment Variables

Use `.env.example` as the only committed template. Copy it to `.env` and replace placeholders with real values.

| Variable | Required | Description |
| --- | --- | --- |
| `REACT_APP_API_PROCESS_LOGIN` | Yes | Frontend URL for the email/password login endpoint |
| `REACT_APP_API_PROCESS_LOGIN_GG` | Yes | Frontend URL for the Google login endpoint |
| `REACT_APP_API_NOTES` | Yes | Frontend URL used to fetch notes |
| `REACT_APP_API_ADD_NOTE` | Yes | Frontend URL used to create a new note |
| `REACT_APP_API_DELETE_NOTE` | Yes | Frontend URL used to delete a note |
| `REACT_APP_API_UPDATE_NOTE` | Yes | Frontend URL used to update a note |
| `REACT_APP_API_IMAGE_UPLOAD` | Yes | Frontend URL used to upload note images |
| `REACT_APP_GOOGLE_CLIENT_ID` | Recommended | Google Sign-In client ID for the frontend; a legacy fallback exists in code for compatibility |
| `CLOUDY_NAME` | Yes | Cloudinary cloud name used by the backend upload endpoint |
| `CLOUDY_API_KEY` | Yes | Cloudinary API key |
| `CLOUDY_SECRET` | Yes | Cloudinary API secret |
| `MONGODB_URI` | Yes | MongoDB connection string used by backend data access utilities |
| `JWT_SECRET_KEY` | Yes | Secret key used to sign backend JWT access tokens |
| `GOOGLE_CLIENT_ID` | Recommended | Google Sign-In client ID for backend token verification; a legacy fallback exists in code for compatibility |

For local development, the sample values point directly to the FastAPI process. For reverse-proxied environments, these values can be changed to `/api/...` style routes.

## Automation

Phase 1 introduces the `scripts/` directory for reusable Linux automation.

- `scripts/setup.sh`: prepares an Ubuntu host with the runtimes and directories required by this project. It installs system packages for Node.js and Python, creates runtime folders, prepares the backend virtual environment, and installs frontend dependencies.
- `scripts/verify.sh`: performs a lightweight verification of tool versions and expected runtime directories after setup.
- `scripts/README.md`: explains assumptions, configurable variables, and expected usage for the scripts.

Run `scripts/setup.sh` on a fresh Ubuntu host before performing a manual deployment in Phase 2. The script intentionally does not contain secrets and does not deploy the application by itself.

## High-Level Deployment Approach

### Phase 2: Traditional Host-Based Deployment

The application will be deployed directly on an Ubuntu cloud server. The host will be prepared with `scripts/setup.sh`, the backend will run inside a Python virtual environment, the frontend will be built for production, and Nginx plus a service manager such as systemd will be used for HTTPS exposure and process persistence.

### Phase 3: Docker and Docker Compose Deployment

The same application will later be packaged into containers. The web application will be built into a production image, published to a registry, and deployed alongside a containerized MongoDB instance through Docker Compose. The host-level reverse proxy configured in Phase 2 will be retained and pointed at the containerized web service.

## Git Workflow Expectations

This repository is intended to be maintained under a professional pull-request workflow:

- All implementation work should happen on feature branches.
- The `main` branch should be protected against direct pushes and force pushes.
- Every merge to `main` should occur through a pull request.
- Each pull request should have a clear title, a concise technical description, and at least one reviewer approval.
- Evidence of branch protection, pull requests, reviews, and contributor history should be stored under `phase1/evidence/`.

## Security Notes

- Never commit `.env`, tokens, passwords, API keys, or database credentials.
- Commit only `.env.example` with placeholder values.
- Do not commit generated artifacts such as `build/`, dependency directories, or runtime logs.
- Screenshots and evidence for the report must be real project evidence; they must not be fabricated.

## Phase Deliverables

- `phase1/` contains the Phase 1 checklist, evidence requirements, and summary notes.
- `phase2/` is reserved for the traditional Ubuntu deployment artifacts.
- `phase3/` is reserved for the Docker and Docker Compose artifacts.

## Legacy Deployment Notes

The repository still contains early deployment working files such as `nginx.conf`, `backend.service`, and `Deploy-step.md`. These are preserved as reference material and will be formalized during Phase 2.
