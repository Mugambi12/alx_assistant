document.addEventListener('DOMContentLoaded', function() {
  var chatMessages = document.getElementById('chat-messages');
  var messageInput = document.getElementById('message');
  var sendButton = document.getElementById('send-button'); // Assuming you have a button with the id 'send-button'

  function appendMessage(message, sender) {
      var messageDiv = document.createElement('div');
      messageDiv.className = sender;
      messageDiv.innerText = message;
      chatMessages.appendChild(messageDiv);
      chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function simulateTyping(callback) {
      var typingDiv = document.createElement('div');
      typingDiv.className = 'bot-typing';
      typingDiv.innerHTML = '<span class="dot"></span><span class="dot"></span><span class="dot"></span>';
      chatMessages.appendChild(typingDiv);
      chatMessages.scrollTop = chatMessages.scrollHeight;
      setTimeout(function() {
          typingDiv.remove();
          callback();
      }, 35); // Simulating typing for 1.5 seconds
  }

  function sendBotMessage(message) {
    simulateTyping(function() {
        appendMessage(message, 'bot-message');
        chatMessages.scrollTop = chatMessages.scrollHeight;
    });
  }

  function sendMessage() {
      var message = messageInput.value.trim();
      if (message) {
          appendMessage(message, 'user-message');
          messageInput.value = '';

          // Send user message to server
          fetch('/chat', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                  message: message
              })
          })
          .then(response => response.json())
          .then(data => {
              var botMessage = data.message;
              sendBotMessage(botMessage);
          });
      }
  }

  messageInput.addEventListener('keydown', function(event) {
      if (event.key === 'Enter') {
          event.preventDefault();
          sendMessage();
      }
  });

  sendButton.addEventListener('click', function() {
      sendMessage();
  });
});
