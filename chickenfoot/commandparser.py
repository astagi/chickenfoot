class CommandParser:

    def __init__(self):
        pass

    def parse(self, data):
        (module, data) = data.split('=')
        params = data.split('?')
        action = params[0]
        namevalue = {}
        if len(params) > 1:
            couples = params[1].split('-')
            for couple in couples:
                (name, value) = couple.split(":")
                namevalue[name] = value
        return (module, action, namevalue)