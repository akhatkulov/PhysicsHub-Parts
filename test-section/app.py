import json
from flask import Flask, render_template, request

app = Flask(__name__)

# JSON faylini o'qish
def load_questions():
    with open('questions.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    # Savollarni JSON faylidan o'qish
    questions = load_questions()
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    answers = {f'question-{q["id"]}': request.form.get(f'question-{q["id"]}')
               for q in load_questions()}
    print(answers)
    correct_answers = {f'question-{q["id"]}': q['answer'] for q in load_questions()}

    score = sum(1 for qid, answer in answers.items() if answer == correct_answers.get(qid))
    
    return render_template('result.html', score=score, total=len(correct_answers))

if __name__ == '__main__':
    app.run(debug=True)
