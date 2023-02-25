# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#   return render_template('')

# file = open("alumnos.txt", "r")

# nombres = file.read()
# print(nombres)

# nombres2 = file.readlines()
# print(nombres2)
# file.close()

# for nombre in nombres2:
  # nombre = nombre.replace("\n", "")
  # print(nombre, end='')

# file = open("alumnos1.txt", "a")
# file.write("Pedro\n")
# file.write("Que\n")
# file.write("Gusto\n")
# file.write("De\n")
# file.write("Verte\n")
# file.close()

alumno = {'Matricula': '20112312', 'Nombre': 'Juan', 'Apellidos': 'Rocio', 'Edad': 28, 'Sexo': 'H'}
file = open("alumnos.txt", "w")
for word in alumno:
  file.write(f'{word}: {alumno[word]}\n')