import math

from flask import Flask, render_template, request, redirect
import pickle
import pandas as pd
import sklearn
import imblearn

app = Flask(__name__)
#
answers = {
    'General_Health': 0,
    'Exercise': 0,
    'Skin_Cancer': 0,
    'Other_Cancer': 0,
    'Depression': 0,
    'Arthritis': 0,
    'Sex': 0,
    'Age_Category': 0,
    'Smoking_History': 0,
    'Alcohol_Consumption': 0,
    'Fruit_Consumption': 0,
    'Green_Vegetables_Consumption': 0,
    'FriedPotato_Consumption': 0,
    'Checkup_Within the past 2 years': 0,
    'Checkup_Within the past year': 0,
    'Diabetes_No': 0,
    'Diabetes_No, pre-diabetes or borderline diabetes': 0,
    'Diabetes_Yes': 0,
    'Diabetes_Yes, but female told only during pregnancy': 0,
    'BMI_Normal weight': 0,
    'BMI_Obesity': 0,
    'BMI_Overweight': 0
}


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
    with open("./static/best_model.pkl", "rb") as f:
        model_object = pickle.load(f)

        model = model_object['model']
        user_data = pd.DataFrame([data])

        predict = model.predict(user_data)
        print(predict[0])
    return render_template('Finish.html', data=predict[0])


def save_data(form):
    if 'age_category' in form:
        answers['Age_Category'] = int(form['age_category'])
    if 'sex' in form:
        if form['sex'] == "female":
            answers['Sex'] = 1
    if 'cent' in form:
        h = int(form['cent'])
        w = int(form['weight'])
        bmi = calculate_bmi_metric(h, w)
        save_bmi(bmi)
    if 'feet' and 'inches' in form:
        feet = int(form['feet'])
        inches = int(form['inches'])
        w = int(form['cent'])
        bmi = calculate_bmi_imperial(feet, inches, w)
        save_bmi(bmi)
    if 'smoke' in form:
        if form['smoke'] == "yes":
            answers['Smoking_History'] = 1
    if 'general_health' in form:
        answers['General_Health'] = int(form['general_health'])
    if 'doctor_visit' in form:
        doc = int(form['doctor_visit'])
        if doc == 1:
            answers['Checkup_Within the past year'] = 1
        elif doc == 2:
            answers['Checkup_Within the past 2 years'] = 1
    if 'exercise' in form:
        if form['exercise'] == "yes":
            answers['Exercise'] = 1
    if 'depressive_disorder' in form:
        if form['depressive_disorder'] == "yes":
            answers['Depression'] = 1
    if 'diabetes' in form:
        if form['diabetes'] == "yes":
            answers['Diabetes_Yes'] = 1
    if 'arthritis' in form:
        if form['arthritis'] == "yes":
            answers['Arthritis'] = 1
    if 'skin_cancer' in form:
        if form['skin_cancer'] == "yes":
            answers['Skin_Cancer'] = 1
    if 'other_cancer' in form:
        if form['other_cancer'] == "yes":
            answers['Other_Cancer'] = 1
    if 'drink_range' in form:
        answers['Alcohol_Consumption'] = int(form['drink_range'])
    if 'eat_fruit' in form:
        answers['Fruit_Consumption'] = int(form['eat_fruit'])
    if 'veggies' in form:
        answers['Green_Vegetables_Consumption'] = int(form['veggies'])
    if 'fried' in form:
        answers['FriedPotato_Consumption'] = int(form['fried'])

    print(answers)


def calculate_bmi_metric(height, weight) -> float:
    meter = height / 100
    return weight / math.pow(meter, 2)


def calculate_bmi_imperial(feet, inch, weight) -> float:
    height = (feet * 12) + inch
    return 703 * (weight / math.pow(height, 2))


def save_bmi(bmi):
    if bmi < 18.5:
        pass
    elif 18.5 <= bmi < 25:
        answers['BMI_Normal weight'] = 1
    elif 25 <= bmi < 30:
        answers['BMI_Overweight'] = 1
    else:
        answers['BMI_Obesity'] = 1


if __name__ == '__main__':
    app.run(debug=True, port=5000)
