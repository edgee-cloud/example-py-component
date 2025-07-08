from edge_function.types import Err
from edge_function.imports.types import (
    IncomingRequest
)
from edge_function.imports.streams import StreamError_Closed
import json


def get_headers(request: IncomingRequest) -> dict:
    fields = request.headers()
    headers = dict(fields.entries())
    return headers


def get_settings(headers: dict) -> dict:
    # Extract and return settings from headers
    settings = headers.get("x-edgee-component-settings", "{}")
    try:
        return json.loads(settings)
    except json.JSONDecodeError:
        print("Invalid JSON in x-edgee-component-settings")
        return {}


def get_body(request: IncomingRequest) -> str:
    body = request.consume()
    stream = body.stream()
    output = bytearray()
    while True:
        try:
            chunk = stream.read(1024)
            if not chunk:
                break
            output += bytearray(chunk)
        except Err as e:
                if isinstance(e.value, StreamError_Closed):
                    break
    return output.decode("utf-8")
