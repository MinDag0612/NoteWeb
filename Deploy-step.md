sau khi ssh và server



clone git repo về

* **mkdir /var/www**
* **cd /var/www**
* **git clone https://github.com/MinDag0612/NoteWeb**
* 

Kiểm tra

* **ls ->** thấy project là ok



tải Node.js LTS

* **curl -fsSL https://deb.nodesource.com/setup\_20.x | sudo -E bash -**
* **sudo apt install -y nodejs**



Chạy file scrips

* **chmod +x deploy.sh**
* **./deploy.sh**
* Phải thấy === DEPLOY DONE ===



Set môi trường

* **nano /var/www/NoteWeb/.env**
* Dán .env vào -> save lại
* **change mode cho .env: chmod 600 /var/www/NoteWeb/.env**

chmod 600 nghĩa là



Owner   : read + write   (rw-)

Group   : ---            (không xem được)

Others  : ---            (không xem được)



Chỉ user sở hữu file mới đọc/ghi được .env



config NginX

*  	**apt install nginx** -> cài NginX
*  	nano **/var/www/NoteWeb/nginx.conf** -> tự config

&nbsp;	hoặc **cp /var/www/NoteWeb/nginx.conf /etc/nginx/sites-available/noteweb** -> copy file qua -> Kiểm tra nano -> lưu ý config lại theo IP của mình



*  	**ln -s /etc/nginx/sites-available/noteweb /etc/nginx/sites-enabled/** -> Kích hoạt site
*  	**rm /etc/nginx/sites-enabled/default** -> Disable mặc định
*  	**nginx -t** -> tets lại
*  	**systemctl reload nginx** -> reload
*  	Check lại 	**ls /etc/nginx/sites-available**
* 

&nbsp;			**ls /etc/nginx/sites-enabled**



**-> Đến đây có thể truy cập vào ip xem UI lên chưa -> không cần mở port hay cấu hình firewall vì 80 mở mặc định**





Tạo systemd service cho backend

* **nano /etc/systemd/system/backend.service**



\\\\\\\\\\

\[Unit]

Description=FastAPI Backend

After=network.target



\[Service]

User=root

WorkingDirectory=/var/www/NoteWeb

EnvironmentFile=/var/www/NoteWeb/.env



ExecStart=/var/www/NoteWeb/backendSrc/venv/bin/gunicorn \\

          backendSrc.main:app \\

          --bind 127.0.0.1:8000 \\

          --workers 2 \\

          --worker-class uvicorn.workers.UvicornWorker



Restart=always



\[Install]

WantedBy=multi-user.target

\\\\\\\\\\\\



Chạy systemd để FastAPI chạy trong venv



**systemctl daemon-reexec**

**systemctl daemon-reload**

**systemctl enable backend**

**systemctl start backend**



**systemctl status backend** -> test





**curl http://127.0.0.1:8000/**-> check nội bộ, phải thấy {"status":"API is running"}



**journalctl -u backend -n 50 --no-pager** -> xem lỗi nếu có



Có thể vào máy ảo (**source venv/bin/activate**) - ở thư mục NoteWeb chạy thử **uvicorn backendSrc.main:app --reload --host 127.0.0.1 --port 8000 -** nếu có lỗi app sẽ khong lên













