#!/usr/bin/env python
from chickenfoot import Chickenfoot
from chickenfoot import Amotor
from chickenfoot import Pmotor
from chickenfoot.tcp_communicator import TcpCommunicator

comm = TcpCommunicator(ip='127.0.0.1', port=5005)
cf = Chickenfoot(comm)
cf.add_module('M1', Amotor(pin=4))
cf.add_module('M2', Pmotor(pin=5))
cf.listen()
