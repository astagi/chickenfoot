from chickenfoot import Chickenfoot
import socket

class TestChickenfootClient():

    def setUp(self):
        TCP_IP = '192.168.0.6'
        TCP_PORT = 5005
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((TCP_IP, TCP_PORT))

    def tearDown(self):
        self.s.close()

    def test_moves(self):
        self.left()
        self.right()
        self.stop_wheel()
        self.up()
        self.down()
        self.stop()

    def left(self):
        bundle = """
        {
            "m" : "M1",
            "a" : "rl",
            "p" : {
                "p1name" : "p1",
                "p2name": 5
            }
        }
        """
        assert self.__send(bundle)

    def right(self):
        bundle = """
        {
            "m" : "M1",
            "a" : "rr",
            "p" : {
                "p1name" : "p1"
            }
        }
        """
        assert self.__send(bundle)

    def up(self):
        bundle = """
        {
            "m" : "M2",
            "a" : "fw",
            "p" : {
                "p1name" : "p1",
                "p2name" : "p2"
            }
        }
        """
        assert self.__send(bundle)

    def down(self):
        bundle = """
        {
            "m" : "M2",
            "a" : "rw"
        }
        """
        assert self.__send(bundle)

    def stop(self):
        bundle = """
        {
            "m" : "M1",
            "a" : "stop",
            "p" : {
                "p1name" : "stop"
            }
        }
        """
        assert self.__send(bundle)

    def stop_wheel(self):
        bundle = """
        {
            "m" : "M2",
            "a" : "stop",
            "p" : {
                "p1name" : "stop_wheel"
            }
        }
        """
        assert self.__send(bundle)

    def __send(self, data):
        byte_to_send = len(data) + 1
        byte_sent = self.s.send(data + "\n")
        return byte_sent == byte_to_send