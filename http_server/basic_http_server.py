from http.server import HTTPServer, BaseHTTPRequestHandler


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        res = "This is a post request  \n" + "Received: " + str(body)
        self.wfile.write(res.encode())


PORT = 8000
my_server = HTTPServer(('localhost', PORT), CustomHTTPRequestHandler)

print("Serving on port ", PORT)
my_server.serve_forever()