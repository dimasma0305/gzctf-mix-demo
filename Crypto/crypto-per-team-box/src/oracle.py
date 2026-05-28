# Tiny XOR oracle — demonstrates DynamicContainer auto-build.
# In a real challenge, FLAG would be substituted at container start
# via the GZCTF_FLAG env var (per-team).
import os, socketserver, struct
FLAG = os.environ.get("GZCTF_FLAG", "FINDIT{crypto_per_team_box_placeholder}").encode()
KEY = b"shhh-its-a-secret-key-32-bytes!!"

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        pt = self.request.recv(1024).rstrip()
        ct = bytes(a ^ b for a, b in zip(pt, KEY))
        self.request.sendall(b"ciphertext: " + ct.hex().encode() + b"\n")

with socketserver.TCPServer(("0.0.0.0", 80), Handler) as srv:
    srv.serve_forever()
