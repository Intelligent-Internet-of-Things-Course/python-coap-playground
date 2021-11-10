import aiocoap.resource as resource
import aiocoap
from model.message_descriptor import MessageDescriptor
from model.temperature_sensor import TemperatureSensor
import time


class TemperatureSensorResource(resource.Resource):
    """Example Temperature Sensor resources which supports only the GET Method and the Json Format."""

    def __init__(self):
        super().__init__()
        self.temperature_sensor = TemperatureSensor()

    async def render_get(self, request):
        print("GET Request Received ...")
        print("Reading updated temperature value ...")
        self.temperature_sensor.measure_temperature()
        print("Updated Temperature Value: %f" % self.temperature_sensor.temperature_value)

        payload_string = MessageDescriptor(int(time.time()),
                                           "TEMPERATURE_SENSOR",
                                           self.temperature_sensor.temperature_value).to_json()

        return aiocoap.Message(content_format=50, payload=payload_string.encode('utf8'))