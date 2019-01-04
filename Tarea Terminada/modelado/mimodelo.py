# Se crea la clase Estudiante
class Estudiante(object):
  def __init__(self, nombre, apellido, edad, promedio):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.promedio = promedio

  #Metodos set y get
  def agregarNombre(self, nombre):
    self.nombre = nombre

  def obtenerNombre(self):
    return self.nombre

  def agregarApellido(self, apellido):
    self.apellido = apellido

  def obtenerApellido(self):
    return self.apellido

  def agregarEdad(self, edad):
    self.edad = edad

  def obtenerEdad(self):
    return self.edad

  def agregarPromedio(self, promedio):
    self.promedio = promedio

  def obtenerPromedio(self):
    return self.promedio

  # Método para imprimir
  def __str__(self):
    return "%s - %s - %s - %f" % (self.nombre, self.apellido, self.edad, self.promedio)