# https://realpython.com/python-multiple-constructors/
from datetime import date
from time import time
from pathlib import Path
from functools import singledispatchmethod
# Using Multiple Constructors in Your Python Classes
# Sometimes you need to write a Python class that provides multiple ways to construct objects. In other words, you want a class that implements multiple constructors. This kind of class comes in handy when you need to create instances using different types or numbers of arguments. Having the tools to provide multiple constructors will help you write flexible classes that can adapt to changing needs.
# Python offers several techniques and tools that you can use to construct classes, including simulating multiple constructors through optional arguments, customizing instance creation via class methods, and doing special dispatch with decorators.
# Use optional arguments and type checking to simulate multiple constructors
# Write multiple constructors using the built-in @classmethod decorator
# Overload your class constructors using the @singledispatchmethod decorator
import math
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

# Using Multiple Class Constructors

# Using @classmethod for multiple class constructors
# It turns a regular method into a class method
# Does not take an instance - self - as an argument
# Takes current class - cls - instead


class DemoClass:
    @classmethod
    def class_method(cls):
        return f"A class method from {cls.__name__}!"


demo = DemoClass()
print(demo.class_method())
print(DemoClass.class_method())

# Using classmethod as constructor
# Does not need an instance to be called
# Add multiple explicit constructors
# The @classmethod returns the instance
# Pythonic way to define multiple constructors
# Known as an alternative constructor


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(radius=diameter/2)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    @classmethod
    def create_from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __repr__(self):
        return f"{self.__class__.__name__}(raduis={self.radius})"


circle = Circle(42)
print(circle)
print(circle.area())
print(circle.perimeter())
circle = Circle.from_diameter(84)
print(circle)
print(circle.area())
print(circle.perimeter())

# Even though __init__ and classmethod are separate methods, you can use a classmethod to create an instance and then call __init__ behind the scenes to initialize the object's attributes.
# When you define a classmethod (e.g., frombirthyear), it typically serves as an alternative constructor for the class. When it creates a new instance of the class, it internally calls the __init__ method of that class, passing the necessary arguments.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def frombirthyear(cls, name, birthyear):
        age = date.today().year - birthyear
        return cls(name, age)

    def __repr__(self):
        return f"{self.name} is {self.age} years old"


# john = Person("John Doe", 34)
sam = Person.frombirthyear('Samuel Nweni', 1998)
# print(john)
print(sam)

# Commonly used
# Allows Precise Name Selection
# Makes code Readable and Maintainable

# Building a Polar Point From Cartesian Coordinates


class PolarPoint:
    def __init__(self, distance, angle):
        self.distance = distance
        self.angle = angle

    @classmethod
    def from_cartesian(cls, x, y):
        distance = math.dist((0, 0), (x, y))
        angle = math.degrees(math.atan2(y, x))
        return cls(distance, angle)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(distance={self.distance:.1f},angle={self.angle:.1f})"
        )


point1 = PolarPoint(13.0, 22.6)
print(point1)
point2 = PolarPoint.from_cartesian(12, 5)
print(point2)

# Providing Multiple class constructors
# Exploring Multiple class constructors in existing classes
# dict
# datetime.date
# pathlib.Path

allowed_animals = ["dog", "cat", "python", "turtle"]

animal_inventory = dict.fromkeys(allowed_animals, 0)
print(animal_inventory)
print(date.today())
print(date.fromtimestamp(1661241609))
print(date.fromtimestamp(time()))
print(date.fromordinal(738390))
print(date.fromisoformat("2022-08-23"))

print(Path.home())
print(Path.cwd())

# Using @singledispatchmethod for Multiple Class Constructors

# Single-Dispatch Generic Function


class DemoClass:
    @singledispatchmethod
    def generic_method(self, arg):
        return (f"Do something with argument of type: {type(arg).__name__}")

    @generic_method.register
    def _(self, arg: int):
        return "Implementation for an int argument..."

    @generic_method.register(str)
    def _(self, arg):
        print("Implemenation for a str argument...")


demo = DemoClass()
print(demo.generic_method(42))
print(demo.generic_method("Hello, World"))
print(demo.generic_method([1, 2, 3]))


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise ValueError(f"unsupported date format: {birth_date}")

    @__init__.register(date)
    def _from_date(self, birth_date):
        self.date = birth_date

    @__init__.register(str)
    def _from_isoformat(self, birth_date):
        self.date = date.fromisoformat(birth_date)

    @__init__.register(int)
    @__init__.register(float)
    def _from_timestamp(self, birth_date):
        self.date = date.fromtimestamp(birth_date)

    def age(self):
        return date.today().year - self.date.year


class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self._birth_info = BirthInfo(birth_date)

    @property
    def age(self):
        return self._birth_info.age()

    @property
    def birth_date(self):
        return self._birth_info.date


john = Person("John Doe", date(1998, 5, 15))
print(john.age)
print(john.birth_date)

jane = Person('Jane Doe', "2000-11-29")
print(jane.age)
print(jane.birth_date)
linda = Person("Linda Smith", 1011222000)

print(linda.age)
print(linda.birth_date)

# david = Person("David Smith", {"year": 2000, "month": 7, "day": 25})

# Single-Dispatch Function Limitation
# Relies on Sinle Argument
