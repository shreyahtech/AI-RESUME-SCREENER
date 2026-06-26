
import streamlit as st
import pandas as pd
from utils.parser import extract_text
from utils.skills import get_skills
from utils.bert_matcher import get_semantic_score
from utils.interview import generate_questions

st.title("Advanced AI Resume Screening System")

jd = st.text_area("Paste Job Description")
resumes = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if resumes and jd:
    results = []

    for resume in resumes:
        text = extract_text(resume)
        score = get_semantic_score(text, jd)

        skills = get_skills(text)
        jd_skills = get_skills(jd)

        missing = list(set(jd_skills) - set(skills))

        results.append({
            "Candidate": resume.name,
            "Score": round(score,2),
            "Skills": ", ".join(skills),
            "Missing Skills": ", ".join(missing)
        })

    df = pd.DataFrame(results)
    df = df.sort_values("Score", ascending=False)

    st.subheader("Candidate Ranking")
    st.dataframe(df)

    st.download_button(
        "Download Results CSV",
        df.to_csv(index=False),
        "candidate_ranking.csv"
    )

    top = df.iloc[0]
    st.success(f"Recommended Candidate: {top['Candidate']}")

    st.subheader("Suggested Interview Questions")
    for q in generate_questions(jd):
        st.write("•", q)
