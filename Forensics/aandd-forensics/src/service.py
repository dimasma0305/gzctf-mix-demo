# Forensics A&D — exposes a few 'files' for download; one has the flag in metadata.
import os, http.server, time
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/files/"):
            name = self.path[len("/files/"):]
            # Vulnerable: the 'metadata.txt' file embeds /flag verbatim.
            if name == "metadata.txt":
                flag = open("/flag","rb").read().strip() if os.path.exists("/flag") else b"no-flag"
                body = b"Sensor: cam-01\nTimestamp: " + str(time.time()).encode() + b"\nNote: " + flag + b"\n"
            else:
                body = b"unknown file"
        else:
            body = b"GET /files/{name}\n"
        self.send_response(200); self.send_header("content-length", str(len(body))); self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a, **k): pass
http.server.HTTPServer(("0.0.0.0", 80), H).serve_forever()
