from module import Module

class Pmotor(Module):

    def __init__(self, **params):
        Module.__init__(self, **params)
        self.binder.bind('fw', self.fw)
        self.binder.bind('rw', self.rw)

    def fw(self, **data):
        print data

    def rw(self, **data):
        print data