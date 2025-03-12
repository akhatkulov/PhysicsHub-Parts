from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Deepseek API kaliti
DEEPSEEK_API_KEY = 'sk-e4361543abfa4a2491f94c3e02a0762c'
DEEPSEEK_API_URL = 'https://api.deepseek.com/v1/chat/completions'

@app.route('/chat', methods=['POST'])
def chat():
    # Foydalanuvchi xabarini olish
    user_message = request.json.get('message')

    # Deepseek API ga so'rov yuborish
    headers = {
        'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'deepseek-chat',  # Model nomi
        'messages': [{'role': 'user', 'content': user_message}]
    }
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)

    # Javobni qaytarish
    if response.status_code == 200:
        bot_response = response.json()['choices'][0]['message']['content']
        return jsonify({'response': bot_response})
    else:
        return jsonify({'error': 'Xatolik yuz berdi', 'status_code': response.status_code}), 500

if __name__ == '__main__':
    app.run(debug=True)