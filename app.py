from flask import Flask
from config import SECRET_KEY, iniciar_BD
from database import db

app = Flask(__name__)
app.secret_key = SECRET_KEY 
iniciar_BD(app)

with app.app_context():
    db.create_all()

from routes import *

if __name__ == "__main__":
    app.run(debug=True)
    