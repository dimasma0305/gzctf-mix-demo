# Tiny "hill" — accepts PUT /koth/king with a token body, persists
# it to the marker file, and serves the marker on GET.
# Demonstrates a real KotH auto-built challenge end-to-end.
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
MARKER = Path("/koth/king")
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/koth/king":
            body = MARKER.read_bytes() if MARKER.exists() else b""
        else:
            body = b"king of the hill — PUT /koth/king\n"
        self.send_response(200); self.send_header("content-length", str(len(body))); self.end_headers()
        self.wfile.write(body)
    def do_PUT(self):
        ln = int(self.headers.get("content-length", "0"))
        MARKER.write_bytes(self.rfile.read(ln))
        self.send_response(204); self.end_headers()
    def log_message(self, *a, **k): pass
HTTPServer(("0.0.0.0", 80), H).serve_forever()
