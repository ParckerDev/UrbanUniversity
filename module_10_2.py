from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        super().__init__()

    