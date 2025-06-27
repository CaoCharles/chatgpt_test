import argparse
import os
from cryptography.fernet import Fernet
import google.generativeai as genai
import openai
import anthropic


def _decrypt(value: str, secret: str | None) -> str:
    if secret:
        f = Fernet(secret.encode())
        return f.decrypt(value.encode()).decode()
    return value


def _load_api_key(provider: str, secret: str | None) -> str | None:
    env_enc = f"{provider.upper()}_API_KEY_ENC"
    env_plain = f"{provider.upper()}_API_KEY"
    val = os.getenv(env_enc)
    if val:
        return _decrypt(val, secret)
    return os.getenv(env_plain)


def _chat_loop(send_func, name: str):
    print(f"{name} Chatbot. 輸入 'exit' 離開。")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break
        try:
            reply = send_func(user_input)
            print(f"{name}: {reply}")
        except Exception as e:
            print(f"[error] {e}")


def _run_gemini(api_key: str, model: str = "gemini-1.5-pro"):
    genai.configure(api_key=api_key)
    m = genai.GenerativeModel(model)
    chat = m.start_chat(history=[])

    def send(msg: str) -> str:
        return chat.send_message(msg).text

    _chat_loop(send, "Gemini")


def _run_openai(api_key: str, model: str = "gpt-3.5-turbo"):
    openai.api_key = api_key

    def send(msg: str) -> str:
        resp = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": msg}])
        return resp.choices[0].message.content.strip()

    _chat_loop(send, "ChatGPT")


def _run_azure(api_key: str, endpoint: str, deployment: str, api_version: str):
    openai.api_type = "azure"
    openai.api_base = endpoint
    openai.api_version = api_version
    openai.api_key = api_key

    def send(msg: str) -> str:
        resp = openai.ChatCompletion.create(engine=deployment, messages=[{"role": "user", "content": msg}])
        return resp.choices[0].message.content.strip()

    _chat_loop(send, "AzureGPT")


def _run_claude(api_key: str, model: str = "claude-3-opus-20240229"):
    client = anthropic.Anthropic(api_key=api_key)

    def send(msg: str) -> str:
        resp = client.messages.create(model=model, max_tokens=1024, messages=[{"role": "user", "content": msg}])
        return resp.content[0].text

    _chat_loop(send, "Claude")


def main():
    parser = argparse.ArgumentParser(description="多模型聊天機器人")
    parser.add_argument("--provider", choices=["gemini", "openai", "azure", "claude"], default="gemini")
    parser.add_argument("--secret", help="解密 API 金鑰用的密鑰")
    parser.add_argument("--azure-endpoint")
    parser.add_argument("--azure-deployment")
    parser.add_argument("--model", help="指定模型名稱")
    args = parser.parse_args()

    api_key = _load_api_key(args.provider, args.secret)
    if not api_key:
        raise SystemExit(f"找不到 {args.provider.upper()} API 金鑰")

    if args.provider == "gemini":
        _run_gemini(api_key, args.model or "gemini-1.5-pro")
    elif args.provider == "openai":
        _run_openai(api_key, args.model or "gpt-3.5-turbo")
    elif args.provider == "azure":
        if not args.azure_endpoint or not args.azure_deployment:
            raise SystemExit("Azure 需要 --azure-endpoint 與 --azure-deployment")
        _run_azure(api_key, args.azure_endpoint, args.azure_deployment, args.model or "2024-02-15-preview")
    else:  # claude
        _run_claude(api_key, args.model or "claude-3-opus-20240229")


if __name__ == "__main__":
    main()
