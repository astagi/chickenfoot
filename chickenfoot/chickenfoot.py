from binder import Binder
from commandparser import CommandParser
from modules_register import get_module
from communications_register import get_communication
import json

class Chickenfoot:

    def __init__(self):
        self.modules = {}
        self.communicator = None
        self.cparser = CommandParser()

    def init_from_file(self, filename):
        json_file_content = open(filename, 'r').read()
        params = json.loads(json_file_content)
        self.set_communication(params['communication']['type'], **params['communication']['parameters'])
        for module in params['modules']:
            self.add_module(module['name'], module['type'], **module['parameters'])

    def set_communication(self, comm_name, **data):
        self.communicator = get_communication(comm_name, **data)

    def add_module(self, id, module_name, **data):
        self.modules[id] = get_module(module_name, **data)

    def listen(self):
        self.communicator.listen()
        while 1:
            data = self.communicator.receive()
            if data:
                (module, action, parameters) = self.cparser.parse(data)
                if parameters:
                    self.modules[module].execute(action, **parameters)
                else:
                    self.modules[module].execute(action)
        self.communicator.close()

