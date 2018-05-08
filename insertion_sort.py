"""
Insertion sort

1.- We need to loop the list (starting at index: 1)
2.- it compares if the element in the left is lower than the current one
3.- If the condition matches, it swaps the values
4.- The loop continues comparing the elements in the left and if they are lower they swaps the position
"""

lista = [5, 10, 3,12,10, 6]

for i in range(1,len(lista)):
    aux = lista[i]
    j = i - 1
    while j >= 0 and aux < lista[j]:
        lista[j+1] = lista[j]
        lista[j] = aux
        j -= i
print(lista)
