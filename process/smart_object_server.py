import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
from resources.core_temperature_sensor_resource import CoreTemperatureSensorResource
from resources.core_switch_actuator_resource import CoreSwitchActuatorResource

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.INFO)
# logging.getLogger("coap-server").setLevel(logging.DEBUG)


def main():
    # Resource tree creation
    root = resource.Site()

    device_name = "urn:demo-smartobject-0001"

    # Add WellKnownCore Resource to support the standard Resource Discovery
    root.add_resource(['.well-known', 'core'], resource.WKCResource(root.get_resources_as_linkheader, impl_info=None))
    root.add_resource(['temperature'], CoreTemperatureSensorResource(device_name))
    root.add_resource(['switch'], CoreSwitchActuatorResource(device_name))
    asyncio.Task(aiocoap.Context.create_server_context(root, bind=('127.0.0.1', 5683)))
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
