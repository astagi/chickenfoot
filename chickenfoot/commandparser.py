import json

class CommandParser:

    def __init__(self):
        pass

    def parse(self, data):
        data = json.loads(data)
        module = data['m']
        action = data['a']
        if 'p' in data:
            parameters = data['p']
        else:
            parameters = None
        return (module, action, parameters)