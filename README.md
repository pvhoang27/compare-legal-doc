# ⚖️ So sánh Văn bản Pháp luật (Compare Legal Documents)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.27%2B-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Đây là một ứng dụng web đơn giản được xây dựng bằng Streamlit giúp người dùng dễ dàng so sánh sự khác biệt giữa hai văn bản pháp luật (hoặc bất kỳ hai văn bản nào khác). Ứng dụng sẽ làm nổi bật những đoạn văn bản đã được thêm, xóa, hoặc thay đổi.

## 🌟 Tính năng chính

- Tải lên hai file văn bản (hỗ trợ các định dạng như `.txt`, `.pdf`, `.docx`).
- Giao diện so sánh song song (side-by-side) trực quan, dễ theo dõi.
- Tự động làm nổi bật (highlight) các điểm khác biệt:
    - <span style="background-color: #d4edda; color: #155724;">**Nội dung được thêm vào.**</span>
    - <span style="background-color: #f8d7da; color: #721c24;">**Nội dung bị xóa đi.**</span>
- Hiển thị tóm tắt số lượng thay đổi.

## 📸 Demo / Hình ảnh

*(Bạn nên chụp ảnh màn hình ứng dụng đang chạy và dán vào đây để người xem dễ hình dung)*

![Demo ứng dụng](https://user-images.githubusercontent.com/26888748/189931328-9557476c-31b3-4421-b8a7-70f9595c2e36.png)
*Giao diện so sánh văn bản*

## 🛠️ Công nghệ sử dụng

- **Backend & Frontend:** Python, Streamlit
- **Xử lý văn bản:** [Ghi tên thư viện bạn dùng, ví dụ: PyPDF2, python-docx, difflib]

## 📦 Cài đặt & Khởi chạy

Để chạy ứng dụng trên máy của bạn, hãy làm theo các bước sau:

**1. Clone repository về máy:**
```bash
git clone [https://github.com/pvhoang27/compare-legal-doc.git](https://github.com/pvhoang27/compare-legal-doc.git)
cd compare-legal-doc
```

**2. (Khuyến khích) Tạo và kích hoạt môi trường ảo:**
- Đối với Windows:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
- Đối với macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

**3. Cài đặt các thư viện cần thiết:**
```bash
pip install -r requirements.txt
```

**4. Chạy ứng dụng:**
- Chạy giao diện chính:
  ```bash
  streamlit run app.py
  ```
- Chạy phiên bản phụ / thử nghiệm:
  ```bash
  streamlit run app2.py
  ```

Sau khi chạy lệnh, mở trình duyệt và truy cập vào địa chỉ `http://localhost:8501`.

## 🤝 Đóng góp

Mọi sự đóng góp đều được chào đón! Nếu bạn có ý tưởng cải thiện dự án, vui lòng:

1.  **Fork** dự án này.
2.  Tạo một **Branch** mới (`git checkout -b feature/AmazingFeature`).
3.  **Commit** những thay đổi của bạn (`git commit -m 'Add some AmazingFeature'`).
4.  **Push** lên branch (`git push origin feature/AmazingFeature`).
5.  Mở một **Pull Request**.

## 📄 Giấy phép

Dự án này được cấp phép theo Giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## 📧 Liên hệ

[Tên của bạn] - [Email của bạn]

Link dự án: [https://github.com/pvhoang27/compare-legal-doc](https://github.com/pvhoang27/compare-legal-doc)