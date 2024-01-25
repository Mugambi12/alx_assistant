import unittest
from models.chatbot import process_message

class TestChatbot(unittest.TestCase):

    def test_process_message_greetings(self):
        message = "Hello"
        response = process_message(message)
        self.assertEqual(response, "Hello! How can I assist you?")

#    def test_process_message_hub_location(self):
#        message = "Tell me about the hubs"
#        response = process_message(message)
#        self.assertTrue("hub information" in response)

    def test_process_message_unknown(self):
        message = "Random Message"
        response = process_message(message)
        self.assertEqual(response, "I'm sorry, I didn't understand that. Type 'help' for assistance.")

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
