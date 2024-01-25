document.getElementById('weather-form').addEventListener('submit', function(e) {
  e.preventDefault();
  var city = document.getElementById('city-input').value;
  var tempFormat = document.getElementById('temp-format').value;

  fetch('/get_weather', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: 'city-input=' + encodeURIComponent(city) + '&temp-format=' + encodeURIComponent(tempFormat)
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('weather-result').innerHTML = data.weather_result;

      // Add the weather info to history (limit to 5 entries)
      let history = JSON.parse(localStorage.getItem('weatherHistory')) || [];
      history.unshift({ city: city, tempFormat: tempFormat, result: data.weather_result, timestamp: new Date().toLocaleString() });
      if (history.length > 20) {
          history.pop(); // Remove the oldest entry
      }
      localStorage.setItem('weatherHistory', JSON.stringify(history));

      // Update the displayed history
      displayHistory();
      scrollToBottom();
  });
});

document.getElementById('clear-btn').addEventListener('click', function() {
  document.getElementById('city-input').value = '';
  document.getElementById('temp-format').value = 'C';
  document.getElementById('weather-result').innerHTML = '';

  // Clear the history
  localStorage.removeItem('weatherHistory');

  // Update the displayed history
  displayHistory();
});

// Function to display weather history
function displayHistory() {
  let historyContainer = document.getElementById('weather-history');
  historyContainer.innerHTML = ''; // Clear previous entries

  let history = JSON.parse(localStorage.getItem('weatherHistory')) || [];

  // Display up to 5 recent requests
  for (let i = 0; i < history.length; i++) {
      let entry = document.createElement('div');
      entry.classList.add('mb-3');

      let city = history[i].city;
      let tempFormat = history[i].tempFormat;
      let result = history[i].result;
      let timestamp = history[i].timestamp;

      entry.innerHTML = `
          <div class="accordion" id="accordion-${i}">
              <div class="accordion-item">
                  <h2 class="accordion-header" id="heading-${i}">
                      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-${i}" aria-expanded="false" aria-controls="collapse-${i}">
                          ${city} - ${timestamp}
                      </button>
                  </h2>
                  <div id="collapse-${i}" class="accordion-collapse collapse" aria-labelledby="heading-${i}" data-bs-parent="#accordion-${i}">
                      <div class="accordion-body">
                          <strong>City:</strong> ${city}<br>
                          <strong>Temperature Format:</strong> ${tempFormat}<br>
                          <strong>Result:</strong> ${result}<br>
                          <strong>Time:</strong> ${timestamp}
                      </div>
                  </div>
              </div>
          </div>
      `;

      historyContainer.appendChild(entry);
  }
}


// Call the displayHistory function to initially display any existing history
displayHistory();
