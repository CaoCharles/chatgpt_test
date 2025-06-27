from .config import MODEL

chat = MODEL.start_chat(history=[])


def ask(question: str, context: str) -> str:
    """將問題與檢索到的上下文送入 Gemini 模型，取得回答。"""
    response = chat.send_message(f"{question}\n\nContext:\n{context}")
    return response.text
