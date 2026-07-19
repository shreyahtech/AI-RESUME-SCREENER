import streamlit as st


def metric_card(title, value, emoji):

    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-icon">
                {emoji}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-title">
                {title}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


def show_metrics(best_score, total_candidates, total_skills, ats_score):

    c1, c2, c3, c4 = st.columns(4, gap="large")

    with c1:
        metric_card("Match Score", f"{best_score:.1f}%", "🎯")

    with c2:
        metric_card("Candidates", total_candidates, "👥")

    with c3:
        metric_card("Skills", total_skills, "🛠️")

    with c4:
        metric_card("ATS Score", f"{ats_score}%", "📄")