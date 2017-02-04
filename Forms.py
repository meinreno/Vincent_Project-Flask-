#!/usr/bin/python

from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class Login_form(Form):
	usuario = StringField('Email',validators=[DataRequired()])
	senha = PasswordField('Senha', validators=[DataRequired()])