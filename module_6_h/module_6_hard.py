from module_6_Figure import Figure
from math import pi


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled=True):
        super().__init__(sides, color, filled)
        self.__radius = round(self.__len__()/(2*pi), 2)

    def get_square(self):
        return self.__radius**2 * pi




class Triangle(Figure):
    pass


class Cube(Figure):
    pass



# TESTS

circle1 = Circle((255, 252, 45), 35)
print(circle1.__dict__)
print(circle1.get_color())
circle1.set_color(54, 64, 30)
print(circle1.get_color())
print(circle1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())