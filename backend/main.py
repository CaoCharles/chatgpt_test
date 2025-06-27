from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from pymongo import MongoClient
import os

app = FastAPI()

# Configure API key and MongoDB connection
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")
chat = model.start_chat(history=[])

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
mongo_db = client["gemini_chat"]
history_col = mongo_db["history"]
knowledge_col = mongo_db["knowledge"]

class ChatRequest(BaseModel):
    message: str
    database: str | None = None


def search_mcp(query: str, database: str | None):
    """Placeholder MCP retrieval from MongoDB."""
    collection = mongo_db[database] if database else knowledge_col
    docs = collection.find({"$text": {"$search": query}}).limit(3)
    return " ".join(doc.get("content", "") for doc in docs)


@ app.post("/chat")
def chat_endpoint(req: ChatRequest):
    rag_context = search_mcp(req.message, req.database)
    response = chat.send_message(f"{req.message}\n\nContext:\n{rag_context}")
    history_col.insert_one({"user": req.message, "bot": response.text})
    return {"reply": response.text}


@ app.get("/history")
def get_history():
    return list(history_col.find({}, {"_id": 0}))


@ app.get("/databases")
def list_databases():
    return {"databases": mongo_db.list_collection_names()}

