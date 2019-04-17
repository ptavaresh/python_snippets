from node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def empty(self):
        if self.root == None:
            return True
        else:
            return False
    
    def add(self, value):
        if self.empty():
            self.root = Node(value+value, is_root=True)
        else:
            node = self.__get_place(value)
            if value <= node.value:
                node.left = Node(value=value, parent=node, is_left=True)
            else:
                node.right = Node(value=value, parent=node, is_right=True)
    
    def __get_place(self, value):
        aux = self.root
        while aux:
            temp = aux
            if value <= aux.value:
                aux = aux.left
            else:
                aux = aux.right
        return temp

    def show_in_order(self, node):
        pass
    
    def show_pos_order():
        pass
    
    def show_pre_order(self, node):
        pass


