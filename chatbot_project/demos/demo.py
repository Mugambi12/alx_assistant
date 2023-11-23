import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer

# Download NLTK data
nltk.download('punkt')

# Define courses
courses = {
    'AWS Cloud Computing, ',
    'Data Analytics, ',
    'Salesforce Administrator, ',
    'Software Engineering Plus, ',
    'Intro To Software Engineering, '
}

# Flag to track if the bot has already greeted in the current conversation
greeted = False

# Define a custom tokenizer that tokenizes based on whitespace and punctuation
tokenizer = RegexpTokenizer(r'\w+|[^\w\s]')

def process_message(user_message):
    global greeted

    if not user_message.strip() and not greeted:
        greeted = True
        return "Welcome! How can I assist you today?"

    tokens = tokenizer.tokenize(user_message.lower())

    # Initialize variables for specific questions
    asking_about_courses = False
    enrolling = False

    for token in tokens:
        if 'courses' in token or 'course' in token:
            asking_about_courses = True

        if token == 'enroll':
            enrolling = True

    # Conditions based on specific questions
    if asking_about_courses:
        response = "Here are some popular courses:\n"

        for course in courses:
            response += f"{course}\n"
        return response

    if enrolling:
        for token in tokens:
            if token in courses.keys():
                return f"You are now enrolled in the course: {courses[token]}"
        return "Sorry, I couldn't find that course."

    if 'school' in tokens or 'education' in tokens:
        response = "Our school offers a variety of courses including:\n"
        response += '\n'.join([f'{value}' for value in courses.values()])
        return response

    if 'hello' in tokens:
        return "Hello! How can I assist you today?"

    if 'hi' in tokens:
        return "Hi! How can I assist you today?"

    if 'hey' in tokens:
        return "Hey! How can I assist you today?"

    if 'help' in tokens or 'assistance' in tokens:
        return "You can ask me about available courses or enroll in a specific course."

    if 'admissions' in tokens:
        return "ALX offers admissions for various programs. You can find more information on our website."

    if 'events' in tokens:
        return "ALX hosts events to connect professionals and foster innovation. Check our blog for updates."

    if 'programs' in tokens:
        return "ALX offers programs in AWS Cloud Computing, Data Analytics, Salesforce, and Software Engineering."

    if 'blog' in tokens:
        return "Our blog features career tips, tech insights, spotlights on talent, and stories from our ALX community across Africa."

    if any(keyword in user_message.lower() for keyword in ['what is alx?', 'who is alx?', 'alx', 'alx africa', 'alx_africa']):
        return "ALX offers job-ready training in the tech fields employers need most. ALX, in partnership with The ROOM, is brought to you by the organisation that leads African Leadership Academy, African Leadership University, and Anzisha Prize Foundation."

    if any(keyword in user_message.lower() for keyword in ['what is your selection process like', 'selection process', 'admission process']):
        return "The ALX Selection Process is a two-step online process. First applicants will be required to complete a registration form which will take a few minutes to complete. Once this has been submitted, applicants will be directed to our online application platform. The application will take approximately 90 mins to complete and consists of three sections; including an English proficiency test. Applicants will also receive access to the online application via email. Your link to the application is personal and therefore cannot be shared."

    if 'what are the payment terms and options?' in user_message.lower():
        return "Find out about our available payment terms and options here. Eligible candidates can apply directly for sponsored placements in the programme here."

    if 'what skills do i need to become a software engineer?' in user_message.lower():
        return "Becoming a successful software engineer requires a combination of technical expertise, such as proficiency in programming, and non-technical skills, such as creativity, problem-solving, teamwork, adaptability, and communication."

    if 'what subjects do software engineers study?' in user_message.lower():
        return "Computing and IT are the most important subjects to study, but other technical subjects like physics and design technology may also be useful."

    if 'what happens after my programme ends and i need to find a job?' in user_message.lower():
        return "All ALX learners are invited to join The ROOM Fellowship community where you will have access to a global network of resources, job opportunities, and ongoing career support."

    if 'what is the difference between software engineering and software engineering plus?' in user_message.lower():
        return "The ALX Software Engineering Plus Programme includes the highly rated 3-month ALX Foundations module, preparing learners with the crucial soft skills expected by global employers prior to starting their technical programme."

    if 'am i able to go to the hubs?' in user_message.lower():
        return "Attending the in-person hubs is a benefit of the ALX learning experience. The in-person co-working spaces are designed to provide accountability, peer support, and the opportunity for face-to-face interaction and networking. This is intended to boost productivity and help individuals achieve their goals."

    if 'how can i get in touch with alx africa to answer the questions i have?' in user_message.lower():
        return "Please ask LEA our Learning Experience Assistant for more information and answers to any additional questions."

    if 'if i don’t meet the age and origin requirements, can i still apply for a sponsored place?' in user_message.lower():
        return "Learners who do not meet the country of origin or age requirements for sponsored placements have the option to pay for the programme, or apply for our ALX Global programmes. ALX Global programmes are offered at reduced time and rate, however will not include the foundation modules or offer access to any of our in-person, community or hub activations."

    if 'can i register for multiple programmes at the same time?' in user_message.lower():
        return "Due to training requirements and programme rigour, ALX permits learners to be enrolled in one programme at any given time. If you have applied to or are currently enrolled in a programme, you will not be eligible to apply to another programme."

    return "I'm sorry, I didn't understand that. Type 'help' for assistance."


























import requests
from bs4 import BeautifulSoup

url = "https://www.alxafrica.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

program_names = [program.text for program in soup.find_all("h3", class_="program-name")]

print(program_names)
