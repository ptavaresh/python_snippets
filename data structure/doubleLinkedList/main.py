"""
Lista doblemente enlazada
Una listadoblemente enlazada es una lista enlazada de nodos,
donde cada uno tiene un par de campos de enlace, uno al nodo siuguiente y otro al anterior.

Caracteristicas:

1: Recorrer la estructura en ambos sentidos, de inicio a fin y de fin a inicio.
2:Borrando mas simple de datos
3:Estructura dinamica
"""

from doubleLinkedList import ListaDoblementeEnlazada
from os import system

system('clear')

lista = ListaDoblementeEnlazada()

lista.agregar_final(12)
lista.agregar_final(56)
lista.agregar_final(21)
lista.agregar_final(10)
lista.agregar_final(11)

lista.recorrer_inicio()
print('*'*25)
lista.recorrer_fin()
lista.agregar_final(15)
lista.agregar_inicio(15)
print('*'*25)
lista.recorrer_inicio()

