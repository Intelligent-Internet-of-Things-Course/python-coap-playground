import aiocoap.resource as resource
import aiocoap
import aiocoap.numbers as numbers
import time
from model.switch_actuator import SwitchActuator
from aiocoap.numbers.codes import Code
from kpn_senml import *


class CoreSwitchActuatorResource(resource.Resource):
    """Example Temperature Sensor resources which supports only the GET Method and the Json Format."""

    def __init__(self, device_name):
        super().__init__()
        self.device_name = device_name
        self.if_ = "core.a"
        self.ct = numbers.media_types_rev['application/senml+json']
        self.rt = "it.unimore.device.switch"
        self.title = "Switch Actuator"
        self.actuator = SwitchActuator()

    def build_senml_json_payload(self):
        pack = SenmlPack(self.device_name)
        temp = SenmlRecord("switch",
                           value=self.actuator.status,
                           time=int(time.time()))
        pack.add(temp)
        return pack.to_json()

    async def render_get(self, request):
        print("GET Request Received ...")
        print("Reading updated temperature value ...")
        print("Updated Temperature Value: %f" % self.actuator.status)

        payload_string = self.build_senml_json_payload()

        return aiocoap.Message(content_format=numbers.media_types_rev['application/senml+json'],
                               payload=payload_string.encode('utf8'))

    async def render_post(self, request):
        self.actuator.change_status()
        return aiocoap.Message(code=Code.CHANGED)

    async def render_put(self, request):
        payload_string = request.payload.decode('UTF-8')
        if payload_string == "false":
            self.actuator.status = False
        elif payload_string == "true":
            self.actuator.status = True
        else:
            return aiocoap.Message(code=Code.BAD_REQUEST)

        return aiocoap.Message(code=Code.CHANGED)
