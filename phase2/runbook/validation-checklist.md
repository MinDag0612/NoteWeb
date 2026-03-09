# Phase 2 Validation Checklist

Mark each line only after collecting real evidence.

- [ ] Ubuntu host provisioned with least privilege SSH access
- [ ] Firewall/security groups expose only 22, 80, 443
- [ ] `scripts/setup.sh` executed successfully on target host
- [ ] `.env` created from `phase2/env/phase2.env.example`
- [ ] Backend process runs as non-root service (`noteweb-backend`)
- [ ] Service is enabled at boot (`systemctl is-enabled noteweb-backend`)
- [ ] Nginx serves frontend build with SPA fallback
- [ ] `/api/*` routes proxy correctly to backend
- [ ] `/uploads/*` routes are accessible from public domain
- [ ] DNS A/AAAA records map domain to cloud server
- [ ] HTTPS certificate issued by Let's Encrypt (or equivalent)
- [ ] Full app works via HTTPS domain (login, notes CRUD, upload)
- [ ] Database connectivity validated in production runtime
- [ ] Reboot persistence validated (service and app remain available)
- [ ] Evidence files captured and stored in `phase2/evidence/`
