# Se importa la clase a ejecutar
from paquete_archivos.miarchivo import MiArchivo
from modelado.modelo import Equipo, OperacionesEquipo

m = MiArchivo()

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
# print(lista)
listaEquipos = []
lista = lista[1:]
lista.sort()

for d in lista:
  p = Equipo(d[0], d[1], d[2], d[3])
  listaEquipos.append(p)

operaciones = OperacionesEquipo(listaEquipos)

print("Nombres ordenados: ", operaciones.ordenarPorNombre())
print("Campeonatos ordenados: ", operaciones.ordenarCampeonatos())

'''class Principal:

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
  #print(estudiante4)'''

