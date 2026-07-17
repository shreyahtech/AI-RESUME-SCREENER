import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


def show_dashboard():

    st.set_page_config(
        page_title="AI Resume Screener Pro",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    local_css("assets/style.css")

    st.markdown(
        """
<div class="hero">

    <div class="hero-title">
        🤖 AI Resume Screener Pro
    </div>

    <div class="hero-subtitle">
        AI-Powered Recruitment Dashboard
    </div>

    <div class="hero-text">
        Semantic Matching • ATS Analysis • AI Feedback • Resume Intelligence
    </div>

</div>
        """,
        unsafe_allow_html=True,
    )