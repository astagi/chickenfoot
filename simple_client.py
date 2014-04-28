import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def receive():
    c = ''
    data = ""
    while c != '\0':
        c = s.recv(BUFFER_SIZE)
        data = data + c
    return data[:-1]

bundle = """
{
    "m" : "M2",
    "a" : "fw",
    "p" : {
        "speed" : 5000
    }
}
"""

s.send(bundle + "\0")
print receive()

time.sleep(3)

bundle = """
{
    "m" : "M2",
    "a" : "rw",
    "p" : {
        "speed" : 2000
    }
}
"""

s.send(bundle + "\0")
print receive()

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
print receive()

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
print receive()