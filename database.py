
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "college.db"

# Each entry: (question, answer)
COURSE_FAQS = [
    # General course questions
    ("What courses are available?", "Excel Institutions Group-la pala fields irukkalaam. Current course list institution and academic year-ai poruthadhu. Endha institution or subject venum nu sollunga."),
    ("List all available courses", "Courses institution-wise vary aagum. Arts and Science, Engineering, Architecture, Polytechnic, Business, Education and healthcare-related fields-ku official current course list check pannunga."),
    ("Which UG courses are available?", "UG courses are undergraduate programmes. Available programmes and eligibility-ai relevant Excel institution-oda current admission details-la verify pannunga."),
    ("Which PG courses are available?", "PG courses are postgraduate programmes. Current availability and eligibility institution and academic year-ai poruthadhu."),
    ("What courses can I study after 12th?", "Ungaloda 12th group, subjects and interest-ai sollunga. Adhuku suitable-aana course options-ai compare panna help pannuren."),
    ("What courses are available after 10th?", "10th-ku apram eligible diploma and other programmes explore pannalaam. Exact options institution admission rules-ai poruthadhu."),
    ("Which course is best for me?", "Ungaloda qualification, favourite subjects and career goal sollunga. Suitable course options-ai identify panna help pannuren."),
    ("Which course has more job opportunities?", "Job opportunities skills, experience, industry and location-ai poruthadhu. Ungalukku pidicha field-ai choose panni practical skills develop pannunga."),
    ("What is UG?", "UG means Undergraduate. School education-kku piragu eligible students join pannura degree programmes."),
    ("What is PG?", "PG means Postgraduate. Usually bachelor's degree mudichadhukku piragu eligible students pursue pannura programmes."),
    ("How can I find the syllabus?", "Relevant institution-oda official website or department office-la current syllabus details check pannunga."),
    ("How do I find course fees?", "Fees course and institution-ai poruthadhu. Current fee structure-ku official admissions office-ai contact pannunga."),
    ("How do I apply for admission?", "Official admission page-la application steps, eligibility, documents and deadlines check pannunga."),
    ("Does completing a course guarantee a job?", "Course complete pannina mattum job guarantee illa. Skills, projects, experience and employer requirements mukkiyam."),

    # BCA
    ("What is BCA?", "BCA stands for Bachelor of Computer Applications. Idhu computer applications and computing-related undergraduate programme."),
    ("What is the full form of BCA?", "BCA stands for Bachelor of Computer Applications."),
    ("What do we study in BCA?", "BCA-la programming, computer fundamentals, databases, software development and web technologies maadhiri topics irukkalaam. Exact syllabus institution-ai poruthadhu."),
    ("What is BCA eligibility?", "BCA eligibility and required school subjects institution-oda current admission rules-ai poruthadhu. Official criteria verify pannunga."),
    ("Can Commerce students study BCA?", "Commerce students apply panna mudiyuma enbadhu current institution eligibility rules-ai poruthadhu. Required subjects and marks verify pannunga."),
    ("Can Arts students study BCA?", "Arts students eligibility course admission rules and required school subjects-ai poruthadhu. Official criteria check pannunga."),
    ("Does BCA require Mathematics?", "Mathematics requirement institution and current admission regulations-ai poruthadhu. Official eligibility details check pannunga."),
    ("Is coding taught in BCA?", "Aama, BCA programmes-la generally programming-related subjects irukkum. Exact languages and syllabus college curriculum-ai poruthadhu."),
    ("Is BCA difficult for beginners?", "Beginner-a irundhaalum step-by-step practice moolama programming kathukkalaam. Regular practice mukkiyam."),
    ("What programming languages are taught in BCA?", "Programming languages curriculum-ai poruthadhu. Current syllabus-la exact language list check pannunga."),
    ("What jobs can I get after BCA?", "Possible career paths: web developer, software developer, software tester and IT support. Skills and employer requirements mukkiyam."),
    ("Can I do MCA after BCA?", "MCA eligibility university rules, degree and required subjects-ai poruthadhu. Current admission criteria verify pannunga."),
    ("Can I get an IT job after BCA?", "IT job opportunities irukkalaam. Programming skills, projects, communication and interview preparation help pannum."),
    ("BCA-ku enna qualification venum?", "BCA eligibility college rules and required school subjects-ai poruthadhu. Official admission criteria check pannunga."),
    ("BCA padikka coding theriyanuma?", "Admission-ku prior coding knowledge thevaiyaa enbadhu institution rules-ai poruthadhu. Course-la programming kathukka vendiyirukkum."),
    ("BCA mudichitu enna job pogalam?", "Web development, software testing, IT support and related roles explore pannalaam. Skills and job requirements mukkiyam."),
    ("BCA mudichitu MCA padikkalama?", "MCA-ku apply panna mudiyuma enbadhu university eligibility rules-ai poruthadhu. Current criteria check pannunga."),

    # B.Com
    ("What is BCom?", "B.Com stands for Bachelor of Commerce. Idhu commerce and business-related undergraduate degree."),
    ("What is the full form of B.Com?", "B.Com stands for Bachelor of Commerce."),
    ("What subjects are taught in BCom?", "B.Com-la accounting, commerce, finance, business and related subjects irukkalaam. Exact syllabus vary aagum."),
    ("What is BCom eligibility?", "B.Com eligibility and minimum marks institution-oda current admission rules-ai poruthadhu."),
    ("What jobs can I get after BCom?", "Accounting, finance, banking, taxation and business operations-related roles explore pannalaam."),
    ("Can I do MCom after BCom?", "M.Com admission eligibility university and programme rules-ai poruthadhu."),
    ("Is BCom useful for banking jobs?", "B.Com commerce and finance foundation provide pannalaam. Banking recruitment-ku separate eligibility and selection requirements irukkum."),
    ("What is the difference between BCom and BBA?", "B.Com mainly commerce and accounting-focused; BBA business administration and management-focused."),
    ("BCom-ku enna qualification venum?", "B.Com eligibility and required marks institution admission rules-ai poruthadhu."),
    ("BCom mudichitu enna job kidaikkum?", "Accounting, finance, banking and business-related roles explore pannalaam. Skills and qualifications mukkiyam."),

    # BBA and management
    ("What is BBA?", "BBA stands for Bachelor of Business Administration."),
    ("What is the full form of BBA?", "BBA stands for Bachelor of Business Administration."),
    ("What subjects are taught in BBA?", "BBA-la management, marketing, business operations, finance and organisational topics irukkalaam."),
    ("Can I do MBA after BBA?", "MBA eligibility institution admission rules and any applicable entrance requirements-ai poruthadhu."),
    ("What jobs can I get after BBA?", "Sales, marketing, customer relations and business operations-related roles explore pannalaam."),
    ("What is the difference between BBA and MBA?", "BBA is an undergraduate business degree; MBA is a postgraduate management degree."),

    # B.Sc and science
    ("What is BSc?", "B.Sc stands for Bachelor of Science."),
    ("What is the full form of BSc?", "B.Sc stands for Bachelor of Science."),
    ("What is BSc Computer Science?", "B.Sc Computer Science is a science degree focused on computing concepts and related subjects. Availability and syllabus-ai verify pannunga."),
    ("What is BSc eligibility?", "B.Sc eligibility depends on the chosen subject, school subjects and institution admission rules."),
    ("What jobs can I get after BSc?", "Career options chosen subject, skills and further qualifications-ai poruthadhu."),
    ("What is BSc Mathematics?", "B.Sc Mathematics focuses on mathematical concepts, analytical methods and problem-solving."),
    ("What is BSc Physics?", "B.Sc Physics studies matter, energy, motion and physical principles."),
    ("What is Microbiology?", "Microbiology studies microorganisms such as bacteria and fungi. Course availability-ai institution-la verify pannunga."),
    ("What is Biochemistry?", "Biochemistry studies chemical processes and molecules in living organisms."),
    ("Can I do MSc after BSc?", "M.Sc admission depends on bachelor's degree subject and university eligibility rules."),

    # Computer and technology fields
    ("What is Artificial Intelligence?", "Artificial Intelligence (AI) is a computing field that develops systems for tasks such as language processing, prediction and pattern recognition."),
    ("What is Machine Learning?", "Machine Learning is a branch of AI where computer systems learn patterns from data."),
    ("What is Data Science?", "Data Science uses data, statistics and computing to discover patterns and generate insights."),
    ("What is Cyber Security?", "Cyber Security focuses on protecting computers, networks and data from digital threats."),
    ("What is Information Technology?", "Information Technology involves computers, software, networks and information systems."),
    ("What is Web Development?", "Web Development is creating websites and web applications using technologies such as HTML, CSS and JavaScript."),
    ("What is Full Stack Development?", "Full Stack Development involves working on both the front end and back end of a web application."),
    ("What is Cloud Computing?", "Cloud Computing provides computing resources and services over a network, commonly the internet."),
    ("What is Software Testing?", "Software Testing checks whether software works as expected and helps identify defects."),
    ("What is Database Management?", "Database Management involves storing, organising, retrieving and maintaining data."),
    ("Is Python useful for IT jobs?", "Python is used in automation, web development, data analysis and other computing tasks. Job requirements vary."),
    ("Can I learn AI after BCA?", "BCA mudichitu AI concepts and projects learn pannalaam. Advanced course admission requirements vary aagum."),
    ("What jobs are available in AI?", "AI-related careers may include AI development, data analysis and machine learning roles, depending on qualifications and experience."),
    ("Which computer course is good for beginners?", "Computer basics, programming fundamentals and web development are common starting points. Ungaloda interest-ai poruththu choose pannunga."),

    # Engineering
    ("What is BE?", "BE stands for Bachelor of Engineering."),
    ("What is the full form of BE?", "BE stands for Bachelor of Engineering."),
    ("What is BTech?", "B.Tech stands for Bachelor of Technology."),
    ("What is the difference between BE and BTech?", "Both are undergraduate engineering qualifications. Curriculum and naming institution and programme-ai poruthadhu."),
    ("What is engineering eligibility?", "Engineering eligibility depends on the branch, qualifying subjects, marks and current admission rules."),
    ("What is Computer Science Engineering?", "Computer Science Engineering covers computing, algorithms, programming and software-related systems."),
    ("What is Mechanical Engineering?", "Mechanical Engineering focuses on machines, mechanical systems, design and manufacturing."),
    ("What is Civil Engineering?", "Civil Engineering covers infrastructure such as buildings, roads, bridges and water systems."),
    ("What is Electrical Engineering?", "Electrical Engineering studies electrical systems, circuits and power-related topics."),
    ("What is Electronics Engineering?", "Electronics Engineering covers electronic circuits, devices and related technologies."),
    ("What is AI Engineering?", "AI-related engineering study focuses on artificial intelligence, computing and intelligent systems. Verify the exact programme title and availability."),
    ("Can I study engineering after diploma?", "Eligible diploma students may have further-study or lateral-entry options under applicable admission regulations."),
    ("What jobs can I get after engineering?", "Career options depend on engineering branch, practical skills, projects and employer requirements."),
    ("Engineering-ku enna qualification venum?", "Engineering eligibility branch, required school subjects and current admission rules-ai poruthadhu."),
    ("Engineering mudichitu enna job kidaikkum?", "Career options engineering branch, practical skills and employer requirements-ai poruthadhu."),

    # Polytechnic and diploma
    ("What is Polytechnic?", "Polytechnic institutions commonly offer diploma-level technical education. Current programme list and eligibility-ai verify pannunga."),
    ("What is a diploma course?", "Diploma is a qualification focused on a specific field. Duration and entry requirements vary by programme."),
    ("What is the difference between diploma and degree?", "Diploma and degree qualifications differ in level, curriculum, duration and eligibility."),
    ("What is Polytechnic eligibility?", "Polytechnic admission requirements depend on the programme and current admission rules."),
    ("What jobs can I get after diploma?", "Career options depend on diploma field, practical skills and employer requirements."),

    # Architecture
    ("What is Architecture?", "Architecture focuses on planning and designing buildings and spaces."),
    ("What is BArch?", "B.Arch stands for Bachelor of Architecture. Check the current programme availability and admission requirements."),
    ("What is Architecture eligibility?", "Architecture has specific subject and admission requirements that must be checked against current regulations."),
    ("What jobs can I get after Architecture?", "Career options may include architecture-related design and planning roles, subject to professional qualifications and employer requirements."),

    # Pharmacy, Nursing and healthcare
    ("What is Pharmacy?", "Pharmacy is a healthcare-related field concerned with medicines and their safe use. Verify programme availability and eligibility."),
    ("What is BPharm?", "B.Pharm stands for Bachelor of Pharmacy. Check the institution for current course availability and admission rules."),
    ("What is DPharm?", "D.Pharm stands for Diploma in Pharmacy. Check current availability and eligibility requirements."),
    ("What is Pharmacy eligibility?", "Pharmacy admission requirements depend on the programme, qualifying subjects and current regulations."),
    ("What is Nursing?", "Nursing is a healthcare profession focused on patient care. Programme eligibility and availability must be checked officially."),
    ("What is BSc Nursing?", "B.Sc Nursing stands for Bachelor of Science in Nursing. Verify current course availability and admission requirements."),
    ("What is Nursing eligibility?", "Nursing eligibility depends on the programme, required school subjects, marks and current regulations."),
    ("What is Physiotherapy?", "Physiotherapy focuses on movement, physical function and rehabilitation. Check current programme information."),
    ("What is Naturopathy?", "Naturopathy is a health-related field associated with natural approaches to wellbeing. Verify approved programme details and requirements."),
    ("What is Siddha?", "Siddha is a traditional system of medicine. Check current programme availability and professional regulations."),
    ("What is Homoeopathy?", "Homoeopathy is a system of medicine with specific educational and professional regulations. Verify current course information."),

    # Admission, duration and careers
    ("How long does a course take?", "Course duration programme and applicable regulations-ai poruthadhu. Course name sollunga; more specific guidance tharen."),
    ("What is a semester?", "Semester is an academic period within a course. Number and duration depend on the programme structure."),
    ("What documents are required for admission?", "Common documents may include qualifying exam records, transfer certificate, identity documents and photographs. Official checklist-ai verify pannunga."),
    ("When does admission start?", "Admission dates institution, programme and academic year-ai poruthadhu. Official announcements check pannunga."),
    ("Are scholarships available?", "Scholarship availability and eligibility scheme and institution-ai poruthadhu. Official scholarship details verify pannunga."),
    ("Can I change my course after admission?", "Course change institution rules, seat availability and eligibility-ai poruthadhu. Admissions office-ai contact pannunga."),
    ("Can I study PG after graduation?", "Eligible graduates can explore postgraduate programmes according to degree and admission requirements."),
    ("How do I prepare for a course interview?", "Subject basics review pannunga, course interest explain panna practice pannunga, required documents ready pannunga."),
    ("Course mudikka evlo years aagum?", "Course duration programme-ai poruthadhu. Exact duration-ku official course details check pannunga."),
    ("Course-ku epdi apply pannurathu?", "Relevant institution-oda official admission page-la application steps and deadlines check pannunga."),
    ("Course mudichaa job guarantee irukka?", "Course mudichadhunaala mattum job guarantee illa. Skills, projects, experience and employer requirements mukkiyam."),
    ("Course syllabus enga paarkalam?", "Current syllabus-ku institution-oda official website or department office-ai contact pannunga."),
    ("Course fees evlo?", "Exact fees course and institution-ai poruthadhu. Current fee structure-ku official admissions office-ai contact pannunga."),
    ("Enakku suitable-aana course eppadi choose pannurathu?", "Ungaloda qualification, favourite subjects and career goal sollunga. Suitable options compare panna help pannuren."),
]


