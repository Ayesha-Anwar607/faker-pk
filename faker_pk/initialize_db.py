import sqlite3
import os

MALE_NAMES = [
    "Ahmed", "Muhammad", "Ali", "Hassan", "Hussain", "Bilal", "Hamza", "Umar", "Usman", "Abdullah",
    "Abdul Rehman", "Abdul Basit", "Abdul Hadi", "Abdul Wahab", "Abdul Samad", "Abdul Qadir", "Abdul Majeed",
    "Abdul Rauf", "Abdul Aziz","Abdul Kareem", "Abdul Aleem", "Abdul Ghaffar", "Abdul Ghani", "Abdul Haq", 
    "Abdul Shakoor", "Abdul Sattar", "Abdul Wasi", "Ahmad","Zeeshan", "Danish", "Faizan", "Fahad", 
    "Waleed", "Zain", "Saad", "Ahsan", "Adeel", "Asad","Arsalan", "Shahzaib", "Shehryar", "Salman",
    "Noman", "Omer", "Tahir", "Talha", "Kashif", "Kamran","Shahid", "Naveed", "Imran", "Junaid", "Farhan",
    "Faisal", "Khalid", "Raza", "Rizwan", "Adnan","Arif", "Yasir", "Irfan", "Zubair", "Shayan", "Sameer", "Umair",
    "Huzaifa", "Ayaan", "Rayyan","Azaan", "Areeb", "Raheel", "Sufyan", "Haris", "Anas", "Arham", "Asim", "Moiz", 
    "Ibtisam", "Saif", "Ilyas", "Ismail", "Ibrahim", "Eesa", "Musa", "Yousuf", "Dawood", "Yunus","Hashir",
    "Nuh", "Luqman", "Taimoor", "Murtaza", "Baqir", "Shahmeer", "Shaheer", "Daniyal", "Abdul Malik",
    "Zarar", "Zaryab", "Aafaq", "Abrar", "Adil", "Amaan", "Amjad", "Anees", "Anwar", "Aqeel",
    "Arqam", "Arsal", "Asghar", "Ashar", "Atif", "Awais", "Ayaz", "Azhar", "Azlan", "Barkat",
    "Basim", "Babar", "Burhan", "Ehtisham", "Ehsan", "Faraz", "Farid", "Fawad", "Feroz", "Ghazanfar",
    "Haider", "Hammad", "Hameed", "Hasan", "Haseeb", "Hashim", "Hisham","Adeel", "Huzaifah", "Ijaz", "Imad",
    "Inam", "Javed", "Kamal", "Khalil", "Khizar", "Mahad", "Mahir", "Mansoor", "Maaz", "Mazhar","Abdul Rahman",
    "Mehdi", "Muneeb", "Mustafa", "Naeem", "Nouman", "Qasim", "Rameez", "Rehan", "Sadiq", "Safeer",
    "Saifullah", "Sarfaraz", "Shahbaz", "Shafqat", "Shafiq", "Sharjeel", "Shehzad", "Sohail", "Subhan", "Sultan",
    "Tabish", "Talal", "Tauseef", "Tufail", "Ubaid", "Umer", "Usama", "Wajid", "Waqas", "Wasif",
    "Yasir", "Yawar", "Yameen", "Yasin", "Zakariya", "Zaman", "Zawwar", "Zia", "Zohaib", "Zubair",
    "Zain ul Abidin","Taha", "Irtaza", "Raza", "Ehtesham", "Mirza", "Azeem", "Saqib", "Shabbir",
    "Tahseen", "Salman", "Fahim", "Jawad", "Sarmad", "Nabeel", "Faiq", "Rashid", "Rahim", "Habib",
    "Munir", "Zameer", "Akram", "Zafar", "Wasim", "Nauman", "Nasir", "Khalil", "Jibran", "Kashan",
    "Adi", "Fakhir", "Sabtain", "Farooq", "Faiz", "Nisar", "Salman","Gohar","ghazangfar",
    "Rifat", "Tahmid", "Zohair", "Zaeem", "Sarmal", "Arsal", "Areez", "Sarim","Aoun",
    "Zayyan", "Razaq", "Asfar", "Affan", "Hanzala", "Hammad", "Ziyad", "Adeel",
    "Karim", "Qadeer", "Hanan", "Rameen", "Taha", "Shahroz", "Sameer", "Yasrab", "Ammar",
    "Shakir", "Rauf", "Danish", "Hamdaan", "Maher", "Uzair", "Shareef",
    "Zarrar", "Faris", "Azmat", "Riaz", "Munawwar", "Kaleem", "Sufyan", "Zameel", "Sajid", "Sarim",
    "Tabriz", "Yasin", "Attiq", "Zaid", "Murtaza", "Aneeb", "Moazzam",
    "Fida", "Najam", "Tauqeer", "Shakeel", "Najeeb", "Basit", "Faizan","Farhan", "Haris", "Ahsan", "Taimoor",  "Fahad", "Waris",
]

