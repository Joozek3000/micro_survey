from .extensions import db  # Importing the SQLAlchemy instance from extensions.py

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    question_type = db.Column(db.String(50))  # e.g., 'text', 'multiple-choice'

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    questions = db.relationship('Question', backref='survey', lazy=True)


    def __repr__(self):
        return f'<Survey {self.title}>'