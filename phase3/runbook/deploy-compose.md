# Phase 3 Deployment Runbook (Compose on Ubuntu)

## 1. Install Docker Engine + Compose Plugin

```bash
sudo apt-get update
sudo apt-get install -y docker.io docker-compose-plugin
sudo systemctl enable docker
sudo systemctl start docker
```

## 2. Prepare Compose Project Files

```bash
cd /var/www/NoteWeb/phase3/compose
cp .env.compose.example .env
cp runtime.env.example runtime.env
nano .env
nano runtime.env
chmod 600 runtime.env
```

## 3. Pull and Start Containers

```bash
docker compose -f docker-compose.prod.yml pull
docker compose -f docker-compose.prod.yml up -d
```

## 4. Keep Host-Level Nginx from Phase 2

Do not remove HTTPS/domain configuration. Only change upstream targets:

- frontend upstream -> `127.0.0.1:3000`
- backend API/upload upstream -> `127.0.0.1:8000`

In Phase 3, do not run application runtime with PM2 or systemd.
Only Docker services should run the app processes.

## 5. Validate Runtime

```bash
docker compose -f docker-compose.prod.yml ps
docker compose -f docker-compose.prod.yml logs --tail=100 backend
docker compose -f docker-compose.prod.yml logs --tail=100 frontend
docker compose -f docker-compose.prod.yml logs --tail=100 mongodb
```

## 6. Restart Persistence Validation

```bash
sudo reboot
# reconnect after reboot
cd /var/www/NoteWeb/phase3/compose
docker compose -f docker-compose.prod.yml ps
```

Verify that containers restart automatically and data still exists.
