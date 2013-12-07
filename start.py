#!/usr/bin/env python
from chickenfoot import Chickenfoot
from chickenfoot.tcp_communicator import TcpCommunicator

comm = TcpCommunicator(ip='127.0.0.1', port=5005)
cf = Chickenfoot(comm)
cf.listen()
