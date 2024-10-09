#!/usr/bin/python3
"""import http.server & import json module"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPI(BaseHTTPRequestHandler):
    """Definition of the SimpleAPI class"""

    def do_GET(self):
        """manage GET requests"""
        if self.path == "/data":

            self.send_response(200)
            """return ok if is good with code(200)"""
            self.send_header("Content-type", "application/json")
            """Spécification du type de contenu (JSON)"""
            self.end_headers()
            """End of HTTP header transmission"""

            data = {
                "name": "john",
                "age": "30",
                "city": "New York"
            }

            """Sending JSON data encoded in UTF-8"""
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Error 404: Endpoint not found")


server_adress = ("", 8000)
httpd = HTTPServer(server_adress, SimpleAPI)
print("Serving port 8000...")
httpd.serve_forever()
