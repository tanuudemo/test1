import http.server
import socketserver
from http import HTTPStatus

class InitialHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Initial http service for test1')

socketserver.TCPServer(('', 9000), InitialHandler).serve_forever()
