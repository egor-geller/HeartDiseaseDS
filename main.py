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
    print(answers)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
