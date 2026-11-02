import http.server
import socketserver
import webbrowser
import os

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print(f"=======================================================")
print(f" AURA DERMA & HAIR STUDIO - Live Local Server")
print(f" Serving directory: {DIRECTORY}")
print(f" URL: http://localhost:{PORT}")
print(f"=======================================================")

# Automatically open browser
webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server is running... Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped gracefully.")