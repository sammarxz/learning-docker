from http.server import BaseHTTPRequestHandler, HTTPServer

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("Hello from Python!", "utf-8"))
        return

def run():
    httpd = HTTPServer(('0.0.0.0', 8080), testHTTPServer_RequestHandler)
    httpd.serve_forever()

run() 