import json

from extractor.json_generator import extract_resume_information


files = [
    "sample_resumes/resume_john_doe.pdf",
    "sample_resumes/resume_jane_smith.docx",
]


for file_path in files:

    print("=" * 60)
    print(f"TESTING: {file_path}")
    print("=" * 60)

    try:
        data = extract_resume_information(file_path)

        print(json.dumps(data, indent=4))

    except Exception as e:
        print("ERROR:", e)

    print()