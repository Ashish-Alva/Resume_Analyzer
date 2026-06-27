# Database config
from database.bootstrap import create_database_if_not_exists
from database.db import engine
from database.models import Base
from services.db_service import save_analysis

create_database_if_not_exists()
Base.metadata.create_all(engine)


# Streamlit config
import streamlit as st
import plotly.graph_objects as go

from services.resume_parser import extract_resume_text
from services.openai_service import (
    extract_skills,
    generate_suggestions
)
from services.ats_analyzer import analyze_resume


st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

def show_tags(tags, color):

    if not tags:
        st.caption("No skills found")
        return

    # Convert comma-separated string to list if needed
    if isinstance(tags, str):
        tags = [tag.strip() for tag in tags.split(",")]

    html = """
    <div style="
        display:flex;
        flex-wrap:wrap;
        gap:8px;
        align-items:center;
    ">
    """

    for tag in tags:

        html += f"""
        <span style="
            background:{color};
            color:white;
            padding:4px 10px;
            border-radius:999px;
            font-size:12px;
            font-weight:600;
            white-space:nowrap;
        ">
            {tag}
        </span>
        """

    html += "</div>"

    st.html(html)

def create_ats_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "ATS Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#2563eb"},
                "steps": [
                    {"range": [0, 40], "color": "#ef4444"},
                    {"range": [40, 70], "color": "#f59e0b"},
                    {"range": [70, 100], "color": "#22c55e"}
                ]
            }
        )
    )

    fig.update_layout(
        height=300,
        margin=dict(l=30, r=30, t=60, b=30)
    )

    return fig


st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

resume_text = ""

if uploaded_file:

    resume_text = extract_resume_text(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📄 Resume Content")

        st.text_area(
            "Extracted Resume Text",
            resume_text,
            height=450
        )

    with col2:

        st.subheader("💼 Job Description")

        job_description = st.text_area(
            "Paste Job Description Here",
            height=450
        )

    st.divider()

    if st.button(
        "Analyze Resume",
        use_container_width=True
    ):

        if not job_description.strip():

            st.warning(
                "Please enter a Job Description."
            )

        else:

            with st.spinner("Analyzing resume using AI..."):

                # Extract skills using OpenAI
                resume_skills = extract_skills(
                    resume_text
                )

                jd_skills = extract_skills(
                    job_description
                )

                # Compare skills and calculate ATS score
                result = analyze_resume(
                    resume_skills,
                    jd_skills
                )

                # Generate AI suggestions
                suggestions = generate_suggestions(
                    resume_text,
                    job_description,
                    result["missing"]
                )

                save_analysis(

                    filename=uploaded_file.name,

                    score=result["score"],

                    matched_skills=result["matched"],

                    missing_skills=result["missing"],

                    recommendations=suggestions
                )
                
                st.success("Analysis saved successfully!")

            st.success("Analysis Complete!")

            # ATS Gauge
            st.plotly_chart(
                create_ats_gauge(result["score"]),
                use_container_width=True
            )

            

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### ✅ Matching Skills")

                show_tags(
                    result["matched"],
                    "#22c55e"
                )


            with col2:

                st.markdown("### ❌ Missing Skills")

                show_tags(
                    result["missing"],
                    "#ef4444"
                )

            st.divider()

            st.subheader("💡 AI Suggestions")

            for suggestion in suggestions:

                st.info(suggestion)