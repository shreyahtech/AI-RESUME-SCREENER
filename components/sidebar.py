import streamlit as st

def show_sidebar():
    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Go to",
        [
            "Resume Analysis",
            "ATS Checker",
            "Analytics",
            "Interview Questions",
            "About"
        ]
    )

    return page