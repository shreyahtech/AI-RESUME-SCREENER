import streamlit as st

def show_metrics(best_score, total_candidates, total_skills):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🏆 Best Match",
            f"{best_score}%"
        )

    with col2:
        st.metric(
            "📄 Candidates",
            total_candidates
        )

    with col3:
        st.metric(
            "🛠 Skills Found",
            total_skills
        )