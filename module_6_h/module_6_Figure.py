
class Figure:
    sides_count = 0
    def __init__(self,sides: tuple[int], color: tuple[int], filled: bool):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self) -> list:
        return list(self.__color)
    
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
        return list(self.__sides)
    
    def __len__(self):
        sum_ = sum(self.get_sides())
        return sum_
    
    def set_sides(self, *args):
        if self.__is_valid_sides(args):
            self.__sides = list(args)