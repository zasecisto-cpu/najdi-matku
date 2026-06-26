import os
import json
import http.server
import socketserver

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class GameServer(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/api/leaderboard':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            # Read leaderboard
            db_path = os.path.join(DIRECTORY, 'leaderboard.json')
            if not os.path.exists(db_path):
                # Pre-populate with fun defaults
                defaults = [
                    {"name": "Včelka Mája", "time": 6.82},
                    {"name": "Medový Král", "time": 9.45},
                    {"name": "Trubec Rychlík", "time": 12.10},
                    {"name": "Mladý Včelař", "time": 15.30},
                    {"name": "Medvěd Brumlík", "time": 21.05}
                ]
                with open(db_path, 'w', encoding='utf-8') as f:
                    json.dump(defaults, f, ensure_ascii=False, indent=2)
            
            try:
                with open(db_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception:
                data = []
            
            # Sort by time ascending
            data = sorted(data, key=lambda x: x['time'])[:10]
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/leaderboard':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                new_entry = json.loads(post_data.decode('utf-8'))
                name = str(new_entry.get('name', 'Anonym')).strip()[:15] or 'Anonym'
                time_val = float(new_entry.get('time', 999.99))
                
                db_path = os.path.join(DIRECTORY, 'leaderboard.json')
                data = []
                if os.path.exists(db_path):
                    try:
                        with open(db_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                    except Exception:
                        data = []
                
                data.append({"name": name, "time": round(time_val, 2)})
                
                # Sort and limit to top 50
                data = sorted(data, key=lambda x: x['time'])[:50]
                
                with open(db_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True}).encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        # Support CORS preflight
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with ThreadingTCPServer(("", PORT), GameServer) as httpd:
        print(f"Game server running locally at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down game server.")
