import sqlite3
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATABASE = "college.db"

# ------------------------------------------------------------
# Excel Group Institutions - core information
# ------------------------------------------------------------

GROUP_ADDRESS = (
    "Excel Group Institutions, NH-544, Salem Main Road, Sankari West, "
    "Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu - 637303."
)

CONTACT = (
    "General contact: +91 99655 23999 | Email: info@excelcolleges.com"
)

INSTITUTIONS = {
    "engineering": (
        "Excel Engineering College - Autonomous. It offers engineering, "
        "technology, architecture and management-related programmes. "
        "The official site lists UG areas including CSE, AI & ML, AI & DS, "
        "IT, ECE, EEE, Biomedical, Aeronautical, Civil, Mechanical, "
        "Safety & Fire and other engineering programmes."
    ),
    "commerce": (
        "Excel College for Commerce and Science. It offers undergraduate "
        "and postgraduate programmes in arts, commerce, computer science, "
        "data science, IT, cyber security, life sciences, fashion and related areas."
    ),
    "education": (
        "Excel College of Education is one of the institutions under Excel Group Institutions."
    ),
    "architecture": (
        "Excel College of Architecture and Planning is an institution under Excel Group Institutions "
        "and offers architecture-related programmes."
    ),
    "polytechnic": (
        "Excel Polytechnic College is an institution under Excel Group Institutions offering diploma/polytechnic education."
    ),
    "business": (
        "Excel Business School is part of Excel Group Institutions and focuses on management and business education."
    ),
    "naturopathy": (
        "Excel Medical College for Naturopathy and Yogic Sciences is part of Excel Group Institutions."
    ),
    "nursing": (
        "Excel Nursing College is part of Excel Group Institutions."
    ),
    "pharmacy": (
        "Excel College of Pharmacy is part of Excel Group Institutions."
    ),
    "physiotherapy": (
        "Excel College of Physiotherapy and Research Centre is part of Excel Group Institutions."
    ),
    "siddha": (
        "Excel Siddha Medical College and Research Centre is part of Excel Group Institutions."
    ),
    "homoeopathy": (
        "Excel Homoeopathy Medical College is part of Excel Group Institutions."
    ),
    "school": (
        "Excel Public School is part of Excel Group Institutions and provides school education."
    ),
}

ALL_INSTITUTIONS_ANSWER = """Excel Group Institutions includes multiple educational institutions across technical, arts and science, management, education, medical and school education areas.

Main institutions include:
• Excel Engineering College - Autonomous
• Excel College for Commerce and Science
• Excel College of Education
• Excel College of Architecture and Planning
• Excel Polytechnic College
• Excel Business School
• Excel Medical College for Naturopathy and Yogic Sciences
• Excel Nursing College
• Excel College of Pharmacy
• Excel College of Physiotherapy and Research Centre
• Excel Siddha Medical College and Research Centre
• Excel Homoeopathy Medical College
• Excel Public School

For the latest institution list and programme details, the official Excel website should be checked."""

COURSE_ANSWERS = {
    "bca": "BCA (Bachelor of Computer Applications) is offered by Excel College for Commerce and Science. The official eligibility information includes Higher Secondary with Mathematics, or specified Computer Science/Computer Applications/IT/Computer Technology/Business Mathematics/Statistics routes; a 15-day Mathematics bridge course may apply where Mathematics was not studied.",
    "bba": "BBA (Bachelor of Business Administration) is offered by Excel College for Commerce and Science. The official eligibility page states that a student should pass HSC, with preference for Commerce and Accountancy streams.",
    "bcom": "Excel College for Commerce and Science offers B.Com and related programmes including B.Com Accounting and Finance, B.Com Professional Accounting, B.Com Computer Application and B.Com Information Technology.",
    "engineering": "Excel Engineering College - Autonomous offers many B.E./B.Tech programmes. Official information lists areas such as Aeronautical, Civil, Mechanical, CSE, CSE with AI & ML, AI & Data Science, IT, ECE, EEE, Biomedical, Food Technology, Safety & Fire, Computer Science and Business Systems and Petrochemical Technology.",
    "mca": "Excel Engineering College offers MCA. The official eligibility information requires a recognized bachelor's degree with the required Mathematics/IT/Computer Science route and marks as prescribed by the applicable regulations.",
    "mba": "Excel Engineering College offers MBA programmes. The official eligibility information includes a recognized bachelor's degree for the 2-year MBA route and a Plus Two route for the integrated MBA, subject to applicable norms.",
}

