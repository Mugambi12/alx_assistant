# models/chatbot.py

import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from models.responses import keyword_responses

# Define a custom tokenizer that tokenizes based on whitespace and punctuation
tokenizer = RegexpTokenizer(r'\w+|[^\w\s]')

# Define a set of stopwords
stop_words = set(stopwords.words('english'))

# Flag to track if the bot has already greeted in the current conversation
greeted = False

def process_message(user_message):
    global greeted
    user_message = user_message.lower()
    tokens = tokenizer.tokenize(user_message)

    # Remove stop words from the tokens
    tokens = [token for token in tokens if token not in stop_words]

    response = find_response(tokens)

    if response:
        return response
    else:
        return keyword_responses['unknown']

def find_response(tokens):
    # Join the tokens into a space-separated string
    user_message = ' '.join(tokens)

    # Use a regular expression to find the matching phrase
    for phrase, response in keyword_responses.items():
        if re.search(fr'\b{re.escape(phrase)}\b', user_message, re.IGNORECASE):
            return response

    return None
