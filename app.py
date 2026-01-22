import streamlit as st
import os
from streamlit_pdf_viewer import pdf_viewer

# 1. Səhifə Ayarları
st.set_page_config(
    layout="wide", 
    page_title="Sənəd Görüntüləyici"
)

# Kənarları təmizləmək üçün CSS
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
</style>
""", unsafe_allow_html=True)

# 2. Faylın Adı
FILE_NAME = "sened.pdf"

# 3. PDF-i Göstərən Hissə
if os.path.exists(FILE_NAME):
    # Bu kitabxana faylı birbaşa təhlükəsiz şəkildə açır
    pdf_viewer(FILE_NAME, width=1000, height=1000) 
else:
    st.error(f"⚠️ Xəta: '{FILE_NAME}' faylı tapılmadı. Zəhmət olmasa GitHub-da 'app.py' ilə eyni yerdə 'sened.pdf' faylının olduğuna əmin olun.")
