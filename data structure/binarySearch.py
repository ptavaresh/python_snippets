"""
Busqueda Binaria

Funcionamiento:
Buscar datos en una coleccion de datos

Ventajas:
Realiza menos comparaciones que el metodo de Busqueda Lineal

Requisitos antes de realizar el algoritmo:
Tener la lista ordenada de manera acendente (MENOS A MAYOR)

Algoritmo:
1: Calcular el punto medio, (izquierda + derecha) / 2
2: Comparar el punto medio con el dato a buscar
3: Si es igual el dato al punto medio, izquierda es igual al valor del medio + 1
4: Si el dato a buscar es mayor que el punto medio, izquierda es igual al valor del medio + 1
5: Si el dato a buscar es menor que el punto medio, derecha es igual al valor dl medio -1
6: Se seguira ejecutando siempre y cuando izquierda sea menor o igual a derecha
"""

def busqueda_binaria(dato):
    izquierda = 0
    derecha = len(lista)-1
    while izquierda <= derecha:
        medio = (izquierda + derecha)//2
        if dato == lista[medio]:
            return medio
        elif dato < lista[medio]:
            derecha = medio -1
        else:
            izquierda = medio + 1
    return None

def buscar(dato):
    if busqueda_binaria(dato) == None:
        return "El dato %d no se encontro"%(dato)
    else:
        return "El dato %d se encontro en el indice: %d"%(dato, busqueda_binaria(dato))

lista = [5,12,15,30,50,65,70,87,88,96]

for i in range(len(lista)):
    print("[%d] => %d"%(i, lista[i]))

print(buscar(70))