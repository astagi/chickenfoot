import socket
from binder import Binder
from commandparser import CommandParser
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20

class Chickenfoot:

    def __init__(self):
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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((TCP_IP, TCP_PORT))
        s.listen(1)

        conn, addr = s.accept()
        print 'Connection address:', addr
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if data:
                print "received data:", data
                (action, namevalue) = self.cparser.parse(data)
                self.binder.execute(action, **namevalue)
        conn.close()

