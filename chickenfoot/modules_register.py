from modules.front_motor import FrontMotor
from modules.back_motor import BackMotor

modules = {}

def get_module(module_name, **data):
    return modules[module_name](**data)

def register_module(module_name, cls):
    modules[module_name] = cls

register_module('FrontMotor', FrontMotor)
register_module('BackMotor', BackMotor)