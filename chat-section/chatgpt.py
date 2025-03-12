from flask import Flask, render_template, request, jsonify
import openai
import markdown

app = Flask(__name__, static_url_path='/static')

# OpenAI API kaliti
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    if not user_message:
        return jsonify({"error": "Xabar bo'sh bo'lishi mumkin emas"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response["choices"][0]["message"]["content"]
        
        # Markdown ni HTML ga o‘tkazish
        reply_html = markdown.markdown(reply)

        return jsonify({"reply": reply_html})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
