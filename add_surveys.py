# add_surveys.py
from app import create_app, db
from app.models import Survey

app = create_app()
with app.app_context():
    # Create sample surveys
    survey1 = Survey(title="Survey 1")
    survey2 = Survey(title="Survey 2")

    # Add surveys to the session and commit
    db.session.add(survey1)
    db.session.add(survey2)
    db.session.commit()
