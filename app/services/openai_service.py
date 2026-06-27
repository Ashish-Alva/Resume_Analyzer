import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

MODEL = "openai/gpt-oss-120b:free"

def extract_skills(text):

    prompt = f"""
Extract all technical skills from this text.

Include:
- Programming languages
- Frameworks
- Databases
- Cloud technologies
- DevOps tools
- Libraries
- Platforms

Return ONLY valid JSON.

Example:

{{
    "skills": [
        "Python",
        "Docker",
        "AWS",
        "Kubernetes"
    ]
}}

TEXT:

{text}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    # Remove markdown if model returns ```json
    content = content.replace("```json", "")
    content = content.replace("```", "").strip()

    return json.loads(content)["skills"]


def generate_suggestions(
    resume_text,
    job_description,
    missing_skills
):

    prompt = f"""
You are an ATS Resume Expert.

Missing Skills:
{missing_skills}

Job Description:
{job_description}

Provide 5 concise suggestions to improve the resume.

Return ONLY JSON:

{{
    "suggestions": [
        "...",
        "..."
    ]
}}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content

    content = content.replace("```json", "")
    content = content.replace("```", "").strip()

    return json.loads(content)["suggestions"]