# Extra general college FAQs
GENERAL_FAQS = [
    ("What is Excel Institutions Group?", "Excel Institutions Group includes institutions across multiple educational and professional fields. For the current official list, visit https://excelinstitutions.com/."),
    ("Where is Excel College for Commerce and Science?", "The college address listed for Excel College for Commerce and Science is NH-544, Salem Main Road, Sankari West, Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu - 637303. Please verify current details with the official website."),
    ("How can I contact Excel Institutions?", "For current contact details, visit https://excelinstitutions.com/ or the relevant institution's official contact page."),
    ("What facilities are available?", "Facilities vary by institution and campus. Please check the relevant institution's official website for current details."),
    ("Is hostel available?", "Hostel availability and rules vary by institution and campus. Confirm current availability with the admissions office."),
    ("What about placements?", "Placement activities and outcomes vary by institution, programme and year. Check the relevant institution's official placement information."),
    ("What is the admission procedure?", "Admission steps depend on the institution and programme. Check the official admissions page for eligibility, documents and deadlines."),
    ("What is the scholarship procedure?", "Scholarship eligibility and application procedures depend on the scheme. Check the institution's official scholarship details."),
    ("What institutions are available in Excel Group?", "Excel Institutions Group has institutions in different fields. Check https://excelinstitutions.com/ for the current official list."),
    ("What is the full form of ECCS?", "The institution name is Excel College for Commerce and Science."),
]


