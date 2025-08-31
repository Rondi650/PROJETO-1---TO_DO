from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL
from datetime import datetime

db = SQLAlchemy()

class ToDo(db.Model):
    __tablename__ = 'ListaTarefas'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    tarefa = db.Column(db.String(500), nullable = False)
    status = db.Column(db.Boolean, default=False)
    
    @property
    def feito(self):
        return 'Feito' if self.status else 'Nao Feito'
    
    def concluir_tarefa(self):
        self.status = True
        
    def reabrir_tarefa(self):
        self.status = False
        
class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    senha = db.Column(db.String(100), nullable = False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    ativo = db.Column(db.Boolean, default=True)    
    
    @property
    def status(self):
        return 'Ativo' if self.ativo else 'Desativado'       
               
def iniciar_BD(app):
    connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=Todo;Trusted_Connection=yes;"
    connection_url = URL.create(
        "mssql+pyodbc", query={"odbc_connect": connection_string}
    )
    
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)