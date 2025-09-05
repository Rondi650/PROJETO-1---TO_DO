from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, length
 
class FormularioTodo(FlaskForm):
    tarefa = StringField('Nome do Jogo', validators=[DataRequired(), length(min=10, max=200)])
    salvar = SubmitField('Salvar')
    
class FormularioUsuario(FlaskForm):
    nome = StringField('Nome de usuário:', validators=[DataRequired(), length(min=5, max=100)])
    email = StringField('E-mail::', validators=[DataRequired(), length(min=5, max=20)])
    senha = PasswordField('Senha:', validators=[DataRequired(), length(min=3, max=100)])
    salvar = SubmitField('Salvar')