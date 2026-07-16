import re

def calculate_ats_score(text):

    score = 0
    checks = {}

    # Email
    email = bool(
        re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    )
    checks["Email"] = email
    if email:
        score += 15

    # Phone
    phone = bool(
        re.search(r"(\+?\d[\d\s\-]{8,15}\d)", text)
    )
    checks["Phone"] = phone
    if phone:
        score += 15

    # Education
    education = any(
        word in text.lower()
        for word in [
            "education",
            "b.tech",
            "bachelor",
            "university",
            "college",
        ]
    )
    checks["Education"] = education
    if education:
        score += 15

    # Experience
    experience = "experience" in text.lower()
    checks["Experience"] = experience
    if experience:
        score += 15

    # Skills
    skills = "skills" in text.lower()
    checks["Skills"] = skills
    if skills:
        score += 15

    # Projects
    projects = "project" in text.lower()
    checks["Projects"] = projects
    if projects:
        score += 15

    # LinkedIn
    linkedin = "linkedin.com" in text.lower()
    checks["LinkedIn"] = linkedin
    if linkedin:
        score += 10

    return score, checks