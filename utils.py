import spacy
import re
from PyPDF2 import PdfReader

nlp = spacy.load("en_core_web_sm")

# Extract text from PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# Skill database (expanded)
SKILL_DB = [
    "python", "java", "c++", "machine learning", "deep learning",
    "nlp", "data science", "sql", "tensorflow", "pytorch",
    "fastapi", "streamlit", "pandas", "numpy", "scikit-learn",
    "communication", "teamwork", "leadership",
    "tf-idf", "cosine similarity", "text processing"
]

# Extract skills
def extract_skills(text):
    doc = nlp(text)
    found_skills = set()

    # Token-based matching
    for token in doc:
        for skill in SKILL_DB:
            if skill in token.text.lower():
                found_skills.add(skill)

    # Phrase-based matching
    for skill in SKILL_DB:
        if skill in text.lower():
            found_skills.add(skill)

    return list(found_skills)