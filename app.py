import streamlit as st
import pandas as pd

# Components
from components.dashboard import show_dashboard
from components.sidebar import show_sidebar
from components.upload import upload_files
from components.cards import show_metrics
from components.profile import show_profile
from components.charts import show_gauge
from components.feedback import show_feedback
from components.ats_card import show_ats

# Utils
from utils.parser import extract_text, extract_details
from utils.skills import get_skills
from utils.bert_matcher import get_semantic_score
from utils.interview import generate_questions
from utils.ats import calculate_ats_score


# ---------------------- UI ----------------------

show_dashboard()
page = show_sidebar()

# Upload section
jd, resumes = upload_files()


# ---------------------- Resume Analysis ----------------------

if resumes and jd:

    results = []

    for resume in resumes:

        # Extract text
        text = extract_text(resume)
        ats_score, ats_checks = calculate_ats_score(text)
        details = extract_details(text)

        # Semantic similarity score
        score = get_semantic_score(text, jd)

        # Skills
        resume_skills = get_skills(text)
        jd_skills = get_skills(jd)

        missing_skills = list(set(jd_skills) - set(resume_skills))

        results.append(
            {
                "Candidate": resume.name,
                "Score": round(score, 2),
                "Skills": ", ".join(resume_skills),
                "Missing Skills": ", ".join(missing_skills),
                "Details": details
            }
        )

    # Create dataframe
    df = pd.DataFrame(results)

    # Sort candidates
    df = df.sort_values("Score", ascending=False)

    # Best candidate
    best = df.iloc[0]
    show_profile(best["Details"])
    show_gauge(best["Score"])
    show_feedback(best["Score"])

    # ---------------------- Dashboard Metrics ----------------------

    show_metrics(
        best_score=best["Score"],
        total_candidates=len(df),
        total_skills=len(jd_skills),
    )

    st.markdown("---")

    # ---------------------- Candidate Ranking ----------------------

    st.subheader("🏆 Candidate Ranking")

    st.dataframe(
        df,
        use_container_width=True,
    )

    st.download_button(
        label="📥 Download Results CSV",
        data=df.to_csv(index=False),
        file_name="candidate_ranking.csv",
        mime="text/csv",
    )

    st.markdown("---")

    # ---------------------- Recommendation ----------------------

    st.success(
        f"✅ Recommended Candidate: **{best['Candidate']}** "
        f"with a score of **{best['Score']}%**"
    )

    # ---------------------- Interview Questions ----------------------

    st.subheader("💬 Suggested Interview Questions")

    questions = generate_questions(jd)

    for question in questions:
        st.write(f"• {question}")