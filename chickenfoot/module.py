from binder import Binder

class Module:

    def __init__(self, **params):
        self.binder = Binder()

    def execute(self, id, **data):
        self.binder.execute(id, **data)