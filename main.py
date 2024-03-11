# save this as app.py
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

answers = {}


@app.route("/")
def welcome_page():
    return render_template('index.html')


@app.route("/questions", methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        if 'agree' in request.form:
            progress_bar = None
            if progress_bar is not None:
                return render_template('questions_0.html', progress_bar=progress_bar, question_number=0)
            else:
                progress_bar = 0
                return render_template('questions_0.html', progress_bar=progress_bar, question_number=0)
        elif 'disagree' in request.form:
            return redirect('/')
    elif request.method == 'GET':
        return redirect('/')


@app.route("/answer", methods=['POST'])
def answer():
    if request.method == 'POST':
        save_data(request.form)
        if 'next' in request.form:
            quest_num = int(request.form['question_number'])
            template_name = 'questions_' + str(quest_num + 1) + '.html'
            progress_bar = (quest_num + 1) / 10 * 100
            return render_template(template_name, progress_bar=progress_bar, question_number=quest_num + 1)


def save_data(form):
    if 'user_name' in form:
        answers['name'] = form['user_name']
    elif 'age_category' in form:
        answers['age_category'] = form['age_category']
    elif 'sex' in form:
        answers['sex'] = form['sex']
    elif 'height' in form:
        answers['height'] = form['height']
    elif 'smoke_yes' in form:
        answers['smoke'] = form['smoke_yes']
    elif 'smoke_no' in form:
        answers['smoke'] = form['smoke_no']
    elif 'general_health' in form:
        answers['general_health'] = form['general_health']
    elif 'doctor_visit' in form:
        answers['doctor_visit'] = form['doctor_visit']
    elif 'exercise_yes' in form:
        answers['exercise_yes'] = form['exercise_yes']
    elif 'exercise_no' in form:
        answers['exercise_no'] = form['exercise_no']
    elif 'depressive_disorder_yes' in form:
        answers['depressive_disorder_yes'] = form['depressive_disorder_yes']
    elif 'depressive_disorder_no' in form:
        answers['depressive_disorder_no'] = form['depressive_disorder_no']
    elif 'diabetes_yes' in form:
        answers['diabetes_yes'] = form['diabetes_yes']
    elif 'diabetes_no' in form:
        answers['diabetes_no'] = form['diabetes_no']
    elif 'arthritis_yes' in form:
        answers['arthritis_yes'] = form['arthritis_yes']
    elif 'arthritis_no' in form:
        answers['arthritis_no'] = form['arthritis_no']
    elif 'skin_cancer_yes' in form:
        answers['skin_cancer_yes'] = form['skin_cancer_yes']
    elif 'skin_cancer_no' in form:
        answers['skin_cancer_no'] = form['skin_cancer_no']
    elif 'other_cancer_yes' in form:
        answers['other_cancer_yes'] = form['other_cancer_yes']
    elif 'other_cancer_no' in form:
        answers['other_cancer_no'] = form['other_cancer_no']

    print(answers)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
