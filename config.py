from sqlalchemy.engine import URL
from sqlalchemy import create_engine, text
from database import db

SECRET_KEY = 'Rondi'


def iniciar_BD(app):
    connection_url = URL.create(
        "postgresql+psycopg2",
        username="rondi",
        password="rondi",
        host="psql",
        port=5432,
        database="ToDo"
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
