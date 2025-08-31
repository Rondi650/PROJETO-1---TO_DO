from flask import Flask, render_template, request, url_for, redirect
from conexao_bd import db, ToDo, init_app

app = Flask(__name__)
init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tarefas = ToDo.query.all()
    return render_template('index.html', titulo = 'Lista de Tarefas', tarefas = tarefas)

@app.route('/criar')
def criar():
    return render_template('criar.html', titulo='Criar Nova Tarefa')

@app.route('/criar_tarefa', methods = ['POST'])
def criar_tarefa():
    tarefa = request.form['tarefa']
    nova_tarefa = ToDo(tarefa = tarefa)
    db.session.add(nova_tarefa)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)