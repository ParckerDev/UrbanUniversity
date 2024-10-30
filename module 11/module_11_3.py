import inspect
from pprint import pprint


class Monitor:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def is_work(self):
        print(f'Monitor {self.name} is work')

def introspection_info(obj):
    return {
        'type': type(obj),
        'name': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': inspect.getmodule(obj)
        }


number_info = introspection_info(Monitor('LG Flatron', 45, 24))
pprint(number_info)
