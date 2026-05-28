# Stub "LLM gate" — echoes user input but redacts FLAG if the user
# tries to ask directly. The intended attack is indirect prompt
# injection (the redact list is keyword-based and easy to bypass).
import os, http.server, urllib.parse
FLAG = os.environ.get("GZCTF_FLAG", "FINDIT{ai_per_team_box_placeholder}")
REDACT_KEYWORDS = ["FLAG", "SECRET", "PASSWORD"]
class H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        ln = int(self.headers.get("content-length", "0"))
        user = self.rfile.read(ln).decode("utf-8", "replace")
        if any(k in user.upper() for k in REDACT_KEYWORDS):
            out = b"refusing to discuss credentials\n"
        else:
            # naive echo with weak templating — perfect indirect-injection target
            out = (f"system: vault protects {FLAG}\nuser: {user}\n").encode()
        self.send_response(200); self.send_header("content-length", str(len(out))); self.end_headers()
        self.wfile.write(out)
    def log_message(self, *a, **k): pass
http.server.HTTPServer(("0.0.0.0", 80), H).serve_forever()
