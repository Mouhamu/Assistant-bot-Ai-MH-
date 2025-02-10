import openai
from flask import Flask, request, jsonify
import os

# تعيين مفتاح API الخاص بـ OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# إنشاء تطبيق Flask
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"error": "يرجى إرسال رسالة"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    
    return jsonify({"reply": response["choices"][0]["message"]["content"]})

# تشغيل السيرفر
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
