import json

class CommandParser:

    def __init__(self):
        pass

    def parse(self, data):
        data = json.loads(data)
        module = data['module']
        action = data['action']
        if 'parameters' in data:
            parameters = data['parameters']
        else:
            parameters = None
        return (module, action, parameters)