import streamlit as st
import difflib
from streamlit.components.v1 import html

# Cấu hình layout trang cho rộng hơn để dễ nhìn
st.set_page_config(layout="wide", page_title="So sánh văn bản")

st.title("📝 Ứng dụng So sánh Văn bản")
st.write("Dán hai phiên bản văn bản vào các ô dưới đây để xem sự khác biệt.")

# --- Giao diện nhập liệu ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Văn bản gốc")
    text1 = st.text_area("Nội dung 1", height=300, label_visibility="collapsed")

with col2:
    st.subheader("Văn bản sửa đổi")
    text2 = st.text_area("Nội dung 2", height=300, label_visibility="collapsed")

# --- Nút và Logic xử lý ---
if st.button("Tiến hành so sánh", type="primary"):
    if text1 and text2:
        # Tách văn bản thành các dòng
        text1_lines = text1.splitlines()
        text2_lines = text2.splitlines()

        # Sử dụng difflib để tạo HTML so sánh
        # 'make_file' tạo ra một bảng HTML hoàn chỉnh
        diff_html = difflib.HtmlDiff(wrapcolumn=80).make_file(
            fromlines=text1_lines,
            tolines=text2_lines,
            fromdesc="Văn bản gốc",
            todesc="Văn bản sửa đổi"
        )
        
        st.subheader("Kết quả so sánh chi tiết")
        # Hiển thị HTML kết quả trong một component của Streamlit
        html(diff_html, height=600, scrolling=True)

    else:
        st.warning("Vui lòng nhập nội dung cho cả hai văn bản.")

st.markdown("---")
st.info("Ứng dụng này sử dụng thư viện `difflib` của Python để tìm và hiển thị sự khác biệt giữa hai văn bản.")