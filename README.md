# Gemini Chatbot

This repository demonstrates a small Gemini chatbot with a separated
frontend and backend.  The backend uses FastAPI and connects to MongoDB
through a placeholder **MCP** search to provide RAG context for the
Gemini API.  The frontend is a web page that displays conversation
history, suggests follow-up questions and lets you choose which database
collection to query.

## Requirements

- Python 3.11 or later
- `fastapi`, `uvicorn`, `pymongo`, `google-generativeai`
- A running MongoDB server

## Running

Install the dependencies and start the backend:

```bash
pip install fastapi uvicorn pymongo google-generativeai
export GEMINI_API_KEY=YOUR_API_KEY
export MONGO_URI="mongodb://localhost:27017"
uvicorn backend.main:app --reload
```

Open `frontend/index.html` in your browser. The page communicates with
`http://localhost:8000` to send messages, view history and select a
database.
