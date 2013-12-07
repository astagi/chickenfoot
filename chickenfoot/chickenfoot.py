from binder import Binder
from commandparser import CommandParser

class Chickenfoot:

    def __init__(self, comm):
        self.communicator = comm
        self.binder = Binder()
        self.binder.bind('rl', self.left)
        self.binder.bind('rr', self.right)
        self.binder.bind('fw', self.fw)
        self.binder.bind('rw', self.rw)
        self.cparser = CommandParser()

    def left(self, **data):
        print data

    def right(self, **data):
        print data

    def fw(self, **data):
        print data

    def rw(self, **data):
        print data

    def listen(self):
        self.communicator.listen()
        while 1:
            data = self.communicator.receive()
            if data:
                (action, namevalue) = self.cparser.parse(data)
                self.binder.execute(action, **namevalue)
        self.communicator.close()

