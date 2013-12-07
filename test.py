#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005

class Client():

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((TCP_IP, TCP_PORT))

    def left(self):
        self.s.send("rl?p1n:p1-p2n:p2")

    def right(self):
        self.s.send("rr?p1n:p1-p2n:p2")

    def shutdown(self):
        self.s.close()

client = Client()
client.left()
client.shutdown()

