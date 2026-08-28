from extractor.parser import extract_text
from extractor.extractors import (
    extract_name,
    extract_email,
    extract_phone,
    extract_skills,
    extract_education,
    extract_experience,
    extract_linkedin,
    extract_github,
)


def extract_resume_information(file_path):
    """
    Extract information from a PDF or DOCX resume
    and return it as a structured dictionary.
    """

    text = extract_text(file_path)

    resume_data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
        "linkedin": extract_linkedin(text),
        "github": extract_github(text),
    }

    return resume_data