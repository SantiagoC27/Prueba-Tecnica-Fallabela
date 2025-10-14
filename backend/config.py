import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../data/database.db')

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATA_DIR}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False