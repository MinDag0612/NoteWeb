# Phase 2 Host Deployment Runbook

## 1. Provision Ubuntu Server

1. Create an Ubuntu 22.04+ cloud instance.
2. Create a dedicated deploy user and disable root SSH login.
3. Open only required ports:
   - 22/tcp (restricted source)
   - 80/tcp
   - 443/tcp

## 2. Clone Repository and Prepare Runtime

```bash
sudo mkdir -p /var/www
sudo chown -R $USER:$USER /var/www
cd /var/www
git clone <your-repository-url> NoteWeb
cd NoteWeb
bash scripts/setup.sh
```

## 3. Configure Environment

```bash
cp phase2/env/phase2.env.example .env
nano .env
chmod 600 .env
```

Replace all placeholder values, especially JWT and database credentials.

## 4. Build Frontend and Prepare Service User

```bash
npm run build
sudo useradd --system --home /var/www/NoteWeb --shell /usr/sbin/nologin noteweb || true
sudo chown -R noteweb:noteweb /var/www/NoteWeb/uploads /var/www/NoteWeb/logs
```

## 5. Install and Enable Backend systemd Service

```bash
sudo cp phase2/config/systemd/noteweb-backend.service /etc/systemd/system/noteweb-backend.service
sudo systemctl daemon-reload
sudo systemctl enable noteweb-backend
sudo systemctl start noteweb-backend
sudo systemctl status noteweb-backend --no-pager
```

## 6. Configure Nginx Reverse Proxy

### Before HTTPS

```bash
sudo cp phase2/config/nginx/noteweb.host.http.conf /etc/nginx/sites-available/noteweb
sudo ln -sf /etc/nginx/sites-available/noteweb /etc/nginx/sites-enabled/noteweb
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
```

### After DNS points to server IP

```bash
sudo certbot --nginx -d your-domain.example -d www.your-domain.example
```

Then replace with `phase2/config/nginx/noteweb.host.https.conf`, validate and reload Nginx.

## 7. Validate Runtime

```bash
curl -I http://127.0.0.1:8000/
curl -I https://your-domain.example
sudo systemctl is-enabled noteweb-backend
sudo journalctl -u noteweb-backend -n 100 --no-pager
```

Record screenshots and logs under `phase2/evidence/`.
