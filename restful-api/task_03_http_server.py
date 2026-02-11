#!/usr/bin/python3
"""
Task 3: Develop a simple API using Python http.server
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Simple API Handler using http.server"""

    def _send_text(self, status_code, message):
        """Send plain text response."""
        data = message.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_json(self, status_code, payload):
        """Send JSON response."""
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
            return

        if self.path == "/status":
            self._send_text(200, "OK")
            return

        if self.path == "/data":
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(200, sample_data)
            return

        if self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._send_json(200, info)
            return

        self._send_text(404, "Endpoint not found")

    def do_POST(self):
        """
        Handle POST requests.
        Endpoint: /echo
        - Accepts JSON body and returns it back as JSON
        """
        if self.path != "/echo":
            self._send_text(404, "Endpoint not found")
            return

        content_length = self.headers.get("Content-Length")
        if not content_length:
            self._send_text(400, "Missing Content-Length")
            return

        try:
            length = int(content_length)
        except ValueError:
            self._send_text(400, "Invalid Content-Length")
            return

        body_bytes = self.rfile.read(length)

        try:
            body_text = body_bytes.decode("utf-8")
        except UnicodeDecodeError:
            self._send_text(400, "Body must be UTF-8")
            return

        try:
            payload = json.loads(body_text) if body_text.strip() else {}
        except json.JSONDecodeError:
            self._send_text(400, "Invalid JSON")
            return

        self._send_json(200, {"received": payload})


def run(host="0.0.0.0", port=8000):
    """Start the HTTP server."""
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
