# Hardware A&D — emulates a UART. The flag is streamed on the right 'baud' command.
import os, socketserver
FLAG = lambda: open("/flag").read().strip() if os.path.exists("/flag") else "no-flag"
class H(socketserver.StreamRequestHandler):
    def handle(self):
        self.wfile.write(b"uart-emul> ")
        cmd = self.rfile.readline().strip()
        # Vulnerable: undocumented "debug_115200" command spills /flag.
        if cmd == b"debug_115200":
            self.wfile.write(FLAG().encode() + b"\n")
        else:
            self.wfile.write(b"unknown cmd\n")
socketserver.TCPServer.allow_reuse_address = True
socketserver.TCPServer(("0.0.0.0", 80), H).serve_forever()
