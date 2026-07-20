import streamlit as st
import pandas as pd


# ---------------------- Components ----------------------

from components.dashboard import show_dashboard
from components.sidebar import show_sidebar
from components.upload import upload_files

from components.cards import show_metrics
from components.feedback import show_feedback
from components.ats_card import show_ats
from components.analytics import show_summary
from components.top_candidates import show_top_candidates
from components.comparison import show_comparison
from components.candidate_card import show_candidate_card
from components.skill_badges import show_skill_badges
from components.summary import show_recruiter_summary

from components.charts import (
    show_gauge,
    show_candidate_bar,
    show_skill_pie,
)


# ---------------------- Utils ----------------------

from utils.parser import extract_text, extract_details
from utils.skills import get_skills
from utils.bert_matcher import get_semantic_score
from utils.interview import generate_questions
from utils.ats import calculate_ats_score
from utils.summary import generate_summary



# ======================================================
# Dashboard
# ======================================================

show_dashboard()

page = show_sidebar() 

jd, resumes = upload_files()



# ======================================================
# Resume Analysis
# ======================================================

if resumes and jd:

    results = []

    jd_skills = get_skills(jd)


    for resume in resumes:

        text = extract_text(resume)

        details = extract_details(text)

        ats_score, ats_checks = calculate_ats_score(text)

        score = get_semantic_score(
            text,
            jd
        )

        resume_skills = get_skills(text)


        missing_skills = list(
            set(jd_skills) - set(resume_skills)
        )


        results.append(
            {
                "Candidate": resume.name,

                "Score": round(score, 2),

                "Skills": ", ".join(resume_skills),

                "Skill List": resume_skills,

                "Missing Skills": ", ".join(missing_skills),

                "Missing Skill List": missing_skills,

                "Details": details,

                "ATS Score": ats_score,

                "ATS Checks": ats_checks,

                "Resume Text": text,
            }
        )

        
    # ======================================================
    # DataFrame
    # ======================================================

    df = pd.DataFrame(results)

    df = df.sort_values(
        "Score",
        ascending=False
    )



    # ======================================================
    # Candidate Selector
    # ======================================================

    st.subheader(
        "👥 Select Candidate"
    )


    selected_candidate = st.selectbox(
        "Choose a Resume",
        df["Candidate"]
    )


    best = df[
        df["Candidate"] == selected_candidate
    ].iloc[0]

    display_df = df[
    [
        "Candidate",
        "Score",
        "ATS Score",
        "Skills",
        "Missing Skills",
    ]
]
if page == "🏠 Resume Analysis":

    # ======================================================
    # Metrics
    # ======================================================

    show_metrics(
        best_score=best["Score"],
        total_candidates=len(df),
        total_skills=len(jd_skills),
        ats_score=best["ATS Score"]
    )
elif page == "📄 ATS Checker":

    st.subheader("📄 ATS Analysis")

    show_ats(
        best["ATS Score"],
        best["ATS Checks"]
    )

elif page == "📊 Analytics":

    st.subheader("📊 Analytics")

    matched = len(best["Skill List"])
    missing = len(best["Missing Skill List"])

    col1, col2 = st.columns(2)

    with col1:
        show_candidate_bar(display_df)

    with col2:
        show_skill_pie(
            matched,
            missing
        )
    st.divider()

    show_top_candidates(df)

    st.divider()

    show_comparison(df)

elif page == "💬 Interview Questions":

    st.subheader("💬 AI Interview Questions")

    questions = generate_questions(
        jd,
        best["Skill List"]
    )

    for question in questions:
        st.write(f"• {question}")

    # ======================================================
    # Overview
    # ======================================================

    show_summary(df)



    st.divider()



    # ======================================================
    # Candidate Profile
    # ======================================================

    show_candidate_card(best)



    st.divider()



    # ======================================================
    # Skills
    # ======================================================

    col1, col2 = st.columns(2)


    with col1:

        show_skill_badges(
            best["Skill List"],
            "✅ Matched Skills",
            "#28a745"
        )


    with col2:

        show_skill_badges(
            best["Missing Skill List"],
            "❌ Missing Skills",
            "#dc3545"
        )



    st.divider()



    # ======================================================
    # Match Score + ATS
    # ======================================================

    col1, col2 = st.columns(2)


    with col1:

        show_gauge(
            best["Score"]
        )


        st.progress(
            float(best["Score"]) / 100)



    with col2:

        show_ats(
            best["ATS Score"],
            best["ATS Checks"]
        )



    st.divider()



    # ======================================================
    # AI Feedback
    # ======================================================

    show_feedback(
        best["Score"],
        best["Details"],
        best["Skill List"],
        best["Missing Skill List"],
        best["ATS Score"],
    )



    st.divider()



    # ======================================================
    # Recruiter Summary
    # ======================================================

    summary = generate_summary(best)

    show_recruiter_summary(
        summary
    )



    st.divider()



    # ======================================================
    # Resume Preview
    # ======================================================

    with st.expander(
        "📄 Resume Preview"
    ):

        st.write(
            best["Resume Text"][:3000]
        )



    st.divider()



    # ======================================================
    # Candidate Ranking
    # ======================================================

    st.subheader(
        "🏆 Candidate Ranking"
    )


    display_df = df[
        [
            "Candidate",
            "Score",
            "ATS Score",
            "Skills",
            "Missing Skills",
        ]
    ]


    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
    )



    st.divider()


    # ======================================================
    # Top Candidates
    # ======================================================

    show_top_candidates(df)



    st.divider()



    # ======================================================
    # Candidate Comparison
    # ======================================================

    show_comparison(df)



    st.divider()



    # ======================================================
    # Download
    # ======================================================

    st.download_button(
        label="📥 Download Results CSV",

        data=display_df.to_csv(index=False),

        file_name="candidate_ranking.csv",

        mime="text/csv",
    )



    st.divider()



    # ======================================================
    # Recommendation
    # ======================================================

    st.success(
        f"🏆 Recommended Candidate: **{df.iloc[0]['Candidate']}** "
        f"with Match Score **{df.iloc[0]['Score']}%**"
    )



    st.divider()



    # ======================================================
    # Interview Questions
    # ======================================================

    st.subheader(
        "💬 Suggested Interview Questions"
    )


    questions = generate_questions(
        jd,
        best["Skill List"]
    )


    for question in questions:

        st.write(
            f"• {question}"
        )