# Crypto A&D — AES-CTR oracle with nonce reuse (intended exploit).
import os, socketserver, hashlib
FLAG = lambda: open("/flag").read().strip() if os.path.exists("/flag") else "no-flag-yet"
KEY = hashlib.sha256(b"shared-vault-secret").digest()
STATIC_NONCE = b"\x00" * 12  # vulnerable: same nonce for every request

def keystream(n):
    out = b""
    for i in range((n+15)//16):
        out += hashlib.sha256(KEY + STATIC_NONCE + i.to_bytes(4,"big")).digest()[:16]
    return out[:n]

class H(socketserver.StreamRequestHandler):
    def handle(self):
        msg = self.rfile.readline().strip()
        if msg == b"flag":
            pt = FLAG().encode()
        else:
            pt = msg
        ct = bytes(a^b for a,b in zip(pt, keystream(len(pt))))
        self.wfile.write(ct.hex().encode() + b"\n")

socketserver.TCPServer.allow_reuse_address = True
socketserver.TCPServer(("0.0.0.0", 80), H).serve_forever()