FEMALE_NAMES = [
    "Aliya", "Amna", "Anaya", "Anisa", "Asia", "Aasma", "Abida", "Adeela", "Adeelah",
    "Afifa", "Afsheen", "Hifza", "Afreen", "Aiman", "Aina", "Aiza", "Aleena",
    "Aleesha", "Aleeza", "Ayla", "Alishba", "Amal", "Ammara", "Amber", "Ameena", "Amira", "Anabia",
     "Anila", "Aniqa", "Anisa", "Anum", "Anusha", "Anzela", "Aqsa", "Arfa", "Arisha",
    "Urwa", "Asfa", "Asma", "Asmara", "Atiya", "Ayesha", "Ayra", "Azka",
    "Azra", "Bisma", "Batool", "Benish", "Bushra", "Dur-e-Fatima","Dur e Fishan", "Dua", "Ayman", "Esha",
    "Eiman","Erum", "Faiza", "Fakhra", "Falaq", "Falak",
    "Fariha", "Farwah", "Farzana", "Fatima", "Fauzia", "Fiza", "Ghazal", "Ghazala", "Gulnaz",
    "Mahrukh", "Habiba", "Hafsa", "Haleema", "Hania", "Hadia", "Hareem", "Haseena", "Hiba", "Hifza",
    "Hina", "Hira", "Humaira", "Humna", "Iffat", "Ifra", "Iqra",
    "Irum", "Isha", "Ishaal", "Eshwa", "Isra", "Jameela", "Javeria", "Jannat", "Yasmeen",
    "Jiya", "Kainat", "Khadija", "Khansa", "Kiran", "Komal", "Laiba", "Laila", "Laraib",
    "Lehna", "Lubna", "Mahira", "Mahjabeen", "Mahnoor", "Maha", "Maliha", "Maria",
    "Mariam", "Marwa","Maheen", "Mehak", "Mehr", "Mehwish", "Minal", "Mishal", "Misbah",
    "Mona", "Mubashira", "Muqaddas", "Meesha", "Nabeela", "Nadia", "Nafisa", "Naila", "Najma", "Natasha",
    "Naureen", "Nayyab", "Neha", "Nida", "Nimra", "Nishat", "Noreen", "Nosheen", "Nusrat","Faqiha",
    "Naima", "Zubaidah", "Parveen", "Qandeel", "Qurat tul Ain", "Rabiya", "Rabia", "Rafia", "Rafiya", "Rameen",
    "Rania", "Rozena", "Rashida", "Rida", "Rimsha", "Rizwana", "Soha", "Romana", "Roohi", "Ruba",
    "Rubina", "Rukhsar", "Rumaisa","Rumaisha","Rimsha", "Ruqayya", "Saba", "Sabeen", "Sabahat", "Sadia", "Sadra", "Sania",
     "Sahar", "Saira", "Saria","Sajida", "Sakina", "Salma", "Samina", "Samiya", "Sana", "Sanober","Sarah", "Sasha",
    "Subha", "Subhana", "Suhana", "Sumaira", "Sumaiya", "Sundus", "Tabinda", "Tabassum", "Taha", "Tahira",
    "Tahreem", "Tahirah", "Tania", "Tanisha", "Tanzeela", "Tayyaba", "Tehreem", "Tooba", "Ujala", "Umama","Umaima","Ajwa",
    "Umm e Habiba", "Umm e Hani", "Umm e Kulsoom", "Umm e Hani", "Umm e Rubab","Rutab","Rahaf", "Umm e Salma", "Urooj",
    "Urwa", "Uzma", "Wajiha","Wardah", "Yashma", "Yasmeen", "Yumna", "Zainab", "Zakia","Haram",
    "Zeenia", "Zahra", "Zaib", "Zakia", "Zeba","Zareen", "Zarish", "Zarmeen","Atfa","Tooba","Anshara","Zeba","Naina","Namal",
    "Zarqa", "Zartaj", "Zaryab", "Zehra", "Zeenat", "Zimal", "Zobia", "Zohra", "Farwa", "Farheen", "Gulshan",
    "Zonaira", "Zoya","Zoha", "Zubaida", "Zulekha", "Zunaisha","Adeeba", "Areeba","Fakhira", "Fariha", "Faryal",
    "Maheen", "Arooba","Bareera","Bushra", "Dania", "Dua", "Eshaal","Urwa","Uswa","Mawra","Shibrah","Haya",
    "Hajra", "Haleemah", "Hamna", "Huriya","Hurain","Nayarra", "Insha","Ishaal","Noor","Saffa","Minahil",
    "Jannat", "Kinza","Khizra","Saima","Madeeha","Maleeha","Komal","Shanza","Shanzay","Faiqa","Hareem","Gohar",
    "Laiba", "Laila", "Mehwish", "Maida", "Memoona", "Momina","Marjan", "Mehreen", "MehruNisa", "Minal",
     "Maira", "Naheed","Naveed", "Naila","Noshaba","Parveen", "Rabi", "Rafia", "Ramsha","Iraj","Rija","Reshma",
    "Aruba", "Rukhsana","Rehanna" , "Saba", "Sabiha","Nabeeha","Saeeda", "Sahar","Sameera", "Samra", "Samia",
]

