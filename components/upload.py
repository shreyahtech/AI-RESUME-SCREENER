import streamlit as st

def upload_files():

    jd = st.text_area(
        "📄 Paste Job Description",
        height=200
    )

    resumes = st.file_uploader(
        "📁 Upload Resume PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    return jd, resumes