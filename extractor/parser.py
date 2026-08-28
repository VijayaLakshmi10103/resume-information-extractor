import pymupdf
from docx import Document


def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF resume.
    """

    try:
        document = pymupdf.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        if not text.strip():
            raise ValueError("The PDF does not contain readable text.")

        return text

    except Exception as e:
        raise ValueError(f"Unable to read PDF file: {e}")


def extract_text_from_docx(file_path):
    """
    Extract text from a DOCX resume.
    """

    try:
        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                paragraphs.append(paragraph.text)

        text = "\n".join(paragraphs)

        if not text.strip():
            raise ValueError("The DOCX does not contain readable text.")

        return text

    except Exception as e:
        raise ValueError(f"Unable to read DOCX file: {e}")


def extract_text(file_path):
    """
    Detect the file type and extract text.
    Supports PDF and DOCX.
    """

    if not file_path:
        raise ValueError("No file path was provided.")

    file_path_lower = file_path.lower()

    if file_path_lower.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif file_path_lower.endswith(".docx"):
        return extract_text_from_docx(file_path)

    else:
        raise ValueError(
            "Unsupported file format. Please upload a PDF or DOCX file."
        )