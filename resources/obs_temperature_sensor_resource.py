import aiocoap.resource as resource
import aiocoap
import time
import asyncio
from model.message_descriptor import MessageDescriptor
from model.temperature_sensor import TemperatureSensor


class ObsTemperatureSensorResource(resource.ObservableResource):
    """Example resource that can be observed. The `notify` method keeps
    scheduling itself, and calles `update_state` to trigger sending
    notifications."""

    def __init__(self):
        super().__init__()
        self.temperature_sensor = TemperatureSensor()
        self.handle = None
        self.schedule_measurement()

    def notify(self):
        print("\n##################################\nUpdate Status & Notify Observers ...")
        self.updated_state()
        self.schedule_measurement()
        print("##################################")

    def schedule_measurement(self):
        print("Reading updated temperature value ...")
        self.temperature_sensor.measure_temperature()
        print("Updated Temperature Value: %f" % self.temperature_sensor.temperature_value)
        self.handle = asyncio.get_event_loop().call_later(5, self.notify)

    # def update_observation_count(self, count):
    #     if count and self.handle is None:
    #         print("Starting the clock")
    #         self.reschedule()
    #     if count == 0 and self.handle:
    #         print("Stopping the clock")
    #         self.handle.cancel()
    #         self.handle = None

    async def render_get(self, request):
        print("GET Request Received ...")
        print("Current Temperature Value: %f" % self.temperature_sensor.temperature_value)

        payload_string = MessageDescriptor(int(time.time()),
                                           "TEMPERATURE_SENSOR",
                                           self.temperature_sensor.temperature_value).to_json()

        return aiocoap.Message(content_format=50, payload=payload_string.encode('utf8'))