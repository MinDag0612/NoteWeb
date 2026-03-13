# Phase 2 - Traditional Deployment on Ubuntu

For assignment-wide status and ownership tracking, start with `../CHECKLIST_MASTER.md`.

This directory contains the production templates and verification assets for the host-based deployment phase.

## Goal

Deploy the current application on an Ubuntu cloud server without Docker for app runtime, while keeping the system secure, persistent after reboot, and reachable through HTTPS.

## Directory Layout

- `config/nginx/`: Nginx virtual host templates for HTTP and HTTPS modes.
- `config/systemd/`: Non-root backend service template.
- `env/`: Safe environment template for Phase 2 host deployment.
- `runbook/`: Step-by-step deployment and validation procedures.
- `evidence/`: Checklist and placeholders for screenshots/log captures.

## What Is Included

- Reverse proxy templates for SPA + backend API + uploaded file access.
- Backend process persistence template using systemd.
- Deployment runbook and validation checklist in technical English.
- Evidence checklist that maps exactly to assignment requirements.

## What Must Be Completed Manually

- Provision Ubuntu cloud server and configure firewall/security groups.
- Register domain and configure DNS A records.
- Issue HTTPS certificates with Let's Encrypt.
- Capture operational screenshots and logs under `phase2/evidence/`.

## Compliance Notes

This folder is intentionally template-driven. It does not fabricate runtime evidence.
All screenshots and runtime outputs must be collected from the real server.
