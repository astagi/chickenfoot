from binder import Binder
from commandparser import CommandParser
from modules_register import get_module
from service_register import services
from communications_register import get_communication
import json
from nanpy import serial_manager
from nanpy import Arduino

class Chickenfoot:

    def __init__(self):
        self.modules = {}
        self.communicator = None
        self.services = None
        self.cparser = CommandParser()

    def init_from_file(self, filename):
        json_file_content = open(filename, 'r').read()
        self.params = json.loads(json_file_content)
        if 'nanpy_dev' in self.params['arduino']:
            serial_manager.open(self.params['arduino']['nanpy_dev'])
        self.set_communication(self.params['communication']['type'], **self.params['communication']['parameters'])
        for module in self.params['modules']:
            self.add_module(module['name'], module['type'], **module['parameters'])

    def set_communication(self, comm_name, **data):
        self.communicator = get_communication(comm_name, **data)

    def add_module(self, id, module_name, **data):
        self.modules[id] = get_module(module_name, **data)

    def listen(self):
        self._start_services()
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

    def _start_services(self):
        json_services = self.params['services']
        for service in services:
            current_service = services[service]()
            current_service.execute(json_services[service])

