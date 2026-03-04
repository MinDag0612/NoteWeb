# Phase 1 Compliance Checklist

This checklist records the repository changes completed for Phase 1 and identifies the evidence that must still be collected manually from GitHub or GitLab.

| Requirement | Status | Repository Evidence | How to Verify |
| --- | --- | --- | --- |
| Professional root README exists | Done in repo | `README.md` | Open `README.md` and confirm that it documents overview, stack, local setup, env vars, automation, deployment approach, Git workflow, and security notes |
| Dedicated automation directory exists | Done in repo | `scripts/setup.sh`, `scripts/verify.sh`, `scripts/README.md` | Run `bash -n scripts/setup.sh` and `bash -n scripts/verify.sh`; review `scripts/README.md` |
| Ubuntu setup script prepares runtime environment | Done in repo | `scripts/setup.sh` | Run `bash scripts/setup.sh --help` and inspect the script comments and package installation steps |
| Safe environment template exists | Done in repo | `.env.example` | Run `git ls-files .env.example` and confirm that `.env.example` contains placeholders only |
| Real `.env` must not be tracked | Manual verification after index cleanup | `.gitignore`, `.env.example` | Run `git ls-files .env`; the command must return no tracked file after cleanup |
| Generated frontend artifacts must not be tracked | Manual verification after index cleanup | `.gitignore` | Run `git ls-files build`; the command must return no tracked files after cleanup |
| `.gitignore` excludes secrets and generated output | Done in repo | `.gitignore` | Run `git check-ignore -v .env build node_modules` |
| Deliverable directories `phase1/`, `phase2/`, and `phase3/` exist | Done in repo | `phase1/`, `phase2/`, `phase3/` | Run `rg --files phase1 phase2 phase3` |
| Evidence checklist for Git workflow exists | Done in repo | `phase1/evidence/README.md` | Open `phase1/evidence/README.md` |
| Branch protection on `main` is enabled | Manual evidence required | `phase1/evidence/` | Capture screenshots from repository settings showing PR requirements and restricted direct pushes |
| Pull requests and reviews are documented | Manual evidence required | `phase1/evidence/` | Capture screenshots or links to representative PRs with review approvals |
| Contributors from all team members are visible | Manual evidence required | `phase1/evidence/` | Capture GitHub Insights or GitLab equivalent contributor history screenshots |
