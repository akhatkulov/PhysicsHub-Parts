from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret'  # Flash xabarlar ishlashi uchun

problems = [
    {
        "id": 1,
        "title": "Erkin tushish tezligi",
        "main": "Og'irligi 2 kg bo'lgan jism erkin tushmoqda. 3 sekunddan keyin uning tezligi qancha bo‘ladi? (g = 9.8 m/s²)",
        "helper": "Erkin tushayotgan jismning tezligi v = g*t formulasi orqali topiladi.",
        "correct": "29.4"
    },
    {
        "id": 2,
        "title": "Newton ikkinchi qonuni",
        "main": "10 kg massali jismga 20 N kuch ta’sir qilmoqda. Jism tezlanishini hisoblang.",
        "helper": "Newtonning ikkinchi qonuniga ko‘ra, a = F/m.",
        "correct": "2"
    },
    {
        "id": 3,
        "title": "Ish va energiya",
        "main": "5 kg og‘irlikdagi jism 4 m balandlikka ko‘tarildi. Ishni hisoblang. (g = 9.8 m/s²)",
        "helper": "Ish W = m*g*h formulasi bo‘yicha topiladi.",
        "correct": "196"
    }
]

@app.route('/')
def home():
    return render_template("index.html", problems=problems)

@app.route('/solve/<int:problem_id>', methods=['GET', 'POST'])
def solve(problem_id):
    problem = next((p for p in problems if p["id"] == problem_id), None)
    if not problem:
        flash("❌ Masala topilmadi!", "danger")
        return redirect(url_for('home'))

    if request.method == 'POST':
        user_answer = request.form['answer'].strip()
        correct_answer = problem["correct"]
        if user_answer == correct_answer:
            flash(f"✅ To‘g‘ri javob! ({user_answer})", "success")
        else:
            flash(f"❌ Noto‘g‘ri javob! To‘g‘ri javob: {correct_answer}", "danger")
        return redirect(url_for('solve', problem_id=problem_id))

    return render_template("solve.html", problem=problem)

if __name__ == '__main__':
    app.run(debug=True)
