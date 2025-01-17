
# https://realpython.com/python-classes/
from pathlib import Path
import math


def circle_area(raduis):
    return math.pi * pow(raduis, 2)


print(circle_area(3))

circle = {
    'raduis': 3,
    "color": "blue"
}
print(circle_area(circle['raduis']))

person = {
    "first": "Geralt",
    "last": "of Rivia"
}

employee = {
    "first": "Yennefer",
    "last": 'of Vengerberg',
    "ID": 3023342
}

print(Path)
p = Path('class-concepts.py')
print(p.name)
print(p.exists())
# print(dir(p))


class Circle:
    def __init__(self, raduis):
        self.raduis = raduis

    def area(self):
        return self.raduis ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.raduis

    def __repr__(self):

        return f'Circle({(self.raduis)})'


small = Circle(3)
large = Circle(42)
print(small)
print(small.raduis)
print(small.area())

name = 'Sunday'
print(name)
print(large.raduis)
print(large.area())

# Atrributes are also editable
large.raduis = 8
print(large.area())


class ObjectCounter:
    num_instances = 0

    def __init__(self):
        # To access the class attributes
        # use the name of the class
        ObjectCounter.num_instances += 1


one = ObjectCounter()
print(one)

# Object inherits the attributes of its class
print(one.num_instances)

two = ObjectCounter()
print(two)

# Object attributes are shared among all instances
print(two.num_instances)
print(one.num_instances)
print(ObjectCounter.num_instances)

# Class vs Instance Attributes
# Class attributes can be accessed through an object instance
# Class attributes can only be modified through the Class reference
# Objects can have attributes assigned dynamically
# Attempting to assign a class attribute through the object results in the creation of an instance attribute

one = ObjectCounter()
print(one.num_instances)
print(ObjectCounter.num_instances)

one.value = 42
print(one.value)

one.num_instances = 85
print(ObjectCounter.num_instances)
print(one.num_instances)

# Get class attributes
# Get an object class
one.__class__
# Get an object class attribute
one.__class__.num_instances
print(one.__class__.num_instances)

# It is a good practice to access class attributes from the class its
# to avoid confusion

# Properties and Descriptors
# The @property decoratore allows you to create a method that is accessed like an attribute
# This means you can do calculation to return a value


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Must not take any arguments besides self
    # This makes sense because if you are accessing it as an attribute
    # You have no way of passing arguments in

    @property
    def full_name(self):
        return f"{self.first} {self.last}"


geralt = Person('Geralt', 'of Rivia')
print(geralt.first)
print(geralt.last)
# The property hides that this is method from the user

print(geralt.full_name)

# Discriptors
# The @property decorator is for accessing a value
# You can also set a value by defining a companion method
# Decorate the method using the property name and @.setter
# Allows you to perform side-effects when a value is set

# Perform caculations, caching or Error checks

# A common pattern you'll find in code:
# Argument .__init__() passes in initial value
# Value is assigned to private attribute
# @Property method with the same name uses the private attribute
# @.setter method with the same name sets the private attribute with error checking


class Circle:
    def __init__(self, radius):
        self._radius = radius

    # The property doesn't need an argument
    @ property
    def radius(self):
        return self._radius

    # The setter does need an argument - the new value being set
    @radius.setter
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError('Radius must be a positive number')
        self._radius = value

    def area(self):
        return self._radius ** 2 * math.pi


circle = Circle(3)
# Assigning a new value actually calls the setter
# circle.radius = "4"

# circle._radius = 9
print(circle.__dict__)
print(circle.radius)
print(circle._radius)
print(Circle.__dict__)
print(Circle.area(circle))

# Methods
# There are three types of methods in Python
# Instance methos, Class methos, Static methods

# Instance Methods
# The methods you've used so far are instance methdos
# Require an instantiated object
# Typically used to perform operations on associated data
# First argument is always an instance of the object
# By convention named self

# Class Methods
# Methods that operate on the class itself
# Created using the @classmethod decorator
# First argument is always a reference to the class
# By convention named cls
# Used for:
# Manipulating data common across all instances
# Factories
# A factory is a method that return an instance of a new object
# It's an alternative to a constructor and usually done if some sort of sides effect are to be achieved when creating an objects

# Statit Methods
# Static methods require neither a class nor instance
# Created using the @staticmethod decorator
# It can take arguments but none is required

# Typically used for
# Grouping data-less functions together (although this can be done equally well with a module)
# Very seldom needed in Python and always be achieved with a classmethod


class Vechicle:

    # def __init__(self):

    @classmethod
    def water_vehicle(cls, name, dimensions):
        vehicle = Vechicle()
        vehicle.name = name
        vehicle.dimensions = dimensions
        vehicle.floats = True
        vehicle.num_wheels = 0
        return vehicle

    @classmethod
    def road_vehicle(cls, name, dimensions, num_wheels):
        vehicle = Vechicle()
        vehicle.name = name
        vehicle.dimensions = dimensions
        vehicle.num_wheels = num_wheels
        vehicle.floats = False
        return vehicle

    def volume(self):
        return self.dimensions[0] * self.dimensions[1] * self.dimensions[2]

    @staticmethod
    def all_float(*vehicles):
        for vehicle in vehicles:
            if not vehicle.floats:
                return False
        return True


boat = Vechicle.water_vehicle('Minnow', (30, 40, 10))

print(boat.name)
print(boat.num_wheels)
print(Vechicle.__dict__)
print(boat.volume())

car = Vechicle.road_vehicle('Kitt', (4, 3, 1.5), 4)
print(car.name)
print(car.num_wheels)
print(boat.num_wheels)
print(car.volume())
# You call static method like you call the class method - on the class itself

print(Vechicle.all_float(boat))
print(Vechicle.all_float(boat, boat))
print(Vechicle.all_float(boat, boat, car))

# Quick Tangent
# When using a classmethod, the cls, reference is a class
# We can instantiate an object by calling it with parenthesis
# You can use the **kwargs mechanism to instantiate a class
# Key/value pairs in the dictionary become the arguments to the constructor
