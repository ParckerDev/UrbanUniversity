class IncorrectVinNumber(Exception):
        def __init__(self, message):
             self.message = message


class IncorrectCarNumbers(Exception):
     def __init__(self, message):
          self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        self.__numbers = numbers

    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if isinstance(vin_number, int) and (1000000 > vin_number or 9999999 < vin_number):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True
        
    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if isinstance(numbers, str) and len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True
         

