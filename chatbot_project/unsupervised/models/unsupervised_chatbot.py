from models.responses import Responses

class UnsupervisedChatbot:
    def __init__(self):
        self.responses = Responses()

    def get_response(self, user_message):
        return self.responses.get_response(user_message)
