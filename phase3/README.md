# Phase 3 - Docker + Docker Compose Deployment

For assignment-wide status and ownership tracking, start with `../CHECKLIST_MASTER.md`.

This directory contains production templates and runbooks for containerizing the application on the same Ubuntu server used in Phase 2.

## Goal

Replace host-based app runtime with Docker Compose while preserving:

- the HTTPS domain and host-level reverse proxy from Phase 2
- backend API behavior and upload functionality
- data persistence for MongoDB and uploaded files

## Directory Layout

- `docker/`: production Dockerfiles for backend and frontend.
- `compose/`: production compose project files (`image:` pull model).
- `runbook/`: build/publish/deploy/validation instructions.
- `evidence/`: screenshot and log checklist for grading.

## Key Compliance Points Implemented

- Compose file uses pre-published images (`image:`), not `build:`.
- MongoDB and upload storage are both persistent volumes.
- Restart policy is defined for all runtime services.
- App runtime does not depend on PM2/systemd in Phase 3.
- Host-level Nginx remains the public HTTPS entrypoint.

## Manual Steps Still Required

- Build and push images to your own registry namespace.
- Deploy on actual Ubuntu server and configure runtime secrets.
- Update Nginx upstream targets to container loopback ports.
- Capture real evidence under `phase3/evidence/`.
