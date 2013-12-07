#!/usr/bin/env python
'''
               ..oo800ooo..                    ..ooo008oo..
           .ox88888888'                          '888888888o.
        .o888888888"             .   .              "888888888o.
      .o8888888888~             /|   |\              ~8888888888o.
    .{88888888888.              8\___/8               .88888888888}.
   o8888888888888              .8888888.               8888888888888o
  888888888888888              888888888               888888888888888
 o888888888888888.             o8888888o              .888888888888888o
 88888888888888888.           o{8888888}o            .88888888888888888
^888888888888888888.         J88888888888L          .888888888888888888^
!88888888888888888888oo..oo88888888888888888oo..oo888888888888888888888!
{8888888888888888888888888888888888888888888888888888888888888888888888}
{88888 It's not who I am underneath but what I do that defines me 88888}
'8888888888888888888888888888888888888888888888888888888888888888888888'
 o88888888888888888888888888888888888888888888888888888888888888888888o
  88888888888888;'~`^Y8887^''o88888888888o''^Y8887^`~';888888888888888
  '88888888888'       `8'    `'888888888'     `8'       '888888888888'
   !8888888887         !       '8888888'       !         V888888888!
    ^o888888!                   '88888'                   !888888o^
      ^88888"                    88888                    "88888^
        'o888`                   ^888'                   '888o'
          ~888.                   888.                  .888~
            '8;.                  `8'                  .;8'
               '.                  !                  .`
'''

from chickenfoot import Chickenfoot
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
