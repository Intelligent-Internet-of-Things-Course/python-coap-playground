import logging
import asyncio
import aiocoap
from aiocoap import *

logging.basicConfig(level=logging.INFO)


async def main():
    protocol = await Context.create_client_context()

    request = Message(code=aiocoap.GET, uri='coap://127.0.0.1:5683/temperature-sensor-obs', observe=0)

    pr = protocol.request(request)

    r = await pr.response
    print("First response: %s\n%r" % (r, r.payload))

    async for r in pr.observation:
        print("Next result: %s\n%r" % (r, r.payload))
        pr.observation.cancel()
        break
    print("Loop ended, sticking around")
    await asyncio.sleep(50)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
