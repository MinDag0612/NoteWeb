# Scripts Overview

This directory contains Phase 1 automation assets for the DevOps midterm project.

## Purpose

The scripts in this folder are intended to make Ubuntu host preparation explicit, repeatable, and easy to audit. They do not contain secrets and they do not replace later deployment steps such as Nginx configuration, TLS provisioning, or Docker orchestration.

## Files

- `setup.sh`: prepares the host runtime for this repository
- `verify.sh`: performs a lightweight post-setup verification

## `setup.sh`

`setup.sh` is designed for Ubuntu-based servers and assumes that the repository will be placed under `/var/www/NoteWeb` unless overridden through environment variables.

It performs the following actions:

1. Updates apt package metadata.
2. Installs system packages required by the React and FastAPI stack.
3. Installs Node.js LTS when it is missing or older than the configured version.
4. Creates runtime directories (`logs/`, `uploads/`, and `data/`) for later deployment phases.
5. Creates a backend Python virtual environment.
6. Installs backend Python dependencies from `backendSrc/requirements.txt`.
7. Installs frontend dependencies from `package.json` using `npm ci` or `npm install`.

Supported overrides:

- `PROJECT_DIR`
- `FRONTEND_DIR`
- `BACKEND_DIR`
- `PYTHON_VENV_DIR`
- `NODE_MAJOR`
- `INSTALL_FRONTEND_DEPS`
- `INSTALL_BACKEND_DEPS`
- `INSTALL_NGINX`
- `INSTALL_CERTBOT`

Example:

```bash
PROJECT_DIR=/srv/noteweb bash scripts/setup.sh
```

## `verify.sh`

`verify.sh` is a read-only validation helper. It reports:

- whether `node`, `npm`, `python3`, and `pip` are available
- the detected runtime versions
- whether the expected runtime directories exist
- whether the backend virtual environment is present

Example:

```bash
bash scripts/verify.sh
```

## Operational Guidance

- Run `setup.sh` on a fresh Ubuntu host before manual deployment work in Phase 2.
- Run `verify.sh` after setup or before recording evidence for the technical report.
- Keep secrets in `.env` only. Never add secrets to these scripts.
- Use `INSTALL_NGINX=1` and `INSTALL_CERTBOT=1` only when you intentionally want the script to install those packages.
