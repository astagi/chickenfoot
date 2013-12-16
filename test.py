#!/usr/bin/env python
from chickenfoot import Chickenfoot
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

class Client():

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((TCP_IP, TCP_PORT))

    def left(self):
        bundle = """
        {
            "module" : "M1",
            "action" : "rl",
            "parameters" : {  
                "p1name" : "p1",
                "p2name": 5
            }
        }
        """
        self.__send(bundle)

    def right(self):
        bundle = """
        {
            "module" : "M1",
            "action" : "rr",
            "parameters" : {  
                "p1name" : "p1"
            }
        }
        """
        self.__send(bundle)

    def up(self):
        bundle = """
        {
            "module" : "M2",
            "action" : "fw",
            "parameters" : {  
                "p1name" : "p1",
                "p2name" : "p2"
            }
        }
        """
        self.__send(bundle)

    def down(self):
        bundle = """
        {
            "module" : "M2",
            "action" : "rw"
        }
        """
        self.__send(bundle)

    def __send(self, data):
        self.s.send(data + "\0")

    def shutdown(self):
        self.s.close()

client = Client()
client.left()
client.right()
client.up()
client.down()
client.shutdown()

