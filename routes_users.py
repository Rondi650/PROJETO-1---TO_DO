from flask import render_template, request, url_for, redirect, session, flash
from database import db
from app import app
from models import Usuarios
from forms import FormularioUsuario


@app.route('/login')
def login():
    form = FormularioUsuario()
    return render_template('login.html', titulo = 'Login', form=form)

@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    novo_usuario = Usuarios(nome=nome, email=email, senha=senha)
    db.session.add(novo_usuario)
    db.session.commit()
    flash(f'{novo_usuario.nome} cadastrado com sucesso!', 'success')
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

@app.route('/logout')
def logout():
    session.clear()
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('login'))