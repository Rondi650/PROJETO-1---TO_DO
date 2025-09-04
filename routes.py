from flask import render_template, request, url_for, redirect, session, flash
from database import db
from app import app
from models import Usuarios, ToDo

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

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo = 'Cadastro' )

@app.route('/alternar/<int:id>')
def alternar(id):
    tarefa = ToDo.query.filter_by(id=id).first()
    if tarefa:
        tarefa.alternar_status()
        db.session.add(tarefa)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    tarefa = ToDo.query.filter_by(id=id).first()
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
        flash('Tarefa deletada com sucesso', 'info')
    return redirect(url_for('index'))
    
@app.route('/logout')
def logout():
    session.clear()
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('login'))

@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    novo_usuario = Usuarios(nome=nome, email=email, senha=senha)
    db.session.add(novo_usuario)
    db.session.commit()
    flash('Usuario cadastrado com sucesso!', 'success')
    return redirect(url_for('login'))

@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']
    usuario = Usuarios.query.filter_by(email=email, senha=senha).first()
    if usuario:
        session['usuario_id'] = usuario.id
        flash(usuario.nome + ' logado com sucesso!', 'success')
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
    flash('Tarefa cadastrada com sucesso!', 'success')
    return redirect(url_for('index'))