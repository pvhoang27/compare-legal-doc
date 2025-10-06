import streamlit as st
import difflib
import pdfplumber
from streamlit.components.v1 import html

# --- Cấu hình trang ---
st.set_page_config(layout="wide", page_title="So sánh File PDF")

# --- Hàm trích xuất văn bản từ PDF ---
def extract_text_from_pdf(uploaded_file):
    """Mở và đọc văn bản từ một file PDF được tải lên."""
    if uploaded_file is None:
        return ""
    
    all_text = ""
    try:
        # pdfplumber.open() có thể đọc trực tiếp đối tượng file của Streamlit
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    all_text += page_text + "\n" # Thêm ký tự xuống dòng giữa các trang
        return all_text
    except Exception as e:
        st.error(f"Lỗi khi đọc file PDF: {e}")
        return ""

# --- Giao diện chính ---
st.title("📄 So sánh Nội dung hai File PDF")
st.write("Tải lên hai phiên bản của một tài liệu PDF để xem sự khác biệt về mặt văn bản.")

# --- Giao diện tải file lên ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Văn bản gốc")
    pdf_file1 = st.file_uploader("Tải lên file PDF gốc", type="pdf", key="file1")

with col2:
    st.subheader("Văn bản sửa đổi")
    pdf_file2 = st.file_uploader("Tải lên file PDF sửa đổi", type="pdf", key="file2")

# --- Nút và Logic xử lý ---
if st.button("🔎 Tiến hành so sánh", type="primary"):
    if pdf_file1 and pdf_file2:
        with st.spinner("Đang trích xuất văn bản từ PDF và so sánh..."):
            # Trích xuất văn bản từ cả hai file
            text1 = extract_text_from_pdf(pdf_file1)
            text2 = extract_text_from_pdf(pdf_file2)

            if text1 and text2:
                # Tách văn bản thành các dòng
                text1_lines = text1.splitlines()
                text2_lines = text2.splitlines()

                # Tạo HTML so sánh bằng difflib
                diff_html = difflib.HtmlDiff(wrapcolumn=80).make_file(
                    fromlines=text1_lines,
                    tolines=text2_lines,
                    fromdesc=pdf_file1.name,
                    todesc=pdf_file2.name
                )
                
                st.subheader("Kết quả so sánh chi tiết")
                # Hiển thị kết quả
                html(diff_html, height=800, scrolling=True)
            else:
                st.error("Không thể trích xuất văn bản từ một hoặc cả hai file PDF. File có thể bị lỗi hoặc không chứa văn bản.")

    else:
        st.warning("Vui lòng tải lên cả hai file PDF để thực hiện so sánh.")

st.markdown("---")
st.info("Lưu ý: Công cụ này chỉ so sánh phần **văn bản (text)** trong file PDF, không so sánh hình ảnh, bảng biểu hay định dạng.")