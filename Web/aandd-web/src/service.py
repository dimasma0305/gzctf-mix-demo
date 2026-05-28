# Web A&D — tiny HTTP server with a path-traversal-ish endpoint.
import os, http.server, urllib.parse
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        # Intended vuln: ../../flag traversal via the q parameter
        path = urllib.parse.parse_qs(u.query).get("file", ["index.html"])[0]
        safe = os.path.normpath(os.path.join("/var/www", path))
        try:
            body = open(safe, "rb").read()
        except Exception:
            body = b"not found"
        self.send_response(200); self.send_header("content-length", str(len(body))); self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a, **k): pass
os.makedirs("/var/www", exist_ok=True)
open("/var/www/index.html","w").write("Web A&D — try /?file=...\n")
http.server.HTTPServer(("0.0.0.0", 80), H).serve_forever()
