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
        "ai&
