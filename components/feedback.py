import streamlit as st


def show_feedback(score):

    st.subheader("🤖 AI Recommendation")

    if score >= 85:

        st.success(
            "Highly Recommended for Interview"
        )

    elif score >= 70:

        st.warning(
            "Recommended with Minor Skill Gaps"
        )

    else:

        st.error(
            "Needs Significant Improvement"
        )