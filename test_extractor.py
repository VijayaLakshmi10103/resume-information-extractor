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


files = [
    "sample_resumes/resume_john_doe.pdf",
    "sample_resumes/resume_jane_smith.docx",
]


for file_path in files:

    print("=" * 60)
    print("TESTING:", file_path)
    print("=" * 60)

    try:
        text = extract_text(file_path)

        print("Name:", extract_name(text))
        print("Email:", extract_email(text))
        print("Phone:", extract_phone(text))
        print("Skills:", extract_skills(text))
        print("Education:", extract_education(text))
        print("Experience:", extract_experience(text))
        print("LinkedIn:", extract_linkedin(text))
        print("GitHub:", extract_github(text))

    except Exception as error:
        print("ERROR:", error)

    print()