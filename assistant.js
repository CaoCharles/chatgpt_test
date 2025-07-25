const bioText = document.getElementById('bio-text').innerText;
let apiKey = localStorage.getItem('openai_key') || '';

function askBio() {
  const q = document.getElementById('question').value;
  if (!q) return;
  if (!apiKey) {
    apiKey = prompt('Enter your OpenAI API key');
    if (!apiKey) return;
    localStorage.setItem('openai_key', apiKey);
  }
  const answerDiv = document.getElementById('answer');
  answerDiv.innerText = 'Thinking...';
  fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + apiKey
    },
    body: JSON.stringify({
      model: 'gpt-3.5-turbo',
      messages: [
        { role: 'system', content: 'You are an assistant who knows the following biography: ' + bioText },
        { role: 'user', content: q }
      ]
    })
  }).then(r => r.json()).then(data => {
    answerDiv.innerText = data.choices && data.choices[0].message.content.trim();
  }).catch(err => {
    answerDiv.innerText = 'Error: ' + err.message;
  });
}
