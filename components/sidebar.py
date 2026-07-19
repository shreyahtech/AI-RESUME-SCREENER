import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div style="text-align:center;padding-bottom:20px;">
                <h1 style="font-size:42px;margin-bottom:0;">🤖</h1>
                <h2 style="margin-top:5px;margin-bottom:5px;color:white;">
                    AI Resume Screener
                </h2>
                <p style="color:#A5B4FC;font-size:14px;">
                    Next-Gen Recruitment AI
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        page = st.radio(
    "Navigation",
    [
        "🏠 Resume Analysis",
        "📄 ATS Checker",
        "📊 Analytics",
        "💬 Interview Questions",
        "ℹ️ About",
    ],
    label_visibility="collapsed"
)

        st.markdown("---")

        st.markdown(
            """
            <div style="text-align:center;color:#7C8DB5;font-size:13px;padding-top:15px;">
                AI Resume Screener Pro<br>
                Version 2.0
            </div>
            """,
            unsafe_allow_html=True,
        )

    return page