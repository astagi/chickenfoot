import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

bundle = """
{
    "m" : "M2",
    "a" : "fw",
    "p" : {  
        "speed" : 1000
    }
}
"""

s.send(bundle + "\0")

time.sleep(3)

bundle = """
{
    "m" : "M2",
    "a" : "rw",
    "p" : {  
        "speed" : 1000
    }
}
"""

s.send(bundle + "\0")

time.sleep(3)

bundle = """
{
    "m" : "M1",
    "a" : "rl",
    "p" : {  
        "speed" : 1000
    }
}
"""

s.send(bundle + "\0")

time.sleep(3)

bundle = """
{
    "m" : "M1",
    "a" : "rr",
    "p" : {  
        "speed" : 1000
    }
}
"""

s.send(bundle + "\0")