def analyze_resume(
    resume_skills,
    jd_skills
):

    resume_set = {
        skill.lower().strip()
        for skill in resume_skills
    }

    jd_set = {
        skill.lower().strip()
        for skill in jd_skills
    }

    matched = sorted(
        resume_set & jd_set
    )

    missing = sorted(
        jd_set - resume_set
    )

    score = 0

    if jd_set:

        score = int(
            len(matched)
            / len(jd_set)
            * 100
        )

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }