from flask import Flask, request, redirect
from werkzeug.exceptions import MethodNotAllowed

from controllers.DiccionarioController import DiccionarioController

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root(): return DiccionarioController.index(request.args.get('seccion'))

@app.route('/guardar', methods=['POST'])
def guardar(): return DiccionarioController.guardar(request.form)

@app.route('/traducir', methods=['POST'])
def traducir(): return DiccionarioController.traducir(request.form)

@app.errorhandler(MethodNotAllowed)
def method_not_allowed(e): return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)