LAST_NAMES = [
    "Abbasi", "Abbas", "Abid", "Afzal", "Ahmad","Akbar", "Akhter", "Alam", "Ali","Sethi","Anwar",
    "Amjad", "Anjum", "Ansari", "Arif", "Asad", "Ashfaq", "Asghar", "Aslam", "Atif", "Awan",
    "Azam", "Azhar", "Babar", "Baig", "Bajwa", "Bakht", "Baloch", "Bangash", "Basit", "Batool",
    "Bhatti", "Bukhari", "Butt", "Chaudhry", "Cheema", "Chishti", "Dar", "Danish", "Daud", "Deen",
    "Durrani", "Ejaz", "Fahim", "Faheem", "Farid", "Farooq", "Farrukh", "Fazal", "Feroz", "Ghafoor",
    "Ghani", "Ghazanfar", "Ghaznavi", "Ghauri", "Gohar", "Habib", "Hafeez", "Hafiz",
    "Haider", "Hameed", "Hamid", "Hanif", "Hashim", "Hasnain", "Hassan", "Hayat", "Hussain", "Hyder",
    "Iftikhar", "Ijaz", "Ilyas", "Imam", "Imran", "Inam", "Iqbal", "Irshad", "Ismail", "Ishaq",
    "Jahangir", "Jamal", "Jamali", "Jamshed", "Javed", "Jawad", "Kabir", "Qadir", "Kaleem",
    "Kamran", "Kamil", "Karim", "Kashif", "Kazmi", "Khalid", "Khalil", "Khan", "Khizar", "Khurram",
    "Latif", "Mahmood", "Malik", "Manzoor", "Masood", "Mazhar", "Mehmood", "Mir", "Mirza", "Moin",
    "Mohsin", "Moinuddin", "Monis", "Mubashir", "Mujeeb", "Mukhtar", "Munir", "Murad", "Mustafa", "Murtaza",
    "Nadeem", "Naeem", "Naseem", "Nasir", "Nawaz", "Niaz", "Noor", "Noman", "Numan", "Obaid",
    "Qadir", "Qaiser", "Qamar", "Qasim", "Qayyum", "Qureshi", "Rafiq", "Rafique", "Rahim", "Raja",
    "Rameez", "Rana", "Rasheed", "Rauf", "Raza", "Razzaq", "Rehman", "Riaz", "Rizwan",
    "Sabir", "Sadiq", "Safeer", "Shafi", "Saeed", "Shafiullah", "Sajid",  "Saleem", "Salman",
    "Sami", "Sarfaraz","Shafi", "Shafique", "Shahid", "Shakeel", "Sharif", "Shaukat", "Sheikh",
    "Shehzad", "Sheraz", "Shoukat", "Siddiq","Sadiq", "Siddique", "Sohail", "Suleman", "Sultan", "Tahir", "Talib",
    "Tariq", "Tufail", "Ubaid", "Umar", "Usman", "Waheed", "Wali", "Waseem", "Yaseen", "Yasin",
    "Yousaf", "Younas", "Zafar", "Zahid", "Zakir", "Zaman", "Zameer", 
    "Abbass", "Aftab", "Akram", "Alvi", "Ashraf", "Aziz", "Badar", "Bari", "Bashir",
    "Basharat", "Burhan", "Chughtai", "Zawar", "Ejaz", "Ehsan", "Faisal", "Farhan", "Fazal",
    "Gul", "Gulzar", "Haqqani", "Hashmi", "Hussaini", "Jalil", "Jamil", "Junaid", "Kabir",
    "Kamal", "Khawaja", "Khattak", "Kiani", "Khoso", "Khokhar", "Khosa", "Lodhi", "Mahmud",
    "Malook", "Mandokhel", "Memon", "Mughal", "Naqvi", "Naseer", "Niazi", "Orakzai", "Pirzada",
    "Qadri", "Qasmi", "Rashidi", "Saboor", "Sadaqat", "Sajjad", "Saleh", "Samiullah", "Sarwar", "Shafiullah",
    "Shah", "Shahbaz", "Shahzad", "Shams", "Sharafat", "Sharifuddin", "Sikandar", "Sohaib", "Subhan",
    "Tabassum", "Taha", "Talha", "Tanveer", "Tauqeer", "Tariq", "Wahid", "Wajid", "Waqas",
    "Yaseer", "Zaheer", "Zaman", "Zarrar", "Zeeshan", "Agha","Yousafzai", "Asmat", "Atta", "Baber", "Baloch", "Chohan",
    "Dasti", "Dogar",  "Gandapur", "Gill", "Gulshan", "Khatri",
    "Hingoro", "Hoti", "Jakhrani", "Jatoi", "Junejo", "Kalhoro", "Kakar", "Kashmiri", "Khoso",
    "Langah", "Laghari", "Liaqat", "Lodhi", "Mahsud", "Magsi", "Marwat", "Mashwani",
    "Mengal", "Mirani", "Naseeruddin", "Niazi","Qasoori","Warind",
    "Rajput", "Rind", "Samar", "Samad", "Sandhu", "Shahwani", "Sheerazi", "Sial",
    "Soomro", "Soomra", "Talpur", "Tanoli", "Tarin", "Tiwana", "Toor",
    "Turk", "Wazir", "Yusufzai", "Zehri", "Zuberi", "Kiyani", "Khakwani", "Taj", "Meer",
    "Mirwani", "Bhutta", "Randhawa", "Ghuman", "Gillani", "Naqash", "Abbassi", "Bohra", "Rajpoot",
    "Siddiqui", "Qaim", "Shuja", "Irfan"
]

