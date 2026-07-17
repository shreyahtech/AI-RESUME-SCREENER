import streamlit as st


def show_candidate_card(best):

    details = best["Details"]

    st.subheader("👤 Candidate Overview")

    st.markdown(
        f"""
<div style="padding:25px;
border-radius:15px;
background:#f8f9fa;
box-shadow:0px 4px 10px rgba(0,0,0,0.15);">

<h2>{details["name"]}</h2>

<p>⭐ <b>Match Score:</b> {best["Score"]}%</p>

<p>🎯 <b>ATS Score:</b> {best["ATS Score"]}%</p>

<hr>

<p>📧 {details["email"]}</p>

<p>📱 {details["phone"]}</p>

<p>🔗 {details["linkedin"]}</p>

<p>💻 {details["github"]}</p>

</div>
""",
        unsafe_allow_html=True,
    )