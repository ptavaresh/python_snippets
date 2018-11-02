def mydecorator(msg='Message'):

    def decorated(f):# calling the function to be decorated

        def wrapper(*args, **kwargs): # passing arguments
            print('Message is: ' + msg)
            print('Inside of the decorator before calling the function.')
            f(*args, **kwargs) # using the function to be decorated
            print('Inside of the decorator after calling the function.')

        return wrapper # return the function
    return decorated


@mydecorator(msg='Hello ') #decorator with attributes
def printName(name):
    print(name)

printName('pedro')


# class MyClass:
#     def method(self):
#         return 'instance method called', self
#
#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls
#
#     @staticmethod
#     def staticmethod():
#         return 'static method called'
#
# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         Pizza({self.ingredients})
#         return Pizza
#
#     @classmethod
#     def margherita(cls):
#         return cls(['cheese', 'tomatoes'])
#
#     @classmethod
#     def prosciutto(cls):
#         return cls (['cheese', 'tomatoes', 'ham', 'mushrooms'])
#
# obj = MyClass()
#
# print(obj.method())
# print(obj.classmethod())
# print(obj.staticmethod())
#
# print(Pizza.margherita())
# print(Pizza.prosciutto())
