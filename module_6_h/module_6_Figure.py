
class Figure:
    # Doc string
    sides_count = 0
    def __init__(self, color: tuple[int], *sides, filled: bool = True):
        # проверяем количество переданных сторон
        if len(sides) != self.sides_count: # если сторон не столько же, чему равно количесво сторон в классе, то
            self.__sides = [1 for _ in range(self.sides_count)] # стороны будут равняться 1 каждая.
        else: # если количество сторон совпадает
            if self.sides_count == 3: # проверяем могут ли заданные стороны быть сторонами треугольника
                if self.is_triangle(sides):
                    self.__sides = list(sides) # если могут, то присваиваем их в sides
                else:
                    print('Введённые стороны не могут быть сторонами треугольника!\nПриняты служебные размеры сторон равные "1"!!!')
                    self.__sides = [1, 1, 1] # если не могут, то стороны будут равны 1
            if self.sides_count == 1:
                self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    @staticmethod
    def is_triangle(sides):
        a, b, c = sides
        return (a + b) > c and ((a + c) > b) and ((b + c) > a)

    def get_color(self) -> list:
        return self.__color
    
    # проверка переменных цвета на валидность
    @staticmethod
    def __is_valid_color(*rgb):
        if len(rgb) == 3:
            for num in rgb:
                if (0 > num or num > 255) or not isinstance(num, int):
                    print('wrong color digits')
                    return False
            print('True color')
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
        if self.__is_valid_sides(*args):

            self.__sides = list(args)