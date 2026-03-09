# Secrets Hygiene Checklist

Use this checklist if secrets were ever committed in history or shared in logs.

## 1. Rotate Exposed Credentials Immediately

- [ ] MongoDB credentials / URI tokens
- [ ] JWT secret key
- [ ] Cloudinary API key + secret
- [ ] Google OAuth client secret (if exposed)

## 2. Confirm Secret Files Are Not Tracked

```bash
git ls-files .env
```

Expected output: no tracked file.

## 3. Confirm Ignore Rules

```bash
git check-ignore -v .env phase3/compose/runtime.env
```

## 4. Replace Local Runtime Files with Templates

- Keep `.env.example`, `phase2/env/phase2.env.example`, and `phase3/compose/runtime.env.example` in git.
- Keep real secrets only in server-local files:
  - `/var/www/NoteWeb/.env` (Phase 2)
  - `/var/www/NoteWeb/phase3/compose/runtime.env` (Phase 3)

## 5. Platform Cleanup (if secret commit exists in remote history)

- Rotate credentials first.
- Optionally rewrite git history with dedicated tooling only if required by policy.
- Inform team members to discard old clones after history rewrite.

## 6. Evidence for Report

Capture proof of secure secret handling (without revealing secret values):

- masked screenshots of environment files on server
- `.gitignore` rules screenshot
- command output showing `.env` is not tracked
