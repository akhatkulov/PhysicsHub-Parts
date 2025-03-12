import json
from flask import Flask, render_template, request

app = Flask(__name__)

# JSON faylini o'qish
def load_questions():
    with open('example.json', 'r', encoding='utf-8') as f:
        return json.load(f)['data']

@app.get('/')
def index():
    questions = load_questions()
    return render_template('index.html', questions=questions)

@app.post('/')
def submit():
    questions = load_questions()
    questions_dict = {f'question-{q["id"]}': q for q in questions}
    answers = {f'question-{q["id"]}': request.form.get(f'question-{q["id"]}') for q in questions}
    correct_answers = {f'question-{q["id"]}': q['answer'] for q in questions} 
    score = users_ball = 0  
    for qid, answer in answers.items(): 
        correct_answer = correct_answers.get(qid)  
        if answer == correct_answer:  
            score += 1  
            users_ball += questions_dict[qid]['ball']  
    return render_template('result.html',ball=users_ball, score=score, total=len(correct_answers))


if __name__ == '__main__':
    app.run(debug=True)
