# Class constructors are a fundamental part of object-oriented programming in Python. They allow you to create and properly initialize objects of a given class, making those objects ready to use. Class constructors internally trigger Python’s instantiation process, which runs through two main steps: instance creation and instance initialization.
# Understand Python’s internal instantiation process
# Customize object initialization using .__init__()
# Fine-tune object creation by overriding .__new__()

# With this knowledge, you’ll be able to tweak the creation and initialization of objects in your custom Python classes, which will give you control over the instantiation process at a more advanced level.
from random import choice
from operator import itemgetter
# https://realpython.com/python-class-constructor/


class SomeClass:
    pass


print(SomeClass())

# The class instantiation process
# Creation, Initialization and Return

# calling a class is not the same as calling the instance of class
# To make a class object callable
# implement .__call__() Method Needed # Nothing to do with python instantiation process

# Understanding Python's Instantiation process
# Create a new instance of the target class
# Initialize the new instance with an appropriate initial state


# Instance Creation
# Special Method .__new__()
# Creates and returns a new empty object
# Instance initialization
# Special method .__init__()
# new object passed as self
# Sets required instance to a valid state

# Practical Example: The Point class


class Point:
    def __new__(cls, *args, **kwargs):
        print('1. Create a new instance of Point.')
        # Create a new point instance by calling the parent classes __new__(cls)
        return super().__new__(cls)
        # This instance will be the first argument to init

    def __init__(self, x, y):
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

# A sutle and important detail to note about the __new__() method is that
# It can also return the instance of a class different from the class that implements the method itself
# When that happens, python does not call the .__init__() in the current class


class A:
    def __init__(self, a_value):
        print("Initialize the new instance of A.")
        self.a_value = a_value


class B:
    def __new__(cls, *args, **kwargs):
        return A(42)

    def __init__(self, b_value):
        print('Initialize the new instance of B.')
        self.b_value = b_value


# point = Point(21, 42)
# print(point)
# Object Initialization with .__init__()
# The most commonly overriden special method
# Almost all classes need a custom .__init__()
# Allows proper Initialization

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


rectangle = Rectangle(21, 42)
print(rectangle.width)
print(rectangle.height)

# __init__() for transformation


class Rectangle:
    def __init__(self, width, height):
        if not (isinstance(width, int | float) and width > 0):
            raise ValueError(f"positive width expected, got {width}")
        self.width = width
        if not (isinstance(height, int | float) and height > 0):
            raise ValueError(f"positive height expected, got {height}")
        self.height = height


# rectangle = Rectangle(3, -5)
# print(rectangle)

# Using .__init__() with Inheritance
# .__init__() Must call base class .__init__()
# Use super() to do this

class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date


class Employee(Person):
    def __init__(self, name, birth_date, position):
        super().__init__(name, birth_date)
        self.position = position


john = Employee('John Doe', '2001-02-02', "Python Developer")

print(john.name)
print(john.birth_date)
print(john.position)

# .__init__() comes from object base class
# Automatically called when .__init__() is not overridden

# Building Flexible Object Initializers
# Optional Arguments
# Allows constructor to accept different sets of arguments
# argumenst depend on context


class Greeter:
    def __init__(self, name, formal=False):
        self.name = name
        self.formal = formal

    def greet(self):
        if self.formal:
            print(f"Good morning, {self.name}")
        else:
            print(f"Hello, {self.name}!")


informal_greeter = Greeter("Pythonista")
informal_greeter.greet()

# Object Creating with .__new__()
# Custom .__new__() normally not needed
# Base implementation from object sufficient
# Some interesting use cases
# Subclassing int, float, tuple, string

# Providing custome object creators

# Create a new instance with super().__new__()
# Customize the New instance
# Return the new instance


class SomeClass:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        # Customize your instance here --
        return instance
# Object.__new__()
# Only accepts a single argument - cls
# Passes over arguments to .__init__() if not overridden


class SomeClass:
    def __init__(self, value):
        self.value = value


some_obj = SomeClass(42)
print(some_obj)

# Subclassing Immutable Built-in Types
# Distance as a sublcass of float type


# class Distance(float):
#     def __init__(self, value, unit):
#         super().__init__(value)
#         self.unit = unit


# in_miles = Distance(42.0, 'Miles')
# print(in_miles)
# Problems with this approach
# Value is set during creation
# float.__new__() extra argument behavvior is differnt


class Distance(float):
    def __new__(cls, value, unit):
        instance = super().__new__(cls, value)
        instance.unit = unit
        return instance


in_miles = Distance(42.0, 'Miles')
print(in_miles)
print(in_miles.unit)
print(in_miles + 42.0)
# print(dir(in_miles))

# Returning instances of a different class
# Python skips .__init__()
# Initialization is your responsibility


class Pet:
    def __new__(cls):
        other = choice([Dog, Cat, Python])
        instance = super().__new__(other)
        print(f"I am a {type(instance).__name__}")
        return instance

    def __init__(self):
        print("Never runs!")


class Dog:
    def communicate(self):
        print('woof! woof!')


class Cat:
    def communicate(self):
        print("meow! meow!")


class Python:
    def communicate(self):
        print("hiss hiss!")


pet = Pet()
pet.communicate()

# Allowing only as single instance in your classes


class Singleton(object):
    _instance = None

    def __new__(cls, *arg, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


first = Singleton()
second = Singleton()
print(first is second)

# Partially emulating collection.namedtuple
# Factory Function
# Create Subclasses of tuple
# The namedtuple allows you to create a subcass of tuple
# with having named fields for accessing the items in the tuple


def named_tuple_factory(type_name, *fields):
    num_fields = len(fields)

    class NamedTuple(tuple):
        __slots__ = ()

        def __new__(cls, *args):
            if len(args) != num_fields:
                raise TypeError(
                    f"{type_name} expected exactly {num_fields}"
                    f"argumets, got {len(args)}"
                )
            cls.__name__ = type_name
            for index, field in enumerate(fields):
                setattr(cls, field, property(itemgetter(index)))
            return super().__new__(cls, args)

        def __repr__(self):
            return f"""{type_name} ({", ".join(repr(arg) for arg in self)})"""
    return NamedTuple


Point = named_tuple_factory("Point", 'x', "y")
point = Point(21, 42)
print(point)
print(point.x)
print(point.y)
print(point[0])
print(point[2])
# print(point[2])
