import streamlit as st

# Function to load CSS
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
        layout="wide"
    )

    # Load the CSS file
    local_css("assets/style.css")

    st.title("🤖 AI Resume Screener Pro")
    st.caption("Helping Recruiters Hire Smarter")

    st.markdown("---")