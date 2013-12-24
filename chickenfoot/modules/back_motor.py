from chickenfoot.module import Module

class BackMotor(Module):

    def __init__(self, **params):
        Module.__init__(self, **params)
        self.binder.bind('fw', self.fw)
        self.binder.bind('rw', self.rw)
        self.binder.bind('stop', self.stop)

    def fw(self, **data):
        print data

    def rw(self, **data):
        print data

    def stop(self, **data):
        print data