import aiocoap.resource as resource
import aiocoap
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class StringDemoResource(resource.Resource):
    """Example String based resources which supports the GET, POST and PUT methods."""

    def __init__(self):
        super().__init__()
        self.string_value = generate_random_string(10)

    async def render_get(self, request):
        print("GET Request Received ...")
        return aiocoap.Message(content_format=0, payload=self.string_value.encode('utf8'))

    async def render_post(self, request):
        self.string_value = generate_random_string(10)
        print("New Random String generated: %s" % self.string_value)
        """If the resources has been created the code should be CREATED"""
        return aiocoap.Message(code=aiocoap.CHANGED, content_format=0, payload=self.string_value.encode('utf8'))

    async def render_put(self, request):
        print('PUT Byte payload: %s' % request.payload)
        payload_string = request.payload.decode('UTF-8')
        print('PUT String payload: %s' % payload_string)
        self.string_value = payload_string
        return aiocoap.Message(code=aiocoap.CHANGED, content_format=0, payload=self.string_value.encode('utf8'))
