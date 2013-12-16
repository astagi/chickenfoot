from chickenfoot.module import Module

class FrontMotor(Module):

    def __init__(self, **params):
        Module.__init__(self, **params)
        self.binder.bind('rl', self.left)
        self.binder.bind('rr', self.right)

    def left(self, **data):
        print data

    def right(self, **data):
        print data