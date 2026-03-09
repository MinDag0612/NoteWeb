# Phase 1 Compliance Checklist

| Requirement | Status | Repository Evidence | Manual Action Needed |
| --- | --- | --- | --- |
| Professional root README in technical English | Implemented | `README.md` | Keep it synchronized with deployment reality |
| Correct `.gitignore` for secrets/artifacts | Implemented | `.gitignore` | Verify no sensitive files are currently tracked |
| Ubuntu automation script exists | Implemented | `scripts/setup.sh` | Execute on real target host and keep logs |
| Setup verification helper exists | Implemented | `scripts/verify.sh` | Run after setup and capture outputs |
| Safe `.env` template exists | Implemented | `.env.example` | Fill real values only on deployment host |
| No hard-coded credentials in scripts | Implemented | `scripts/` | Keep this policy during future edits |
| Feature-branch + PR workflow | Pending manual | `phase1/evidence/README.md` | Perform real PR workflow and capture evidence |
| Branch protection on `main` | Pending manual | `phase1/evidence/README.md` | Configure on GitHub/GitLab and capture screenshots |
| At least one reviewer per PR | Pending manual | `phase1/evidence/README.md` | Enforce and capture reviewed PR artifacts |
| Visible contribution from all members | Pending manual | `phase1/evidence/README.md` | Capture contributor/insights screenshots |
