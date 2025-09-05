from flask import Flask
from database import db
from config import SECRET_KEY, iniciar_BD
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
 
app = Flask(__name__)
app.secret_key = SECRET_KEY
iniciar_BD(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)
 
with app.app_context():
    db.create_all()
    
from routes_todo import *
from routes_users import *

if __name__ == '__main__':
    app.run(debug=True)
    