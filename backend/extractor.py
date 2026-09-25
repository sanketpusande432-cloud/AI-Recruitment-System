import re

def extract_skills(text):

    skills_list = [
        "python",
        "java",
        "sql",
        "machine learning",
        "deep learning",
        "data science",
        "fastapi",
        "django",
        "flask",
        "html",
        "css",
        "javascript",
        "postgresql",
        "git",
        "github"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills

def extract_experience(text):

    text = text.lower()

    pattern = r"(\d+)\+?\s*(?:years|year|yrs|yr)\s+(?:of\s+)?experience"

    match = re.search(pattern, text)

    if match:
        return int(match.group(1))

    return 0

def extract_education(text):

    education_list = [
        "b.tech",
        "b.e",
        "bca",
        "b.sc",
        "m.tech",
        "mca",
        "m.sc",
        "mba",
        "bachelor",
        "master"
    ]

    found_education = []

    text = text.lower()

    for education in education_list:
        if education in text:
            found_education.append(education)

    return found_education

def extract_job_skills(required_skills):

    skills = required_skills.split(",")

    clean_skills = []

    for skill in skills:
        clean_skills.append(skill.strip().lower())

    return clean_skills