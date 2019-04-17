

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

#tree.show_in_order(tree.root)
#tree.show_pos_order(tree.root)
tree.show_pre_order(tree.root)

