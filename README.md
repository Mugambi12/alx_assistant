# ALXAssist

ALXAssist is a web application that combines a chatbot with weather information retrieval functionality. This application is designed to provide users with a seamless experience when seeking information about courses and current weather conditions. It is particularly useful for individuals interested in technology-related courses and staying updated with local weather forecasts.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Testing](#testing)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

ALXAssist serves as a comprehensive platform for users to interact with a chatbot for course-related queries and obtain real-time weather information for specific cities. The application leverages Python's Flask framework for server-side operations and incorporates HTML, CSS, and JavaScript for the frontend interface.

## Features

- **Chatbot Interface**:
  - Users can interact with the chatbot to inquire about available courses, enrollment procedures, and other educational details.
  - The chatbot is equipped with natural language processing capabilities to understand and respond to user queries effectively.

- **Weather Information**:
  - Users can retrieve current weather conditions for a specified city.
  - The application provides temperature information in both Celsius and Fahrenheit formats, along with personalized recommendations based on weather conditions.

- **Responsive Design**:
  - The user interface is designed to be mobile-friendly, ensuring a seamless experience on various devices.

## Project Structure

- **static/**
    - **css/**
        - `chatbot.css`: Contains styling for the chatbot interface.
        - `weather.css`: Contains styling for the weather information section.
    - **js/**
        - `chatbot.js`: Handles client-side interactions for the chatbot.
        - `weather.js`: Manages client-side interactions related to weather information.
- **templates/**
    - `index.html`: Main page template that integrates chatbot, weather, and navbar templates.
    - `chatbot.html`: Template for the chatbot interface.
    - `weather.html`: Template for displaying weather information.
    - `navbar.html`: Template for the navigation bar.
- **models/**
    - `chatbot.py`: Contains logic for processing user messages and generating bot responses.
    - `weather.py`: Retrieves weather information for a specified city.
- `app.py`: Main application file responsible for routing and server setup.
- `requirements.txt`: List of Python packages required for the project.
- `README.md`: This file, providing an overview of the project and its structure.

## Installation

1. Ensure you have Python and pip installed on your system.
2. Clone this repository to your local machine:

```bash
git clone https://github.com/mugambi12/
```

3. Navigate to the project directory:

```bash
cd ALXAssist
```

4. Install the required packages:

```bash
pip install -r requirements.txt
```

## Testing

Run the following script for testing the model.

```markdown
python -m unittest discover tests
```

## Usage

1. Run the application:

```bash
cd application
```

```bash
python app.py
```

2. Access the application in your web browser at `http://localhost:5000`.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. We welcome your input!

## License

This project is licensed under the [MIT License](LICENSE).

---
