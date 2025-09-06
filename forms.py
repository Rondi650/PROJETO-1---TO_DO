from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, validators
from wtforms.validators import DataRequired, length

class FormularioTodo(FlaskForm):
    tarefa = StringField('Nova Tarefa:', validators=[DataRequired(), length(min=10, max=200)])
    salvar = SubmitField('Salvar')
    
class FormularioUsuario(FlaskForm):
    nome = StringField('Nome de usuário:', validators=[DataRequired(), length(min=5, max=100)])
    email = EmailField('E-mail:', validators=[DataRequired(), length(min=5, max=100)])
    senha = PasswordField('Senha:', [
        validators.DataRequired(),
        validators.EqualTo('confirmar_senha', message='Senhas devem coincidir')
    ])
    confirmar_senha = PasswordField('Confirmar Senha:', validators=[DataRequired()])
    salvar = SubmitField('Salvar')