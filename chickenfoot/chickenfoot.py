from binder import Binder
from commandparser import CommandParser

class Chickenfoot:

    def __init__(self, comm):
        self.modules = {}
        self.communicator = comm
        self.cparser = CommandParser()

    def add_module(self, id, module):
        self.modules[id] = module

    def listen(self):
        self.communicator.listen()
        while 1:
            data = self.communicator.receive()
            if data:
                (module, action, namevalue) = self.cparser.parse(data)
                self.modules[module].execute(action, **namevalue)
        self.communicator.close()

