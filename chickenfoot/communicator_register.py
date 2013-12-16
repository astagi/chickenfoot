from tcp_communicator import TcpCommunicator

communicators = {}

def get_communicator(comm_name, **data):
    return communicators[comm_name](**data)

def register_communicator(comm_name, cls):
    communicators[comm_name] = cls

register_communicator('tcp', TcpCommunicator)