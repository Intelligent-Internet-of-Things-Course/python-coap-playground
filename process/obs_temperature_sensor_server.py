import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
from resources.obs_temperature_sensor_resource import ObsTemperatureSensorResource

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.INFO)
# logging.getLogger("coap-server").setLevel(logging.DEBUG)


def main():
    # Resource tree creation
    root = resource.Site()

    root.add_resource(['temperature-sensor-obs'], ObsTemperatureSensorResource())
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683)))
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
