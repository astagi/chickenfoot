from chickenfoot.communication import Communication
import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 19

class TcpCommunication(Communication):

    def __init__(self, **config):
        if 'ip' in config:
            self.ip = config['ip']
        else:
            self.ip = TCP_IP
        if 'port' in config:
            self.port = config['port']
        else:
            self.port = TCP_PORT
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self):
        self.s.bind((self.ip, self.port))
        self.s.listen(1)
        self.conn, addr = self.s.accept()
        print 'Connection address:', addr

    def receive(self):
        data = self.conn.recv(BUFFER_SIZE)
        if data:
            print "received data:", data
            return data

    def close(self):
        self.conn.close()