from extractor.parser import extract_text


files = [
    "sample_resumes/resume_john_doe.pdf",
    "sample_resumes/resume_jane_smith.docx",
]


for file_path in files:
    print("=" * 60)
    print(f"TESTING: {file_path}")
    print("=" * 60)

    try:
        text = extract_text(file_path)

        print(text)

    except Exception as e:
        print(f"ERROR: {e}")

    print()