INTENT_ANSWERS = {
    "address": GROUP_ADDRESS,
    "contact": CONTACT,
    "hostel": "Yes. Excel provides hostel facilities. The official campus information describes separate accommodation for men and women and different room/occupancy options.",
    "transport": "Excel provides transport facilities for students. For current route, timing and fee details, please confirm with the college transport office.",
    "library": "Excel provides library facilities and online/library resources for students. The exact current collection and timings should be confirmed with the respective institution.",
    "placement": "Excel has training and placement support. For Excel College for Commerce and Science, the official placement page lists Dr. Yuvaraj as Placement Officer (9965579666) and Mrs. V. Aarthi as Training and Placement Coordinator (9600851841). Emails: eccsplacement@excelcolleges.com and aarthi.eccs@excelcolleges.com.",
    "scholarship": "Excel lists scholarship/support schemes including government scholarships and institution-level schemes. Examples include PMS Minority, SC/ST/SCA, BC/MBC, Pudhumai Penn, Tamil Pudhalvan, SRET and TART. Eligibility and current amounts should be verified from the latest official scholarship instructions.",
    "admission": "Excel admissions are based on the applicable eligibility criteria and Tamil Nadu Government/university norms. Students can enquire online, by phone or at the admission office. General admission contact: +91 99655 77789; emails: admission@excelcolleges.com and exceladmission@gmail.com.",
    "facilities": "Excel campuses provide facilities such as classrooms, laboratories, library resources, hostels, sports, transport, cafeteria/food facilities, Wi-Fi/IT infrastructure and student support services. Exact facilities vary by institution.",
    "rules": "Students are expected to follow the respective institution's code of conduct, ID-card, discipline and campus rules. The current rules should be checked with the concerned institution.",
    "antiragging": "Yes. Anti-ragging support/committee is listed by Excel College for Commerce and Science.",
    "grievance": "Student grievance redressal support is available. Excel College for Commerce and Science lists a Student Grievance Redressal Committee and Ombudsperson for Students' Grievances.",
    "courses_general": "Excel offers programmes across engineering, technology, arts, commerce, computer applications, management, architecture, education, medical/paramedical and school education. Tell me the institution or field, for example Engineering, Commerce & Science, Polytechnic, Pharmacy or Nursing, and I can give the relevant programmes.",
    "engineering_courses": COURSE_ANSWERS["engineering"],
    "commerce_courses": "Excel College for Commerce and Science offers BA Tamil, BA English, BBA, BCA, B.Com and its variants, B.Sc AI & Data Science, B.Sc AI & Machine Learning, B.Sc Computer Science, B.Sc Cyber Security, B.Sc Data Science, B.Sc Information Technology, B.Sc Biochemistry, B.Sc Clinical Laboratory Technology, B.Sc Costume Design and Fashion and other listed programmes. It also offers PG programmes including M.Com, M.Sc Computer Science, M.Sc Microbiology, M.S.W and M.Sc Textile/Fashion Designing.",
}

# ------------------------------------------------------------
# Normalization: English + Tamil transliteration + common typos
# ------------------------------------------------------------

