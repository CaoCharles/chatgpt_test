import argparse
import google.generativeai as genai


def main():
    parser = argparse.ArgumentParser(description="Gemini 2.5 Pro Chatbot")
    parser.add_argument('--api-key', required=True, help='Gemini API key')
    args = parser.parse_args()

    genai.configure(api_key=args.api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
    chat = model.start_chat(history=[])

    print("Gemini Chatbot. Type 'exit' to quit.")
    while True:
        user_input = input('You: ')
        if user_input.strip().lower() == 'exit':
            break
        response = chat.send_message(user_input)
        print('Gemini: ' + response.text)


if __name__ == '__main__':
    main()
