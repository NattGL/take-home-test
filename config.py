import os


class BaseConfig:
    LOCAL_HOST = os.environ.get("LOCAL_HOST", "0.0.0.0")
    LOCAL_PORT = os.environ.get("LOCAL_PORT", "8000")

    DATABASE_NAME = "db/salary_survey_data.db"

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.abspath(os.getcwd())}/{DATABASE_NAME}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
