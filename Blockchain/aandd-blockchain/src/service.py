# Blockchain A&D — toy 'RPC' that returns the flag on the right method.
import os, socketserver, json
FLAG = lambda: open("/flag").read().strip() if os.path.exists("/flag") else "no-flag"
class H(socketserver.StreamRequestHandler):
    def handle(self):
        line = self.rfile.readline().strip()
        try:
            req = json.loads(line)
        except Exception:
            self.wfile.write(b'{"err":"bad json"}\n'); return
        # Vulnerable: any caller can invoke 'admin_withdraw' — no auth.
        if req.get("method") == "admin_withdraw":
            self.wfile.write(json.dumps({"flag": FLAG()}).encode()+b"\n")
        else:
            self.wfile.write(b'{"err":"unknown method"}\n')
socketserver.TCPServer.allow_reuse_address = True
socketserver.TCPServer(("0.0.0.0", 80), H).serve_forever()
