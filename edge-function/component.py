from edge_function import exports
from edge_function.types import (Ok, Err)
from edge_function.imports.types import (
    IncomingRequest, ResponseOutparam,
    OutgoingResponse, Fields, OutgoingBody
)

from edge_function.imports.streams import StreamError_Closed

import json

index = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Coming Soon</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: system-ui, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      text-align: center;
      height: 100vh;
      background-color: #f4f4f4;
      color: #333;
    }
    .container {
      max-width: 400px;
      padding: 2rem;
    }
    h1 {
      font-size: 2.5rem;
      margin-bottom: 1rem;
    }
    p {
      font-size: 1.1rem;
      margin-bottom: 2rem;
    }
    footer {
      font-size: 0.9rem;
      color: #888;
    }
    a {
      color: #007bff;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Coming Soon</h1>
    <p>We're working hard to launch something awesome. Stay tuned!</p>
    <footer>Served by <a href="https://www.edgee.cloud">Edgee</a></footer>
  </div>
</body>
</html>
'''

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

class IncomingHandler(exports.IncomingHandler):
    def handle(self, request: IncomingRequest, response_out: ResponseOutparam):
        incomingHeaders = get_headers(request)
        settings = get_settings(incomingHeaders)
        body = get_body(request)

        outgoingResponse = OutgoingResponse(Fields.from_list([]))
        outgoingResponse.set_status_code(200)
        outgoingBody = outgoingResponse.body()
        ResponseOutparam.set(response_out, Ok(outgoingResponse))
        stream = outgoingBody.write()
        stream.write(bytes(index, "utf-8"))
        stream.flush()
        stream.__exit__(None, None, None)
        OutgoingBody.finish(outgoingBody, None)
