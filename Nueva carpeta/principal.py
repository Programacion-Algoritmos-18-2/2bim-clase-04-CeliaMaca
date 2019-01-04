# Se importa la clase a ejecutar
from modelado.mimodelo import *

class Principal:
  # Creación de objetos por constructor
  estudiante1 = Estudiante("Julio", "Zapata", 35, 10.2)
  estudiante2 = Estudiante("Pedro", "Andrade", 20, 18.1)
  estudiante3 = Estudiante("Vanesa", "Gallardo", 45, 15.6)
  estudiante4 = Estudiante("Beatriz", "Lima", 33, 8.8)

  lista_estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4]
  lista =[]
  for r in lista_estudiantes:
    lista.append(r.nombre)
    #pass
  # operacion = Operaciones(lista_estudiantes)
  # print(operacion.ordenar())
  lista = [e.promedio for e in lista_estudiantes]
  lista = [e.nombre for e in lista_estudiantes]
  lista.sort()
  print(lista)
  # Se imprimen los objetos
  #print(estudiante1)
  #print(estudiante2)
  #print(estudiante3)
  #print(estudiante4)

