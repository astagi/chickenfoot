from services.temperature_sensor import TemperatureSensor

services = {}

def get_service(service_name, **data):
    return services[service_name](**data)

def register_service(service_name, cls):
    services[service_name] = cls

register_service('TemperatureSensor', TemperatureSensor)