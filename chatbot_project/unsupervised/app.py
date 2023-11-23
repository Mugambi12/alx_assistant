from flask import Flask, render_template, jsonify, request
from models.unsupervised_chatbot import UnsupervisedChatbot

app = Flask(__name__)
chatbot = UnsupervisedChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_response = chatbot.get_response(user_message)
    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run(port=8080)
