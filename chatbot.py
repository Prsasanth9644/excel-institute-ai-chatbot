import re
import sqlite3
from difflib import SequenceMatcher

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATABASE = "college.db"


# ============================================================
# 1. TEXT NORMALIZATION
# ============================================================

REPLACEMENTS = {
    "eligiblity": "eligibility",
    "eligiblity": "eligibility",
    "qualifiction": "qualification",
    "admisson": "admission",
    "admsn": "admission",
    "placment": "placement",
    "scholrship": "scholarship",
    "scholar ship": "scholarship",
    "collage": "college",
    "colleg": "college",

    # Tanglish
    "padika": "study",
    "padikka": "study",
    "padipu": "course",
    "padippu": "course",
    "join panna": "admission",
    "join pannalama": "admission",
    "join panlama": "admission",

    "enga": "where",
    "yenga": "where",
    "engae": "where",

    "evlo": "how much",
    "evalo": "how much",

    "ethana": "how many",

    "iruka": "available",
    "irukka": "available",
    "irukku": "available",

    "venum": "need",
    "venuma": "need",

    "sollu": "tell",
    "sollunga": "tell",
}


STOP_WORDS = {
    "the",
    "is",
    "are",
    "am",
    "was",
    "were",
    "a",
    "an",
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

    # Tanglish filler words
    "da",
    "macha",
    "ah",
    "aa",
    "nu",
    "la",
    "um",
    "enna",
    "epdi",
    "eppadi",
    "sollu",
    "sollunga",
}


def normalize(text):

    text = str(text).lower().strip()

    for old, new in sorted(
        REPLACEMENTS.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):
        text = text.replace(old, new)

    # Keep English, numbers, spaces and Tamil characters
    text = re.sub(
        r"[^\w\s\u0B80-\u0BFF&.+-]",
        " ",
        text
    )

    text = re.sub(r"\s+", " ", text).strip()

    return text


def get_tokens(text):

    text = normalize(text)

    tokens = re.findall(
        r"[\w\u0B80-\u0BFF]+",
        text
    )

    return [
        token
        for token in tokens
        if token not in STOP_WORDS and len(token) > 1
    ]


# ============================================================
# 2. INTENT DETECTION
# ============================================================

INTENT_PATTERNS = {

    "greeting": [
        r"\bhi\b",
        r"\bhello\b",
        r"\bhey\b",
        r"\bvanakkam\b",
        r"good morning",
        r"good afternoon",
        r"good evening",
    ],

    "thanks": [
        r"thank you",
        r"thanks",
        r"nandri",
    ],

    "bye": [
        r"\bbye\b",
        r"goodbye",
        r"see you",
    ],

    "eligibility": [
        r"eligibility",
        r"qualification",
        r"eligible",
        r"qualify",
        r"தகுதி",
    ],

    "admission": [
        r"admission",
        r"apply",
        r"application",
        r"joining",
        r"join",
        r"admit",
        r"சேர்க்கை",
    ],

    "fees": [
        r"fee",
        r"fees",
        r"tuition",
        r"cost",
        r"amount",
        r"charges",
        r"கட்டணம்",
    ],

    "scholarship": [
        r"scholarship",
        r"scholarships",
        r"financial aid",
        r"உதவித்தொகை",
    ],

    "hostel": [
        r"hostel",
        r"hostels",
        r"accommodation",
        r"தங்கும் விடுதி",
        r"விடுதி",
    ],

    "placement": [
        r"placement",
        r"placements",
        r"job",
        r"jobs",
        r"career",
        r"campus interview",
        r"வேலைவாய்ப்பு",
    ],

    "course": [
        r"course",
        r"courses",
        r"program",
        r"programme",
        r"degree",
        r"degrees",
        r"பாடநெறி",
        r"படிப்பு",
    ],

    "address": [
        r"address",
        r"location",
        r"where",
        r"முகவரி",
        r"எங்கே",
    ],

    "contact": [
        r"contact",
        r"phone",
        r"mobile",
        r"number",
        r"email",
        r"mail",
        r"தொடர்பு",
    ],

    "facilities": [
        r"facility",
        r"facilities",
        r"library",
        r"wifi",
        r"wi-fi",
        r"canteen",
        r"cafeteria",
        r"sports",
        r"transport",
        r"bus",
        r"atm",
        r"lab",
        r"laboratory",
        r"வசதி",
        r"நூலகம்",
        r"விளையாட்டு",
    ],

    "rules": [
        r"rule",
        r"rules",
        r"dress code",
        r"id card",
        r"anti ragging",
        r"ragging",
        r"discipline",
    ],

    "management": [
        r"chairman",
        r"principal",
        r"director",
        r"management",
        r"vice chairman",
    ],
}


def detect_intents(text):

    normalized = normalize(text)

    detected = []

    for intent, patterns in INTENT_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, normalized):

                detected.append(intent)

                break

    return detected


# ============================================================
# 3. EXCEL INSTITUTION DETECTION
# ============================================================

