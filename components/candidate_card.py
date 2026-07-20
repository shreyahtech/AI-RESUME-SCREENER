import streamlit as st

def show_candidate_card(best):

    details = best["Details"]

    name = details.get("name", "Unknown")
    email = details.get("email", "Not Available")
    phone = details.get("phone", "Not Available")
    linkedin = details.get("linkedin", "Not Available")
    github = details.get("github", "Not Available")

    score = best["Score"]
    ats = best["ATS Score"]

    if score >= 85:
        recommendation = "🟢 Strong Hire"
    elif score >= 70:
        recommendation = "🟡 Consider"
    else:
        recommendation = "🔴 Needs Review"

    st.markdown(
        f"""
<div class="candidate-card">

<div class="candidate-top">

<div class="candidate-info">

<div class="candidate-name">
{name}
</div>

<div class="candidate-role">
Top Ranked Candidate
</div>

</div>

<div class="candidate-score">
⭐ {score:.1f}%
</div>

</div>

<div class="candidate-divider"></div>

<div class="candidate-contact">

<div>📧 {email}</div>

<div>📱 {phone}</div>

<div>💼 {linkedin}</div>

<div>💻 {github}</div>

</div>

<div class="candidate-divider"></div>

<div class="candidate-bottom">

<div class="score-pill">
🎯 Match Score
<br>
<b>{score:.1f}%</b>
</div>

<div class="score-pill">
📄 ATS Score
<br>
<b>{ats}%</b>
</div>

<div class="recommend-pill">
{recommendation}
</div>

</div>

</div>
        """,
        unsafe_allow_html=True,
    )