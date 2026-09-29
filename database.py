import sqlite3

DATABASE = "college.db"

data = [
    # ============================================================
    # EXCEL GROUP INSTITUTIONS - GENERAL
    # ============================================================
    (
        "What is Excel Group Institutions?",
        "Excel Group Institutions is a group of educational institutions located at Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu."
    ),
    (
        "What colleges are there in Excel Group Institutions?",
        "Excel's official website lists institutions including Excel Engineering College (Autonomous), Excel College for Commerce and Science, Excel College of Education, Excel Medical College for Naturopathy and Yoga, Excel Public School, Excel Nursing College, Excel Siddha Medical College and Research Centre, Excel Homeopathy Medical College, Excel College of Pharmacy, Excel College of Physiotherapy and Research Centre, Excel College of Occupational Therapy, Excel College of Architecture and Planning, and Excel Polytechnic College."
    ),
    (
        "Excel institute la enna colleges irukku?",
        "Excel Group Institutions-la Excel Engineering College, Excel College for Commerce and Science, Excel College of Education, Excel Medical College for Naturopathy and Yoga, Excel Nursing College, Excel Polytechnic College and other institutions irukku."
    ),
    (
        "Where is Excel Group Institutions located?",
        "Excel Group Institutions is located at NH-544, Salem Main Road, Sankari West, Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu - 637303."
    ),
    (
        "Excel college enga irukku?",
        "Excel Group Institutions and Excel College for Commerce and Science are at NH-544, Salem Main Road, Sankari West, Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu - 637303."
    ),
    (
        "What is the Excel Group contact number?",
        "The general Excel contact number listed on the official website is +91 99655 23999."
    ),
    (
        "What is the Excel Group email?",
        "The general email listed by Excel is info@excelcolleges.com."
    ),
    (
        "How far is Excel from Bhavani?",
        "Excel Group Institutions' official contact page says the campus is about 9 km from Bhavani."
    ),
    (
        "How far is Excel from Erode?",
        "Excel's official contact page says the campus is about 20 km from Erode Railway Junction."
    ),
    (
        "How far is Excel from Salem?",
        "Excel's official contact page says the campus is about 40 km from Salem."
    ),
    (
        "How far is Excel from Coimbatore airport?",
        "Excel's official contact page says the campus is about 107 km from Coimbatore Airport."
    ),

    # ============================================================
    # EXCEL COLLEGE FOR COMMERCE AND SCIENCE - ABOUT
    # ============================================================
    (
        "Tell me about Excel College for Commerce and Science.",
        "Excel College for Commerce and Science was established in 2018 by Rengaswamy Educational Trust. It is located at Komarapalayam and offers undergraduate and postgraduate programmes in arts, commerce, computer science, data science and other disciplines."
    ),
    (
        "When was Excel College for Commerce and Science established?",
        "Excel College for Commerce and Science was established in 2018 by Rengaswamy Educational Trust."
    ),
    (
        "Who established Excel College for Commerce and Science?",
        "Excel College for Commerce and Science was established by Rengaswamy Educational Trust."
    ),
    (
        "What is the vision of Excel College for Commerce and Science?",
        "The college vision is to develop graduates who are morally upright, intellectually capable, emotionally stable and practically effective, with special attention to students from remote areas."
    ),
    (
        "What is the mission of Excel College for Commerce and Science?",
        "The mission includes moral and ethical development, high-standard education, preparation for the competitive world, awareness of social and environmental concerns, and exposure to science and modern teaching techniques."
    ),
    (
        "Is Excel College for Commerce and Science affiliated?",
        "Yes. The official website states that Excel College for Commerce and Science is affiliated with Periyar University, Salem."
    ),
    (
        "Is Excel College for Commerce and Science approved?",
        "Yes. The official website states that Excel College for Commerce and Science is approved by the Government of Tamil Nadu."
    ),
    (
        "What is the government approval of Excel College?",
        "The official approvals page lists Government of Tamil Nadu approval through G.O. MS No. 160, Higher Education (EI) Department, dated 13.07.2018."
    ),
    (
        "Who is the principal of Excel College for Commerce and Science?",
        "The official contact page lists Dr. R. Vimal Nishant as Principal of Excel College for Commerce and Science, Komarapalayam."
    ),
    (
        "Principal phone number enna?",
        "The official contact page lists the Principal's contact number as 9865140111."
    ),
    (
        "Principal email enna?",
        "The Principal's official email listed by the college is v.principalarts@excelcolleges.com."
    ),
    (
        "What is the address of Excel College for Commerce and Science?",
        "NH-544, Salem Main Road, Sankari West, Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu - 637303."
    ),
    (
        "Excel College address sollu.",
        "Excel College for Commerce and Science, NH-544, Salem Main Road, Sankari West, Pallakkapalayam, Komarapalayam, Namakkal District, Tamil Nadu - 637303."
    ),

    # ============================================================
    # UG COURSES
    # ============================================================
    (
        "What UG courses are available at Excel College?",
        "The official programme list includes BA Tamil, BA English, BBA, B.Com, B.Com Computer Application, B.Com Accounting and Finance, B.Com Professional Accounting, B.Com Information Technology, BCA, B.Sc Artificial Intelligence and Machine Learning, B.Sc Computer Science, B.Sc Data Science, B.Sc Information Technology, B.Sc Computer Science Cyber Security, B.Sc Computer Science Artificial Intelligence and Data Science, B.Sc Microbiology, B.Sc Clinical Laboratory Technology, B.Sc Biochemistry, B.Sc Textile and Fashion Designing, B.Sc Costume Design and Fashion, and B.Sc Visual Communication."
    ),
    (
        "Excel college la BCA irukka?",
        "Yes. BCA - Bachelor of Computer Applications is offered at Excel College for Commerce and Science."
    ),
    (
        "Excel college la B.Com irukka?",
        "Yes. B.Com is offered, along with B.Com Computer Application, B.Com Accounting and Finance, B.Com Professional Accounting and B.Com Information Technology."
    ),
    (
        "Excel college la BBA irukka?",
        "Yes. BBA - Bachelor of Business Administration is offered."
    ),
    (
        "Excel college la BA courses enna?",
        "The official UG programme list includes BA Tamil and BA English."
    ),
    (
        "Excel college la B.Sc courses enna?",
        "B.Sc options listed by the college include Artificial Intelligence and Machine Learning, Computer Science, Data Science, Information Technology, Cyber Security, Artificial Intelligence and Data Science, Microbiology, Clinical Laboratory Technology, Biochemistry, Textile and Fashion Designing, Costume Design and Fashion, and Visual Communication."
    ),
    (
        "Does Excel have B.Sc Computer Science?",
        "Yes. B.Sc Computer Science is listed in the official UG programme list."
    ),
    (
        "Does Excel have B.Sc Data Science?",
        "Yes. B.Sc Data Science is listed in the official UG programme list."
    ),
    (
        "Does Excel have B.Sc Information Technology?",
        "Yes. B.Sc Information Technology is listed in the official UG programme list."
    ),
    (
        "Does Excel have B.Sc Cyber Security?",
        "Yes. B.Sc Computer Science Cyber Security is listed in the official UG programme list."
    ),
    (
        "Does Excel have AI courses?",
        "Yes. The official programme list includes B.Sc Artificial Intelligence and Machine Learning and B.Sc Computer Science Artificial Intelligence and Data Science."
    ),
    (
        "Does Excel have B.Sc Microbiology?",
        "Yes. B.Sc Microbiology is listed in the official programme and eligibility information."
    ),
    (
        "Does Excel have B.Sc Biochemistry?",
        "Yes. B.Sc Biochemistry is listed in the official programme and eligibility information."
    ),
    (
        "Does Excel have B.Sc Clinical Laboratory Technology?",
        "Yes. B.Sc Clinical Laboratory Technology is listed in the official programme and eligibility information."
    ),
    (
        "Does Excel have Visual Communication?",
        "Yes. B.Sc Visual Communication is listed in the official UG programme list."
    ),
    (
        "Does Excel have Textile and Fashion Designing?",
        "Yes. B.Sc Textile and Fashion Designing is listed in the official UG programme list."
    ),
    (
        "Does Excel have Costume Design and Fashion?",
        "Yes. B.Sc Costume Design and Fashion is listed in the official UG programme list."
    ),

    # ============================================================
    # PG COURSES
    # ============================================================
    (
        "What PG courses are available at Excel College?",
        "The official PG programme list includes M.A English, M.Com, M.Sc Microbiology, M.Sc Computer Science, M.Sc Textile and Fashion Designing, and Master of Social Work."
    ),
    (
        "Excel college la MA English irukka?",
        "Yes. M.A English is listed as a postgraduate programme."
    ),
    (
        "Excel college la M.Com irukka?",
        "Yes. M.Com is listed as a postgraduate programme."
    ),
    (
        "Excel college la M.Sc Computer Science irukka?",
        "Yes. M.Sc Computer Science is listed as a postgraduate programme."
    ),
    (
        "Excel college la M.Sc Microbiology irukka?",
        "Yes. M.Sc Microbiology is listed as a postgraduate programme."
    ),
    (
        "Excel college la MSW irukka?",
        "Yes. Master of Social Work (MSW) is listed as a postgraduate programme."
    ),
    (
        "Excel college la M.Sc Textile Fashion irukka?",
        "Yes. M.Sc Textile and Fashion Designing is listed as a postgraduate programme."
    ),

    # ============================================================
    # ELIGIBILITY - UG
    # ============================================================
    (
        "What is the eligibility for BCA at Excel?",
        "For BCA, the official eligibility page states that the student should pass Higher Secondary with Mathematics, or pass with Computer Science, Computer Applications, Information Technology, Computer Technology, Business Mathematics or Statistics. Students without Mathematics in the relevant route may need a 15-day Mathematics bridge course."
    ),
    (
        "BCA eligibility enna?",
        "BCA-ku Higher Secondary pass with Mathematics, or the specified Computer Science/Computer Applications/IT/Computer Technology/Business Mathematics/Statistics subjects is accepted. If Mathematics was not studied in the specified route, a 15-day Mathematics bridge course may be required."
    ),
    (
        "What is BBA eligibility?",
        "BBA eligibility is a pass in HSC. The official page says preference should be given to Commerce and Accountancy streams."
    ),
    (
        "What is B.Com eligibility?",
        "For B.Com and related commerce programmes, the official page accepts Higher Secondary with Commerce and Accountancy or specified subjects such as Commerce, Accountancy, Mathematics, Business Mathematics, Statistics, Computer Science, Corporate Secretaryship, Information Technology, Computer Applications or Computer Technology. A bridge course may be required for students without Commerce or Accountancy."
    ),
    (
        "What is BA English eligibility?",
        "BA English requires a pass in the +2 examination according to the official eligibility page."
    ),
    (
        "What is BA Tamil eligibility?",
        "BA Tamil requires a pass in Higher Secondary with Tamil as a language paper according to the official eligibility page."
    ),
    (
        "What is B.Sc Computer Science eligibility?",
        "B.Sc Computer Science requires Higher Secondary with Mathematics, or specified Computer Science/Computer Applications/IT/Computer Technology/Business Mathematics/Statistics subjects. A 15-day Mathematics bridge course may be required where applicable."
    ),
    (
        "What is B.Sc AI and Data Science eligibility?",
        "The official eligibility page lists Higher Secondary with Mathematics, or specified Computer Science/Computer Applications/IT/Computer Technology/Business Mathematics/Statistics subjects. A 15-day Mathematics bridge course may be required where applicable."
    ),
    (
        "What is B.Sc AI and Machine Learning eligibility?",
        "The official eligibility page lists Higher Secondary with Mathematics, or specified Computer Science/Computer Applications/IT/Computer Technology/Business Mathematics/Statistics subjects. A 15-day Mathematics bridge course may be required where applicable."
    ),
    (
        "What is B.Sc Microbiology eligibility?",
        "B.Sc Microbiology requires Higher Secondary with a biological science subject such as Botany, Zoology or Biology, subject to the university and government norms stated by the college."
    ),
    (
        "What is B.Sc Biochemistry eligibility?",
        "B.Sc Biochemistry requires Higher Secondary with Chemistry and Biology, or Chemistry with Botany and Zoology, or Biochemistry and Chemistry, according to the official eligibility page."
    ),
    (
        "What is B.Sc Clinical Laboratory Technology eligibility?",
        "B.Sc Clinical Laboratory Technology requires Higher Secondary with Chemistry and Biology, or Chemistry with Botany and Zoology, or Biochemistry and Chemistry, according to the official eligibility page."
    ),
    (
        "What is B.Sc Visual Communication eligibility?",
        "B.Sc Visual Communication requires a pass in Higher Secondary or an accepted equivalent qualification, including the eligibility route mentioned by the university."
    ),
    (
        "What is the eligibility for B.Sc Textile and Fashion Designing?",
        "The official eligibility page accepts Higher Secondary in regular academic or vocational stream from State Board, CBSE, ICSE or an accepted equivalent. A relevant three-year diploma can be eligible for direct second year subject to university conditions."
    ),

    # ============================================================
    # ADMISSION
    # ============================================================
    (
        "How can I apply to Excel College?",
        "Students can use the admission/enquiry facility on the official Excel website or contact the college for the current admission procedure and eligibility."
    ),
    (
        "How do I get admission in Excel College?",
        "Check the course eligibility first and then contact the Excel admission office or use the official online admission enquiry facility."
    ),
    (
        "Excel college admission epdi pandrathu?",
        "First course eligibility check pannunga. Apram official Excel admission enquiry facility use pannalaam or college admission office-a contact pannalaam."
    ),
    (
        "What documents are needed for admission?",
        "The exact documents can vary by programme and admission category. Students should check the current admission instructions and confirm with the college admission office before submitting originals."
    ),
    (
        "What is the Excel admission contact?",
        "For general Excel enquiries, the official website lists +91 99655 23999 and info@excelcolleges.com. Course-specific admission contacts should be confirmed with the college."
    ),
    (
        "Is online admission available?",
        "The official Excel website provides an online admission/enquiry facility. Students should use the current official admission page for the application process."
    ),

    # ============================================================
    # SCHOLARSHIPS
    # ============================================================
    (
        "What scholarships are available at Excel College?",
        "The official scholarship page lists PMS Minority, PMS ADTW for SC/ST/SCA, BC/MBC Scholarship, Pudhumai Penn, Tamil Pudhalvan, TN Uzhavan, SRET Scholarship and TART Scholarship."
    ),
    (
        "Excel college scholarship irukka?",
        "Yes. Excel College for Commerce and Science lists several government and institution-level scholarship schemes."
    ),
    (
        "What is PMS Minority scholarship?",
        "The college lists a PMS Minority Scholarship for eligible minority students. The official page gives eligibility, income and document requirements and directs applicants to the National Scholarship Portal."
    ),
    (
        "What is SC ST scholarship at Excel?",
        "The college lists PMS ADTW scholarship for eligible SC, ST and SCA students. Students should contact the college nodal officer and verify the current government requirements."
    ),
    (
        "Is BC MBC scholarship available?",
        "Yes. Excel College lists BC/MBC scholarship support for eligible students. Current eligibility and documents should be confirmed with the college nodal officer."
    ),
    (
        "What is Pudhumai Penn scholarship?",
        "The Excel scholarship page states that eligible girl students who studied Classes 6 to 12 in government schools or government model schools can receive Rs.1,000 per month until uninterrupted completion of eligible higher education, subject to the scheme rules."
    ),
    (
        "What is Tamil Pudhalvan scholarship?",
        "The Excel scholarship page states that eligible boys who studied Classes 6 to 12 in government schools or government model schools can receive Rs.1,000 per month until uninterrupted completion of eligible undergraduate degree, subject to scheme rules."
    ),
    (
        "What is SRET scholarship?",
        "Excel College lists SRET scholarship support based on HSC merit. The official page currently lists 100% HSC as Free, 90% and above as 50% fee concession, 75% and above as Rs.5,000, and 60% and above as Rs.3,000."
    ),
    (
        "What is TART scholarship?",
        "TART is the Talent Reward Test. The college lists scholarship amounts based on TART score: 75% and above Rs.5,000; 51-74% Rs.3,000; below 50% Rs.2,000."
    ),
    (
        "How do I apply for scholarship?",
        "Depending on the scholarship, students may apply through the relevant government portal or contact the Excel scholarship nodal officer. Check the current official scholarship instructions before applying."
    ),

    # ============================================================
    # PLACEMENT
    # ============================================================
    (
        "Does Excel College have placement?",
        "Yes. Excel College for Commerce and Science has a Training and Placement Cell that provides training and placement support."
    ),
    (
        "How is placement training at Excel?",
        "The placement cell provides training in domain-specific skills, communication, aptitude and personality development, along with placement support and industry-oriented training."
    ),
    (
        "When does placement training start?",
        "The official placement page says employability training begins from the first year and continues throughout the year."
    ),
    (
        "Who is the placement officer?",
        "The official placement contact page lists Dr. Yuvaraj as Placement Officer, Excel Group Institutions, with contact 9965579666."
    ),
    (
        "Who is the placement coordinator for Excel College for Commerce and Science?",
        "The official placement contact page lists Mrs. V. Aarthi as Training and Placement Coordinator. The listed contact is 9600851841."
    ),
    (
        "What is the placement email?",
        "The placement contact page lists eccsplacement@excelcolleges.com and aarthi.eccs@excelcolleges.com."
    ),
    (
        "What does the placement cell do?",
        "The placement cell identifies industry training needs, trains students, conducts Student Development Programmes and provides placement support."
    ),

    # ============================================================
    # FACILITIES
    # ============================================================
    (
        "What facilities are available at Excel College?",
        "Excel's official site lists facilities and student support areas including library, infrastructure facilities, general amenities, sports, hostel, clubs and societies, differently-abled student support and other campus services."
    ),
    (
        "Does Excel College have a library?",
        "Yes. Excel College for Commerce and Science has a library and the official website provides a dedicated library section."
    ),
    (
        "Does Excel College have hostel?",
        "Yes. The college provides hostel facilities. The official site lists separate accommodation for men and women and describes single, double and multi-occupancy options."
    ),
    (
        "Excel college hostel irukka?",
        "Aama, Excel College-la hostel facility irukku. Official information-la men and women-ku separate accommodation and different room occupancy options mention pannirukku."
    ),
    (
        "Does Excel have Wi-Fi?",
        "The official information for Excel's campus states that the campus has Wi-Fi-enabled IT infrastructure."
    ),
    (
        "Does Excel have cafeteria?",
        "Yes. Excel's official information lists cafeteria facilities on campus."
    ),
    (
        "Does Excel have ATM or banking facility?",
        "Yes. The official campus information lists on-campus banking facilities and ATMs."
    ),
    (
        "Does Excel have sports facilities?",
        "Yes. Sports facilities are listed by Excel, including playgrounds and courts."
    ),
    (
        "Does Excel have clubs and societies?",
        "Yes. The official site lists clubs and societies including NSS, RRC, YRC, Women Empowerment Cell, Citizen Consumer Club, Entrepreneurship Development Cell, Rotaract Club and Fine Arts Club."
    ),
    (
        "What student clubs are available?",
        "Listed student activities include NSS, Red Ribbon Club, Youth Red Cross, Women Empowerment Cell, Citizen Consumer Club, Entrepreneurship Development Cell, Rotaract Club and Fine Arts Club."
    ),
    (
        "Does Excel have medical support?",
        "Excel's campus information includes student support and health-related facilities. For a current medical or emergency contact, students should confirm with the college office."
    ),
    (
        "Is there support for differently-abled students?",
        "Yes. Excel College lists facilities and support for differently-abled students and an Equal Opportunity Cell."
    ),

    # ============================================================
    # STUDENT SUPPORT / CELLS
    # ============================================================
    (
        "What student support cells are available at Excel?",
        "The official site lists Anti-ragging Committee, Career Guidance Cell, Entrepreneurship Cell, Caste Discrimination Cell, Internal Compliance Committee, Differently-Abled Students Cell, Student Grievance Redressal Committee, Ombudsperson for Students' Grievances, Anti-Narcotic Committee, Discipline Committee, SC/ST/OBC Cell and Minority Cell."
    ),
    (
        "Does Excel have anti ragging committee?",
        "Yes. An Anti-ragging Committee is listed on the official college website."
    ),
    (
        "Does Excel have grievance redressal?",
        "Yes. Student Grievance Redressal Committee and an Ombudsperson for Students' Grievances are listed by the college."
    ),
    (
        "Does Excel have career guidance?",
        "Yes. Career Guidance Cell is listed among the college's non-statutory bodies."
    ),
    (
        "Does Excel have entrepreneurship cell?",
        "Yes. An Entrepreneurship Cell is listed."
    ),
    (
        "Does Excel have minority cell?",
        "Yes. A Minority Cell is listed."
    ),
    (
        "Does Excel have SC ST OBC cell?",
        "Yes. The official website lists an SC/ST/OBC Cell."
    ),

    # ============================================================
    # RULES / CAMPUS
    # ============================================================
    (
        "What is the dress code at Excel College?",
        "The college code of conduct says students are expected to follow a simple and modest dress code. It specifies formal dress requirements for boys and sari or salwar kameez/chudithar for girls, with additional restrictions on casual wear."
    ),
    (
        "Is ID card compulsory at Excel?",
        "Yes. The college code of conduct says students must wear and carry the photographic ID card on campus."
    ),
    (
        "Can students wear jeans in Excel College?",
        "The published code of conduct states that T-shirts, jeans and casual wear are not allowed."
    ),
    (
        "Can two wheelers enter the Excel campus?",
        "The published code of conduct states that two-wheelers and four-wheelers are not permitted to enter inside the college premises."
    ),
    (
        "What are the main campus rules?",
        "Students are expected to follow the dress code, carry their ID card, follow discipline rules and comply with the college code of conduct."
    ),

    # ============================================================
    # ACADEMICS / IQAC / EXAM
    # ============================================================
    (
        "Does Excel have IQAC?",
        "Yes. Excel College for Commerce and Science has an Internal Quality Assurance Cell (IQAC)."
    ),
    (
        "What is IQAC in Excel College?",
        "IQAC is the Internal Quality Assurance Cell. The college says it works on academic quality, evaluation, teaching-learning practices, research, accountability and continuous improvement."
    ),
    (
        "Does Excel have an exam cell?",
        "Yes. The official website has a dedicated Examination section covering exam cell information, internal assessment, results and related procedures."
    ),
    (
        "Where can I find Excel academic calendar?",
        "The official website provides an Academic Calendar section under Academics. Students should check the current calendar published by the college."
    ),
    (
        "Where can I find Excel syllabus?",
        "The official website provides Curriculum and Syllabus under the Academics section."
    ),

    # ============================================================
    # PRINCIPAL / ACADEMIC CONTACTS
    # ============================================================
    (
        "Who is the chairman of Excel Group Institutions?",
        "The official governing body page lists Prof. Dr. A. K. Natesan as Management Trustee and Chairman of Excel Group Institutions."
    ),
    (
        "Who is the vice chairman of Excel Group Institutions?",
        "The official governing body page lists Dr. N. Mathan Karthick as Vice-Chairman of Excel Group Institutions."
    ),
    (
        "Who is the executive director of Excel Group Institutions?",
        "The official governing body page lists Dr. K. Bommanna Raja as Executive Director, Excel Technical Campus."
    ),
    (
        "Who is the programme head of commerce?",
        "The official academic council page lists Dr. S. Subramaniam as Programme Head, School of Commerce."
    ),
    (
        "Who is the programme head of computer science?",
        "The official academic council page lists Dr. K. Munusamy as Programme Head, School of Computer Science."
    ),
    (
        "Who is the head of department of commerce?",
        "The academic council page lists Mr. T. Kumar as Head, Department of Commerce."
    ),
    (
        "Who is the head of department of business administration?",
        "The academic council page lists Mr. P. Varunkumar as Head, Department of Business Administration."
    ),
    (
        "Who is the head of data science cyber security and IT?",
        "The academic council page lists Mr. P. Dhineshkumar as Head, Department of Data Science, Cyber Security & Information Technology."
    ),

    # ============================================================
    # NATURAL QUESTIONS / COMMON CHAT
    # ============================================================
    (
        "Hi",
        "Hello! 👋 I am the Excel College AI Assistant. Ask me about courses, admission, eligibility, scholarships, hostel, facilities, placement or contact details."
    ),
    (
        "Hello",
        "Hello! 👋 I am the Excel College AI Assistant. How can I help you?"
    ),
    (
        "Hey",
        "Hey! 👋 Ask me anything about Excel College."
    ),
    (
        "Vanakkam",
        "Vanakkam! 🙏 Excel College pathi enna information venum?"
    ),
    (
        "Thanks",
        "You're welcome! 😊"
    ),
    (
        "Thank you",
        "You're welcome! 😊"
    ),
    (
        "Bye",
        "Bye! 👋 Have a great day!"
    ),
    (
        "What can you tell me?",
        "I can provide information about Excel Group Institutions, Excel College for Commerce and Science, courses, eligibility, admission, scholarships, hostel, facilities, student support, placement and contact details."
    ),
]

def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    cursor.execute("DELETE FROM faq")

    cursor.executemany(
        "INSERT INTO faq (question, answer) VALUES (?, ?)",
        data
    )

    connection.commit()
    connection.close()

    print(f"Database created successfully with {len(data)} FAQs!")


if __name__ == "__main__":
    create_database()
