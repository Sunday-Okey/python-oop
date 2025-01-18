# Supercharge Your Classes With Python super()
# While Python isn’t purely an object-oriented language, it’s flexible enough and powerful enough to allow you to build your applications using the object-oriented paradigm. One of the ways in which Python achieves this is by supporting inheritance, which it does with super().
# Compose a class
# Use super() to access parent methods
# Understand single and multiple inheritance
# https://realpython.com/python-super/
class Square:
    pass


square = Square()
square.length = 3
print(square.length)
print(dir(square))
print(square.__class__)


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return 4 * self.length


square = Square(3)

print(square.length)
print(square.area())
print(square.perimeter())
print(dir(square))


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def what_am_i(self):
        return 'Rectangle'


rectangle = Rectangle(2, 4)
print(rectangle.area())
print(rectangle.perimeter())


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def what_am_i(self):
        return 'Square'


square = Square(5)
print(square.area())
print(square.perimeter())
print(square.__class__.__base__)


class Cube(Square):
    # Same paramters as Square, no need to redefine __init__
    def surface_area(self):
        face_area = self.area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

    def what_am_i(self):
        return 'Cube'

    def family_tree(self):
        # super() is a shortcut for super(Cube, self)
        return self.what_am_i() + ' child of ' + super().what_am_i()


cube = Cube(3)
print(cube.surface_area())
print(cube.volume())

# Calling an object's method
# When you call a method on an object, Python
# looks for a method with that name on the current object
# If it finds it, it calls it
# If it doesn't find it, it tries to find a method with that name in the parent object
# It keeps going up the inheritance chain until it finds the method or if it never finds it an AttributeError will be thrown


rectangle = Rectangle(2, 4)
print(rectangle.what_am_i())
square = Square(4)
print(square.what_am_i())

# Forms of super()
# super() called within a class method gives you access to the parent object
# super() can be called with parameters indicating the class and object to access
# super(class, object). This form doesn't even have to be inside the object method
# Inside a class method "super()" is a shortcut for super(my_class, self)

cube = Cube(3)
print(cube.what_am_i())

print(super(Cube, cube).what_am_i())
print(super(Square, cube).what_am_i())

cube = Cube(3)
print(cube.family_tree())

# Multiple Inheritance
# Multiple inheritance is the process of inheriting from multiple classes into your base class


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def what_am_i(self):
        return "Triangle"


class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def what_am_i(self):
        return "RightPyramid"


rightpyramid = RightPyramid(2, 3)
print(super(RightPyramid, rightpyramid).what_am_i())
print(rightpyramid.__class__)
print(rightpyramid.__class__.__bases__)
print(RightPyramid.__mro__)


class A:
    def __init__(self):
        print('A')
        super().__init__()


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


class X:
    def __init__(self):
        print('X')
        super().__init__()


class Forward(B, X):
    def __init__(self):
        print('Forward')
        super().__init__()


class Backward(X, B):
    def __init__(self):
        print('Backward')
        super().__init__()


forward = Forward()
print(forward)

backward = Backward()
