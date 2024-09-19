from module_6_Figure import Figure
from math import pi


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled=True):
        super().__init__(sides, color, filled)
        self.__radius = self.__len__()/(2*pi)

    def get_square(self):
        return self.__radius**2 * pi




class Triangle(Figure):
    pass


class Cube(Figure):
    pass



c1 = Circle([165], [255, 4, 78])
print(c1.get_color())