from chickenfoot.service import Service
from nanpy import DallasTemperature
import time

class TemperatureSensor(Service):

    def on_init(self):
        self.communicator.listen()
        print 'init'
        print self.params['tp1']
        self.sensors = DallasTemperature(self.params['tp1'])

    def on_shutdown(self):
        pass

    def on_process(self):
        self.sensors.requestTemperatures(0)
        addr = self.sensors.getAddress(0)
        temp = self.sensors.getTempC(addr)
        print temp
        self.communicator.send(str(temp))
        time.sleep(5)