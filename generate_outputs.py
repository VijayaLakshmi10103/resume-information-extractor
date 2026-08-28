import json
import os

from extractor.json_generator import extract_resume_information


files = [
    "sample_resumes/resume_john_doe.pdf",
    "sample_resumes/resume_jane_smith.docx",
]


os.makedirs("sample_outputs", exist_ok=True)


for file_path in files:

    data = extract_resume_information(file_path)

    filename = os.path.splitext(
        os.path.basename(file_path)
    )[0]

    output_path = f"sample_outputs/{filename}.json"

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Created: {output_path}")