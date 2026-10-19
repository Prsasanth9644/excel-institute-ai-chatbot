import re
import sqlite3

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
        with sqlite3.connect(str(DATABASE)) as connection:
            rows = connection.execute(
                "SELECT question, answer FROM faq"
            ).fetchall()
        return rows
    except Exception as error:
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
        REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True
    ):
        text = text.replace(old, new)

    text = re.sub(r"[^\w\s\u0B80-\u0BFF.+&-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# =========================================================
# EXCEL GROUP INSTITUTION LIST
# =========================================================

def is_institution_list_question(text):
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
        "institutions available", "how many colleges",
        "how many institutions",
    ]
    return any(phrase in text for phrase in phrases)


def institution_list_answer():
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
        "Ask me about any one institution or its courses."
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
    return None


# =========================================================
# FAQ MATCHING
# =========================================================

def faq_answer(user_text):
    """Find the closest FAQ using TF-IDF and cosine similarity."""
    faqs = load_faqs()
    if not faqs:
        return None

    questions = [row[0] for row in faqs]
    answers = [row[1] for row in faqs]
    normalized_questions = [normalize(question) for question in questions]
    normalized_user_text = normalize(user_text)

    if not normalized_user_text:
        return None

    try:
        vectorizer = TfidfVectorizer(ngram_range=(1, 2), analyzer="word")
        matrix = vectorizer.fit_transform(normalized_questions + [normalized_user_text])
        scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()
        best_index = int(scores.argmax())
        best_score = float(scores[best_index])

        # Conservative threshold to reduce unrelated answers.
        if best_score >= 0.18:
            return answers[best_index]
    except Exception as error:
        print("FAQ matching error:", error)

    return None


# =========================================================
# MAIN RESPONSE FUNCTION
# =========================================================

def get_response(user_message):
    """Return a chatbot response for the Flask /chat route."""
    message = (user_message or "").strip()
    if not message:
        return "Please enter a question."

    normalized_message = normalize(message)

    greeting = greeting_response(normalized_message)
    if greeting:
        return greeting

    # Check this first so institution-list questions don't receive
    # a generic FAQ answer or only the website link.
    if is_institution_list_question(normalized_message):
        return institution_list_answer()

    answer = faq_answer(normalized_message)
    if answer:
        return answer

    return (
        "Sorry, I couldn't find an exact answer to that question yet.\n\n"
        "You can ask me about Excel Group institutions, courses, admission, "
        "eligibility, scholarships, hostel, placements, or contact details.\n\n"
        "Official website: https://excelinstitutions.com/"
    )
