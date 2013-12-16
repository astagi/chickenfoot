from amotor import Amotor
from pmotor import Pmotor

modules = {}

def get_module(module_name, **data):
    return modules[module_name](**data)

def register_module(module_name, cls):
    modules[module_name] = cls

register_module('Amotor', Amotor)
register_module('Pmotor', Pmotor)