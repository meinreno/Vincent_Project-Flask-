#!/usr/bin/python

from flask import Flask, render_template, request, make_response, redirect, url_for, session
from Forms import Login_form
from flask_sqlalchemy import SQLAlchemy
import json
from Model import *
from flask.ext.login import LoginManager, logout_user, login_user, current_user , login_required
from Classes import CriptografiaSenha



import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/royal210_vincentProject'

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'





@app.route("/")
def index():
	form = Login_form()
	return render_template("login_form.html", form=form)
	
@app.route("/login", methods=['POST'])
def login():
	form = Login_form()
	email = request.form['usuario']
	dados_usuario = usuarios.query.filter_by(email=email).first()
	if dados_usuario != None:
		senha = request.form['senha']
		gerarSenha = CriptografiaSenha(senha)
		HashGerada = gerarSenha.gerarHash(dados_usuario.salt)
		
		if HashGerada == dados_usuario.senha:
			login_user(dados_usuario)
		

	
	
	return redirect(url_for('index'))
	

@app.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))
	

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)

