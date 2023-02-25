from wtforms import Form, StringField, RadioField, validators

class TraductorForm(Form):
  
  palabra = StringField('palabra', [
      validators.DataRequired(message='Ingresa una palabra que deseas traducir.'),
      validators.Regexp('^[a-zA-ZñÑá-úÁ-Ú ]*$', message='La palabra solo puede contener letras.')
  ])

  idioma = RadioField('idioma', choices=['es', 'en'],
  validators=[
      validators.DataRequired(message='Selecciona un idioma.')
  ])