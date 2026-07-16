import streamlit as st

def show_ats(score, checks):

    st.subheader("📄 ATS Compatibility")

    st.metric("ATS Score", f"{score}%")

    for item, passed in checks.items():

        if passed:
            st.success(f"✔ {item}")

        else:
            st.error(f"✖ {item}")