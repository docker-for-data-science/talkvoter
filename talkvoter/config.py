import os


class Config(object):

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///:memory:")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ERROR_404_HELP = False
