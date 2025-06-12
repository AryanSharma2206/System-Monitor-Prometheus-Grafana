from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/metrics':
            result = subprocess.run(["./failed_logins.sh"], capture_output=True, text=True)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(result.stdout.encode())

server = HTTPServer(('0.0.0.0', 9000), Handler)
print("Exporter running on http://localhost:9000/metrics")
server.serve_forever()
