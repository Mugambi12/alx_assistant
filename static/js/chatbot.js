document.addEventListener('DOMContentLoaded', function() {
  var chatBubble = document.getElementById('chat-bubble');
  var chatContainer = document.getElementById('chat-container');
  var messageInput = document.getElementById('message');
  var chatMessages = document.getElementById('chat-messages');
  var sendButton = document.querySelector('.send-btn');
  var popup = document.querySelector('.popup');

  var introMessageDisplayed = false;

  chatBubble.addEventListener('click', function() {
      chatContainer.classList.toggle('active');
      scrollToBottom();

      if (!introMessageDisplayed) {
          var introMessage = document.createElement('div');
          introMessage.className = 'intro-message';
          introMessage.innerHTML = 'Hey, I am your AI-powered assistant. How can I help you today?';
          document.getElementById('chat-messages').appendChild(introMessage);

          introMessageDisplayed = true;
      }
  });

  document.addEventListener('click', function(event) {
      if (!event.target.closest('#chat-container') && !event.target.closest('#chat-bubble')) {
          chatContainer.classList.remove('active');
      }
  });

  messageInput.addEventListener('keydown', function(event) {
      if (event.key === 'Enter') {
          sendMessage();
          event.preventDefault();
      }
  });

  sendButton.addEventListener('click', function() {
      sendMessage();
  });

  sendButton.addEventListener('mouseover', function() {
      popup.style.visibility = 'visible';
      popup.style.opacity = '1';
  });

  sendButton.addEventListener('mouseout', function() {
      popup.style.visibility = 'hidden';
      popup.style.opacity = '0';
  });

  function scrollToBottom() {
      chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function sendMessage() {
      var message = document.getElementById('message').value;

      if (!message.trim()) {
          return;
      }

      var userMessage = document.createElement('div');
      userMessage.className = 'user-message';
      userMessage.innerHTML = '<strong>You:</strong> ' + message;
      document.getElementById('chat-messages').appendChild(userMessage);

      var botTyping = document.createElement('div');
      botTyping.className = 'bot-typing';
      botTyping.innerHTML = '<strong>Alexy is typing...</strong>';
      document.getElementById('chat-messages').appendChild(botTyping);

      // Remove the intro message if it exists
      var introMessage = document.querySelector('.intro-message');
      if (introMessage) {
          introMessage.remove();
      }

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
          document.getElementById('chat-messages').removeChild(botTyping);

          var botMessage = document.createElement('div');
          botMessage.className = 'bot-message';
          botMessage.innerHTML = '<strong>Alexy:</strong> ';
          document.getElementById('chat-messages').appendChild(botMessage);

          simulateTyping(data.message, function() {
              scrollToBottom();
          });
      });

      document.getElementById('message').value = '';
  }

  function simulateTyping(message, callback) {
      var index = 0;
      var interval = setInterval(function() {
          var botMessage = document.querySelector('.bot-message:last-child');
          botMessage.innerHTML += message[index];
          index++;
          scrollToBottom();
          if (index === message.length) {
              clearInterval(interval);
              callback();
          }
      }, 25);
  }
});
