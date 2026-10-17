
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
# 12TH COURSE GUIDANCE
# =========================================================

def twelfth_guidance(text):
    keywords = [
        "12th", "12 th", "plus two", "12 mudichu",
        "12 mudichitu", "12th pass", "after 12th",
        "12th completed", "12th mudichu",
    ]

    if any(word in text for word in keywords):
        return (
            "🎓 12th mudichitu enna padikkalaam?\n\n"
            "Un 12th group and interest-ku etha maadhiri "
            "course choose pannalaam.\n\n"
            "• Arts and Science\n"
            "• Engineering\n"
            "• Polytechnic\n"
            "• Pharmacy\n"
            "• Nursing and Health Sciences\n"
            "• Business and Management\n\n"
            "Un 12th group enna?\n"
            "Computer Science, Bio-Maths, Commerce, illa Arts?\n\n"
            "Un group sonna, suitable courses pathi help panren."
        )

    return None


# =========================================================
# DIRECT ANSWERS
# =========================================================

def direct_answer(text):
    # Courses
    if text in {
        "course", "courses", "what courses",
        "which courses", "available courses",
        "course list", "programmes", "programs",
    }:
        return (
            "🎓 Courses at Excel Group Institutions\n\n"
            "Excel Group includes different types of institutions, "
            "such as Arts and Science, Engineering, Polytechnic, "
            "Pharmacy, Nursing, Health Sciences and other fields.\n\n"
            "The exact courses depend on the institution. "
            "Ask about a particular course, such as BCA, B.Com "
            "or Engineering, for more details."
        )

    # BCA
    if re.search(r"\bbca\b", text):
        return (
            "💻 BCA - Bachelor of Computer Applications\n\n"
            "BCA is an undergraduate course related to computer "
            "applications, programming and software concepts.\n\n"
            "Exact availability, eligibility and fees should be "
            "confirmed with the institution."
        )

    # B.Com
    if re.search(r"\bb\.?\s*com\b|\bbcom\b", text):
        return (
            "📘 B.Com - Bachelor of Commerce\n\n"
            "B.Com is an undergraduate programme focused on "
            "commerce, accounting and business subjects.\n\n"
            "Exact availability, eligibility and fees should be "
            "confirmed with the institution."
        )

    # Admission
    if any(word in text for word in [
        "admission", "apply", "application", "join college",
    ]):
        return (
            "📝 Admission Enquiry\n\n"
            "Admission requirements depend on the course and "
            "institution. Contact the relevant Excel institution "
            "to confirm application dates, required certificates "
            "and eligibility."
        )

    # Eligibility
    if any(word in text for word in [
        "eligibility", "eligible", "qualification",
    ]):
        return (
            "📚 Course Eligibility\n\n"
            "Eligibility depends on the programme you choose "
            "and your qualifying examination marks/group.\n\n"
            "Tell me the course name and your 12th group "
            "so I can guide you further."
        )

    # Hostel
    if "hostel" in text:
        return (
            "🏠 Hostel Enquiry\n\n"
            "Hostel availability and facilities can vary by "
            "institution. Please confirm current availability, "
            "fees and rules with the relevant campus."
        )

    # Placement
    if "placement" in text or "placements" in text:
        return (
            "💼 Placement Enquiry\n\n"
            "Placement opportunities and training depend on "
            "the institution, course and academic year. "
            "Contact the relevant department for current "
            "placement information."
        )

    # Scholarship
    if "scholarship" in text:
        return (
            "🎓 Scholarship Enquiry\n\n"
            "Scholarship eligibility depends on the scheme, "
            "student category and applicable rules. Contact "
            "the institution office to confirm current schemes "
            "and required documents."
        )

    # Address
    if any(word in text for word in [
        "address", "location", "where is excel",
    ]):
        return (
            "📍 Excel Group Institutions\n\n"
            "NH-544, Salem Main Road, Sankari West, "
            "Pallakkapalayam, Komarapalayam, "
            "Namakkal District, Tamil Nadu - 637303.\n\n"
            "Please verify the address of the specific campus "
            "before visiting."
        )

    # Contact
    if any(word in text for word in [
        "contact", "phone number", "email", "telephone",
    ]):
        return (
            "📞 Contact Enquiry\n\n"
            "For the latest phone number, email and department "
            "contact details, please check the official Excel "
            "Group website or contact the relevant campus."
        )

    return None


# =========================================================
# FAQ SIMILARITY SEARCH
# =========================================================

def faq_answer(user_text):
    rows = load_faqs()

    if not rows:
        return None

    questions = [
        normalize(str(question))
        for question, answer in rows
        if question and answer
    ]

    valid_rows = [
        (question, answer)
        for question, answer in rows
        if question and answer
    ]

    if not questions:
        return None

    try:
        vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True,
            strip_accents=None,
        )

        matrix = vectorizer.fit_transform(
            questions + [normalize(user_text)]
        )

        similarities = cosine_similarity(
            matrix[-1],
            matrix[:-1],
        ).flatten()

        best_index = int(similarities.argmax())
        best_score = float(similarities[best_index])

        if best_score >= 0.18:
            answer = str(valid_rows[best_index][1])

            # Avoid showing the abbreviation ECCS in answers
            answer = re.sub(
                r"\bECCS\b",
                "Excel College for Commerce and Science",
                answer,
                flags=re.IGNORECASE,
            )

            return answer

    except ValueError as error:
        print("FAQ matching error:", error)

    return None


# =========================================================
# MAIN RESPONSE FUNCTION
# =========================================================

def get_response(user_message):
    text = normalize(user_message)

    if not text:
        return "Please enter a question."

    # 1. Greetings
    answer = greeting_response(text)
    if answer:
        return answer

    # 2. 12th completed guidance
    answer = twelfth_guidance(text)
    if answer:
        return answer

    # 3. Direct responses
    answer = direct_answer(text)
    if answer:
        return answer

    # 4. FAQ database + TF-IDF
    answer = faq_answer(text)
    if answer:
        return answer

    # 5. Unknown question
    return (
        "🤖 I couldn't find a reliable answer for that question "
        "in my Excel Group database.\n\n"
        "Try asking about courses, BCA, admission, eligibility, "
        "hostel, placement, scholarship or institution details.\n\n"
        "You can also ask in Tamil or Tanglish."
    )


# =========================================================
# TEST LOCALLY
# =========================================================

if __name__ == "__main__":
    print("EXCEL GROUP AI CHATBOT")
    print("Type 'exit' to stop.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() in {"exit", "quit"}:
            break

        print("\nBot:", get_response(question))
