#!/usr/bin/python

from flask import Flask, render_template, request, make_response, redirect, url_for, session
from Forms import Login_form

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
	form = Login_form()
	if 'emailUsuario' in session:
		
		return render_template("login_form.html", form=form)
	else:
		return "Tem que logar seu bosta"
@app.route("/login", methods=['POST'])
def login():
	form = Login_form();
	if form.validate_on_submit():
		
		#session['emailUsuario'] = "teste"
		#return form.usuario.data
		return redirect('/')
	else:
		return render_template("login_form.html", form=form)

@app.route("/logout")
def logout():
	session.pop('emailUsuario', None)
	return "logout com sucesso"
	

if __name__ == "__main__":
	app.run(debug=True)

