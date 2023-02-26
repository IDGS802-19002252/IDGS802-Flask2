from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, PasswordField
from wtforms.fields import EmailField, TextAreaField
from wtforms import validators

class LoginForm(Form):
    username = StringField('usuario', [
        validators.DataRequired(message='El usuario es requerido')
    ])

    password = PasswordField('password', [
        validators.DataRequired(message='El usuario es requerido')
    ])