BANKS_WITH_CODES = [
    ("Habib Bank", "HABB"),
    ("MCB Bank", "MUCB"),
    ("UBL", "UNIL"),
    ("Bank Alfalah", "ALFH"),
    ("Standard Chartered", "SCBL"),
    ("Allied Bank", "ABPA"),
    ("Meezan Bank", "MEZN"),
    ("Bank of Punjab", "BPUN")
]

SIM_PREFIXES = {
    "Jazz": ["300", "301", "302", "303", "304", "305", "306", "307", "308", "309", "320", "321", "322", "323", "324", "325"],
    "Zong": ["310", "311", "312", "313", "314", "315", "316", "317", "318", "319"],
    "Ufone": ["330", "331", "332", "333", "334", "335", "336", "337"],
    "Telenor": ["340", "341", "342", "343", "344", "345", "346", "347", "348", "349"]
}

CASTES = ["Sheikh", "Ansari", "Raja", "Malik", "Qureshi", "Chaudhry", "Jutt", "Butt", "Rajput", "Rana","Mahar"]
SECTS = ["Sunni", "Shia"]

# Province with City postcard
PROVINCE_CITIES = {
    "Punjab": [
        ("Lahore", 54000), ("Faisalabad", 38000), ("Rawalpindi", 46000), 
        ("Multan", 60000), ("Gujranwala", 52250), ("Sialkot", 51310), 
        ("Bahawalpur", 63100), ("Sargodha", 40100), ("Sahiwal", 57000), 
        ("Dera Ghazi Khan", 32200),("Rahim yar  khan",64200)
    ],
    "Sindh": [
        ("Karachi", 74000), ("Hyderabad", 71000), ("Sukkur", 65200), 
        ("Larkana", 77150), ("Mirpur Khas", 69000), ("Nawabshah", 67450), 
        ("Shikarpur", 64200), ("Khairpur", 66020), ("Jacobabad", 79000), 
        ("Thatta", 73130)
    ],
    "Khyber Pakhtunkhwa": [
        ("Peshawar", 25000), ("Mardan", 23200), ("Abbottabad", 22010), 
        ("Swat", 19130), ("Charsadda", 24420), ("Bannu", 28100), 
        ("Kohat", 26000), ("Dera Ismail Khan", 29050), ("Haripur", 22620), 
        ("Mansehra", 21300)
    ],
    "Balochistan": [
        ("Quetta", 87300), ("Gwadar", 91200), ("Sibi", 82000), 
        ("Khuzdar", 89100), ("Turbat", 92600), ("Chaman", 86000), 
        ("Zhob", 85200), ("Bela", 90150), ("Makran", 92500), 
        ("Pasni", 91300)
    ],
    "Gilgit Baltistan": [
        ("Gilgit", 15100), ("Skardu", 16100), ("Hunza", 15700), 
        ("Ghizer", 15200), ("Diamer", 14100), ("Astore", 14200), 
        ("Shigar", 16300), ("Kharmang", 16200)
    ],
    "Islamabad Capital Territory": [
        ("Islamabad", 44000)
    ]
}

