"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    x = num1 + num2
    return x


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    y = num1 - num2
    return y


def multiply(num1, num2):
    """Multiply the two inputs together."""
    a = num1 * num2
    return a


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    b = num1 / num2
    return b


def square(num1):
    """Return the square of the input."""
    c = num1 ** 2
    return c


def cube(num1):
    """Return the cube of the input."""
    d = num1 ** 3
    return d


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    e = num1 ** num2
    return e


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    f = num1 % num2
    return f


def square_root(num1):
    """Return the square root of the input."""
    g = num1 ** 0.5
    return g


def add_multiply(num1, num2, num3):
    """returns the sum of num1 and num2 multiplied by num3"""
    h = (num1 + num2) * num3
    return h


def cubes_sum(num1, num2):
    """Returns the sum of the cubes of num1 and num2."""
    i = cube(num1) + cube(num2)
    return i
