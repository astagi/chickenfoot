from chickenfoot import Chickenfoot
from controller import Controller

cf = Chickenfoot()
contr = Controller()

contr.bind('rl', cf.left)
contr.bind('rr', cf.right)
contr.bind('fw', cf.fw)
contr.bind('rw', cf.rw)

contr.execute('rl')
contr.execute('rr')
contr.execute('fw')
contr.execute('rw')
