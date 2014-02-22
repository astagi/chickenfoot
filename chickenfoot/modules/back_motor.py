from chickenfoot.module import Module
from nanpy import Arduino

class BackMotor(Module):

    def __init__(self, **params):
        Module.__init__(self, **params)
        self.binder.bind('fw', self.fw)
        self.binder.bind('rw', self.rw)
        self.binder.bind('stop', self.stop)
        self.cp1 = params['cp1']
        self.cp2 = params['cp2']
        self.ep = params['ep']

    def fw(self, **data):
        print data
        Arduino.digitalWrite(self.cp1, 0)
        Arduino.digitalWrite(self.cp2, 1)
        Arduino.analogWrite(self.ep, data['speed'])

    def rw(self, **data):
        print data
        Arduino.digitalWrite(self.cp1, 1)
        Arduino.digitalWrite(self.cp2, 0)
        Arduino.analogWrite(self.ep, data['speed'])

    def stop(self, **data):
        print data
        Arduino.analogWrite(self.ep, 0)