INSTITUTIONS = {

    "commerce_science": [
        "excel college for commerce and science",
        "commerce and science",
        "commerce science",
        "eccs",
        "arts and science",
    ],

    "engineering": [
        "excel engineering college",
        "engineering college",
        "engineering",
    ],

    "architecture": [
        "excel college of architecture",
        "architecture",
        "planning",
    ],

    "polytechnic": [
        "excel polytechnic college",
        "polytechnic",
    ],

    "education": [
        "excel college of education",
        "education college",
        "b.ed",
    ],

    "business": [
        "excel business school",
        "business school",
    ],

    "nursing": [
        "excel nursing college",
        "nursing college",
        "nursing",
    ],

    "pharmacy": [
        "excel college of pharmacy",
        "pharmacy college",
        "pharmacy",
    ],

    "naturopathy": [
        "excel medical college for naturopathy",
        "naturopathy",
        "yoga",
    ],

    "siddha": [
        "excel siddha medical college",
        "siddha",
    ],

    "homoeopathy": [
        "excel homoeopathy medical college",
        "homoeopathy",
        "homeopathy",
    ],

    "physiotherapy": [
        "excel college of physiotherapy",
        "physiotherapy",
        "physio",
    ],

    "health_sciences": [
        "excel institute of health sciences",
        "health sciences",
    ],

    "school": [
        "excel public school",
        "public school",
        "cbse school",
    ],
}


def detect_institution(text):

    normalized = normalize(text)

    best_match = None
    best_length = 0

    for institution, aliases in INSTITUTIONS.items():

        for alias in aliases:

            if alias in normalized:

                if len(alias) > best_length:

                    best_match = institution
                    best_length = len(alias)

    return best_match


# ============================================================
# 4. COURSE DETECTION
# ============================================================

COURSES = {

    "bca": [
        "bca",
        "bachelor of computer applications",
    ],

    "bcom": [
        "bcom",
        "b.com",
    ],

    "bba": [
        "bba",
        "business administration",
    ],

    "computer science": [
        "computer science",
        "bsc computer science",
        "b.sc computer science",
    ],

    "artificial intelligence": [
        "artificial intelligence",
        "artificial intelligence and data science",
        "ai",
        "ai&ds",
        "ai ds",
        "data science",
    ],

    "machine learning": [
        "artificial intelligence and machine learning",
        "ai&ml",
        "ai ml",
        "aiml",
        "machine learning",
    ],

    "cyber security": [
        "cyber security",
        "cybersecurity",
    ],

    "information technology": [
        "information technology",
        "information tech",
        "it course",
    ],

    "microbiology": [
        "microbiology",
    ],

    "biochemistry": [
        "biochemistry",
    ],

    "mathematics": [
        "mathematics",
        "maths",
    ],

    "physics": [
        "physics",
    ],

    "english": [
        "english",
        "english literature",
    ],

    "visual communication": [
        "visual communication",
        "viscom",
    ],

    "fashion": [
        "fashion",
        "costume design",
        "textile",
    ],

    "mcom": [
        "mcom",
        "m.com",
    ],

    "msc computer science": [
        "msc computer science",
        "m.sc computer science",
    ],
}


def detect_course(text):

    normalized = normalize(text)

    best_course = None
    best_length = 0

    for course, aliases in COURSES.items():

        for alias in aliases:

            if alias in normalized:

                if len(alias) > best_length:

                    best_course = course
                    best_length = len(alias)

    return best_course


# ============================================================
# 5. DATABASE
# ============================================================

def load_faqs():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        "SELECT question, answer FROM faq"
    )

    rows = cursor.fetchall()

    connection.close()

    return rows


# ============================================================
# 6. KEYWORD SIMILARITY
# ============================================================

def keyword_score(query, document):

    query_words = set(get_tokens(query))

    document_words = set(get_tokens(document))

    if not query_words or not document_words:

        return 0.0

    common = query_words.intersection(document_words)

    total = query_words.union(document_words)

    return len(common) / len(total)


# ============================================================
# 7. FUZZY MATCHING
# ============================================================

def fuzzy_score(query, document):

    query = normalize(query)

    document = normalize(document)

    return SequenceMatcher(
        None,
        query,
        document
    ).ratio()


# ============================================================
# 8. INTENT WORD MATCH
# ============================================================

INTENT_WORDS = {

    "eligibility": [
        "eligibility",
        "qualification",
        "eligible",
    ],

    "admission": [
        "admission",
        "apply",
        "joining",
    ],

    "fees": [
        "fee",
        "fees",
        "cost",
    ],

    "scholarship": [
        "scholarship",
    ],

    "hostel": [
        "hostel",
    ],

    "placement": [
        "placement",
        "career",
    ],

    "course": [
        "course",
        "program",
        "programme",
    ],

    "address": [
        "address",
        "location",
        "where",
    ],

    "contact": [
        "contact",
        "phone",
        "email",
    ],

    "facilities": [
        "facility",
        "facilities",
        "library",
        "wifi",
        "sports",
    ],

    "rules": [
        "rule",
        "dress",
        "ragging",
    ],

    "management": [
        "principal",
        "chairman",
        "director",
    ],
}