INDUSTRIES_RANGES = [
    ("Information Technology", "IT", 50000, 250000),
    ("Finance", "Finance", 40000, 200000),
    ("Healthcare", "Healthcare", 30000, 180000),
    ("Education", "Education", 25000, 120000),
    ("Marketing & Media", "Marketing", 30000, 150000),
    ("Government / Public Sector", "Government", 25000, 120000),
    ("Engineering / Manufacturing", "Engineering", 35000, 180000),
    ("Hospitality / Retail", "Retail", 20000, 100000),
    ("Entrepreneur / Startup", "Entrepreneur", 50000, 300000),
    ("Legal / Consulting", "Consulting", 40000, 200000),
    ("Art & Entertainment", "Art", 25000, 200000),
    ("Politics", "Politics", 50000, 300000),
    ("Agriculture", "Agriculture", 15000, 80000),
    ("Domestic & Personal Services", "Services", 12000, 60000),
    ("Defense & Public Safety", "Defense", 30000, 150000)
]

JOB_TITLE_MAPPING = {
    "IT": [
        "Software Engineer", "Frontend Developer", "Backend Developer",
        "Full Stack Developer", "DevOps Engineer", "Data Scientist","Game Developer","AI Engineer","IOT Engineer",
        "Machine Learning Engineer", "AI Researcher", "Cybersecurity Engineer",
        "Cloud Solutions Architect", "Mobile App Developer", "Blockchain Developer",
        "QA / Test Engineer", "UI/UX Designer", "Network Engineer", "Database Administrator",
        "IT Support Specialist", "Systems Analyst","Cloud Engineer","Data Analyst","Data Engineer"
    ],
    "Finance": [
        "Accountant", "Auditor", "Financial Analyst", "Investment Analyst",
        "Tax Consultant", "Risk Manager", "Credit Analyst", "Loan Officer",
        "Treasury Manager", "Financial Controller","CA","CFO"
    ],
    "Healthcare": [
        "Doctor", "Nurse", "Pharmacist", "Lab Technician", "Radiologist","Cardiologist","Gynecologist","Dermatologist","Cosmetologist",
        "Medical Researcher", "Physiotherapist", "Dietitian", "Surgeon", "Psychologist","Oncologist","Pediatrician","Orthopedic Surgeon"
    ],
    "Education": [
        "Teacher", "Lecturer", "Associate Professor","Assistant Professor","Teaching Assistant(TA)", "Research Associate",
        "Academic Coordinator", "Curriculum Designer", "Educational Consultant"
    ],
    "Marketing": [
        "Graphic Designer", "Content Writer", "Copywriter", "Video Editor",
        "Animator", "Photographer", "Digital Marketing Specialist","Social Media Influencer", "SEO Specialist",
        "Social Media Manager", "Art Director", "Marketing Manager", "Sales Executive"
    ],
    "Government": [
        "Civil Servant", "Policy Analyst", "Administrative Officer","Public Relations Officer", "Intelligence Analyst",
        "Diplomat", "Law Enforcement Officer", "Urban Planner","Public Health Administrator","Emergency Management Specialist"
    ],
    "Engineering": [
        "Civil Engineer", "Mechanical Engineer", "Electrical Engineer",
        "Chemical Engineer", "Industrial Engineer", "Production Manager",
        "Quality Assurance Engineer","Environmental Engineer","Aerospace Engineer"
    ],
    "Retail": [
        "Hotel Manager", "Chef", "Waiter", "Waitress", "Store Manager","Product Manager", 
        "Sales Associate", "Customer Service Representative","Event Manager", "Tour Guide", "Travel Agent",
    ],
    "Entrepreneur": [
        "Entrepreneur", "Startup Founder", "Business Development Manager",
        "Operations Manager", "Strategy Analyst", "Consultant","Investor Relations Manager", "Venture Capitalist"
    ],
    "Consulting": [
        "Legal Advisor", "Lawyer", "Advocate", "Compliance Officer", "Consultant","Business Analyst",
          "Management Consultant", "Strategy Consultant"
    ],
     "Art": [
        "Painter", "Dancer", "Singer", "Actor", "Interior Designer","Event Planner", "Makeup Artist","Sketcher","Home Decorator",
        "Sculptor", "Musician", "Choreographer", "Director", "Photographer","Fashion Designer","Cinematographer","Illustrator","UI/UX Designer"
        ],
    "Politics": [
        "Politician", "Member of National Assembly", "Senator","Governor",
        "Minister", "Mayor", "Councillor", "Campaign Manager", "Political Consultant"
    ],
    "Agriculture": [
        "Farmer", "Farm Manager", "Tractor Driver", "Agronomist", 
        "Dairy Farmer", "Harvesting Worker", "Irrigation Specialist","Agricultural Engineer", "Livestock Specialist"
    ],
    "Services": [
        "Housekeeper", "Maid", "Private Driver", "Gardener", "Plumber", "Electrician","Carpenter","Miner","Welder","Mechanic",
        "Security Guard", "Cook", "Nanny / Babysitter", "Caregiver", "Personal Assistant", "Laundry Worker","Driver"
    ],
    "Defense": [
        "Soldier", "Army Captain", "Police Officer", "Sub-Inspector", 
        "Firefighter", "Security Officer", "Rescue Warden", "Paramedic",
        "Civil Defense Officer", "Emergency Medical Technician (EMT)",
    ]
}

