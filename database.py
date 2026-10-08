import sqlite3

DATABASE = "college.db"


# =========================================================
# FULL EXCEL INSTITUTIONS GROUP
# =========================================================

INSTITUTIONS = [

    {
        "name": "Excel College for Commerce and Science",
        "category": "Arts and Science",
        "aliases": [
            "excel college for commerce and science",
            "commerce and science",
            "arts and science",
            "arts science",
            "eccs"
        ]
    },

    {
        "name": "Excel Engineering College",
        "category": "Engineering",
        "aliases": [
            "excel engineering college",
            "engineering college",
            "engineering",
            "eec"
        ]
    },

    {
        "name": "Excel College of Architecture and Planning",
        "category": "Architecture",
        "aliases": [
            "architecture",
            "architecture college",
            "planning",
            "excel architecture"
        ]
    },

    {
        "name": "Excel Polytechnic College and ITI",
        "category": "Polytechnic and ITI",
        "aliases": [
            "polytechnic",
            "poly",
            "iti",
            "excel polytechnic",
            "excel iti"
        ]
    },

    {
        "name": "Excel College of Education",
        "category": "Education",
        "aliases": [
            "education college",
            "education",
            "excel education"
        ]
    },

    {
        "name": "Kandhaswamy College of Education",
        "category": "Education",
        "aliases": [
            "kandhaswamy",
            "kandhaswamy college",
            "kandhaswamy education"
        ]
    },

    {
        "name": "Excel Business School",
        "category": "Business School",
        "aliases": [
            "business school",
            "b school",
            "management school",
            "excel business"
        ]
    },

    {
        "name": "Excel College of Pharmacy",
        "category": "Pharmacy",
        "aliases": [
            "pharmacy",
            "pharmacy college",
            "excel pharmacy"
        ]
    },

    {
        "name": "Excel Nursing College",
        "category": "Nursing",
        "aliases": [
            "nursing",
            "nursing college",
            "excel nursing"
        ]
    },

    {
        "name": "Excel Institute of Health Sciences",
        "category": "Health Sciences",
        "aliases": [
            "health science",
            "health sciences",
            "health science college",
            "excel health"
        ]
    },

    {
        "name": "Excel College of Physiotherapy and Research Centre",
        "category": "Physiotherapy",
        "aliases": [
            "physiotherapy",
            "physio",
            "physiotherapy college",
            "excel physiotherapy"
        ]
    },

    {
        "name": "Excel College of Occupational Therapy",
        "category": "Occupational Therapy",
        "aliases": [
            "occupational therapy",
            "occupational therapy college",
            "excel occupational therapy"
        ]
    },

    {
        "name": "Excel Medical College for Naturopathy and Yoga",
        "category": "Naturopathy and Yoga",
        "aliases": [
            "naturopathy",
            "naturopathy college",
            "yoga",
            "naturopathy and yoga",
            "bnys"
        ]
    },

    {
        "name": "Excel Siddha Medical College and Research Centre",
        "category": "Siddha",
        "aliases": [
            "siddha",
            "siddha college",
            "siddha medical college",
            "excel siddha",
            "bsms"
        ]
    },

    {
        "name": "Excel Homoeopathy Medical College",
        "category": "Homoeopathy",
        "aliases": [
            "homoeopathy",
            "homeopathy",
            "homeopathy college",
            "bhms"
        ]
    },

    {
        "name": "Excel Public School",
        "category": "School",
        "aliases": [
            "school",
            "public school",
            "cbse",
            "excel school"
        ]
    },

    {
        "name": "Excel Multispeciality Hospitals",
        "category": "Hospital and Healthcare",
        "aliases": [
            "hospital",
            "hospitals",
            "multispeciality",
            "multi speciality",
            "excel hospital"
        ]
    },

    {
        "name": "Excel AYUSH Hospitals",
        "category": "AYUSH Healthcare",
        "aliases": [
            "ayush",
            "ayush hospital",
            "siddha hospital",
            "naturopathy hospital",
            "homoeopathy hospital"
        ]
    },

    {
        "name": "Excel Fitness and Sports Academy",
        "category": "Sports and Fitness",
        "aliases": [
            "fitness",
            "sports",
            "sports academy",
            "excel fitness"
        ]
    }
]


# =========================================================
# COURSES
# =========================================================

COURSES = {

    "BCA": {
        "name": "Bachelor of Computer Applications",
        "institution": "Excel College for Commerce and Science",
        "aliases": ["bca", "computer application", "computer applications"]
    },

    "B.Com": {
        "name": "Bachelor of Commerce",
        "institution": "Excel College for Commerce and Science",
        "aliases": ["bcom", "b.com", "commerce"]
    },

    "BBA": {
        "name": "Bachelor of Business Administration",
        "institution": "Excel College for Commerce and Science",
        "aliases": ["bba", "business administration"]
    },

    "B.Sc Computer Science": {
        "name": "B.Sc Computer Science",
        "institution": "Excel College for Commerce and Science",
        "aliases": ["bsc computer science", "b.sc computer science"]
    },

    "B.Arch": {
        "name": "Bachelor of Architecture",
        "institution": "Excel College of Architecture and Planning",
        "aliases": ["barch", "b.arch", "architecture"]
    },

    "BSMS": {
        "name": "Bachelor of Siddha Medicine and Surgery",
        "institution": "Excel Siddha Medical College and Research Centre",
        "aliases": ["bsms", "siddha medicine", "siddha"]
    },

    "BHMS": {
        "name": "Bachelor of Homoeopathic Medicine and Surgery",
        "institution": "Excel Homoeopathy Medical College",
        "aliases": ["bhms", "homoeopathy", "homeopathy"]
    },

    "BNYS": {
        "name": "Bachelor of Naturopathy and Yogic Sciences",
        "institution": "Excel Medical College for Naturopathy and Yoga",
        "aliases": ["bnys", "naturopathy", "yoga"]
    }
}


