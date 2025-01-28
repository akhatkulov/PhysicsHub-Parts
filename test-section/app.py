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
    # Savollarni yuklash
    questions = load_questions()
    # Savollarni `id` bo'yicha tartiblangan lug'atga o'girish
    questions_dict = {f'question-{q["id"]}': q for q in questions}
    
    # Foydalanuvchi javoblarini olish
    answers = {f'question-{q["id"]}': request.form.get(f'question-{q["id"]}')
               for q in questions}
    print(answers)
    
    # To'g'ri javoblarni yuklash
    correct_answers = {f'question-{q["id"]}': q['answer'] for q in questions}
    print("--[]--", correct_answers)
    
    score = users_ball = 0  
    for qid, answer in answers.items(): 
        correct_answer = correct_answers.get(qid)  
        if answer == correct_answer:  
            score += 1  
            users_ball += questions_dict[qid]['ball']  
    
    print(users_ball)    
    return render_template('result.html',ball=users_ball, score=score, total=len(correct_answers))


if __name__ == '__main__':
    app.run(debug=True)
