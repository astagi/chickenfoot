class Binder:

    def __init__(self):
        self.binders = {}

    def bind(self, id, function):
        self.binders[id] = function

    def execute(self, id, **data):
        self.binders[id](**data)

