from flask import render_template as view, redirect, url_for
from models.DiccionarioModel import Diccionario
from forms.DiccionarioForm import DiccionarioForm
from forms.TraductorForm import TraductorForm

class DiccionarioController:

  diccionario = Diccionario()

  @classmethod
  def index(cls, seccion):
    # diccionario = Diccionario()
    # p = 'verde'
    # palabras = diccionario.buscar_palabra(p)
    # print(f'{palabras["palabra"]} = {palabras["word"]}')
    seccion = 'agregar' if seccion == None else seccion
    return view('diccionario.j2', seccion = seccion)

  @classmethod
  def guardar(cls, _form):
    palabra = ''; word = ''
    form = DiccionarioForm(_form)
    if form.validate():
      palabra = form.palabra.data
      word = form.word.data
      cls.diccionario.guardar_palabra(palabra, word)
    return view('diccionario.j2', form = form)
  
  @classmethod
  def traducir(cls, _form):
    palabra = ''
    traduccion = None
    form = TraductorForm(_form)
    if form.validate():
      palabra = form.palabra.data
      tr = cls.diccionario.buscar_palabra(palabra)
      if tr: traduccion = tr['palabra'] if form.idioma.data == 'es' else tr['word']
    return view('diccionario.j2', form = form, seccion = 'traducir', traduccion = traduccion)