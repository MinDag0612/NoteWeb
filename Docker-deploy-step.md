# CLOUD DEPLOY - DOCKER VERSION

## Các bước sau khi đã ssh vào cloud server
### Clone git repo:
```bash
git clone https://github.com/MinDag0612/NoteWeb
```

### chuyển sang nhánh docker
```bash
git checkout feature-docker-containerization
```

### (Trường hơp nếu chưa có ở local)
```bash
git checkout -b feature-docker-containerization
git pull origin feature-docker-containerization
```

### Cài Docker & Docker Compose
```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
sudo systemctl enable docker
sudo systemctl start docker
```

### Chạy lệnh sau:
```bash
docker compose -f docker-compose.image.yml up -d
```

### Helper commands:

Xóa container + network + volume của compose
```bash
docker compose -f docker-compose.image.yml down  -v
```
