from module_6_Figure import Figure
from math import pi


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = round(self.__len__()/(2*pi), 2)

    def get_square(self):
        return self.__radius**2 * pi


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = 0.5*(len(self))
        a, b, c = self.get_sides()
        square = p*(p-a)*(p-b)*(p-c)
        return square


class Cube(Figure):
    sides_count = 12

    '''def __init__(self, color, *sides):
        if len(sides) != 1:
            self.__sides = [1 for _ in range(12)]
        else:
            side = int(*sides)
            self.__sides = [side for _ in range(12)]
            super().__init__(color, side)'''
        



# TESTS
# Circle
circle1 = Circle((255, 252, 46), 25)
print(circle1.__dict__)
print(circle1.get_sides())
print(len(circle1))
print()

# Triangle
triangle = Triangle((45, 7, 99), 5, 10, 20) # type: ignore
print(triangle.__dict__)

# CUBE
cube = Cube((56, 150, 250), 25, 5) # type: ignore
print(cube.__dict__)
print(cube.get_color())
print(cube.get_sides())