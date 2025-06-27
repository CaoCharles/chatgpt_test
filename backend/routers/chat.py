from fastapi import APIRouter
from pydantic import BaseModel

from ..core import mcp
from ..core import llm
from ..core.mcp import history_col, db

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    database: str | None = None


@router.post("/chat")
def chat_endpoint(req: ChatRequest):
    context = mcp.search(req.message, req.database)
    answer = llm.ask(req.message, context)
    history_col.insert_one({"user": req.message, "bot": answer})
    return {"reply": answer}


@router.get("/history")
def get_history():
    return list(history_col.find({}, {"_id": 0}))


@router.get("/databases")
def list_databases():
    return {"databases": db.list_collection_names()}
