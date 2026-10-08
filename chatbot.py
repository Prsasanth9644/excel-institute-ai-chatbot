import re
import sqlite3
from difflib import SequenceMatcher

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from database import INSTITUTIONS, COURSES


DATABASE = "college.db"


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
    "eppadi": "how"
}


STOP_WORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "am",
    "was",
    "were",
    "be",
    "to",
    "of",
    "in",
    "on",
    "at",
    "for",
    "and",
    "or",
    "can",
    "could",
    "do",
    "does",
    "did",
    "i",
    "me",
    "my",
    "we",
    "you",
    "your",
    "please",
    "tell",
    "about",
    "what",
    "how",
    "want",
    "available",
    "college",
    "da",
    "macha",
    "ah"
}


# =========================================================
# INTENTS
# =========================================================

INTENTS = {

    "course": [
        "course",
        "courses",
        "program",
        "programme",
        "degree",
        "study",
        "படிப்பு",
        "பாடநெறி"
    ],

    "eligibility": [
        "eligibility",
        "qualification",
        "eligible",
        "thaguthi",
        "தகுதி"
    ],

    "admission": [
        "admission",
        "apply",
        "application",
        "join",
        "joining",
        "சேர்க்கை"
    ],

    "fees": [
        "fee",
        "fees",
        "cost",
        "amount",
        "charges",
        "கட்டணம்"
    ],

    "scholarship": [
        "scholarship",
        "financial aid",
        "உதவித்தொகை"
    ],

    "hostel": [
        "hostel",
        "accommodation",
        "விடுதி",
        "தங்கும் விடுதி"
    ],

    "placement": [
        "placement",
        "placements",
        "job",
        "career",
        "வேலை"
    ],

    "facilities": [
        "facility",
        "facilities",
        "library",
        "lab",
        "laboratory",
        "wifi",
        "canteen",
        "sports",
        "transport",
        "bus",
        "atm",
        "வசதி"
    ],

    "address": [
        "address",
        "location",
        "where",
        "எங்கே",
        "முகவரி"
    ],

    "contact": [
        "contact",
        "phone",
        "mobile",
        "number",
        "email",
        "mail",
        "தொடர்பு"
    ],

    "institution": [
        "college",
        "institution",
        "campus",
        "group",
        "excel"
    ]
}


# =========================================================
# NORMALIZE
# =========================================================

