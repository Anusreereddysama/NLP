import streamlit as st
from utils import extract_text_from_pdf, clean_text, extract_skills
from model import calculate_similarity

st.set_page_config(page_title="AI Resume Screening System")

st.title("📄 AI Resume Screening & Job Recommendation System")

# Upload Resume
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job Description
job_desc = st.text_area("Enter Job Description")

# Job Recommendation Function
def recommend_jobs(skills):
    roles = {
        "Data Scientist": ["python", "machine learning", "pandas"],
        "NLP Engineer": ["nlp", "text processing", "spacy"],
        "Backend Developer": ["python", "fastapi", "sql"],
        "Data Analyst": ["python", "sql", "pandas"]
    }

    matched_roles = []

    for role, req_skills in roles.items():
        if any(skill in skills for skill in req_skills):
            matched_roles.append(role)

    return matched_roles

# Skill match logic
def skill_match(resume_skills, jd_skills):
    match = set(resume_skills).intersection(set(jd_skills))
    
    if len(jd_skills) == 0:
        return 0, []

    percentage = (len(match) / len(jd_skills)) * 100
    missing = list(set(jd_skills) - set(resume_skills))

    return round(percentage, 2), missing


if st.button("Analyze"):
    if resume_file and job_desc:

        # Extract text
        resume_text = extract_text_from_pdf(resume_file)

        # Clean text
        resume_clean = clean_text(resume_text)
        jd_clean = clean_text(job_desc)

        # Extract skills
        resume_skills = extract_skills(resume_clean)
        jd_skills = extract_skills(jd_clean)

        # BERT Similarity
        score = calculate_similarity(resume_clean, jd_clean)

        # Skill match
        skill_percent, missing_skills = skill_match(resume_skills, jd_skills)

        # Recommendation logic
        if score > 75 and skill_percent > 60:
            recommendation = "✅ Highly Suitable"
        elif score > 60:
            recommendation = "👍 Moderately Suitable"
        else:
            recommendation = "❌ Not Suitable"

        # Job recommendation
        recommended_jobs = recommend_jobs(resume_skills)

        # Display
        st.subheader("📊 Results")

        st.write(f"**Match Score:** {score}%")
        st.write(f"**Skill Match:** {skill_percent}%")

        st.write("**Resume Skills:**", resume_skills)
        st.write("**Missing Skills:**", missing_skills)

        st.write("### 🎯 Recommendation:", recommendation)
        st.write("### 💼 Recommended Roles:", recommended_jobs)

    else:
        st.warning("Please upload resume and enter job description")