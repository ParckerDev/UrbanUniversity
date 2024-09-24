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
    # закомментировал потомучто реализовал создание сторон через родительский класс
    # Но жду от Вас комментариев!
    '''def __init__(self, color, *sides):
        if len(sides) != 1:
            self.__sides = [1 for _ in range(12)]
        else:
            side = int(*sides)
            self.__sides = [side for _ in range(12)]
            super().__init__(color, side)'''
    
    def get_volume(self):
        return self.get_sides()[0]**3



# lesson tests
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 230), 6)  # type: ignore

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