COMPANY_INDUSTRIES = {
    # 1. Information Technology (IT)
    "Systems Limited": "IT",
    "NetSol Technologies": "IT",
    "Folio3 Software": "IT",
    "Contour Software": "IT",
    "NexGen Digital Solutions": "IT",

    # 2. Finance
    "Habib Metropolitan Financials": "Finance",
    "Pakistan Stock Exchange": "Finance",
    "Lakson Investments": "Finance",
    "JS Bank Limited": "Finance",
    "Alfalah Capital": "Finance",

    # 3. Healthcare
    "Shaukat Khanum Hospital": "Healthcare",
    "Aga Khan University Hospital": "Healthcare",
    "Chughtai Lab": "Healthcare",
    "Indus Hospital Network": "Healthcare",
    "Getz Pharma": "Healthcare",

    # 4. Education
    "Beaconhouse School System": "Education",
    "The City School": "Education",
    "Roots Millennium Schools": "Education",
    "KIPS Academy": "Education",
    "NUST University": "Education",

    # 5. Marketing & Media
    "Symmetry Group": "Marketing",
    "Brainchild Communications": "Marketing",
    "Adcom Leo Burnett": "Marketing",
    "Interflow Communications": "Marketing",
    "Red Communication Arts": "Marketing",

    # 6. Government / Public Sector
    "Federal Board of Revenue (FBR)": "Government",
    "NADRA Pakistan": "Government",
    "Pakistan Post": "Government",
    "WAPDA Pakistan": "Government",
    "Capital Development Authority (CDA)": "Government",

    # 7. Engineering & Manufacturing
    "Indus Motor Company (Toyota)": "Engineering",
    "Pak Suzuki Motor Company": "Engineering",
    "Descon Engineering": "Engineering",
    "Lucky Cement Limited": "Engineering",
    "Pak Arab Refinery (PARCO)": "Engineering",

    # 8. Hospitality / Retail
    "Imtiaz Super Market": "Retail",
    "Metro Cash & Carry Pakistan": "Retail",
    "Al-Fatah Department Store": "Retail",
    "Khaadi Retail": "Retail",
    "Pearl Continental Hotels": "Retail",

    # 9. Entrepreneur / Startup
    "Bazaar Technologies": "Entrepreneur",
    "Dastgyr Technologies": "Entrepreneur",
    "Jugnu Startup Labs": "Entrepreneur",
    "Retailo Pakistan": "Entrepreneur",
    "SastaTicket.pk": "Entrepreneur",

    # 10. Legal / Consulting
    "A.F. Ferguson & Co. (PwC)": "Consulting",
    "Abacus Consulting": "Consulting",
    "KPMG Taseer Hadi": "Consulting",
    "EY Ford Rhodes": "Consulting",
    "BDO Ebrahim & Co.": "Consulting",

    # 11. Art & Entertainment
    "Canvas Art Gallery": "Art",
    "National College of Arts (NCA)": "Art",
    "Coke Studio Pakistan": "Art",
    "Ajoka Theatre Group": "Art",
    "Ghazal Harmonies Studio": "Art",

    # 12. Politics
    "Senate Secretariat": "Politics",
    "National Assembly of Pakistan": "Politics",
    "Policy Research Institute (PRIP)": "Politics",
    "Citizens Coalition for Reforms": "Politics",
    "Election Commission of Pakistan": "Politics",

    # 13. Agriculture
    "Fauji Fertilizer Company (FFC)": "Agriculture",
    "Engro Fertilizers": "Agriculture",
    "Green Punjab Agri Farms": "Agriculture",
    "Sindh Seed Corporation": "Agriculture",
    "Zarai Taraqiati Bank (ZTBL)": "Agriculture",

    # 14. Domestic & Personal Services
    "Domestic Ease Services": "Services",
    "Lahore Security Services": "Services",
    "Pak Plumbers & Electricians Network": "Services",
    "Care & Cleaning Pakistan": "Services",
    "Safe Hands Nanny Agency": "Services",

    # 15. Defense & Public Safety
    "Pakistan Army": "Defense",
    "Punjab Police Department": "Defense",
    "Sindh Police Department": "Defense",
    "Rescue 1122": "Defense",
    "Civil Defense Department": "Defense",
    "Fauji Security Services": "Defense"
}

