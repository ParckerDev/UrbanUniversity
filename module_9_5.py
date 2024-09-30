class StepValueError(ValueError):
    pass

class Iterator():
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step != 0:
            self.step = step
        else:
            raise StepValueError ('шаг не может быть равен 0')
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self
    
    def __next__(self):
        self.pointer += self.step
        if self.step > 0 and self.pointer <= self.stop:
            return self.pointer
        if self.step < 0 and self.pointer >= self.stop:
            return self.pointer
        else:
            return "The end"
        raise StopIteration()
    

    