responses = [
    "if any(keyword in user_message.lower() for keyword in ['what is alx?', 'who is alx?', 'alx', 'alx africa', 'alx_africa']):\n        return \"ALX offers job-ready training in the tech fields employers need most. ALX, in partnership with The ROOM, is brought to you by the organisation that leads African Leadership Academy, African Leadership University, and Anzisha Prize Foundation.\"",

    "if any(keyword in user_message.lower() for keyword in ['what is your selection process like', 'selection process', 'admission process']):\n        return \"The ALX Selection Process is a two-step online process. First applicants will be required to complete a registration form which will take a few minutes to complete. Once this has been submitted, applicants will be directed to our online application platform. The application will take approximately 90 mins to complete and consists of three sections; including an English proficiency test. Applicants will also receive access to the online application via email. Your link to the application is personal and therefore cannot be shared.\"",

    "if 'what are the payment terms and options?' in user_message.lower():\n        return \"Find out about our available payment terms and options here. Eligible candidates can apply directly for sponsored placements in the programme here.\"",

    "if 'what skills do i need to become a software engineer?' in user_message.lower():\n        return \"Becoming a successful software engineer requires a combination of technical expertise, such as proficiency in programming, and non-technical skills, such as creativity, problem-solving, teamwork, adaptability, and communication.\"",

    "if 'what subjects do software engineers study?' in user_message.lower():\n        return \"Computing and IT are the most important subjects to study, but other technical subjects like physics and design technology may also be useful.\"",

    "if 'what happens after my programme ends and i need to find a job?' in user_message.lower():\n        return \"All ALX learners are invited to join The ROOM Fellowship community where you will have access to a global network of resources, job opportunities, and ongoing career support.\"",

    "if 'what is the difference between software engineering and software engineering plus?' in user_message.lower():\n        return \"The ALX Software Engineering Plus Programme includes the highly rated 3-month ALX Foundations module, preparing learners with the crucial soft skills expected by global employers prior to starting their technical programme.\"",

    "if 'am i able to go to the hubs?' in user_message.lower():\n        return \"Attending the in-person hubs is a benefit of the ALX learning experience. The in-person co-working spaces are designed to provide accountability, peer support, and the opportunity for face-to-face interaction and networking. This is intended to boost productivity and help individuals achieve their goals.\"",

    "if 'how can i get in touch with alx africa to answer the questions i have?' in user_message.lower():\n        return \"Please ask LEA our Learning Experience Assistant for more information and answers to any additional questions.\"",
]
