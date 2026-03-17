from sqlalchemy.engine import URL
from sqlalchemy import create_engine, text
from database import db

SECRET_KEY = 'Rondi'

def iniciar_BD(app):
    # First, create the database if it doesn't exist
    temp_url = URL.create(
        "mysql+pymysql",
        username="rondi",
        password="rondi",
        host="localhost",
        port=3306
    )
    engine = create_engine(temp_url)
    with engine.connect() as conn:
        conn.execute(text("CREATE DATABASE IF NOT EXISTS ToDo"))
        conn.commit()
    
    connection_url = URL.create(
        "mysql+pymysql",
        username="rondi",
        password="rondi",
        host="localhost",
        port=3306,
        database="ToDo"
    )
    
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)