from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
ROOT = Path(__file__).resolve().parent
APP = ROOT / "app"
class LocalOnlyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(APP), **kwargs)
    def log_message(self, format, *args):
        pass
if __name__ == "__main__":
    os.chdir(APP)
    server = ThreadingHTTPServer(("127.0.0.1", 8080), LocalOnlyHandler)
    print("SENTINEL: http://127.0.0.1:8080")
    print("Local-only. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("\nSENTINEL stopped.")