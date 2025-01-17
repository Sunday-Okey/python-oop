# https://realpython.com/python-multiple-constructors/
from datetime import date
# Using Multiple Constructors in Your Python Classes
# Sometimes you need to write a Python class that provides multiple ways to construct objects. In other words, you want a class that implements multiple constructors. This kind of class comes in handy when you need to create instances using different types or numbers of arguments. Having the tools to provide multiple constructors will help you write flexible classes that can adapt to changing needs.
# Python offers several techniques and tools that you can use to construct classes, including simulating multiple constructors through optional arguments, customizing instance creation via class methods, and doing special dispatch with decorators.
# Use optional arguments and type checking to simulate multiple constructors
# Write multiple constructors using the built-in @classmethod decorator
# Overload your class constructors using the @singledispatchmethod decorator

# Instantiating Classes in Python
# Object-Oriented Programming
# Classes - The Blueprint for objects
# Instances - The individual objects


class Person:
    def __init__(self, name):
        self.name = name


# Special Methods
# Make iterable - __iter__()
# Provide string  representation - __repr__()
# Initialize instance attribute - __init__()
# ... and Many More
john = Person('John Doe')
print(john.name)

# New instance creation with __new__()
# Creates new instances
# often called class construct
# More accurately called
# Instance creator
# object creator
# Takes underlying class as first argument
# returns a new object
# Typically the input class - handles by __init__()
# Can be an instance of another class - __init__() omitted

# Object Class
# Provides Default implementations of
# __init__()
# __new__()
# __new__() rarely needs overriding

# Defining Multiple Class Constructors
# Arguments of different data types
# Different Number of arguments

# Method Names in Python
# Stored in an internal Dictionary - __dict__
# Holds the Class Namespace
# Dictionaries cannot support repeated keys
# Multiple Methods with the same name are not possible
# Only last implementation of a given nam is stored


class Greeter:
    def say_hello(self):
        return "Hello, World"

    def say_hello(self):
        return "Hello, Pythonista"


greet = Greeter()
print(greet.say_hello())
print(Greeter.__dict__)

# Multiple Dispatch
# Run different implementations of same method
# Dynamically dispatched depending on argument


# Simulating Multiple Class Constructors

# Provide __init__() with:
# Optional arguments and defaults
# Check data types passed to __init__()
# Change behavior as a result

# Using Optional Arguments Values in __init__()
# Optional arguments or appropriate Default values
# Undefined no of positional arguments or keyword arguments


# Cumulative PowerFactory
# Create Callable Objects
# Compute Specific Powers
# Total sum of powers stored
# Initial sum arguments

class CumulativePowerFactory:
    def __init__(self, exponent=2, *, start=0):
        self._exponent = exponent
        self.total = start

    # Turns the instances of the CumulativePowerFactory into callable objects
    def __call__(self, base):
        power = base ** self._exponent
        self.total += power
        return power


square = CumulativePowerFactory()
# print(square.__dict__)
# print(CumulativePowerFactory.__dict__)
print(square(21))
print(square(42))
print(square.total)

cube = CumulativePowerFactory(exponent=3)
print(cube(21))
print(cube(42))
print(cube.total)

initialized_cube = CumulativePowerFactory(3, start=2250)
print(initialized_cube(21))
print(initialized_cube(42))
print(initialized_cube.total)

# Optional Arguments are clean and Pythonic

# Checking Argument Types in __init__()


class Person:
    def __init__(self, name, birth_date):
        self.name = name
        if isinstance(birth_date, date):
            self.birth_date = birth_date
        elif isinstance(birth_date, str):
            self.birth_date = date.fromisoformat(birth_date)
        else:
            raise ValueError(f"unsupported date format: {birth_date}")


jane = Person('John Doe', "2000-11-29")
print(jane.birth_date)
john = Person("John Doe", date(1998, 5, 15))
print(john.birth_date)

# This Technique does not scale well
