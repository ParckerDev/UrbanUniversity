

class Vehicle:
    _COLOR_VARIANTS = ['black', 'white', 'red', 'yellow', 'gray']
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'
    
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    
    def get_color(self):
        return f'Цвет: {self.__color}'
    
    def get_owner(self):
        return f'Владелец: {self.owner}'
    
    def print_info(self):
        print(self.get_model(),
              self.get_horsepower(),
              self.get_color(),
              self.get_owner(),
              sep='\n')
        
    def set_color(self, new_color: str):
        if new_color.lower() not in self._COLOR_VARIANTS:
            print(f'Нельзя сменить цвет на {new_color}')
        else:
            self.__color = new_color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



# TESTS

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()