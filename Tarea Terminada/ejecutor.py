# Se importa la clase a ejecutar
from paquete_archivos.miarchivo import MiArchivo
from modelado.modelo import Equipo, OperacionesEquipo

m = MiArchivo()

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
# print(lista)
listaEquipos = []
lista = lista[0:]
lista.sort()

for d in lista:
  p = Equipo(d[0], d[1], d[2], d[3])
  listaEquipos.append(p)

operaciones = OperacionesEquipo(listaEquipos)

print("Bienvenido\n¿Que desea hacer?\n1. Ordenar por equipos\n2. Ordenar por campeonatos")
print("Ingrese una opcion")
opcion = int(input())  # Obtiene una opcion

if opcion == 1:
  print("Nombres ordenados: ", operaciones.ordenarPorNombre())

if opcion == 2:
  print("Campeonatos ordenados: ", operaciones.ordenarCampeonatos())
