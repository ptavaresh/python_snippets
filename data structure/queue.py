class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

    def mostrar(self):
        return self.items

c=Cola()

c.agregar(4)
c.agregar('perro')
c.agregar(True)

print(c.tamano())
print(c.mostrar())
c.avanzar()
print(c.mostrar())
