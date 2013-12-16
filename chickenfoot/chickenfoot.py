from binder import Binder
from commandparser import CommandParser
from module_register import get_module
from communicator_register import get_communicator
import json

class Chickenfoot:

    def __init__(self):
        self.modules = {}
        self.communicator = None
        self.cparser = CommandParser()

    def init_from_file(self, filename):
        json_file_content = open(filename, 'r').read()
        params = json.loads(json_file_content)
        self.set_communicator(params['communication']['type'], **params['communication']['parameters'])
        for module in params['modules']:
            self.add_module(module['name'], module['type'], **module['parameters'])


    def set_communicator(self, comm_name, **data):
        self.communicator = get_communicator(comm_name, **data)

    def add_module(self, id, module_name, **data):
        self.modules[id] = get_module(module_name, **data)

    def listen(self):
        self.communicator.listen()
        while 1:
            data = self.communicator.receive()
            if data:
                (module, action, namevalue) = self.cparser.parse(data)
                self.modules[module].execute(action, **namevalue)
        self.communicator.close()

