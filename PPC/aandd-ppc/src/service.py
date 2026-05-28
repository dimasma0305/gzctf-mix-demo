# PPC A&D — solve a small problem to retrieve the flag. Timing-leak primitive.
import os, socketserver, time
FLAG = lambda: open("/flag").read().strip() if os.path.exists("/flag") else "no-flag"
class H(socketserver.StreamRequestHandler):
    def handle(self):
        self.wfile.write(b"solve: sum of first 1e6 ints = ?\n")
        ans = self.rfile.readline().strip()
        # Vulnerable: comparison short-circuits → timing leak on the password.
        expected = b"500000500000"
        ok = len(ans) == len(expected)
        for a, b in zip(ans, expected):
            if a != b:
                ok = False; break
            time.sleep(0.01)  # the leak
        if ok:
            self.wfile.write(FLAG().encode() + b"\n")
        else:
            self.wfile.write(b"nope\n")
socketserver.TCPServer.allow_reuse_address = True
socketserver.TCPServer(("0.0.0.0", 80), H).serve_forever()
