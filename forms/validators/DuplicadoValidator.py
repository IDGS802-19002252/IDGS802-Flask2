from wtforms import ValidationError
from models.DiccionarioModel import Diccionario

def validate_duplicado(form, field):
  diccionario = Diccionario()
  if diccionario.buscar_palabra(field.data) != None:
    raise ValidationError('La palabra ya se encuentra en el diccionario.')