from flask import Flask, request, redirect, make_response, render_template, flash
from flask_wtf import CSRFProtect
from werkzeug.exceptions import MethodNotAllowed

import formularios

from controllers.DiccionarioController import DiccionarioController

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
csrf = CSRFProtect()

@app.route('/', methods=['GET'])
def root(): return DiccionarioController.index(request.args.get('seccion'))

@app.route('/guardar', methods=['POST'])
def guardar(): return DiccionarioController.guardar(request.form)

@app.route('/traducir', methods=['POST'])
def traducir(): return DiccionarioController.traducir(request.form)

@app.before_request
def before_request():
  print('before_request')

@app.after_request
def after_request(response):
  print('after_request')
  return response

@app.route("/cookies", methods=["GET", "POST"])
def cookies():
  print('cukis')
  reg_user = formularios.LoginForm(request.form)
  if request.method == 'POST' and reg_user.validate():
    user = reg_user.username.data
    passw = reg_user.password.data
    datos = user + '@' + passw
    flash("Bienvenido {}".format(user))
    resp = make_response(render_template("cookies.j2", form = reg_user))
    resp.set_cookie('username', user)
    resp.set_cookie('password', passw)
    resp.set_cookie('datos', datos)
    return resp
  return render_template("cookies.j2", form = reg_user)

@app.route('/saludo')
def saludo():
  valor_cookie = request.cookies.get('datos') or 'No hay datos'
  nombre = valor_cookie.split('@')
  return render_template("saludo.j2", nom=nombre)

@app.errorhandler(MethodNotAllowed)
def method_not_allowed(e): return redirect('/')

@app.errorhandler(404)
def page_not_found(e): return render_template('404.j2')

if __name__ == '__main__':
  app.run(debug=True)