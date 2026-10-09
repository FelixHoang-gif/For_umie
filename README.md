# Một chút dịu dàng dành cho cậu 🐱

## Chạy trên Windows
1. Cài Python 3.10+ từ python.org (tick "Add Python to PATH").
2. Mở PowerShell trong thư mục này và chạy:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
Trình duyệt sẽ tự mở tại http://localhost:8501

## Đưa lên mạng (Streamlit Community Cloud, miễn phí)
1. Đẩy thư mục này lên một repo GitHub (nên để **private** nếu thư có nội dung riêng tư).
2. Vào share.streamlit.io, đăng nhập GitHub, chọn **Create app**.
3. Chọn repo, branch, file chính `app.py`, nhấn **Deploy**.
4. Nhận đường link dạng `https://ten-cua-ban.streamlit.app` để gửi người ấy (trong Settings có thể đổi tên link).

## Cá nhân hóa
- **Lời thư, ghi chú, thẻ, lời nhắn của mèo, biệt danh**: sửa `config.py`.
- **Màu sắc**: sửa `COLORS` trong `config.py` (mã hex).
- **Nhạc nền**: bỏ file `music.mp3` vào `assets/` (hoặc đổi `MUSIC_PATH`). Không có file thì nút nhạc tự ẩn. Chỉ dùng nhạc không bản quyền (vd: Pixabay Music, Free Music Archive).
- **Ảnh**: bỏ `photo.jpg` vào `assets/`; không có thì phần ảnh tự ẩn.
- **Hình mèo**: vẽ bằng SVG trong hàm `cat()` ở `app.py`; thêm kiểu mới bằng cách thêm một mục vào dict `extra`.

## Ghi chú
- Font Quicksand và Itim tải từ Google Fonts (có font dự phòng nếu mất mạng).
- Trang không thu thập dữ liệu, không ghi lại hay gửi đi bất cứ câu trả lời nào của người nhận.
- Hiệu ứng hạt sáng tự tắt nếu thiết bị bật "giảm chuyển động".
