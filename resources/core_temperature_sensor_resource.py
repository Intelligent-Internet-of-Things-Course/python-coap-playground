import aiocoap.resource as resource
import aiocoap
import aiocoap.numbers as numbers
import time
from model.temperature_sensor import TemperatureSensor
from kpn_senml import *

class CoreTemperatureSensorResource(resource.Resource):
    """Example Temperature Sensor resources which supports only the GET Method and the Json Format."""

    def __init__(self, device_name):
        super().__init__()
        self.device_name = device_name
        self.if_ = "core.s"
        self.ct = numbers.media_types_rev['application/senml+json']
        self.rt = "it.unimore.device.temperature"
        self.title = "Temperature Sensor"
        self.temperature_sensor = TemperatureSensor()

    def build_senml_json_payload(self):
        pack = SenmlPack(self.device_name)
        temp = SenmlRecord("temperature",
                           unit=SenmlUnits.SENML_UNIT_DEGREES_CELSIUS,
                           value=self.temperature_sensor.temperature_value,
                           time=int(time.time()))
        pack.add(temp)
        return pack.to_json()

    async def render_get(self, request):
        print("GET Request Received ...")
        print("Reading updated temperature value ...")
        self.temperature_sensor.measure_temperature()
        print("Updated Temperature Value: %f" % self.temperature_sensor.temperature_value)

        payload_string = self.build_senml_json_payload()

        return aiocoap.Message(content_format=numbers.media_types_rev['application/senml+json'],
                               payload=payload_string.encode('utf8'))
