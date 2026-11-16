# NoteWeb

**NoteWeb** là mini note app để tạo, chỉnh sửa và xóa ghi chú. Ứng dụng dùng
React ở frontend, FastAPI ở backend và MongoDB để lưu dữ liệu.

> Đây là bản mini chỉ có **một tài khoản local mặc định**, chưa có chức năng
> đăng ký thêm tài khoản. Các ghi chú được lưu cho tài khoản này.

## Tính năng

- Đăng nhập bằng tài khoản mặc định.
- Tạo, sửa và xóa ghi chú.
- Tải ảnh lên Cloudinary (cần cấu hình thông tin Cloudinary).

## Tài khoản mặc định

| Email | Mật khẩu |
| --- | --- |
| `admin@gmail.com` | `admin` |

Mật khẩu được lưu trong MongoDB dưới dạng bcrypt hash. Tài khoản này dành cho
môi trường local/demo; hãy đổi mật khẩu trước khi mở ứng dụng ra mạng.

## Chạy bằng Docker Compose

Cần cài Docker Desktop (có Docker Compose).

### 1. Tạo file `.env`

Tạo `.env` từ mẫu nếu chưa có file, sau đó mở và chỉnh sửa:

```powershell
if (-not (Test-Path .env)) { Copy-Item .env.sample .env }
notepad .env
```

Đặt một giá trị bí mật ngẫu nhiên cho `JWT_SECRET_KEY`:

```dotenv
JWT_SECRET_KEY=thay-bang-chuoi-bi-mat-ngau-nhien
```

Không commit `.env` lên Git. Các biến khác:

| Biến | Bắt buộc | Mục đích |
| --- | --- | --- |
| `JWT_SECRET_KEY` | Có | Ký và xác thực JWT của API. |
| `MONGODB_URI` | Chỉ khi chạy local | Địa chỉ MongoDB; Compose tự dùng `mongodb://mongodb:27017`. |
| `GG_CLIENT_ID`, `REACT_APP_GOOGLE_CLIENT_ID` | Không | Google Sign-In, nếu sử dụng. |
| `CLOUDY_NAME`, `CLOUDY_API_KEY`, `CLOUDY_SECRET` | Không | Tải ảnh lên Cloudinary. |

Các biến `REACT_APP_API_*` trong `.env.sample` dành cho frontend chạy local.
Docker Compose đã cấu hình sẵn đường dẫn `/api` và proxy đến backend.

### 2. Khởi động ứng dụng

```powershell
docker compose up --build -d
```

- Frontend: <http://localhost:3000>
- API health check: <http://localhost:3000/api/>
- API docs: <http://localhost:3000/api/docs>

Compose khởi động MongoDB trước, đợi database healthy rồi mới chạy backend.
Dữ liệu MongoDB được giữ trong volume `mongodb_data`.

### 3. Tài khoản trong MongoDB

Khi khởi tạo MongoDB với volume mới, script sẽ tự tạo tài khoản mặc định ở trên.
Nếu volume đã tồn tại từ trước, chạy lệnh sau một lần để thêm tài khoản mà
không xóa dữ liệu:

```powershell
docker compose exec mongodb mongosh --quiet --file /docker-entrypoint-initdb.d/01-create-admin.js
```

### Lệnh thường dùng

```powershell
docker compose ps
docker compose logs -f backend
docker compose down
```

Chỉ dùng `docker compose down -v` khi muốn xóa cả dữ liệu MongoDB.

## Chạy local không dùng Docker

1. Tạo `.env` như hướng dẫn ở trên và đảm bảo MongoDB đang chạy tại địa chỉ
   trong `MONGODB_URI`.
2. Cài và chạy backend:

   ```powershell
   python -m pip install -r requirements.txt
   python -m uvicorn backend.app.main:app --reload
   ```

3. Mở terminal khác, cài và chạy frontend:

   ```powershell
   npm install
   npm start
   ```

Frontend local chạy tại <http://localhost:3000>, backend tại
<http://127.0.0.1:8000>.

## Cấu trúc chính

```text
backend/app/       FastAPI, xác thực, ghi chú và upload ảnh
frontend/          Dockerfile và cấu hình Nginx
mongo-init/        Script khởi tạo tài khoản mặc định
src/               React frontend
requirements.txt   Python dependencies
docker-compose.yml Cấu hình MongoDB, backend và frontend
```
