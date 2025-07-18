from edge_function import exports
from edge_function.types import Ok
from edge_function.imports.types import (
    IncomingRequest, ResponseOutparam,
    OutgoingResponse, Fields, OutgoingBody
)

from helpers import get_headers, get_settings, get_body

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

class IncomingHandler(exports.IncomingHandler):
    def handle(self, request: IncomingRequest, response_out: ResponseOutparam):
        incoming_headers = get_headers(request)
        settings = get_settings(incoming_headers)
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
