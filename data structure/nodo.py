"""
Nodo:
En programacion, concretamente en estructuras de datos, un nodo 
es uno de los elementos de una lista enlazada, de un arbol o de un grafo. 
Cada nodo sera una estructura o registro que se dispondra de varios campos, 
y al menos uno de esos campos sera u puntero o referencia a otro nodo,
de forma que, conocio un nodo, a partir de esa refenrecia, sera posible
en teoria tener acceso a otros nodos de la estructura.
"""

from os import system
system("clear")

class Nodo():

    def __init__(self, dato, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

def recorrer(nodo):
    while nodo != None:
        print(nodo.dato)
        nodo = nodo.siguiente

nodo4 = Nodo(12)
nodo3 = Nodo(45, nodo4)
nodo2 = Nodo(67, nodo3)
nodo1 = Nodo(89, nodo2)

recorrer(nodo1)

