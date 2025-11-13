import math
def area_rectangle(a, b):
    """Calculating the area of a rectangle.\n
    Requires length and width as parameters."""
    return a * b

def area_triangle(base, height):
    """Calculating the area of a triangle.\n
    Requires base and height as parameters."""
    return 0.5 * base * height

def area_circle(r):
    """Calculating the area of a circle.\n
    Requires radius as parameter."""
    return math.pi * r * r