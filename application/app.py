# app.py

from flask import Flask, render_template, jsonify, request
from models.chatbot import process_message
from models.weather import get_weather

app = Flask(__name__)

# Route for rendering the main page
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint for handling chat interactions
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_response = process_message(user_message)
    return jsonify({'message': bot_response})

# Endpoint for getting weather information
@app.route('/get_weather', methods=['POST'])
def get_weather_route():
    city_input = request.form['city-input']
    temp_format = request.form['temp-format']
    weather_result = get_weather(city_input, temp_format)
    return jsonify({'weather_result': weather_result})


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
