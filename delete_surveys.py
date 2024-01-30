# delete_surveys.py
from app import create_app, db
from app.models import Survey

app = create_app()
with app.app_context():
    # Fetch the surveys you want to delete, e.g., all surveys
    surveys_to_delete = Survey.query.all()

    # Delete them
    for survey in surveys_to_delete:
        db.session.delete(survey)

    db.session.commit()
