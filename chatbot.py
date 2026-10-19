
import re
import sqlite3
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from database import create_database, DATABASE


# =========================================================
# DATABASE SETUP
# =========================================================

def load_faqs():
    """Load FAQ question-answer pairs from the database."""
    try:
        create_database()

        connection = sqlite3.connect(str(DATABASE))
        rows = connection.execute(
            "SELECT question, answer FROM faq"
        ).fetchall()
        connection.close()

        return rows

    except (sqlite3.Error, Exception) as error:
        print("FAQ database error:", error)
        return []


# =========================================================
# TEXT NORMALIZATION
# =========================================================

REPLACEMENTS = {
    "collage": "college",
    "colleg": "college",
    "collge": "college",
    "admisson": "admission",
    "admisssion": "admission",
    "eligiblity": "eligibility",
    "eligibilty": "eligibility",
    "placment": "placement",
    "scholrship": "scholarship",
    "hostel iruka": "hostel",
    "hostel irukka": "hostel",
    "hostel available ah": "hostel",
    "iruka": "available",
    "irukka": "available",
    "irukaa": "available",
    "enga": "where",
    "yenga": "where",
    "ethana": "how many",
    "evlo": "how much",
    "evalo": "how much",
    "padika": "study",
    "padikka": "study",
    "padikkanum": "study",
    "venum": "want",
    "venuma": "want",
    "sollu": "tell",
    "sollunga": "tell",
    "enna": "what",
    "epdi": "how",
    "eppadi": "how",
}


def normalize(text):
    text = (text or "").lower().strip()

    for old, new in sorted(
        REPLACEMENTS.items(),
        key=lambda item: len(item[0]),
        reverse=True,
    ):
        text = text.replace(old, new)

    # Keep English, Tamil, numbers and common symbols
    text = re.sub(r"[^\w\s\u0B80-\u0BFF.+&-]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# =========================================================
# EXCEL GROUP INSTITUTION LIST
# =========================================================

def is_institution_list_question(text):
    """Detect questions asking for the full Excel Group institution list."""
    text = normalize(text)
    phrases = [
        "institution list", "institutions list", "list of institutions",
        "all institutions", "institution names", "college list",
        "colleges list", "list of colleges", "all colleges",
        "excel group colleges", "excel group institutions",
        "what institutions", "which institutions", "what colleges",
        "which colleges", "college names", "ella college",
        "ella colleges", "ella institution", "ella institutions",
        "moththa college", "full college list", "available institutions",
        "institutions available", "how many colleges", "how many institutions",
    ]
    return any(phrase in text for phrase in phrases)


def institution_list_answer():
    """Return the Excel Group institution list for institution-list questions."""
    return (
        "🏫 Excel Institutions Group – Institution List\n\n"
        "TECHNICAL CAMPUS\n"
        "1. Excel Engineering College (Autonomous)\n"
        "2. Excel College of Architecture and Planning\n"
        "3. Excel Polytechnic College\n"
        "4. Excel College for Commerce and Science\n"
        "5. Excel College of Education\n"
        "6. Excel Business School\n\n"
        "MEDICAL CAMPUS\n"
        "7. Excel College of Pharmacy\n"
        "8. Excel Institute of Health Sciences\n"
        "9. Excel Nursing College\n"
        "10. Excel Medical College for Naturopathy and Yoga\n"
        "11. Excel Siddha Medical College and Research Centre\n"
        "12. Excel Homoeopathy Medical College\n"
        "13. Excel College of Physiotherapy and Research Centre\n"
        "14. Excel Multispeciality Hospitals\n\n"
        "SCHOOL CAMPUS\n"
        "15. Excel Public School (CBSE)\n\n"
        "For the latest official list and campus details, visit: "
        "https://excelinstitutions.com/\n\n"
        "If you want, ask me about any one institution or its courses."
    )


# =========================================================
# GREETING RESPONSES
# =========================================================

def greeting_response(text):
    greetings = {
        "hi", "hello", "hey", "vanakkam",
        "good morning", "good afternoon", "good evening",
    }

    if text in greetings:
        return (
            "👋 Hello! Welcome to Excel Institute AI Assistant.\n\n"
            "I can help you with:\n"
            "• Courses and programmes\n"
            "• 12th after-study guidance\n"
            "• Eligibility and admission\n"
            "• Scholarships\n"
            "• Hostel and facilities\n"
            "• Placement\n"
            "• Institution address and contact\n\n"
            "Ask your question in English or Tanglish!"
        )
