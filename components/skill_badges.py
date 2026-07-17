import streamlit as st


def show_skill_badges(skills, title, color):

    st.markdown(f"### {title}")

    html = ""

    for skill in skills:

        html += f"""
<span style="
display:inline-block;
padding:8px 14px;
margin:5px;
border-radius:20px;
background:{color};
color:white;
font-weight:bold;
">
{skill}
</span>
"""

    st.markdown(html, unsafe_allow_html=True)