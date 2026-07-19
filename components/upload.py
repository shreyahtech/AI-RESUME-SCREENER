import streamlit as st


def upload_files():

    st.markdown(
        """
        <div class="section-card">
            <h2>📄 Job Description</h2>
            <p>
                Paste the job description below and let AI compare it
                against every uploaded resume.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    jd = st.text_area(
        "",
        placeholder="Paste the job description here...",
        height=220,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-card">
            <h2>📁 Resume Upload</h2>
            <p>
                Upload one or multiple PDF resumes for analysis.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    resumes = st.file_uploader(
        "",
        type=["pdf"],
        accept_multiple_files=True,
    )

    return jd, resumes