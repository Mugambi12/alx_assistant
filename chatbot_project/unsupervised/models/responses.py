class Responses:
    def __init__(self):
        self.responses = {
            'courses': "Here are some popular courses:\nAWS Cloud Computing, Data Analytics, Salesforce Administrator, Software Engineering Plus, Intro To Software Engineering",
            'enroll': "You can enroll in a course by visiting our website and following the enrollment process.",
            'selection_process': "The ALX Selection Process is a two-step online process...",
            'admissions': "ALX offers admissions for various programs. You can find more information on our website.",
            'payment_terms': "Find out about our available payment terms and options here. Eligible candidates can apply directly for sponsored placements in the programme here.",
            'skills_software_engineer': "Becoming a successful software engineer requires a combination of technical expertise, such as proficiency in programming, and non-technical skills, such as creativity, problem-solving, teamwork, adaptability, and communication.",
            'subjects_software_engineer': "Computing and IT are the most important subjects to study, but other technical subjects like physics and design technology may also be useful.",
            'after_program_ends': "All ALX learners are invited to join The ROOM Fellowship community where you will have access to a global network of resources, job opportunities, and ongoing career support.",
            'difference_programs': "The ALX Software Engineering Plus Programme includes the highly rated 3-month ALX Foundations module, preparing learners with the crucial soft skills expected by global employers prior to starting their technical programme.",
            'go_to_hubs': "Attending the in-person hubs is a benefit of the ALX learning experience. The in-person co-working spaces are designed to provide accountability, peer support, and the opportunity for face-to-face interaction and networking. This is intended to boost productivity and help individuals achieve their goals.",
            'get_in_touch_alx': "Please ask LEA our Learning Experience Assistant for more information and answers to any additional questions.",
            'age_origin_requirements': "Learners who do not meet the country of origin or age requirements for sponsored placements have the option to pay for the programme, or apply for our ALX Global programmes. ALX Global programmes are offered at reduced time and rate, however will not include the foundation modules or offer access to any of our in-person, community or hub activations.",
            'register_multiple_programs': "Due to training requirements and programme rigour, ALX permits learners to be enrolled in one programme at any given time. If you have applied to or are currently enrolled in a programme, you will not be eligible to apply to another programme."
        }

    def get_response(self, user_message):
        for keyword, response in self.responses.items():
            if keyword.lower() in user_message.lower():
                return response
        return "I'm not sure I understand. Can you please rephrase?"
