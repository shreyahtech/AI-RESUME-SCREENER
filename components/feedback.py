import streamlit as st


def show_feedback(score, details, skills, missing_skills, ats_score):

    st.subheader("🤖 AI Resume Evaluation")

    # ---------------- Recommendation ----------------

    if score >= 85:
        st.success("✅ Highly Recommended for Interview")

    elif score >= 70:
        st.warning("⚠ Recommended with Minor Skill Gaps")

    else:
        st.error("❌ Needs Significant Improvement")

    st.markdown("---")

    # ---------------- Strengths ----------------

    strengths = []

    if details["email"] != "Not Found":
        strengths.append("Email address is present.")

    if details["phone"] != "Not Found":
        strengths.append("Phone number is available.")

    if details["linkedin"] != "Not Found":
        strengths.append("LinkedIn profile included.")

    if details["github"] != "Not Found":
        strengths.append("GitHub profile included.")

    if len(skills) >= 5:
        strengths.append("Strong technical skill set.")

    if ats_score >= 80:
        strengths.append("Good ATS compatibility.")

    # ---------------- Improvements ----------------

    improvements = []

    if details["linkedin"] == "Not Found":
        improvements.append("Add your LinkedIn profile.")

    if details["github"] == "Not Found":
        improvements.append("Include your GitHub profile.")

    if len(missing_skills) > 0:
        improvements.append(
            "Missing skills: " + ", ".join(missing_skills[:5])
        )

    if ats_score < 70:
        improvements.append(
            "Improve ATS score by adding standard resume sections."
        )

    improvements.append(
        "Add measurable achievements (e.g., Increased accuracy by 15%)."
    )

    # ---------------- Display ----------------

    col1, col2 = st.columns(2)

    with col1:

        st.success("💪 Strengths")

        if strengths:
            for item in strengths:
                st.write(f"• {item}")
        else:
            st.write("No major strengths detected.")

    with col2:

        st.warning("📌 Improvements")

        if improvements:
            for item in improvements:
                st.write(f"• {item}")
        else:
            st.write("No improvements suggested.")