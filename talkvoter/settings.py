import os


SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///:memory:")

SQLALCHEMY_TRACK_MODIFICATIONS = False
