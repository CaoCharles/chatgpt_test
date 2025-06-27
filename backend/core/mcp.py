from .config import db

# collections for RAG
history_col = db["history"]
knowledge_col = db["knowledge"]


def search(query: str, database: str | None = None) -> str:
    """從 MongoDB 搜尋與查詢相關的文件內容並合併回傳。"""
    collection = db[database] if database else knowledge_col
    docs = collection.find({"$text": {"$search": query}}).limit(3)
    return " ".join(doc.get("content", "") for doc in docs)
