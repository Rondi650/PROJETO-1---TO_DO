from database import db
from datetime import datetime
from flask_bcrypt import generate_password_hash

class ToDo(db.Model):
    __tablename__ = 'ListaTarefas'
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    tarefa = db.Column(db.String(500), nullable = False)
    status = db.Column(db.Boolean, default=False)
    
    @property
    def feito(self):
        return 'Feito' if self.status else 'Nao Feito'
    
    def alternar_status(self):
        self.status = not self.status
                
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
    
    def set_senha(self, senha):
        self.senha = generate_password_hash(senha).decode('utf-8')