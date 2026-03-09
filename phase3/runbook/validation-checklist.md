# Phase 3 Validation Checklist

- [ ] Docker Engine and Compose plugin installed on same Ubuntu server
- [ ] Compose file uses `image:` references only (no server-side build)
- [ ] Backend image pull succeeds from registry
- [ ] Frontend image pull succeeds from registry
- [ ] MongoDB runs inside Docker
- [ ] Persistent volume for MongoDB data is configured
- [ ] Persistent volume for uploaded files is configured
- [ ] All services have restart policies
- [ ] Containers auto-start after reboot
- [ ] Host-level reverse proxy from Phase 2 remains active
- [ ] HTTPS domain still serves full application
- [ ] API + upload + database behavior verified in containerized runtime
- [ ] No PM2/systemd used for app runtime in Phase 3
- [ ] Evidence files stored under `phase3/evidence/`
