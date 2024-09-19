from math import pi


class Figure:
    sides_count = 0
    def __init__(self,sides: list, color: list, filled: bool):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self) -> list:
        return self.__color
    
    @staticmethod
    def __is_valid_color(r: int, g: int, b: int):
        color = [r, g, b]
        for num in color:
            if not isinstance(num, int) or (0 <= num <= 255):
                return False
        return True
    
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        
    def __is_valid_sides(self, *args):
        if len(args) != self.sides_count:
            return False
        for num in args:
            if not isinstance(num, int) or num <= 0:
                return False
        return True
    
    def get_sides(self) -> list:
        return self.__sides
    
    def __len__(self):
        sum_ = sum(self.get_sides) # type: ignore
        return sum_
    
    def set_sides(self, *args):
        if self.__is_valid_sides(args):
            self.__sides = list(args)



class Circle(Figure):
    sides_count = 1

    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)
        self.__radius = self.__len__/(2*pi) # type: ignore

    def get_square(self):
        return self.__radius**2 * pi




class Triangle(Figure):
    pass


class Cube(Figure):
    pass