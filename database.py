
import sqlite3

DATABASE = "college.db"

# Additional course-related questions and answers
COURSE_FAQS = [
    # GENERAL COURSE QUESTIONS
    (
        "What courses are available?",
        "Excel Institutions Group covers different educational fields, including Arts and Science, Engineering, Architecture, Polytechnic, Education, Business, Pharmacy, Nursing and Health Sciences. Exact courses vary by institution and academic year. Ask about a specific institution or course."
    ),
    (
        "Enna courses irukku?",
        "Excel Institutions Group-la Arts and Science, Engineering, Architecture, Polytechnic, Education, Business, Pharmacy, Nursing, Health Sciences pondra fields irukku. Specific course availability-ai official college course list-la confirm pannunga."
    ),
    (
        "என்ன courses இருக்கு?",
        "Excel Institutions Group-la pala educational fields irukku: Arts and Science, Engineering, Architecture, Polytechnic, Education, Pharmacy, Nursing and Health Sciences. Exact course details-ku specific institution-ai sollunga."
    ),
    (
        "What UG courses are available?",
        "UG means Undergraduate programmes. Available UG courses depend on the institution and current academic year. Tell me which institution or subject you are interested in."
    ),
    (
        "What PG courses are available?",
        "PG means Postgraduate programmes. The available programmes and eligibility vary by institution. Check the current official course list for your preferred subject."
    ),
    (
        "What courses can I study after 12th?",
        "After 12th, you can explore degree, professional and diploma programmes depending on your subjects and eligibility. Excel Institutions Group has institutions across several fields. Tell me your 12th group to explore suitable options."
    ),
    (
        "12th mudichitu enna course padikkalam?",
        "12th mudichavanga avanga group, marks, interest and eligibility-ku etha maadhiri courses choose pannalaam. Ungaloda 12th group enna: Maths, Biology, Computer Science, Commerce illa Arts?"
    ),
    (
        "Which course is best?",
        "The best course depends on your interests, school subjects, strengths and career goal. Tell me your 12th group and the field you like, and I can help you compare course options."
    ),
    (
        "How do I choose a course?",
        "Choose a course based on your interests, eligibility, career goals, course fees and preferred work field. Tell me your educational background and interests for guidance."
    ),

    # BCA
    (
        "What is BCA?",
        "BCA stands for Bachelor of Computer Applications. It focuses on computing, programming and software-related subjects. Confirm the current course availability and eligibility with the relevant institution."
    ),
    (
        "BCA ku enna qualification venum?",
        "BCA eligibility college rules and current admission requirements-ai poruthadhu. Exact qualification, subjects and minimum marks-ku official institution eligibility details check pannunga."
    ),
    (
        "What is the eligibility for BCA?",
        "BCA eligibility depends on the institution's current admission rules. Check the official eligibility page for the required school qualification, subjects and minimum marks."
    ),
    (
        "How many years is BCA?",
        "BCA duration depends on the programme structure and current regulations. Check the relevant institution's official course details for the exact duration."
    ),
    (
        "What subjects are taught in BCA?",
        "BCA programmes commonly cover programming, computer fundamentals, databases, software development and web technologies. Exact subjects depend on the syllabus followed by the institution."
    ),
    (
        "What jobs can I get after BCA?",
        "Depending on your skills and experience, BCA graduates may explore software development, web development, software testing, IT support, database-related roles or higher studies."
    ),
    (
        "BCA mudichitu enna job kidaikkum?",
        "BCA mudichathukku appuram skills and experience-ku etha maadhiri web developer, software developer, tester, IT support pondra career options explore pannalaam. Placement guarantee-nu solla mudiyadhu."
    ),
    (
        "Can I study BCA after Commerce?",
        "Eligibility for BCA after Commerce depends on the institution's current admission rules. Check the official requirements for accepted school streams and subjects."
    ),
    (
        "Is maths compulsory for BCA?",
        "Mathematics requirements can vary by institution and admission regulations. Check the official BCA eligibility rules before applying."
    ),

    # BCOM AND COMMERCE
    (
        "What is BCom?",
        "B.Com stands for Bachelor of Commerce. It focuses on commerce, accounting, finance and business-related subjects. Confirm the programme and specialisation available at your chosen institution."
    ),
    (
        "What is the eligibility for BCom?",
        "B.Com eligibility depends on the current admission requirements of the institution. Check the official course eligibility details for the accepted school qualification and minimum marks."
    ),
    (
        "What jobs can I get after BCom?",
        "B.Com graduates may explore careers in accounting, finance, banking, taxation, business operations and further professional studies, depending on their skills and qualifications."
    ),
    (
        "BCom mudichitu enna pannalam?",
        "B.Com mudichathukku appuram accounting, finance, banking, taxation, business-related jobs or higher studies-ai explore pannalaam. Career options unga skills and qualification-ai poruthadhu."
    ),
    (
        "What is the difference between BCA and BCom?",
        "BCA mainly focuses on computing and computer applications, while B.Com focuses on commerce, accounting and business subjects. Choose based on your interests and eligibility."
    ),
    (
        "Can Commerce students study computer courses?",
        "Some computer-related programmes may accept Commerce students, while others have specific subject requirements. Check the eligibility rules for the exact course."
    ),

    # BBA AND BUSINESS
    (
        "What is BBA?",
        "BBA stands for Bachelor of Business Administration. It introduces students to management, marketing, business operations and related topics. Confirm current availability with the institution."
    ),
    (
        "What is the eligibility for BBA?",
        "BBA eligibility depends on the institution's current admission rules. Check the official programme page for required qualifications and minimum marks."
    ),
    (
        "What jobs can I get after BBA?",
        "Depending on skills and experience, BBA graduates may explore entry-level roles in marketing, sales, business operations, customer relations or pursue further management studies."
    ),
    (
        "What is a business management course?",
        "Business management courses cover areas such as management, marketing, finance, operations and organisational behaviour. Programme content depends on the qualification and institution."
    ),

    # BSC AND SCIENCE
    (
        "What is BSc Computer Science?",
        "B.Sc Computer Science is a science degree focused on computing, programming and computer science concepts. Check the relevant institution's official course list and eligibility requirements."
    ),
    (
        "What is the eligibility for BSc Computer Science?",
        "Eligibility depends on the institution and its current admission rules, including accepted school subjects and minimum marks. Check the official course eligibility details."
    ),
    (
        "What jobs can I get after BSc Computer Science?",
        "Graduates may explore entry-level IT, software support, testing, programming or further study opportunities depending on their skills and qualifications."
    ),
    (
        "What is Microbiology?",
        "Microbiology is the study of microorganisms such as bacteria, fungi and viruses. Check the relevant institution's current course list for availability and eligibility."
    ),
    (
        "What is Biochemistry?",
        "Biochemistry studies the chemical processes and molecules involved in living organisms. Confirm course availability and eligibility with the relevant institution."
    ),
    (
        "What is Mathematics degree?",
        "A Mathematics degree focuses on mathematical theories, calculations, statistics and analytical methods. The available programme and entry requirements depend on the institution."
    ),
    (
        "What science courses are available?",
        "Science programmes vary by institution and academic year. Tell me the subject you are interested in, such as Computer Science or another science field, and verify availability with the official institution."
    ),

    # ENGINEERING
    (
        "What engineering courses are available?",
        "Engineering programmes and branches vary by institution and academic year. Check the official Excel Engineering College course list for currently offered branches."
    ),
    (
        "Engineering la enna branches irukku?",
        "Engineering branches institution and academic year-ku etha maadhiri maaralaam. Current branches-ai Excel Engineering College official course list-la check pannunga."
    ),
    (
        "What is the eligibility for engineering?",
        "Engineering eligibility depends on the programme, qualifying subjects, marks and applicable admission rules. Check the official eligibility page for the current requirements."
    ),
    (
        "How many years is engineering?",
        "Engineering degree duration depends on the programme and applicable regulations. Check the official course details for the exact duration."
    ),
    (
        "What is Computer Science Engineering?",
        "Computer Science Engineering focuses on computing systems, programming, algorithms, software and related technologies. Check the official institution course list to confirm availability."
    ),
    (
        "What is Information Technology?",
        "Information Technology focuses on computing systems, software, networks, data and technology services. Programme availability and syllabus depend on the institution."
    ),
    (
        "What is Artificial Intelligence?",
        "Artificial Intelligence, or AI, is a field of computing that develops systems capable of performing tasks such as recognising patterns, understanding language and making predictions."
    ),
    (
        "What is Data Science?",
        "Data Science combines data analysis, statistics and computing to find patterns and insights from data. Check the institution's current course list for programme availability."
    ),
    (
        "What is Cyber Security?",
        "Cyber Security focuses on protecting computers, networks, systems and data from digital threats. Course availability and eligibility must be confirmed with the relevant institution."
    ),
    (
        "What is Machine Learning?",
        "Machine Learning is a branch of AI in which computer systems learn patterns from data to make predictions or decisions."
    ),
    (
        "What is the difference between AI and Data Science?",
        "AI focuses on building systems that perform intelligent tasks. Data Science focuses on extracting insights from data using statistics, computing and analytical methods. The fields can overlap."
    ),
    (
        "What jobs can I get after engineering?",
        "Career opportunities depend on the engineering branch, skills and experience. Graduates may pursue technical roles, software-related careers, core engineering jobs or higher studies."
    ),

    # DIPLOMA AND POLYTECHNIC
    (
        "Are diploma courses available?",
        "Excel Institutions Group includes a Polytechnic institution. Check its official course list for current diploma programmes, eligibility and admission details."
    ),
    (
        "What is Polytechnic?",
        "Polytechnic education commonly offers diploma programmes with practical and technical learning. Specific courses, duration and eligibility depend on the institution."
    ),
    (
        "Can I join a diploma after 10th?",
        "Entry eligibility depends on the diploma programme and applicable admission rules. Check the relevant Excel Polytechnic institution's official admission information."
    ),
    (
        "What can I do after a diploma?",
        "After a diploma, possible options may include employment, further technical studies or eligible lateral-entry pathways, depending on the diploma and current regulations."
    ),

    # ARCHITECTURE
    (
        "What is Architecture?",
        "Architecture involves planning and designing buildings and spaces. Check the official Excel Architecture institution's current programme list, entrance requirements and eligibility."
    ),
    (
        "What is the eligibility for Architecture?",
        "Architecture eligibility depends on the programme, required school subjects, qualifying marks and applicable entrance or aptitude requirements. Check the current official rules."
    ),
    (
        "What jobs can I get after Architecture?",
        "Depending on the qualification and professional requirements, architecture graduates may explore architectural design, planning, visualisation and related built-environment careers."
    ),

    # PHARMACY
    (
        "What is Pharmacy?",
        "Pharmacy is a field related to medicines, their use, preparation, safety and effects. Check the relevant Excel Pharmacy institution for current programmes and eligibility."
    ),
    (
        "What Pharmacy courses are available?",
        "Pharmacy programme availability depends on the institution and academic year. Please check the official Excel Pharmacy course list for current programmes and eligibility."
    ),
    (
        "What is the eligibility for Pharmacy?",
        "Pharmacy eligibility depends on the programme, qualifying subjects and applicable admission rules. Confirm the requirements with the official institution."
    ),

    # NURSING AND HEALTH SCIENCES
    (
        "What Nursing courses are available?",
        "Nursing programme availability and eligibility vary by institution and academic year. Check the official Excel Nursing institution course list for current details."
    ),
    (
        "What is the eligibility for Nursing?",
        "Nursing eligibility depends on the programme, school subjects, marks and applicable regulations. Confirm the current requirements with the relevant institution."
    ),
    (
        "What is Health Sciences?",
        "Health Sciences covers fields related to healthcare, health services and human wellbeing. Exact programmes and admission requirements vary by institution."
    ),
    (
        "What is Physiotherapy?",
        "Physiotherapy focuses on movement, physical function, rehabilitation and helping people improve mobility. Check the relevant institution for current programmes and eligibility."
    ),
    (
        "What is Naturopathy and Yoga?",
        "Naturopathy and Yoga programmes focus on natural health approaches, lifestyle practices and yoga-related study. Confirm the exact programme and eligibility with the institution."
    ),
    (
        "What is Siddha?",
        "Siddha is a traditional system of medicine practised in India. Check the relevant institution for programme availability and official admission requirements."
    ),
    (
        "What is Homoeopathy?",
        "Homoeopathy is a system of medicine with its own educational and professional regulations. Confirm programme availability and admission requirements with the relevant institution."
    ),

    # EDUCATION AND SCHOOL
    (
        "What is Education course?",
        "Education programmes prepare students for roles related to teaching and learning. The exact qualifications and eligibility depend on the programme and current regulations."
    ),
    (
        "What courses are available after graduation?",
        "After graduation, you may explore eligible postgraduate programmes, professional qualifications or skill-development courses. Options depend on your degree and career goal."
    ),

    # FEES, ADMISSION, DURATION
    (
        "What are the course fees?",
        "Course fees vary by institution, programme and academic year. Contact the relevant Excel institution or check its official fee information for the current amount."
    ),
    (
        "How can I apply for a course?",
        "Check the official website of the institution offering your chosen course for the current application process, required documents, eligibility and deadlines."
    ),
    (
        "What documents are required for admission?",
        "Admission documents vary by programme. Commonly requested documents may include qualifying examination records, transfer or conduct certificates, identity documents and photographs. Confirm the exact list with the institution."
    ),
    (
        "Can I change my course?",
        "Course changes depend on the institution's rules, seat availability, eligibility and the stage of study. Contact the admissions office for guidance."
    ),
    (
        "Are scholarships available for courses?",
        "Scholarship eligibility and availability depend on the institution, scheme and student qualifications. Check the official scholarship information or contact the admissions office."
    ),
    (
        "Does the college provide placement?",
        "Placement support and opportunities depend on the institution, programme, student eligibility and employer requirements. Check the relevant institution's official placement information."
    ),

    # COMMON TANGlish QUESTIONS
    (
        "Course duration evlo?",
        "Course duration programme-ai poruthadhu. Neenga endha course pathi kekkureenga nu sollunga; official course details-la exact duration verify pannunga."
    ),
    (
        "Course fees evlo?",
        "Course fees institution, programme and academic year-ai poruthadhu. Exact fees-ku relevant Excel institution office or official fee details-ai contact pannunga."
    ),
    (
        "Enakku enna course suitable?",
        "Ungalukku suitable-aana course suggest panna, unga 12th group, interest and future career goal sollunga."
    ),
    (
        "Computer course irukka?",
        "Excel Institutions Group-la computing-related fields irukkum institutions irukku. Exact computer courses and current availability-ai official course list-la verify pannunga."
    ),
    (
        "Arts and Science courses enna?",
        "Arts and Science programmes subject and academic year-ku etha maadhiri vary aagum. Excel College for Commerce and Science official course list-la current UG and PG programmes check pannunga."
    ),
    (
        "PG padikka enna qualification venum?",
        "PG admission-ku usually relevant bachelor's degree thevai; exact eligibility programme and institution rules-ai poruthadhu. Official course eligibility details check pannunga."
    ),
]


def create_database():
    con = sqlite3.connect(DATABASE)
    cursor = con.cursor()

    # Keep the existing FAQ table and its data.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL UNIQUE,
            answer TEXT NOT NULL
        )
    """)

    # Add only new questions. Existing answers are not overwritten.
    cursor.executemany("""
        INSERT OR IGNORE INTO faq (question, answer)
        VALUES (?, ?)
    """, COURSE_FAQS)

    con.commit()

    cursor.execute("SELECT COUNT(*) FROM faq")
    total = cursor.fetchone()[0]

    con.close()

    print("Course FAQs added successfully!")
    print("Total FAQs in database:", total)


if __name__ == "__main__":
    create_database()
