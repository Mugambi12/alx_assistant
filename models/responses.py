# models/responses.py

import json
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Build the full path to responses.json
responses_path = os.path.join(current_dir, 'responses.json')

# Load responses from responses.json
with open(responses_path, 'r') as file:
    responses = json.load(file)

# Define keywords and corresponding responses
keyword_responses = {
    **responses['greetings'],
    **responses['general_information'],
    **responses['school_information'],
    **responses['application_and_selection_process'],
    **responses['payment_and_financing'],
    **responses['se_skills_and_subjects'],
    **responses['post_program_opportunities'],
    **responses['software_engineering_program'],
    **responses['software_engineering_plus_program'],
    **responses['in-person_hubs'],
    **responses['contact_information'],
    **responses['sponsored_placements_and_multiple_programs'],
}