# =========================================================
# GENERAL FAQ DATABASE
# =========================================================

FAQS = [

    (
        "what institutions are available",
        "Excel Group Institutions covers Arts and Science, Engineering, Architecture, Polytechnic and ITI, Education, Business School, Pharmacy, Nursing, Health Sciences, Physiotherapy, Occupational Therapy, Naturopathy and Yoga, Siddha, Homoeopathy, School, Hospitals and other healthcare institutions."
    ),

    (
        "what colleges are there",
        "Excel Group Institutions includes Excel College for Commerce and Science, Excel Engineering College, Excel College of Architecture and Planning, Excel Polytechnic College and ITI, Excel College of Education, Kandhaswamy College of Education, Excel Business School, Excel College of Pharmacy, Excel Nursing College, Excel Institute of Health Sciences, Excel College of Physiotherapy and Research Centre, Excel College of Occupational Therapy, Excel Medical College for Naturopathy and Yoga, Excel Siddha Medical College and Research Centre, Excel Homoeopathy Medical College, Excel Public School, Excel Multispeciality Hospitals and Excel AYUSH Hospitals."
    ),

    (
        "where is excel located",
        "Excel Group Institutions is located at NH-544, Salem Main Road, Sankari West, Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu - 637303."
    ),

    (
        "excel address",
        "Excel Group Institutions is located at NH-544, Salem Main Road, Sankari West, Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu - 637303."
    ),

    (
        "excel contact",
        "The general contact number is +91 99655 23999 and the email is info@excelcolleges.com."
    ),

    (
        "hostel",
        "Excel Group Institutions provides hostel facilities for students. Hostel availability and details can vary depending on the institution and programme."
    ),

    (
        "transport",
        "Excel Group Institutions provides transport facilities for students."
    ),

    (
        "placement",
        "Excel Group Institutions has training and placement activities for students. Placement details can vary by institution and programme."
    ),

    (
        "scholarship",
        "Excel Group Institutions provides scholarship opportunities subject to applicable eligibility criteria and programme requirements."
    ),

    (
        "facilities",
        "Excel Group Institutions provides various student facilities including academic infrastructure, laboratories, library, sports facilities, hostel and transport facilities."
    )
]


# =========================================================
# CREATE DATABASE
# =========================================================

def create_database():

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS faq")

    cursor.execute("""
        CREATE TABLE faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    # Add general FAQs
    for question, answer in FAQS:

        cursor.execute(
            "INSERT INTO faq (question, answer) VALUES (?, ?)",
            (question, answer)
        )

    # Add institution FAQs
    for institution in INSTITUTIONS:

        name = institution["name"]
        category = institution["category"]

        institution_questions = [

            (
                f"{name} details",
                f"{name} is part of Excel Group Institutions and comes under the {category} category."
            ),

            (
                f"{name} information",
                f"{name} is an institution under Excel Group Institutions. It comes under the {category} category."
            ),

            (
                f"{name} course",
                f"{name} offers programmes related to {category}. Current programme availability depends on the academic year."
            ),

            (
                f"{name} eligibility",
                f"Eligibility for {name} depends on the specific programme. Different courses may have different eligibility requirements."
            ),

            (
                f"{name} admission",
                f"Admission to {name} depends on the selected programme and the applicable admission requirements."
            ),

            (
                f"{name} hostel",
                f"Hostel facilities are available within Excel Group campus facilities. Availability can vary by institution and programme."
            ),

            (
                f"{name} facilities",
                f"{name} is part of Excel Group Institutions and students can access applicable campus facilities such as academic infrastructure, hostel, transport and sports facilities."
            ),

            (
                f"{name} location",
                f"{name} is part of Excel Group Institutions located at NH-544, Salem Main Road, Sankari West, Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu - 637303."
            )
        ]

        for question, answer in institution_questions:

            cursor.execute(
                "INSERT INTO faq (question, answer) VALUES (?, ?)",
                (question, answer)
            )

    # Add course FAQs
    for short_name, details in COURSES.items():

        full_name = details["name"]
        institution = details["institution"]

        course_questions = [

            (
                f"{short_name} details",
                f"{full_name} is offered under {institution}."
            ),

            (
                f"{short_name} eligibility",
                f"Eligibility for {full_name} depends on the applicable admission rules for the programme."
            ),

            (
                f"{short_name} admission",
                f"Admission for {full_name} depends on the applicable admission requirements and academic rules."
            ),

            (
                f"{short_name} course",
                f"{full_name} is associated with {institution}."
            )
        ]

        for question, answer in course_questions:

            cursor.execute(
                "INSERT INTO faq (question, answer) VALUES (?, ?)",
                (question, answer)
            )

    connection.commit()

    count = cursor.execute(
        "SELECT COUNT(*) FROM faq"
    ).fetchone()[0]

    connection.close()

    print()
    print("==========================================")
    print("FULL EXCEL GROUP DATABASE CREATED")
    print("==========================================")
    print("Institutions :", len(INSTITUTIONS))
    print("Courses      :", len(COURSES))
    print("FAQ records  :", count)
    print("==========================================")


if __name__ == "__main__":
    create_database()
