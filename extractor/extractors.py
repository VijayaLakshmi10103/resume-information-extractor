import re


# Common skills that may appear in resumes.
SKILLS_LIST = [
    "Python",
    "Java",
    "JavaScript",
    "C",
    "C++",
    "C#",
    "SQL",
    "HTML",
    "CSS",
    "React",
    "Angular",
    "Node.js",
    "Django",
    "Flask",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Data Analysis",
    "Excel",
    "Power BI",
    "Tableau",
    "Git",
    "Docker",
    "AWS",
    "Azure",
]


def extract_email(text):
    """
    Extract an email address from resume text.
    """

    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    match = re.search(pattern, text)

    if match:
        return match.group(0)

    return None


def extract_phone(text):
    """
    Extract a phone number from resume text.
    """

    patterns = [
        r"\+91[\s-]?\d{5}[\s-]?\d{5}",
        r"\+91[\s-]?\d{10}",
        r"\b\d{10}\b",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            return match.group(0)

    return None


def extract_name(text):
    """
    Extract the candidate's name.

    Assumption:
    The candidate's name is usually located near the beginning
    of the resume before contact information.
    """

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if not lines:
        return None

    excluded_words = {
        "resume",
        "curriculum vitae",
        "cv",
        "email",
        "phone",
        "mobile",
        "contact",
        "skills",
        "education",
        "experience",
        "linkedin",
        "github",
    }

    for line in lines[:10]:

        lower_line = line.lower()

        if lower_line in excluded_words:
            continue

        if "@" in line:
            continue

        if "linkedin.com" in lower_line:
            continue

        if "github.com" in lower_line:
            continue

        if re.search(r"\d", line):
            continue

        words = line.split()

        if 2 <= len(words) <= 5:
            return line

    return None


def extract_skills(text):
    """
    Extract skills by matching against a predefined skills list.
    """

    found_skills = []

    text_lower = text.lower()

    for skill in SKILLS_LIST:

        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return found_skills

def extract_education(text):
    """
    Extract education details from resume text.

    Assumption:
    Education entries usually appear after an EDUCATION heading,
    with the degree on one line and institution on the next line.
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    education = []
    in_education = False

    degree_keywords = [
        "b.tech",
        "b.e",
        "b.sc",
        "bca",
        "m.tech",
        "m.e",
        "m.sc",
        "mca",
        "mba",
        "phd",
        "bachelor",
        "master",
        "degree",
    ]

    stop_sections = {
        "experience",
        "work experience",
        "employment",
        "skills",
        "projects",
        "certifications",
        "linkedin",
        "github",
    }

    for i, line in enumerate(lines):
        lower_line = line.lower()

        if lower_line in {"education", "academic background"}:
            in_education = True
            continue

        if in_education and lower_line in stop_sections:
            break

        if in_education:
            if any(keyword in lower_line for keyword in degree_keywords):
                institution = None

                if i + 1 < len(lines):
                    next_line = lines[i + 1]

                    if next_line.lower() not in stop_sections:
                        institution = next_line

                education.append({
                    "degree": line,
                    "institution": institution
                })

    return education


def extract_experience(text):
    """
    Extract basic work experience details.

    Assumption:
    A job role is usually followed by the company name.
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    experience = []
    in_experience = False

    stop_sections = {
        "education",
        "skills",
        "projects",
        "certifications",
        "linkedin",
        "github",
    }

    for i, line in enumerate(lines):
        lower_line = line.lower()

        if lower_line in {
            "experience",
            "work experience",
            "employment",
            "professional experience",
        }:
            in_experience = True
            continue

        if in_experience and lower_line in stop_sections:
            break

        if in_experience:
            role_keywords = [
                "intern",
                "developer",
                "engineer",
                "manager",
                "analyst",
                "designer",
                "consultant",
                "associate",
            ]

            if any(keyword in lower_line for keyword in role_keywords):
                company = None

                if i + 1 < len(lines):
                    next_line = lines[i + 1]

                    if next_line.lower() not in stop_sections:
                        company = next_line

                experience.append({
                    "role": line,
                    "company": company
                })

    return experience


def extract_linkedin(text):
    """
    Extract LinkedIn profile URL.
    """
    pattern = r"https?://(?:www\.)?linkedin\.com/in/[A-Za-z0-9._-]+"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group(0)

    return None


def extract_github(text):
    """
    Extract GitHub profile URL.
    """
    pattern = r"https?://(?:www\.)?github\.com/[A-Za-z0-9._-]+"

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group(0)

    return None