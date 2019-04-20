

from binary_search import BinarySearchTree

tree = BinarySearchTree()

tree.add(8)
tree.add(10)
tree.add(3)
tree.add(14)
tree.add(13)
tree.add(1)
tree.add(6)
tree.add(4)
tree.add(7)

print('Order')
tree.show_in_order(tree.root)
print('Pos-order')
tree.show_pos_order(tree.root)
print('pre -order')
tree.show_pre_order(tree.root)

#print(tree.search(tree.root, 10).value)
#print(tree.search(tree.root, 10).is_left)
#print(tree.search(tree.root, 10).parent.value)

"""
En orden
izquierda - raiz - derecha
# 1, 3, 4, 6, 7, 8, 10, 13, 14 
"""

"""
Pos orden
isquierda - deracha - raiz
1, 4, 7, 6 ,3 ,13 ,14 ,10, 8
"""

"""
Pre orden
raiz - izquierda - deracha
8, 3, 1, 6, 4, 7, 10 ,14 ,13

"""