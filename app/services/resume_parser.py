# services/resume_parser.py

from PyPDF2 import PdfReader
from docx import Document


def parse_pdf(uploaded_file):

    try:

        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:

        raise Exception(
            f"PDF parsing failed: {e}"
        )


def parse_docx(uploaded_file):

    try:

        document = Document(uploaded_file)

        text = ""

        for paragraph in document.paragraphs:

            text += paragraph.text + "\n"

        return text

    except Exception as e:

        raise Exception(
            f"DOCX parsing failed: {e}"
        )


def extract_resume_text(uploaded_file):

    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):

        return parse_pdf(uploaded_file)

    elif filename.endswith(".docx"):

        return parse_docx(uploaded_file)

    else:

        raise ValueError(
            "Only PDF and DOCX files are supported."
        )