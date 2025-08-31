from flask import Flask, render_template, request, url_for, redirect, session, flash
from conexao_bd import db, ToDo, iniciar_BD, Usuarios

app = Flask(__name__)
app.secret_key = 'Rondi'
iniciar_BD(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))    
    tarefas = ToDo.query.all()
    return render_template('index.html', titulo = 'Lista de Tarefas', tarefas = tarefas)

@app.route('/criar')
def criar():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    return render_template('criar.html', titulo='Criar Nova Tarefa')

@app.route('/login')
def login():
    return render_template('login.html', titulo = 'Login')

@app.route('/logout')
def logout():
    session.clear()
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('login'))

@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']
    usuario = Usuarios.query.filter_by(email=email, senha=senha).first()
    if usuario:
        session['usuario_id'] = usuario.id
        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('index'))
    else:
        flash('E-mail ou senha incorretos.', 'danger')
        return redirect(url_for('login'))

@app.route('/criar_tarefa', methods = ['POST'])
def criar_tarefa():
    tarefa = request.form['tarefa']
    nova_tarefa = ToDo(tarefa = tarefa)
    db.session.add(nova_tarefa)
    db.session.commit()
    return redirect(url_for('index'))
  
if __name__ == "__main__":
    app.run(debug=True)
    