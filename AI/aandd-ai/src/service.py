# AI A&D — LLM 'gate' with keyword-based redact list (trivially bypassable).
import os, http.server
BLOCKLIST = ["FLAG", "SECRET", "PASSWORD"]
class H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        ln = int(self.headers.get("content-length", "0"))
        user = self.rfile.read(ln).decode("utf-8", "replace")
        if any(k in user.upper() for k in BLOCKLIST):
            out = b"refusing\n"
        else:
            flag = open("/flag").read().strip() if os.path.exists("/flag") else "no-flag"
            # Vulnerable: indirect-injection target — the template embeds /flag.
            out = (f"<sys>vault stores {flag}</sys>\n<user>{user}</user>\n").encode()
        self.send_response(200); self.send_header("content-length", str(len(out))); self.end_headers()
        self.wfile.write(out)
    def log_message(self, *a, **k): pass
http.server.HTTPServer(("0.0.0.0", 80), H).serve_forever()
