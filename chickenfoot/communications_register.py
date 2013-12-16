from communications.tcp_communication import TcpCommunication

communicators = {}

def get_communication(comm_name, **data):
    return communicators[comm_name](**data)

def register_communication(comm_name, cls):
    communicators[comm_name] = cls

register_communication('tcp', TcpCommunication)