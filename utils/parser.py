import re
import PyPDF2


def extract_text(pdf_file):
    text = ""

    reader = PyPDF2.PdfReader(pdf_file)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_details(text):
    """
    Extract basic information from resume text.
    """

    details = {}

    # ---------------- Email ----------------

    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    details["email"] = (
        email.group()
        if email else "Not Found"
    )

    # ---------------- Phone ----------------

    phone = re.search(
        r"(\+?\d[\d\s\-]{8,15}\d)",
        text
    )

    details["phone"] = (
        phone.group()
        if phone else "Not Found"
    )

    # ---------------- LinkedIn ----------------

    linkedin = re.search(
        r"(https?:\/\/)?(www\.)?linkedin\.com\/[^\s]+",
        text,
        re.IGNORECASE
    )

    details["linkedin"] = (
        linkedin.group()
        if linkedin else "Not Found"
    )

    # ---------------- GitHub ----------------

    github = re.search(
        r"(https?:\/\/)?(www\.)?github\.com\/[^\s]+",
        text,
        re.IGNORECASE
    )

    details["github"] = (
        github.group()
        if github else "Not Found"
    )

    # ---------------- Name ----------------

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    name = "Not Found"

    for line in lines[:10]:

        # Skip emails
        if "@" in line:
            continue

        # Skip URLs
        if (
            "linkedin" in line.lower()
            or "github" in line.lower()
            or "http" in line.lower()
        ):
            continue

        # Skip lines containing numbers
        if any(char.isdigit() for char in line):
            continue

        # Likely candidate name
        if len(line.split()) >= 2:
            name = line
            break

    details["name"] = name

    return details