import streamlit as st
import base64
import os

# Səhifəni tam ekran rejiminə keçiririk
st.set_page_config(layout="wide", page_title="Mənim PDF Sənədim")

# CSS ilə kənarları təmizləyirik (Sayt kimi görünsün)
st.markdown("""
<style>
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    iframe {
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# --- Faylın Adı ---
# PDF faylınızın adı dəqiq belə olmalıdır (və ya buranı dəyişin)
FILE_NAME = "sened.pdf" 

def display_pdf(file_path):
    # Faylı serverdən (qovluqdan) oxuyuruq
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # PDF-i Embed edirik
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}#toolbar=0" width="100%" height="1000px" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Yoxlayırıq: Fayl yerindədirmi?
if os.path.exists(FILE_NAME):
    display_pdf(FILE_NAME)
else:
    st.error(f"Xəta: '{FILE_NAME}' faylı tapılmadı! Zəhmət olmasa PDF faylını GitHub-a kodla birlikdə yüklədiyinizdən əmin olun.")
