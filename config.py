class Config:
    # Secret key for session management. Use a random value in production.
    SECRET_KEY = 'your_secret_key_here'

    # Database configuration
    # For SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///micro_survey.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Additional configuration can be added here
