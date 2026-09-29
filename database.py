import sqlite3

DATABASE = "college.db"


# =========================================================
# FULL EXCEL GROUP INSTITUTIONS
# =========================================================

INSTITUTIONS = [

    # ---------------- TECHNICAL CAMPUS ----------------

    {
        "name": "Excel Engineering College",
        "category": "Engineering",
        "aliases": [
            "engineering",
            "engineering college",
            "excel engineering",
            "excel engineering college",
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
            "excel architecture",
            "excel college architecture"
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
        "name": "Excel College for Commerce and Science",
        "category": "Arts and Science",
        "aliases": [
            "commerce and science",
            "arts and science",
            "excel commerce",
            "excel science",
            "eccs"
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
        "name": "Excel Business School",
        "category": "Business School",
        "aliases": [
            "business school",
            "management",
            "excel business",
            "b school",
            "mba"
        ]
    },

    {
        "name": "Kandhaswamy College of Education",
        "category": "Education",
        "aliases": [
            "kandhaswamy",
            "kandhaswamy education",
            "kandhaswamy college"
        ]
    },

    {
        "name": "Excel Fitness and Sports Academy",
        "category": "Sports and Fitness",
        "aliases": [
            "fitness",
            "sports academy",
            "sports",
            "excel fitness"
        ]
    },


    # ---------------- MEDICAL CAMPUS ----------------

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
        "name": "Excel Institute of Health Science",
        "category": "Health Science",
        "aliases": [
            "health science",
            "health sciences",
            "health science college",
            "excel health science"
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
            "ot college",
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
            "bnys",
            "excel naturopathy"
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
            "homoeopathy college",
            "bhms",
            "excel homeopathy"
        ]
    },

    {
        "name": "Excel Multispeciality Hospitals",
        "category": "Hospital",
        "aliases": [
            "hospital",
            "hospitals",
            "multi speciality hospital",
            "multispeciality",
            "excel hospital"
        ]
    },

    {
        "name": "Excel Physiotherapy, Homoeopathy, Siddha, Naturopathy and AYUSH Hospitals",
        "category": "AYUSH Hospital",
        "aliases": [
            "ayush hospital",
            "ayush",
            "siddha hospital",
            "naturopathy hospital",
            "homoeopathy hospital",
            "physiotherapy hospital"
        ]
    },


    # ---------------- SCHOOL ----------------

    {
        "name": "Excel Public School",
        "category": "School",
        "aliases": [
            "school",
            "public school",
            "cbse",
            "excel school",
            "excel public school"
        ]
    }
]


# =========================================================
# GENERAL INFORMATION
# =========================================================

GENERAL_FAQS = [

    (
        "excel group institutions",
        "Excel Group Institutions is a multidisciplinary educational group with Technical Campus and Medical Campus institutions."
    ),

    (
        "excel institutions",
        "Excel Group Institutions includes Engineering, Architecture, Polytechnic and ITI, Commerce and Science, Education, Business School, Pharmacy, Nursing, Health Science, Physiotherapy, Occupational Therapy, Naturopathy and Yoga, Siddha, Homoeopathy, School and healthcare institutions."
    ),

    (
        "what colleges are there in excel",
        "Excel Group Institutions includes Excel Engineering College, Excel College of Architecture and Planning, Excel Polytechnic College and ITI, Excel College for Commerce and Science, Excel College of Education, Excel Business School, Excel College of Pharmacy, Excel Nursing College, Excel Institute of Health Science, Excel College of Physiotherapy and Research Centre, Excel College of Occupational Therapy, Excel Medical College for Naturopathy and Yoga, Excel Siddha Medical College and Research Centre, Excel Homoeopathy Medical College and Excel Public School."
    ),

    (
        "where is excel institutions located",
        "Excel Group Institutions is located at NH-544, Salem Main Road, Sankari West, Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu - 637303."
    ),

    (
        "excel contact",
        "The general contact number listed by Excel Group Institutions is +91 99655 23999 and the email is info@excelcolleges.com."
    ),

    (
        "excel hostel",
        "Excel Group Institutions provides hostel facilities for students. Hostel information may vary by institution and programme."
    ),

    (
        "excel transport",
        "Excel Group Institutions provides transport facilities for students."
    ),

    (
        "excel sports",
        "Excel Group Institutions provides sports and games facilities, including sports infrastructure on campus."
    ),

    (
        "excel admission",
        "Excel Group Institutions has an admission process for its different institutions and programmes. Admission requirements vary according to the institution and course."
    ),

    (
        "excel scholarship",
        "Excel Group Institutions provides admission with scholarship opportunities. Scholarship eligibility and amount can vary according to the applicable programme and criteria."
    )
]


# =========================================================
# INSTITUTION FAQ TEMPLATES
# =========================================================

INSTITUTION_FAQS = []

for institution in INSTITUTIONS:

    name = institution["name"]
    category = institution["category"]

    INSTITUTION_FAQS.extend([

        (
            f"{name} details",
            f"{name} is part of Excel Group Institutions and comes under the {category} category."
        ),

        (
            f"{name} courses",
            f"{name} offers programmes related to {category}. Course availability and current programmes should be checked for the specific academic year."
        ),

        (
            f"{name} eligibility",
            f"Eligibility for {name} depends on the specific programme. The required qualification can vary from course to course."
        ),

        (
            f"{name} admission",
            f"Admission to {name} depends on the programme and applicable admission requirements."
        ),

        (
            f"{name} hostel",
            f"Hostel facilities are available within the Excel Group campus facilities. Availability can depend on the institution and programme."
        ),

        (
            f"{name} facilities",
            f"{name} is part of Excel Group Institutions, which provides student facilities such as campus infrastructure, transport, sports and hostel facilities."
        ),

        (
            f"{name} location",
            f"{name} is part of Excel Group Institutions located at NH-544, Salem Main Road, Sankari West, Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu - 637303."
        )
    ])


# =========================================================
# COURSE INFORMATION
# =========================================================

COURSES = [

    ("BCA", "Bachelor of Computer Applications", "Commerce and Science"),

    ("B.Com", "Bachelor of Commerce", "Commerce and Science"),

    ("BBA", "Bachelor of Business Administration", "Commerce and Science"),

    ("B.Sc Computer Science",
     "Bachelor of Science in Computer Science",
     "Commerce and Science"),

    ("B.A English",
     "Bachelor of Arts in English",
     "Commerce and Science"),

    ("B.Sc Microbiology",
     "Bachelor of Science in Microbiology",
     "Commerce and Science"),

    ("B.Sc Biochemistry",
     "Bachelor of Science in Biochemistry",
     "Commerce and Science"),

    ("B.Sc Visual Communication",
     "Bachelor of Science in Visual Communication",
     "Commerce and Science"),

    ("B.Arch",
     "Bachelor of Architecture",
     "Architecture"),

    ("M.Arch",
     "Master of Architecture",
     "Architecture"),

    ("DAE Automobile Engineering",
     "Diploma in Automobile Engineering",
     "Polytechnic"),

    ("DCE Civil Engineering",
     "Diploma in Civil Engineering",
     "Polytechnic"),

    ("DECE Electronics and Communication Engineering",
     "Diploma in Electronics and Communication Engineering",
     "Polytechnic"),

    ("DEEE Electrical and Electronics Engineering",
     "Diploma in Electrical and Electronics Engineering",
     "Polytechnic"),

    ("DME Mechanical Engineering",
     "Diploma in Mechanical Engineering",
     "Polytechnic"),

    ("BSMS",
     "Bachelor of Siddha Medicine and Surgery",
     "Siddha"),

    ("BHMS",
     "Bachelor of Homoeopathic Medicine and Surgery",
     "Homoeopathy"),

    ("BNYS",
     "Bachelor of Naturopathy and Yogic Sciences",
     "Naturopathy and Yoga")
]


# =========================================================
# DATABASE CREATION
# =========================================================

def create_database():

    con = sqlite3.connect(DATABASE)

    cursor = con.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS faq
    """)

    cursor.execute("""
        CREATE TABLE faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    # General FAQs
    cursor.executemany(
        "INSERT INTO faq (question, answer) VALUES (?, ?)",
        GENERAL_FAQS
    )

    # Institution FAQs
    cursor.executemany(
        "INSERT INTO faq (question, answer) VALUES (?, ?)",
        INSTITUTION_FAQS
    )

    # Course FAQs
    course_faqs = []

    for short_name, full_name, category in COURSES:

        course_faqs.extend([

            (
                f"{short_name} course",
                f"{full_name} is a programme associated with the {category} category of Excel Group Institutions."
            ),

            (
                f"{short_name} eligibility",
                f"Eligibility for {full_name} depends on the applicable admission rules for the programme."
            ),

            (
                f"{short_name} admission",
                f"Admission requirements for {full_name} depend on the applicable academic and admission rules."
            ),

            (
                f"{short_name} details",
                f"{full_name} is one of the programmes associated with Excel Group Institutions."
            )
        ])

    cursor.executemany(
        "INSERT INTO faq (question, answer) VALUES (?, ?)",
        course_faqs
    )

    con.commit()
    con.close()

    print("Full Excel Group database created successfully!")
    print("Institutions added:", len(INSTITUTIONS))
    print("Courses added:", len(COURSES))


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    create_database()
