# Phase 3 Build and Publish Runbook

The assignment requires compose to pull published images. Build and push on your workstation or CI first.
This repository includes a root `.dockerignore` used by both image builds.

## 1. Backend Image

```bash
docker build -f phase3/docker/backend/Dockerfile -t <registry-user>/noteweb-backend:<tag> .
docker push <registry-user>/noteweb-backend:<tag>
```

## 2. Frontend Image

```bash
docker build -f phase3/docker/frontend/Dockerfile -t <registry-user>/noteweb-frontend:<tag> .
docker push <registry-user>/noteweb-frontend:<tag>
```

## 3. Capture Evidence

Capture and store screenshots/logs for:

- successful `docker build`
- successful `docker push`
- image tags visible in registry

Place artifacts under `phase3/evidence/`.
