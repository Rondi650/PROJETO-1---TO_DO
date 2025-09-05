from flask import render_template, request, url_for, redirect, session, flash
from database import db
from app import app
from models import Usuarios
from forms import FormularioUsuario
from flask_bcrypt import check_password_hash


@app.route('/login')
def login():
    form = FormularioUsuario()
    return render_template('login.html', titulo = 'Login', form=form)

@app.route('/cadastrar')
def cadastrar():
    form = FormularioUsuario()
    return render_template('cadastrar.html', titulo = 'Cadastro', form=form )

@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    form = FormularioUsuario(request.form)

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data

        novo_usuario = Usuarios(nome=nome, email=email)
        novo_usuario.set_senha(senha)

        db.session.add(novo_usuario)
        db.session.commit()

        flash(f'{novo_usuario.nome} cadastrado com sucesso!', 'success')
        return redirect(url_for('login'))

    return render_template('cadastrar.html', titulo='Cadastro', form=form)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    email = form.email.data
    usuario = Usuarios.query.filter_by(email=email).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    
    if usuario and senha:
        session['usuario_id'] = usuario.id
        flash(f'{usuario.nome} logado com sucesso!', 'success')
        return redirect(url_for('index'))
    else:
        flash('E-mail ou senha incorretos.', 'danger')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('login'))