def normalize(text):

    text = (text or "").lower().strip()

    for old, new in sorted(
        REPLACEMENTS.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):

        text = text.replace(old, new)

    text = re.sub(
        r"[^\w\s\u0B80-\u0BFF.+&-]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# =========================================================
# TOKENS
# =========================================================

def get_tokens(text):

    words = re.findall(
        r"[\w\u0B80-\u0BFF]+",
        normalize(text)
    )

    return [
        word
        for word in words
        if word not in STOP_WORDS
        and len(word) > 1
    ]


# =========================================================
# INTENT DETECTION
# =========================================================

def detect_intent(text):

    text = normalize(text)

    detected = []

    for intent, words in INTENTS.items():

        for word in words:

            if word.lower() in text:

                detected.append(intent)
                break

    return detected


# =========================================================
# INSTITUTION DETECTION
# =========================================================

def detect_institution(text):

    text = normalize(text)

    best_match = None
    best_length = 0

    for institution in INSTITUTIONS:

        for alias in institution["aliases"]:

            alias = normalize(alias)

            if alias in text:

                if len(alias) > best_length:

                    best_match = institution
                    best_length = len(alias)

    return best_match


# =========================================================
# COURSE DETECTION
# =========================================================

def detect_course(text):

    text = normalize(text)

    best_course = None
    best_length = 0

    for short_name, details in COURSES.items():

        all_aliases = [
            short_name
        ] + details["aliases"]

        for alias in all_aliases:

            alias = normalize(alias)

            if alias in text:

                if len(alias) > best_length:

                    best_course = (
                        short_name,
                        details
                    )

                    best_length = len(alias)

    return best_course


# =========================================================
# DATABASE
# =========================================================

def load_faqs():

    connection = sqlite3.connect(DATABASE)

    rows = connection.execute(
        "SELECT question, answer FROM faq"
    ).fetchall()

    connection.close()

    return rows


# =========================================================
# DISPLAY CLEANER
# =========================================================

def clean_response(text):

    # Never show ECCS in chatbot output
    text = re.sub(
        r"\bECCS\b",
        "Excel College for Commerce and Science",
        text,
        flags=re.IGNORECASE
    )

    return text


# =========================================================
# DIRECT INSTITUTION ANSWERS
# =========================================================

def institution_answer(institution, intent):

    name = institution["name"]
    category = institution["category"]

    if intent == "course":

        return (
            f"🎓 {name}\n\n"
            f"Category: {category}\n\n"
            f"{name} is part of Excel Group Institutions. "
            f"The courses available depend on the programmes offered "
            f"by this institution."
        )

    if intent == "eligibility":

        return (
            f"✅ Eligibility – {name}\n\n"
            f"Eligibility depends on the specific course selected "
            f"under {name}. Different programmes can have different "
            f"academic requirements."
        )

    if intent == "admission":

        return (
            f"📝 Admission – {name}\n\n"
            f"Admission requirements depend on the selected programme "
            f"and applicable admission rules."
        )

    if intent == "hostel":

        return (
            f"🏠 Hostel – {name}\n\n"
            f"Hostel facilities are available within the Excel Group "
            f"campus facilities. Availability can depend on the "
            f"institution and programme."
        )

    if intent == "placement":

        return (
            f"💼 Placement – {name}\n\n"
            f"Placement and training activities are available across "
            f"Excel Group institutions. Specific placement information "
            f"can vary according to the institution and programme."
        )

    if intent == "facilities":

        return (
            f"🏫 Facilities – {name}\n\n"
            f"Applicable Excel Group campus facilities include "
            f"academic infrastructure, laboratories, library, "
            f"sports, hostel and transport facilities."
        )

    if intent == "address":

        return (
            f"📍 Location – {name}\n\n"
            f"NH-544, Salem Main Road, Sankari West, "
            f"Pallakkapalayam, Komarapalayam, "
            f"Namakkal District, Tamil Nadu - 637303."
        )

    if intent == "contact":

        return (
            f"📞 Contact – {name}\n\n"
            f"General Excel Group contact:\n"
            f"+91 99655 23999\n"
            f"info@excelcolleges.com"
        )

    return (
        f"🏫 {name}\n\n"
        f"Category: {category}\n\n"
        f"This institution is part of Excel Group Institutions."
    )


# =========================================================
# COURSE ANSWERS
# =========================================================

def course_answer(course_data, intent):

    short_name, details = course_data

    course_name = details["name"]
    institution = details["institution"]

    if intent == "eligibility":

        return (
            f"📚 {course_name}\n\n"
            f"Institution: {institution}\n\n"
            f"Eligibility depends on the applicable admission "
            f"requirements for this programme."
        )

    if intent == "admission":

        return (
            f"📝 {course_name}\n\n"
            f"Institution: {institution}\n\n"
            f"Admission depends on the applicable academic and "
            f"admission requirements."
        )

    return (
        f"🎓 {course_name}\n\n"
        f"Institution: {institution}\n\n"
        f"This is a programme associated with the Excel Group "
        f"Institutions."
    )


# =========================================================
# FULL INSTITUTION LIST
# =========================================================

def full_institution_list():

    answer = "🏫 Excel Group Institutions\n\n"

    categories = {}

    for institution in INSTITUTIONS:

        category = institution["category"]

        if category not in categories:
            categories[category] = []

        categories[category].append(
            institution["name"]
        )

    for category, names in categories.items():

        answer += f"📌 {category}\n"

        for name in names:

            answer += f"• {name}\n"

        answer += "\n"

    return answer.strip()


# =========================================================
# GENERAL ANSWERS
# =========================================================

def general_answer(intent):

    if intent == "hostel":

        return (
            "🏠 Hostel\n\n"
            "Excel Group Institutions provides hostel facilities "
            "for students. Availability and specific hostel details "
            "can vary according to the institution and programme."
        )

    if intent == "placement":

        return (
            "💼 Placement\n\n"
            "Excel Group Institutions provides training and placement "
            "activities for students. Placement details vary by "
            "institution and programme."
        )

    if intent == "scholarship":

        return (
            "🎓 Scholarship\n\n"
            "Excel Group Institutions provides scholarship "
            "opportunities subject to applicable eligibility "
            "criteria and programme requirements."
        )

    if intent == "facilities":

        return (
            "🏫 Facilities\n\n"
            "Excel Group Institutions provides facilities such as "
            "academic infrastructure, laboratories, library, "
            "sports, hostel and transport."
        )

    if intent == "address":

        return (
            "📍 Excel Group Address\n\n"
            "NH-544, Salem Main Road, Sankari West, "
            "Pallakkapalayam, Komarapalayam, "
            "Namakkal District, Tamil Nadu - 637303."
        )

    if intent == "contact":

        return (
            "📞 Excel Group Contact\n\n"
            "Phone: +91 99655 23999\n"
            "Email: info@excelcolleges.com"
        )

    return None


# =========================================================
# MAIN AI RESPONSE
# =========================================================

def get_response(user_message):

    original_text = user_message

    text = normalize(user_message)

    if not text:

        return "Please enter a question."


    # -----------------------------------------------------
    # GREETING
    # -----------------------------------------------------

    greetings = [
        "hi",
        "hello",
        "hey",
        "vanakkam",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if text in greetings:

        return (
            "👋 Hello! Welcome to Excel Institute AI Assistant.\n\n"
            "I can help you with:\n"
            "• Excel Group Institutions\n"
            "• Courses\n"
            "• Eligibility\n"
            "• Admission\n"
            "• Fees\n"
            "• Scholarship\n"
            "• Hostel\n"
            "• Placement\n"
            "• Facilities\n"
            "• Address / Contact"
        )


    # -----------------------------------------------------
    # DETECT
    # -----------------------------------------------------

    intents = detect_intent(text)

    institution = detect_institution(text)

    course = detect_course(text)


    # -----------------------------------------------------
    # FULL INSTITUTION LIST
    # -----------------------------------------------------

    list_words = [
        "what institutions",
        "what colleges",
        "which colleges",
        "all colleges",
        "all institutions",
        "excel colleges",
        "excel institutions",
        "enna college",
        "enna colleges",
        "enna institution",
        "college list",
        "institution list"
    ]

    if any(
        word in text
        for word in list_words
    ):

        return full_institution_list()


    # -----------------------------------------------------
    # COURSE DETECTED
    # -----------------------------------------------------

    if course:

        if "eligibility" in intents:

            return clean_response(
                course_answer(
                    course,
                    "eligibility"
                )
            )

        if "admission" in intents:

            return clean_response(
                course_answer(
                    course,
                    "admission"
                )
            )

        return clean_response(
            course_answer(
                course,
                "course"
            )
        )


    # -----------------------------------------------------
    # INSTITUTION DETECTED
    # -----------------------------------------------------

    if institution:

        # Find strongest intent
        preferred_intents = [
            "eligibility",
            "admission",
            "course",
            "fees",
            "scholarship",
            "hostel",
            "placement",
            "facilities",
            "address",
            "contact"
        ]

        selected_intent = None

        for intent in preferred_intents:

            if intent in intents:

                selected_intent = intent
                break

        if selected_intent:

            return clean_response(
                institution_answer(
                    institution,
                    selected_intent
                )
            )

        return clean_response(
            institution_answer(
                institution,
                "institution"
            )
        )


    # -----------------------------------------------------
    # GENERAL INTENT
    # -----------------------------------------------------

    for intent in [
        "hostel",
        "placement",
        "scholarship",
        "facilities",
        "address",
        "contact"
    ]:

        if intent in intents:

            answer = general_answer(intent)

            if answer:

                return clean_response(answer)


    # -----------------------------------------------------
    # TF-IDF FALLBACK
    # -----------------------------------------------------

    rows = load_faqs()

    if rows:

        questions = [
            normalize(question)
            for question, answer in rows
        ]

        vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True
        )

        matrix = vectorizer.fit_transform(
            questions + [text]
        )

        similarities = cosine_similarity(
            matrix[-1],
            matrix[:-1]
        ).flatten()

        best_index = similarities.argmax()

        best_score = float(
            similarities[best_index]
        )

        if best_score >= 0.18:

            return clean_response(
                rows[best_index][1]
            )


    # -----------------------------------------------------
    # UNKNOWN QUESTION
    # -----------------------------------------------------

    return (
        "🤖 I couldn't find a reliable answer for that question "
        "in my Excel Group database.\n\n"
        "Try asking about:\n"
        "• Courses\n"
        "• Eligibility\n"
        "• Admission\n"
        "• Fees\n"
        "• Scholarship\n"
        "• Hostel\n"
        "• Placement\n"
        "• Facilities\n"
        "• Any Excel institution"
    )


# =========================================================
# TEST FROM CMD
# =========================================================

if __name__ == "__main__":

    print()
    print("======================================")
    print("EXCEL GROUP AI CHATBOT")
    print("Type 'exit' to stop")
    print("======================================")

    while True:

        question = input("\nYou: ")

        if question.lower().strip() in [
            "exit",
            "quit"
        ]:

            break

        print("\nBot:")
        print(get_response(question))