COMPANIES = list(COMPANY_INDUSTRIES.keys())

INSTITUTIONS = [
    # Universities — Punjab
    ("University of the Punjab", "university", "Lahore"),
    ("UCP - University of Central Punjab", "university", "Lahore"),
    ("LUMS", "university", "Lahore"),
    ("UET Lahore", "university", "Lahore"),
    ("COMSATS Lahore", "university", "Lahore"),
    ("GCU Lahore", "university", "Lahore"),
    ("BZU Multan", "university", "Multan"),
    ("NTU Faisalabad", "university", "Faisalabad"),

    # Universities — Sindh
    ("University of Karachi", "university", "Karachi"),
    ("NED University", "university", "Karachi"),
    ("IBA Karachi", "university", "Karachi"),
    ("SZABIST Karachi", "university", "Karachi"),
    ("University of Sindh", "university", "Hyderabad"),

    # Universities — KPK
    ("AWKUM - Abdul Wali Khan University", "university", "Peshawar"),
    ("University of Peshawar", "university", "Peshawar"),
    ("COMSATS Abbottabad", "university", "Abbottabad"),
    ("Islamia College University", "university", "Peshawar"),

    # Universities — Islamabad
    ("NUST", "university", "Islamabad"),
    ("COMSATS Islamabad", "university", "Islamabad"),
    ("IIUI - International Islamic University", "university", "Islamabad"),
    ("Quaid-i-Azam University", "university", "Islamabad"),
    ("Air University", "university", "Islamabad"),
    ("FAST-NUCES Islamabad", "university", "Islamabad"),

    # Universities — Balochistan
    ("University of Balochistan", "university", "Quetta"),
    ("BUITEMS", "university", "Quetta"),

    # Colleges — Punjab
    ("Government College Lahore", "college", "Lahore"),
    ("Forman Christian College", "college", "Lahore"),
    ("Punjab College Faisalabad", "college", "Faisalabad"),
    ("Superior College Multan", "college", "Multan"),

    # Colleges — Sindh
    ("DJ Sindh Government Science College", "college", "Karachi"),
    ("Adamjee Government Science College", "college", "Karachi"),

    # Colleges — KPK
    ("Edwardes College Peshawar", "college", "Peshawar"),
    ("Islamia College Peshawar", "college", "Peshawar"),

    # Colleges — Islamabad
    ("F.G. Sir Syed College", "college", "Islamabad"),
    ("Islamabad Model College", "college", "Islamabad"),

    # Schools — spread across cities
    ("Beaconhouse School", "school", "Lahore"),
    ("The City School", "school", "Karachi"),
    ("Roots Millennium", "school", "Islamabad"),
    ("Froebel's International", "school", "Islamabad"),
    ("Aitchison College", "school", "Lahore"),
    ("Karachi Grammar School", "school", "Karachi"),
    ("Peshawar Model School", "school", "Peshawar"),
    ("Army Public School Rawalpindi", "school", "Rawalpindi"),
]


