import threading
from communications_register import get_communication

class Service(threading.Thread):

    def __init__(self):
        super(Service, self).__init__()
        self._onrunning = False

    def run(self):
        self.on_init()
        while self._onrunning:
            self.on_process()
        self.on_shutdown()

    def execute(self, params=None):
        self.params = params['parameters']
        self.communicator = get_communication(params['communication']['type'],
            **params['communication']['parameters'])
        self._onrunning = True
        try:
            self.start()
        except Exception as ex:
            print ex
            self.stop()
            self.on_shutdown()

    def stop(self):
        self._onrunning = False

    def on_init(self):
        raise NotImplementedError('You must define on_init')

    def on_process(self):
        raise NotImplementedError('You must define on_process')

    def on_shutdown(self):
        raise NotImplementedError('You must define on_init')