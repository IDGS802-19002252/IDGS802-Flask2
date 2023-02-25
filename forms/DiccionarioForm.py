from wtforms import Form, StringField, validators
import forms.validators.DuplicadoValidator as custom_val

class DiccionarioForm(Form):

  palabra = StringField('palabra', [
      validators.DataRequired(message='La palabra es obligatoria.'),
      validators.Length(min=3, message='La palabra debe tener al menos 3 caracteres.'),
      validators.Regexp('^[a-zA-ZñÑá-úÁ-Ú ]*$', message='La palabra solo puede contener letras.'),
      custom_val.validate_duplicado
    ])

  word = StringField('word', [
      validators.DataRequired(message='La traducción es obligatoria.'),
      validators.Length(min=3, message='La traducción debe tener al menos tres letras.'),
      validators.Regexp('^[a-zA-Z ]*$', message='La traducción solo puede contener letras.'),
      # custom_val.validate_duplicado(message='La traducción ya se encuentra en el diccionario.')
    ])