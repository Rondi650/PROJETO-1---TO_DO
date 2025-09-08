from flask import render_template, request, url_for, redirect, session, flash
from database import db
from app import app
from models import ToDo
from forms import FormularioTodo

@app.route('/')
def index():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    try:
        tarefas = ToDo.query.all()
        return render_template('index.html', titulo='Lista de Tarefas', tarefas=tarefas)
    except Exception as e:
        print(f'Erro: {e}')
        flash('Erro ao acessar o Banco de dados', 'danger')
        return render_template('index.html', titulo='Lista de Tarefas', tarefas=[])

@app.route('/criar')
def criar():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    form = FormularioTodo()
    return render_template('criar.html', titulo='Criar Nova Tarefa', form=form)

@app.route('/alternar/<int:id>')
def alternar(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    try:
        tarefa = ToDo.query.filter_by(id=id).first()
        if tarefa:
            tarefa.alternar_status()
            db.session.add(tarefa)
            db.session.commit()

        return redirect(url_for('index'))
    except Exception as e:
        print(f'Erro: {e}')
        db.session.rollback()
        flash('Erro ao acessar o Banco de dados', 'danger')
        return render_template('index.html', titulo='Lista de Tarefas', tarefas=[])

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    try:
        tarefa = ToDo.query.filter_by(id=id).first()
        if tarefa:
            db.session.delete(tarefa)
            db.session.commit()
            flash('Tarefa deletada com sucesso', 'info')

        return redirect(url_for('index'))
    except Exception as e:
        print(f'Erro: {e}')
        db.session.rollback()
        flash('Erro ao acessar o Banco de dados', 'danger')
        return render_template('index.html', titulo='Lista de Tarefas', tarefas=[])

@app.route('/criar_tarefa', methods=['POST'])
def criar_tarefa():
    form = FormularioTodo(request.form)
    tarefa = form.tarefa.data
    
    try:
        nova_tarefa = ToDo(tarefa=tarefa)

        db.session.add(nova_tarefa)
        db.session.commit()
        flash('Tarefa cadastrada com sucesso!', 'success')

        return redirect(url_for('index'))
    except Exception as e:
        print(f'Erro: {e}')
        db.session.rollback()
        flash('Erro ao acessar o Banco de dados', 'danger')
        return render_template('index.html', titulo='Lista de Tarefas', tarefas=[])