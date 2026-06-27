# services/db_service.py

from database.db import SessionLocal
from database.models import ResumeAnalysis


def save_analysis(
    filename,
    score,
    matched_skills,
    missing_skills,
    recommendations
):

    session = SessionLocal()

    try:

        analysis = ResumeAnalysis(

            resume_filename=filename,

            ats_score=score,

            matched_skills=", ".join(matched_skills),

            missing_skills=", ".join(missing_skills),

            recommendations="\n".join(recommendations)
        )

        session.add(analysis)
        session.commit()

    except Exception as e:

        session.rollback()
        print(f"Database Error: {e}")

    finally:

        session.close()