import streamlit as st

def show_profile(details):

    st.subheader("👤 Candidate Profile")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Name:** {details['name']}")
        st.write(f"**Email:** {details['email']}")
        st.write(f"**Phone:** {details['phone']}")

    with col2:
        st.write(f"**LinkedIn:** {details['linkedin']}")
        st.write(f"**GitHub:** {details['github']}")