def initialize_database(db_path: str) -> None:
    """Creates the schema and populates the SQLite database with all fake data records."""
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()

        # Create Schema
        cursor.execute("DROP TABLE IF EXISTS industries")
        cursor.execute("""
            CREATE TABLE industries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                code TEXT NOT NULL UNIQUE,
                min_salary INTEGER NOT NULL,
                max_salary INTEGER NOT NULL
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS job_titles")
        cursor.execute("""
            CREATE TABLE job_titles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                industry_code TEXT NOT NULL,
                FOREIGN KEY (industry_code) REFERENCES industries(code)
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS companies")
        cursor.execute("""
            CREATE TABLE companies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                industry_code TEXT,
                FOREIGN KEY (industry_code) REFERENCES industries(code)
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS locations")
        cursor.execute("""
            CREATE TABLE locations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL UNIQUE,
                province TEXT NOT NULL,
                postal_code INTEGER NOT NULL
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS names")
        cursor.execute("""
            CREATE TABLE names (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS sim_providers")
        cursor.execute("""
            CREATE TABLE sim_providers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS sim_prefixes")
        cursor.execute("""
            CREATE TABLE sim_prefixes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                provider_name TEXT NOT NULL,
                prefix TEXT NOT NULL UNIQUE,
                FOREIGN KEY (provider_name) REFERENCES sim_providers(name)
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS castes")
        cursor.execute("""
            CREATE TABLE castes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS sects")
        cursor.execute("""
            CREATE TABLE sects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS banks")
        cursor.execute("""
            CREATE TABLE banks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                iban_code TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("DROP TABLE IF EXISTS institutions")
        cursor.execute("""
            CREATE TABLE institutions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                city TEXT NOT NULL,
                FOREIGN KEY (city) REFERENCES locations(city)
            )
        """)

        # Insert Data
        # 1. Industries
        cursor.executemany(
            "INSERT INTO industries (name, code, min_salary, max_salary) VALUES (?, ?, ?, ?)",
            INDUSTRIES_RANGES
        )

        # 2. Job Titles
        job_titles_data = []
        for code, titles in JOB_TITLE_MAPPING.items():
            for title in titles:
                job_titles_data.append((title, code))
        cursor.executemany("INSERT INTO job_titles (title, industry_code) VALUES (?, ?)", job_titles_data)

        # 3. Companies
        companies_data = [(name, code) for name, code in COMPANY_INDUSTRIES.items()]
        cursor.executemany("INSERT INTO companies (name, industry_code) VALUES (?, ?)", companies_data)

        # 4. Locations
        locations_data = []
        for province, cities in PROVINCE_CITIES.items():
            for city, code in cities:
                locations_data.append((city, province, code))
        cursor.executemany("INSERT INTO locations (city, province, postal_code) VALUES (?, ?, ?)", locations_data)

        names_data = (
            [(name, 'male')   for name in MALE_NAMES] +
            [(name, 'female') for name in FEMALE_NAMES] +
            [(name, 'last')   for name in LAST_NAMES]
        )
        cursor.executemany("INSERT INTO names (name, type) VALUES (?, ?)", names_data)
        
        # 6. SIM Providers and Prefixes
        providers_data = [(provider,) for provider in SIM_PREFIXES.keys()]
        cursor.executemany("INSERT INTO sim_providers (name) VALUES (?)", providers_data)

        prefixes_data = []
        for provider, prefixes in SIM_PREFIXES.items():
            for prefix in prefixes:
                prefixes_data.append((provider, prefix))
        cursor.executemany("INSERT INTO sim_prefixes (provider_name, prefix) VALUES (?, ?)", prefixes_data)

        # 7. Castes
        castes_data = [(caste,) for caste in CASTES]
        cursor.executemany("INSERT INTO castes (name) VALUES (?)", castes_data)

        # 8. Sects
        sects_data = [(sect,) for sect in SECTS]
        cursor.executemany("INSERT INTO sects (name) VALUES (?)", sects_data)

        # 9. Banks
        cursor.executemany("INSERT INTO banks (name, iban_code) VALUES (?, ?)", BANKS_WITH_CODES)

        #10. Institutions
        cursor.executemany(
            "INSERT INTO institutions (name, type, city) VALUES (?, ?, ?)",
            INSTITUTIONS
        )
            

        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    db_file = os.path.join(os.path.dirname(__file__), "faker_pk.db")
    initialize_database(db_file)
    print("Database successfully initialized!")