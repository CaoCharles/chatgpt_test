import argparse
import os
import google.generativeai as genai


def run_chat(api_key: str):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-pro")
    chat = model.start_chat(history=[])
    print("Gemini Chatbot. 輸入 'exit' 離開。")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break
        resp = chat.send_message(user_input)
        print("Gemini: " + resp.text)


def main():
    parser = argparse.ArgumentParser(description="Gemini 2.5 Pro 聊天機器人")
    parser.add_argument("--api-key", help="Gemini API 金鑰，預設讀取環境變數", default=os.getenv("GEMINI_API_KEY"))
    args = parser.parse_args()
    if not args.api_key:
        raise SystemExit("請提供 GEMINI API 金鑰。")
    run_chat(args.api_key)


if __name__ == "__main__":
    main()
