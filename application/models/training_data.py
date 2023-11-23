# models/training_data.py

class Responses:
    # Define courses
    courses = {
        'AWS Cloud Computing, ',
        'Data Analytics, ',
        'Salesforce Administrator, ',
        'Software Engineering Plus, ',
        'Intro To Software Engineering, '
    }

    # Define responses for specific questions
    responses = {
        'asking_about_courses': "Here are some popular courses:\n" + "\n".join(courses),
        'enrolling': "You are now enrolled in the course: {}",
        'no_course_found': "Sorry, I couldn't find that course.",
        'about_school': "Our school offers a variety of courses including:\n" + "\n".join(courses),
        'hello_greeting': "Hello! How can I assist you today?",
        'hey_greeting': "Hey! How can I assist you today?",
        'hi_greeting': "Hi! How can I assist you today?",
        'help': "You can ask me about available courses or enroll in a specific course.",
        'admissions': "ALX offers admissions for various programs. You can find more information on our website.",
        'events': "ALX hosts events to connect professionals and foster innovation. Check our blog for updates.",
        'programs': "ALX offers programs in AWS Cloud Computing, Data Analytics, Salesforce, Software Engineering, and Intro To Software Engineering.",
        'blog': "Our blog features career tips, tech insights, spotlights on talent, and stories from our ALX community across Africa.",
        'about_alx': "ALX offers job-ready training in the tech fields employers need most. ALX, in partnership with The ROOM, is brought to you by the organization that leads African Leadership Academy, African Leadership University, and Anzisha Prize Foundation.",
        'selection_process': "The ALX Selection Process is a two-step online process. First applicants will be required to complete a registration form which will take a few minutes to complete. Once this has been submitted, applicants will be directed to our online application platform. The application will take approximately 90 mins to complete and consists of three sections; including an English proficiency test. Applicants will also receive access to the online application via email. Your link to the application is personal and therefore cannot be shared.",
        'payment_terms': "Find out about our available payment terms and options here. Eligible candidates can apply directly for sponsored placements in the program here.",
        'skills_for_se': "Becoming a successful software engineer requires a combination of technical expertise, such as proficiency in programming, and non-technical skills, such as creativity, problem-solving, teamwork, adaptability, and communication.",
        'subjects_for_se': "Computing and IT are the most important subjects to study, but other technical subjects like physics and design technology may also be useful.",
        'after_program': "All ALX learners are invited to join The ROOM Fellowship community where you will have access to a global network of resources, job opportunities, and ongoing career support.",
        'se_vs_se_plus': "The ALX Software Engineering Plus Program includes the highly rated 3-month ALX Foundations module, preparing learners with the crucial soft skills expected by global employers prior to starting their technical program.",
        'hubs': "Attending the in-person hubs is a benefit of the ALX learning experience. The in-person co-working spaces are designed to provide accountability, peer support, and the opportunity for face-to-face interaction and networking. This is intended to boost productivity and help individuals achieve their goals.",
        'contact_alx': "Please ask LEA our Learning Experience Assistant for more information and answers to any additional questions.",
        'sponsored_place': "Learners who do not meet the country of origin or age requirements for sponsored placements have the option to pay for the program, or apply for our ALX Global programs. ALX Global programs are offered at a reduced time and rate, however will not include the foundation modules or offer access to any of our in-person, community, or hub activations.",
        'multiple_programs': "Due to training requirements and program rigor, ALX permits learners to be enrolled in one program at any given time. If you have applied to or are currently enrolled in a program, you will not be eligible to apply to another program.",
        'unknown': "I'm sorry, I didn't understand that. Type 'help' for assistance."
    }
