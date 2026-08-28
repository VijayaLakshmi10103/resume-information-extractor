# Resume Information Extraction System

A Python-based Resume Information Extraction System that accepts PDF and DOCX resumes and extracts structured candidate information using document parsing, regular expressions, and rule-based techniques.

The system does **not** use external LLM or Generative AI APIs for resume information extraction.

## Project Overview

This project was developed as part of the Tribera internship technical assignment.

The application accepts resumes in:

* PDF format
* DOCX format

It extracts candidate information and returns the result as structured JSON.

## Information Extracted

### Mandatory Fields

* Full Name
* Email Address
* Phone Number
* Skills

### Bonus Fields

* Education
* Work Experience
* LinkedIn Profile
* GitHub Profile

## Example JSON Output

```json
{
    "name": "JOHN DOE",
    "email": "john.doe@gmail.com",
    "phone": "+91 9876543210",
    "skills": [
        "Python",
        "Java",
        "SQL",
        "HTML",
        "CSS",
        "Machine Learning"
    ],
    "education": [
        {
            "degree": "B.Tech in Computer Science",
            "institution": "ABC University"
        }
    ],
    "experience": [
        {
            "role": "Software Developer Intern",
            "company": "ABC Technologies"
        }
    ],
    "linkedin": "https://www.linkedin.com/in/johndoe",
    "github": "https://github.com/johndoe"
}
```

## Features

* PDF resume parsing
* DOCX resume parsing
* Full name extraction
* Email extraction
* Phone number extraction
* Skills extraction
* Education extraction
* Work experience extraction
* LinkedIn profile extraction
* GitHub profile extraction
* Structured JSON generation
* Error handling for unsupported or unreadable files
* Rule-based extraction without external LLM APIs

## Technical Approach

The system follows a simple extraction pipeline:

```text
Resume File
    |
    v
PDF / DOCX Parser
    |
    v
Extracted Text
    |
    v
Rule-Based Information Extraction
    |
    +--> Name
    +--> Email
    +--> Phone
    +--> Skills
    +--> Education
    +--> Experience
    +--> LinkedIn
    +--> GitHub
    |
    v
Structured JSON
```

### PDF Parsing

PDF text is extracted using **PyMuPDF**.

### DOCX Parsing

DOCX text is extracted using **python-docx**.

### Information Extraction

Regular expressions and rule-based techniques are used to identify:

* Email addresses
* Phone numbers
* Social profile URLs
* Candidate names
* Skills
* Education entries
* Work experience entries

Skills are identified using a predefined skills list.

## Technologies Used

* Python
* PyMuPDF
* python-docx
* Regular Expressions
* Rule-based text processing
* JSON

## Project Structure

```text
resume-information-extractor/
│
├── extractor/
│   ├── __init__.py
│   ├── parser.py
│   ├── extractors.py
│   └── json_generator.py
│
├── sample_resumes/
│   ├── resume_john_doe.pdf
│   └── resume_jane_smith.docx
│
├── sample_outputs/
│   ├── resume_john_doe.json
│   └── resume_jane_smith.json
│
├── test_parser.py
├── test_extractor.py
├── test_json.py
├── generate_outputs.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd resume-information-extractor
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Usage

### Test PDF and DOCX parsing

```powershell
python test_parser.py
```

### Test information extraction

```powershell
python test_extractor.py
```

### Test JSON generation

```powershell
python test_json.py
```

### Generate sample JSON output files

```powershell
python generate_outputs.py
```

Generated files will be stored in:

```text
sample_outputs/
```

## Sample Resumes

The repository contains two sample resumes for testing:

1. `resume_john_doe.pdf`
2. `resume_jane_smith.docx`

These demonstrate that the system supports both PDF and DOCX input formats.

## Assumptions

The extraction system uses rule-based assumptions because resumes can have many different layouts.

Examples:

* The candidate name is generally located near the beginning of the resume.
* Email addresses follow common email patterns.
* Phone numbers follow common Indian/international phone number formats.
* Skills are detected from a predefined list of common technical skills.
* Education information is detected around an `EDUCATION` section.
* Work experience is detected around an `EXPERIENCE` section.
* LinkedIn and GitHub profiles are detected using their standard URL patterns.

## Limitations

Because this is a rule-based extraction system, it may not correctly extract information from every possible resume format.

Potential limitations include:

* Highly unusual resume layouts
* Scanned/image-only PDFs without selectable text
* Non-standard section headings
* Skills not included in the predefined skills list
* Complex multi-column resume layouts
* Ambiguous education or experience descriptions

The system is intentionally designed without external LLM or Generative AI services, as required by the assignment.

## Error Handling

The parser validates the file format and handles unsupported or unreadable PDF/DOCX files by returning an appropriate error.

Supported formats:

```text
.pdf
.docx
```

## Testing

The project has been tested with:

* PDF resume input
* DOCX resume input
* Mandatory information extraction
* Bonus information extraction
* Structured JSON generation

Both sample resumes successfully produce structured JSON output.

## Dependencies

Dependencies are listed in:

```text
requirements.txt
```

Current dependencies:

```text
PyMuPDF==1.28.2
python-docx==1.2.0
```

## Security

* No external LLM or Generative AI API is used.
* No API keys or secret credentials are required.
* The virtual environment is excluded from Git using `.gitignore`.
* Python cache files are excluded from Git.

## Assignment Deliverables

This repository contains:

* Source code
* README documentation
* Sample PDF resume
* Sample DOCX resume
* Sample JSON outputs
* Approach and assumptions
* Limitations
* Testing scripts

## Author

Vijaya Lakshmi
