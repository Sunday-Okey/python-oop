# Regular Instance Methods vs Class Methods vs Static Methods

# Instance Methods
# Can modify object instance state
# Can modify class state
import math

# Class Method
# Can't modify object instance state
# Can modify class state

# Static Method:
# Can't modify object instance state
# Can't modify class state
# https://realpython.com/instance-class-and-static-methods-demystified/


class MyClass:
    def method(self):
        return "instance method called", self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return "static method called"


obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())
# print(MyClass().)
print(MyClass.classmethod())
print(MyClass.staticmethod())


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.ingredients})"

    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'])

    def area(self):
        return self._circle_area(self.radius)

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi


# print(Pizza(['cheese', 'tomatoes']))
# print(Pizza.margherita())
# print(Pizza.prosciutto())

print(Pizza(4.5, ['cheese']).area())
print(Pizza._circle_area)
