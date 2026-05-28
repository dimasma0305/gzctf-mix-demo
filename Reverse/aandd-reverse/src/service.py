# Reverse A&D — serves an XOR-obfuscated flag with a hard-coded key.
# Players reverse the key from the binary; flag rotates per tick.
import os, http.server
KEY = b"correct-horse-battery-staple-42!"
def obf():
    f = open("/flag","rb").read().strip() if os.path.exists("/flag") else b"no-flag"
    return bytes(a^b for a,b in zip(f, (KEY * ((len(f)//len(KEY))+1))))
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = obf().hex().encode() + b"\n"
        self.send_response(200); self.send_header("content-length", str(len(body))); self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a, **k): pass
http.server.HTTPServer(("0.0.0.0", 80), H).serve_forever()
