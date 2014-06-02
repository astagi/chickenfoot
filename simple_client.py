import socket
import time

TCP_IP = '192.168.0.6'
TCP_PORT = 5005
BUFFER_SIZE = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def receive():
    return 'ciao'

bundle = '{"m" : "M2","a" : "fw","p" : {"speed" : 5000}}'

s.send(bundle + "\n")
print receive()

time.sleep(3)