def normalize(text):
    text = text.lower().strip()

    replacements = {
        "எங்கே": " enga ",
        "எங்க": " enga ",
        "இருக்கு": " irukku ",
        "இருக்கா": " irukku ",
        "இருக்குமா": " irukku ",
        "என்ன": " enna ",
        "என்னென்ன": " enna enna ",
        "எப்படி": " epdi ",
        "எவ்வளவு": " evlo ",
        "சொல்லு": " sollu ",
        "வேண்டும்": " venum ",
        "வேணும்": " venum ",
        "கல்லூரி": " college ",
        "கல்லூரியில்": " college ",
        "கோர்ஸ்": " course ",
        "படிப்பு": " course ",
        "தங்கும் விடுதி": " hostel ",
        "விடுதி": " hostel ",
        "சேர்க்கை": " admission ",
        "உதவித்தொகை": " scholarship ",
        "கட்டணம்": " fee ",
        "தொடர்பு": " contact ",
        "முகவரி": " address ",
        "பொறியியல்": " engineering ",
        "கணினி": " computer ",
        "வணிகம்": " commerce ",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Common Tanglish / spelling normalization
    replacements2 = {
        "collegela": "college la",
        "collegeah": "college",
        "collegea": "college",
        "excelah": "excel",
        "excel la": "excel",
        "iruka": "irukku",
        "irukaa": "irukku",
        "irukuma": "irukku",
        "irukkuma": "irukku",
        "engae": "enga",
        "enga": "where",
        "epdi": "how",
        "eppadi": "how",
        "enna": "what",
        "evlo": "how much",
        "evalo": "how much",
        "sollu": "tell",
        "solla": "tell",
        "venuma": "need",
        "venum": "need",
        "fees": "fee",
        "courses": "course",
        "details": "information",
        "info": "information",
        "admissionah": "admission",
        "scholarshipah": "scholarship",
        "hostelah": "hostel",
        "placementah": "placement",
        "facilityah": "facility",
        "facilities": "facility",
        "contactah": "contact",
        "addressah": "address",
        "engg": "engineering",
        "artsandscience": "commerce science",
        "arts science": "commerce science",
        "b com": "bcom",
        "b. com": "bcom",
        "bca": "bca",
        "bba": "bba",
        "mca": "mca",
        "mba": "mba",
    }

    for old, new in replacements2.items():
        text = text.replace(old, new)

    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_faqs():
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT question, answer FROM faq")
        rows = cur.fetchall()
        conn.close()
        return rows
    except sqlite3.Error:
        return []


# ------------------------------------------------------------
# Intent detection
# ------------------------------------------------------------

def contains_any(q, words):
    return any(word in q for word in words)


def detect_institution(q):
    if contains_any(q, ["engineering", "engineer", "b e", "btech", "mtech"]):
        return "engineering"
    if contains_any(q, ["commerce science", "commerce and science", "bcom", "bca", "bba", "arts science"]):
        return "commerce"
    if contains_any(q, ["polytechnic", "diploma"]):
        return "polytechnic"
    if contains_any(q, ["architecture", "b arch", "m arch"]):
        return "architecture"
    if contains_any(q, ["education college", "bed", "med", "teacher education"]):
        return "education"
    if contains_any(q, ["business school", "business studies"]):
        return "business"
    if contains_any(q, ["naturopathy", "yogic", "yoga medical"]):
        return "naturopathy"
    if contains_any(q, ["nursing"]):
        return "nursing"
    if contains_any(q, ["pharmacy"]):
        return "pharmacy"
    if contains_any(q, ["physiotherapy", "physio"]):
        return "physiotherapy"
    if contains_any(q, ["siddha"]):
        return "siddha"
    if contains_any(q, ["homoeopathy", "homeopathy"]):
        return "homoeopathy"
    if contains_any(q, ["public school", "cbse school", "school"]):
        return "school"
    return None


def detect_intent(q):
    if q in ["hi", "hello", "hey", "vanakkam", "hai"]:
        return "greeting"
    if contains_any(q, ["thank", "thanks", "nandri"]):
        return "thanks"
    if q in ["bye", "goodbye", "see you"]:
        return "bye"

    # Address/contact should get priority over generic course matching
    if contains_any(q, ["address", "location", "where is", "where college", "where excel", "map", "enga college", "college where"]):
        return "address"

    if contains_any(q, ["phone", "mobile", "number", "email", "mail", "contact"]):
        return "contact"

    if contains_any(q, ["hostel", "stay", "accommodation", "room"]):
        return "hostel"

    if contains_any(q, ["transport", "bus", "college bus", "bus route"]):
        return "transport"

    if contains_any(q, ["library", "books", "reading"]):
        return "library"

    if contains_any(q, ["placement", "job", "jobs", "company", "campus placement"]):
        return "placement"

    if contains_any(q, ["scholarship", "pudhumai penn", "tamil pudhalvan", "sret", "tart"]):
        return "scholarship"

    if contains_any(q, ["admission", "join", "apply", "application", "seat"]):
        return "admission"

    if contains_any(q, ["facility", "facilities", "lab", "canteen", "cafeteria", "sports", "wifi", "infrastructure"]):
        return "facilities"

    if contains_any(q, ["anti ragging", "ragging"]):
        return "antiragging"

    if contains_any(q, ["grievance", "complaint", "problem", "student complaint"]):
        return "grievance"

    if contains_any(q, ["rule", "rules", "dress code", "id card", "discipline"]):
        return "rules"

    # Course-list intent
    if contains_any(q, ["what courses", "course list", "courses available", "course available",
                        "enna course", "course enna", "enna enna course", "course list sollu"]):
        if "engineering" in q or "engineer" in q:
            return "engineering_courses"
        if "commerce" in q or "bca" in q or "bcom" in q or "bba" in q:
            return "commerce_courses"
        return "courses_general"

    # Specific course intent
    if contains_any(q, ["bca"]):
        return "bca"
    if contains_any(q, ["bba"]):
        return "bba"
    if contains_any(q, ["bcom"]):
        return "bcom"
    if contains_any(q, ["mca"]):
        return "mca"
    if contains_any(q, ["mba"]):
        return "mba"

    return None


def answer_by_intent(intent, q):
    if intent == "greeting":
        return "Hello! 👋 I am the Excel Group Institutions AI Assistant. Ask me about institutions, courses, admission, eligibility, hostel, scholarships, placement, facilities or contact."
    if intent == "thanks":
        return "You're welcome! 😊"
    if intent == "bye":
        return "Bye! 👋 Have a great day!"

    if intent in INTENT_ANSWERS:
        # Institution-specific course lists
        institution = detect_institution(q)
        if intent == "facilities" and institution:
            return f"{INSTITUTIONS[institution]}\n\nFor this institution, facilities and services can vary. Please ask me specifically about hostel, transport, library, placement or other facilities."
        return INTENT_ANSWERS[intent]

    if intent in COURSE_ANSWERS:
        return COURSE_ANSWERS[intent]

    if intent == "engineering_courses":
        return COURSE_ANSWERS["engineering"]

    if intent == "commerce_courses":
        return INTENT_ANSWERS["commerce_courses"]

    if intent == "courses_general":
        return INTENT_ANSWERS["courses_general"]

    return None


# ------------------------------------------------------------
# TF-IDF fallback - used only when intent rules don't match
# ------------------------------------------------------------

def tfidf_fallback(user_question, faqs):
    if not faqs:
        return (
            "Sorry, I couldn't find that information yet. "
            "Try asking about courses, admission, eligibility, hostel, "
            "scholarship, placement, facilities, address or contact."
        )

    questions = [normalize(row[0]) for row in faqs]
    answers = [row[1] for row in faqs]
    user_q = normalize(user_question)

    if not user_q:
        return "Please enter a question."

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        sublinear_tf=True,
        min_df=1
    )

    vectors = vectorizer.fit_transform(questions + [user_q])
    scores = cosine_similarity(vectors[-1], vectors[:-1])[0]

    best = scores.argmax()
    confidence = float(scores[best])

    print("TF-IDF confidence:", round(confidence, 3))

    # Higher threshold prevents unrelated questions from getting random FAQ answers.
    if confidence < 0.28:
        return (
            "Sorry , I couldn't understand that clearly. 😕\n\n"
            "You can ask about:\n"
            "• Excel Group Institutions\n"
            "• Engineering / Polytechnic / Architecture\n"
            "• Commerce & Science\n"
            "• Education / Business School\n"
            "• Nursing / Pharmacy / Medical institutions\n"
            "• Courses & eligibility\n"
            "• Admission & scholarship\n"
            "• Hostel / transport / facilities\n"
            "• Placement\n"
            "• Address & contact"
        )

    return answers[best]


def get_response(user_question):
    if not user_question or not user_question.strip():
        return "Please enter a question."

    q = normalize(user_question)

    # 1. Strong intent routing first
    intent = detect_intent(q)
    direct = answer_by_intent(intent, q) if intent else None

    if direct:
        return direct

    # 2. Institution-only question
    institution = detect_institution(q)
    if institution:
        return INSTITUTIONS[institution]

    # 3. Full Excel institution list
    if contains_any(q, [
        "excel group", "excel institutions", "all colleges",
        "all institution", "enna colleges", "which colleges",
        "excel la enna colleges", "full list"
    ]):
        return ALL_INSTITUTIONS_ANSWER

    # 4. Existing FAQ database as a controlled fallback
    faqs = load_faqs()
    return tfidf_fallback(user_question, faqs)


if __name__ == "__main__":
    print("🤖 Excel Group Institutions AI Chatbot")
    print("Type 'exit' to stop.")

    while True:
        question = input("\nYou: ")

        if question.lower().strip() == "exit":
            print("Bot: Goodbye! 👋")
            break

        print("Bot:", get_response(question))
