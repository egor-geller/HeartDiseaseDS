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
        if 'disagree' in request.form:
            return redirect('/')
    if request.method == 'GET':
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
        if 'next_end' in request.form:
            return finish(answers)
        if 'back' in request.form:
            quest_num = int(request.form['question_number'])
            if quest_num <= 0:
                return redirect("/")
            template_name = 'questions_' + str(quest_num - 1) + '.html'
            progress_bar = (quest_num - 1) / 10 * 100
            return render_template(template_name, progress_bar=progress_bar, question_number=quest_num - 1)


def finish(data):
    return render_template('Finish.html', data=data)


def save_data(form):
    if 'user_name' in form:
        answers['name'] = form['user_name']
    if 'age_category' in form:
        answers['age_category'] = form['age_category']
    if 'sex' in form:
        answers['sex'] = form['sex']
    if 'cent' in form:
        answers['cent'] = form['cent']
    if 'feet' and 'inches' in form:
        feet = form['feet']
        inches = form['inches']
        overall_height_in_cent = convert_us_height_to_centimeters(feet, inches)
        answers['height'] = overall_height_in_cent
    if 'smoke' in form:
        answers['smoke'] = form['smoke']
    if 'general_health' in form:
        answers['general_health'] = form['general_health']
    if 'doctor_visit' in form:
        answers['doctor_visit'] = form['doctor_visit']
    if 'exercise_yes' in form:
        answers['exercise_yes'] = form['exercise_yes']
    if 'exercise_no' in form:
        answers['exercise_no'] = form['exercise_no']
    if 'depressive_disorder_yes' in form:
        answers['depressive_disorder_yes'] = form['depressive_disorder_yes']
    if 'depressive_disorder_no' in form:
        answers['depressive_disorder_no'] = form['depressive_disorder_no']
    if 'diabetes_yes' in form:
        answers['diabetes_yes'] = form['diabetes_yes']
    if 'diabetes_no' in form:
        answers['diabetes_no'] = form['diabetes_no']
    if 'arthritis_yes' in form:
        answers['arthritis_yes'] = form['arthritis_yes']
    if 'arthritis_no' in form:
        answers['arthritis_no'] = form['arthritis_no']
    if 'skin_cancer_yes' in form:
        answers['skin_cancer_yes'] = form['skin_cancer_yes']
    if 'skin_cancer_no' in form:
        answers['skin_cancer_no'] = form['skin_cancer_no']
    if 'other_cancer_yes' in form:
        answers['other_cancer_yes'] = form['other_cancer_yes']
    if 'other_cancer_no' in form:
        answers['other_cancer_no'] = form['other_cancer_no']
    if 'drink_range' in form:
        answers['drink_range'] = form['drink_range']
    if 'eat_fruit' in form:
        answers['eat_fruit'] = form['eat_fruit']
    if 'veggies' in form:
        answers['veggies'] = form['veggies']
    if 'fried' in form:
        answers['fried'] = form['fried']

    print(answers)


def convert_us_height_to_centimeters(feet, inch) -> int:
    return int(feet * 30.48 + inch * 2.54)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
