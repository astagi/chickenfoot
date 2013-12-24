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
            "m" : "M1",
            "a" : "rl",
            "p" : {  
                "p1name" : "p1",
                "p2name": 5
            }
        }
        """
        self.__send(bundle)

    def right(self):
        bundle = """
        {
            "m" : "M1",
            "a" : "rr",
            "p" : {  
                "p1name" : "p1"
            }
        }
        """
        self.__send(bundle)

    def up(self):
        bundle = """
        {
            "m" : "M2",
            "a" : "fw",
            "p" : {  
                "p1name" : "p1",
                "p2name" : "p2"
            }
        }
        """
        self.__send(bundle)

    def down(self):
        bundle = """
        {
            "m" : "M2",
            "a" : "rw"
        }
        """
        self.__send(bundle)

    def stop(self):
        bundle = """
        {
            "m" : "M1",
            "a" : "stop",
            "p" : {  
                "p1name" : "stop"
            }
        }
        """
        self.__send(bundle)

    def stop_wheel(self):
        bundle = """
        {
            "m" : "M2",
            "a" : "stop",
            "p" : {  
                "p1name" : "stop_wheel"
            }
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
client.stop_wheel()
client.up()
client.down()
client.stop()
client.shutdown()