def create_database():
    """Create FAQ table if needed and safely add new FAQ entries."""
    connection = sqlite3.connect(str(DATABASE))

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS faq (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL UNIQUE,
                answer TEXT NOT NULL
            )
        """)

        # Support an older FAQ table that has question and answer but no id.
        cursor.execute("PRAGMA table_info(faq)")
        columns = {row[1] for row in cursor.fetchall()}

        if "question" not in columns or "answer" not in columns:
            raise RuntimeError(
                "Existing faq table has an unexpected schema. "
                "Please inspect college.db before changing it."
            )

        all_faqs = GENERAL_FAQS + COURSE_FAQS

        for question, answer in all_faqs:
            # Never display the abbreviation in chatbot answers.
            answer = answer.replace(
                "ECCS", "Excel College for Commerce and Science"
            )

            cursor.execute(
                """
                SELECT 1 FROM faq
                WHERE LOWER(TRIM(question)) = LOWER(TRIM(?))
                LIMIT 1
                """,
                (question,)
            )

            if cursor.fetchone() is None:
                cursor.execute(
                    "INSERT INTO faq (question, answer) VALUES (?, ?)",
                    (question, answer)
                )

        connection.commit()

        cursor.execute("SELECT COUNT(*) FROM faq")
        count = cursor.fetchone()[0]

        print(f"Database ready. Total FAQ questions: {count}")

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


if __name__ == "__main__":
    create_database()
