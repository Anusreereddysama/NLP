# AI Resume Screening & Job Recommendation System

## 🚀 Overview

This project is an AI-powered system that automatically analyzes resumes and matches them with job descriptions using NLP and Machine Learning.

## 🔥 Features

* Resume parsing (PDF)
* Skill extraction using NLP (spaCy)
* Semantic similarity using BERT (Sentence Transformers)
* Match score (0–100%)
* Skill gap analysis
* Job recommendations
* Streamlit UI

## 🧠 Tech Stack

* Python
* Streamlit
* spaCy
* Sentence Transformers (BERT)
* Scikit-learn

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

## 📊 Output

* Match Score
* Skill Match %
* Missing Skills
* Recommendation
* Suggested Job Roles

## 💡 Future Improvements

* Resume ranking system
* Dashboard analytics
* FastAPI backend
* Deployment