# ============================================================
# 9. AI/NLP RANKING
# ============================================================

def rank_answers(user_question, rows):

    if not rows:

        return []

    questions = [
        row[0]
        for row in rows
    ]

    normalized_questions = [
        normalize(q)
        for q in questions
    ]

    normalized_user_question = normalize(
        user_question
    )

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        sublinear_tf=True
    )

    try:

        matrix = vectorizer.fit_transform(
            normalized_questions + [
                normalized_user_question
            ]
        )

        question_matrix = matrix[:-1]

        user_vector = matrix[-1]

        cosine_scores = cosine_similarity(
            user_vector,
            question_matrix
        ).flatten()

    except Exception:

        cosine_scores = [
            0.0
            for _ in questions
        ]

    user_intents = set(
        detect_intents(user_question)
    )

    user_institution = detect_institution(
        user_question
    )

    user_course = detect_course(
        user_question
    )

    ranked = []

    for index, row in enumerate(rows):

        question = row[0]
        answer = row[1]

        question_lower = question.lower()

        # Main ML similarity
        tfidf_score = float(
            cosine_scores[index]
        )

        # Keyword similarity
        key_score = keyword_score(
            user_question,
            question
        )

        # Fuzzy similarity
        fuzzy = fuzzy_score(
            user_question,
            question
        )

        bonus = 0.0

        # Course bonus
        if user_course:

            aliases = COURSES.get(
                user_course,
                []
            )

            if any(
                alias in question_lower
                for alias in aliases
            ):

                bonus += 0.15

        # Institution bonus
        if user_institution:

            aliases = INSTITUTIONS.get(
                user_institution,
                []
            )

            if any(
                alias in question_lower
                for alias in aliases
            ):

                bonus += 0.10

        # Intent bonus
        for intent in user_intents:

            words = INTENT_WORDS.get(
                intent,
                []
            )

            if any(
                word in question_lower
                for word in words
            ):

                bonus += 0.08

                break

        # Combined AI/NLP score
        final_score = (
            (tfidf_score * 0.55)
            + (key_score * 0.20)
            + (fuzzy * 0.15)
            + bonus
        )

        ranked.append(
            (
                final_score,
                question,
                answer,
            )
        )

    ranked.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return ranked


# ============================================================
# 10. MAIN CHATBOT
# ============================================================

def get_response(user_message):

    if not user_message or not user_message.strip():

        return "Please enter a question."

    normalized = normalize(
        user_message
    )

    # Greeting
    if (
        len(get_tokens(normalized)) <= 4
        and any(
            word in normalized
            for word in [
                "hi",
                "hello",
                "hey",
                "vanakkam",
            ]
        )
    ):

        return (
            "Hello! 👋 I'm your Excel Institute AI Assistant.\n\n"
            "You can ask me about courses, eligibility, "
            "admission, fees, scholarships, hostel, "
            "facilities, placement, address and more."
        )

    # Thanks
    if any(
        word in normalized
        for word in [
            "thank you",
            "thanks",
            "nandri",
        ]
    ):

        return (
            "You're welcome! 😊 "
            "Ask me anything about Excel Institute."
        )

    # Bye
    if normalized in [
        "bye",
        "goodbye",
        "see you",
    ]:

        return "Thank you! 👋 Have a great day."

    rows = load_faqs()

    if not rows:

        return (
            "Sorry, the college information database "
            "is currently empty."
        )

    ranked = rank_answers(
        user_message,
        rows
    )

    if not ranked:

        return (
            "Sorry, I couldn't find a matching answer."
        )

    best_score = ranked[0][0]
    best_question = ranked[0][1]
    best_answer = ranked[0][2]

    # Strong match
    if best_score >= 0.55:

        return best_answer

    # Topic-aware medium match
    has_topic = (
        detect_course(user_message)
        or detect_institution(user_message)
        or detect_intents(user_message)
    )

    if has_topic and best_score >= 0.40:

        return best_answer

    # Low confidence — don't hallucinate
    return (
        "I understand your question, but I couldn't "
        "find a reliable matching answer in my Excel "
        "Institute database.\n\n"
        "Try asking with a topic such as:\n"
        "• Courses\n"
        "• BCA eligibility\n"
        "• Admission\n"
        "• Fees\n"
        "• Scholarship\n"
        "• Hostel\n"
        "• Placement\n"
        "• Facilities\n"
        "• Address / Contact"
    )


# ============================================================
# 11. TEST MODE
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Excel Institute AI/NLP Chatbot")
    print("Type 'exit' to stop")
    print("=" * 60)

    while True:

        question = input("\nYou: ")

        if question.lower().strip() in [
            "exit",
            "quit",
        ]:

            print("Bot: Goodbye! 👋")

            break

        print(
            "Bot:",
            get_response(question)
        )
