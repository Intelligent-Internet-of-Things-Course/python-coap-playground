# Python CoAP Playground

This Project contains a group of Python CoAP examples focusing on the following aspects:

- Simple String CoAP Server
- Simple Temperature CoAP Server
- Simple CoAP Client
- Observability
- Content Format Negotiation

Reference Library: AioCoAP - https://github.com/chrysn/aiocoap

# Web Linking & Other Dependencies

- Import LinkHeader module to enable aiocoap to work with WebLinking -> pip install LinkHeader
- Import kpn-senml (https://github.com/kpn-iot/senml-python-library) to work with SenML data format for in Json and CBOR -> pip install kpn-senml