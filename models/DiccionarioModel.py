class Diccionario:
  
  def guardar_palabra(self, palabra, word) -> None:
    file = open('./storage/diccionario.dic', 'a')
    file.write(f'{palabra}={word}\n')
    file.close()
  
  def buscar_palabra(self, palabra) -> str:
    for clave, valor in self.diccionario():
      if palabra.upper() in clave.upper() or palabra.upper() in valor.upper():
        return {'palabra': clave, 'word': valor}

  def diccionario(self) -> list:
    diccionario = {}
    file = open("./storage/diccionario.dic")
    for linea in file:
      (clave, valor) = linea.split('=')
      diccionario[clave] = valor.replace('\n', '')
    file.close()
    return diccionario.items()