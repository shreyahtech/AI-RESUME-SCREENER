def generate_summary(candidate):

    score = candidate["Score"]
    ats = candidate["ATS Score"]
    skills = candidate["Skill List"]
    missing = candidate["Missing Skill List"]
    details = candidate["Details"]

    summary = []

    summary.append(
        f"{candidate['Candidate']} achieved a semantic match score of {score}% "
        f"and an ATS score of {ats}%."
    )

    if score >= 85:
        summary.append(
            "The candidate appears to be a strong match for the job description."
        )
    elif score >= 70:
        summary.append(
            "The candidate is a reasonable match but may require additional evaluation."
        )
    else:
        summary.append(
            "The candidate has several gaps compared to the job requirements."
        )

    if skills:
        summary.append(
            "Key skills identified include: " +
            ", ".join(skills[:6]) + "."
        )

    if missing:
        summary.append(
            "Potential skill gaps include: " +
            ", ".join(missing[:5]) + "."
        )
    else:
        summary.append(
            "No major technical skill gaps were identified."
        )

    if details["github"] != "Not Found":
        summary.append(
            "The candidate has included a GitHub profile."
        )

    if details["linkedin"] != "Not Found":
        summary.append(
            "The candidate has included a LinkedIn profile."
        )

    summary.append(
        "Overall recommendation: Proceed with an interview if the required experience aligns with the role."
    )

    return " ".join(summary)