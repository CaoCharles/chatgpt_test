import { useEffect, useState } from 'react';

export default function Home() {
  const [bio, setBio] = useState(null);
  const [q, setQ] = useState('');
  const [a, setA] = useState('');
  const [key, setKey] = useState('');

  useEffect(() => {
    fetch('/bio.json').then(r => r.json()).then(setBio);
  }, []);

  const ask = async () => {
    if (!key) {
      const k = prompt('Enter OpenAI API key');
      if (!k) return;
      localStorage.setItem('openai_key', k);
      setKey(k);
    }
    const apiKey = key || localStorage.getItem('openai_key');
    if (!apiKey) return;
    setA('Thinking...');
    const res = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + apiKey
      },
      body: JSON.stringify({
        model: 'gpt-3.5-turbo',
        messages: [
          { role: 'system', content: bio ? bio.bio : '' },
          { role: 'user', content: q }
        ]
      })
    });
    const data = await res.json();
    setA(data.choices ? data.choices[0].message.content.trim() : '');
  };

  return (
    <div>
      {bio && (
        <div className="card">
          <h2>{bio.name}</h2>
          <p>{bio.title}</p>
        </div>
      )}
      <div className="chat">
        <textarea value={q} onChange={e => setQ(e.target.value)} placeholder="Ask about me" />
        <button onClick={ask}>Ask</button>
        <div className="answer">{a}</div>
      </div>
    </div>
  );
}
