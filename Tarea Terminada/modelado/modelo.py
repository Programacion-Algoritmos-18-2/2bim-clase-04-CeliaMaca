# Se crea la clase Equipo
class Equipo(object):
  def __init__(self, nombre, ciudad, campeonatos, numJugadores):
    self.nombre = nombre
    self.ciudad = ciudad
    self.campeonatos = int(campeonatos)
    self.numJugadores = numJugadores

  #Metodos set y get
  def agregarNombre(self, nombre):
    self.nombre = nombre

  def obtenerNombre(self):
    return self.nombre

  def agregarCiudad(self, ciudad):
    self.ciudad = ciudad

  def obtenerCiudad(self):
    return self.ciudad

  def agregarCampeonatos(self, campeonatos):
    self.campeonatos = int(campeonatos)

  def obtenerCampeonatos(self):
    return self.campeonatos

  def agregarNumJugadores(self, numJugadores):
    self.numJugadores = numJugadores

  def obtenerNumJugadores(self):
    return self.numJugadores

  # Método para imprimir
  def __str__(self):
    return "%s - %s - %d - %f" % (self.nombre, self.ciudad, self.campeonatos, self.numJugadores)

class OperacionesEquipo(object):
  def __init__(self, listado):
    self.listadoEquipos = listado

  # Ordenar los objetos por nombres
  def ordenarPorNombre(self):
    nombre = ""
    for n in self.listadoEquipos:
      nombre = nombre + n.obtenerNombre() + ", "
    return nombre

  # Ordenar los objetos por campeonatos
  def ordenarCampeonatos(self):
    numero = 0
    nombre = []
    for n in self.listadoEquipos:
      numero = n.obtenerCampeonatos()
      nombre.append(numero)
      nombre.sort()
    return nombre

  def __str__(self):
    cadena = ""
    for n in self.listadoEquipos:
      cadena = "%d" %(self.ordenarPorNombre())
      cadena = "%d" %(self.ordenarCampeonatos())
    return cadena