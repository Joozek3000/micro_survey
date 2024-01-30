from flask import Blueprint, render_template, redirect, url_for, request
from .models import Survey, Question
from .forms import CreateSurveyForm
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    surveys = Survey.query.all()
    print(surveys)  # This will print fetched surveys to the console
    return render_template('index.html', surveys=surveys)


@main.route('/create_survey', methods=['GET', 'POST'])
def create_survey():
    form = CreateSurveyForm()
    if form.validate_on_submit():
        survey = Survey(title=form.title.data)
        question = Question(text=form.question_text.data, question_type=form.question_type.data, survey=survey)
        db.session.add(survey)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create_survey.html', form=form)


@main.route('/edit/<int:survey_id>', methods=['GET', 'POST'])
def edit_survey(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    form = CreateSurveyForm(obj=survey)

    if request.method == 'POST':
        print("POST request received")  # Debugging line
        if form.validate_on_submit():
            print("Form is valid")  # Debugging line
            survey.title = form.title.data
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            print("Form is not valid")  # Debugging line
            print("Form errors:", form.errors)  # Print form errors if any

    elif request.method == 'GET':
        form.title.data = survey.title

    return render_template('edit_survey.html', form=form)



@main.route('/delete/<int:survey_id>', methods=['POST'])
def delete_survey(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    db.session.delete(survey)
    db.session.commit()
    return redirect(url_for('main.index'))
