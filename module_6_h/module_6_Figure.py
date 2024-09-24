
class Figure:
    sides_count = 0
    def __init__(self, color: tuple[int], *sides, filled: bool = True):
        
        if len(sides) != self.sides_count: # проверяем количество переданных сторон
            self.__sides = [1 for _ in range(self.sides_count)]
        else:
            if self.sides_count == 3:
                if self.is_triangle(*sides):
                    self.__sides = list(sides)
                else:
                    self.__sides = [1, 1, 1]
            self.__sides = list(sides)
        self.__color = color
        self.filled = filled

    def is_triangle(sides):
        #a, b, c = sides
        print('check is triangle',*sides)
        #return ((a + b) > c) and ((a + c) > b) and ((b + c) > a)

    def get_color(self) -> list:
        return list(self.__color)
    
    @staticmethod
    def __is_valid_color(r, g, b):
        color = [r, g, b]
        for num in color:
            if (0 > num or num > 254) or not isinstance(num, int):
                print('wrong color digits')
                return False
        print('True color')
        return True
    
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        
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
        if self.__is_valid_sides(*args):

            self.__sides = list(args)