# Mobile A&D — fake mobile-app API. Hardcoded creds in /service.py give /flag.
import os, http.server, json
CREDS = ("admin", "letmein")  # intentional: hardcoded backdoor
class H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        ln = int(self.headers.get("content-length", "0"))
        try:
            d = json.loads(self.rfile.read(ln))
        except Exception:
            d = {}
        if (d.get("user"), d.get("pass")) == CREDS:
            flag = open("/flag").read().strip() if os.path.exists("/flag") else "no-flag"
            body = json.dumps({"flag": flag}).encode()
        else:
            body = b'{"err":"bad creds"}'
        self.send_response(200); self.send_header("content-length", str(len(body))); self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a, **k): pass
http.server.HTTPServer(("0.0.0.0", 80), H).serve_forever()
