# Resume Information Extraction System

A Python-based Resume Information Extraction System that accepts PDF and DOCX resumes and extracts structured candidate information using document parsing, regular expressions, and rule-based techniques.

The system does **not use external LLM or Generative AI APIs**. Resume processing is performed locally and the extracted information is returned as structured JSON.

## Project Overview

This project accepts resumes in:

* PDF format
* DOCX format

The system extracts important candidate information and converts it into a structured JSON object.

## Information Extracted

### Mandatory Information

* Full Name
* Email Address
* Phone Number
* Skills

### Additional Information

* Education
* Work Experience
* LinkedIn Profile
* GitHub Profile

## Features

* PDF resume parsing
* DOCX resume parsing
* Candidate name extraction
* Email extraction
* Phone number extraction
* Skills extraction using a predefined skills list
* Education extraction
* Work experience extraction
* LinkedIn profile extraction
* GitHub profile extraction
* Structured JSON generation
* Error handling for invalid or unreadable files
* Unsupported file format validation
* Local resume processing
* No external LLM or Generative AI API required

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
     +----> Name
     +----> Email
     +----> Phone
     +----> Skills
     +----> Education
     +----> Experience
     +----> LinkedIn
     +----> GitHub
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

* Candidate name
* Email address
* Phone number
* Skills
* Education
* Work experience
* LinkedIn profile
* GitHub profile

Skills are detected using a predefined list of commonly used technical skills.

## Supported File Formats

| Format | Supported |
| ------ | --------- |
| PDF    | Yes       |
| DOCX   | Yes       |

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
|
├── extractor/
│   ├── __init__.py
│   ├── parser.py
│   ├── extractors.py
│   └── json_generator.py
|
├── sample_resumes/
│   ├── resume_john_doe.pdf
│   └── resume_jane_smith.docx
|
├── sample_outputs/
│   ├── resume_john_doe.json
│   └── resume_jane_smith.json
|
├── test_parser.py
├── test_extractor.py
├── test_json.py
├── generate_outputs.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/VijayaLakshmi10103/resume-information-extractor.git
cd resume-information-extractor
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

Place a PDF or DOCX resume inside the `sample_resumes` directory.

### Test PDF and DOCX Parsing

```bash
python test_parser.py
```

### Test Information Extraction

```bash
python test_extractor.py
```

### Test JSON Generation

```bash
python test_json.py
```

### Generate Sample JSON Output Files

```bash
python generate_outputs.py
```

Generated JSON files will be stored inside:

```text
sample_outputs/
```

## Sample Output

Example:

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

## Sample Resumes

The repository contains two sample resumes for testing:

1. `resume_john_doe.pdf`
2. `resume_jane_smith.docx`

These demonstrate that the system supports both PDF and DOCX input formats.

## Assumptions

The extraction system uses rule-based assumptions because resume layouts can vary significantly.

Examples:

* Candidate names are generally located near the beginning of the resume.
* Email addresses follow common email patterns.
* Phone numbers follow common Indian/international phone number formats.
* Skills are detected using a predefined skills list.
* Education information is detected around an `EDUCATION` section.
* Work experience is detected around an `EXPERIENCE` section.
* LinkedIn and GitHub profiles are detected using standard URL patterns.

## Error Handling

The parser validates the input file format and handles invalid or unreadable documents.

Supported formats:

```text
.pdf
.docx
```

Unsupported formats are rejected instead of being processed incorrectly.

## Testing

The project has been tested with:

* PDF resume input
* DOCX resume input
* Candidate name extraction
* Email extraction
* Phone number extraction
* Skills extraction
* Education extraction
* Work experience extraction
* LinkedIn extraction
* GitHub extraction
* Structured JSON generation
* Sample JSON file generation

Both sample resumes successfully produce structured JSON output.

## Dependencies

Dependencies are listed in `requirements.txt`.

```text
PyMuPDF==1.28.2
python-docx==1.2.0
```

## Security

* No API keys or secret credentials are required.
* No external LLM or Generative AI API is used.
* Resume processing is performed locally.
* The virtual environment is excluded using `.gitignore`.
* Python cache files are excluded from version control.
* Environment variable files are excluded from version control.

## Screenshots

Screenshots can be added here to demonstrate:

1. PDF resume input and extracted information.
2. DOCX resume input and extracted information.
3. Generated JSON output.

## Assignment Deliverables

This repository contains:

* Python source code
* PDF resume parser
* DOCX resume parser
* Information extraction logic
* Structured JSON generation
* Sample PDF resume
* Sample DOCX resume
* Sample JSON outputs
* Test scripts
* Requirements file
* `.gitignore`
* Project documentation

## Limitations

This project uses rule-based extraction techniques. Resume formats can vary significantly, so extraction accuracy may depend on the structure and formatting of the input resume.

Potential limitations include:

* Highly unusual resume layouts
* Scanned/image-only PDFs without selectable text
* Non-standard section headings
* Skills not included in the predefined skills list
* Complex multi-column resume layouts
* Ambiguous education or experience descriptions

## Author

**Vijaya Lakshmi**

## License

This project is created for educational and assignment purposes.
