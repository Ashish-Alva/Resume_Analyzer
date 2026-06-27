# database/models.py
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    func
)


class Base(DeclarativeBase):
    pass


class ResumeAnalysis(Base):

    __tablename__ = "resume_analysis"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    resume_filename = Column(
        String(255)
    )

    job_description = Column(
        Text
    )

    ats_score = Column(
        Integer
    )

    matched_skills = Column(
        Text
    )

    missing_skills = Column(
        Text
    )

    recommendations = Column(
        Text
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )