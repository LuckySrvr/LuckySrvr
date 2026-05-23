import os
import json
import http.server
import urllib.request

PORT = 8000
NODES_DIR = "nodes"
ROUTING_TABLE = {}

def load_community_nodes():
    """Dynamically scan the nodes folder for user configurations submitted via PRs."""
    global ROUTING_TABLE
    ROUTING_TABLE.clear()
    
    if not os.path.exists(NODES_DIR):
        os.makedirs(NODES_DIR)
        return

    print("--- Scanning Community Node Registry ---")
    for filename in os.listdir(NODES_DIR):
        if filename.endswith(".json") and filename != "templates.json":
            file_path = os.path.join(NODES_DIR, filename)
            try:
                with open(file_path, "r") as f:
                    data = json.load(f)
                    domain = data.get("domain", "").strip().lower()
                    target = data.get("primary_target_url", "").strip()
                    
                    if domain and target:
                        if not target.startswith("http"):
                            target = f"http://{target}"
                        ROUTING_TABLE[domain] = target
                        print(f"Registered: {domain} -> tracking {target}")
            except Exception as e:
                print(f"Error compiling config file {filename}: {e}")
    print(f"Total protected cluster environments: {len(ROUTING_TABLE)}\n")

class LuckyClusterProxy(http.server.BaseHTTPRequestHandler):
    def handle_request(self, method):
        # Extract incoming domain header to verify who the traffic belongs to
        host = self.headers.get('Host', '').lower()
        
        if host not in ROUTING_TABLE:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Error: Node path not activated on Lucky cluster.")
            return

        target_url = f"{ROUTING_TABLE[host]}{self.path}"
        req = urllib.request.Request(target_url, method=method)
        
        for key, val in self.headers.items():
            if key.lower() != 'host':
                req.add_header(key, val)
                
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length) if content_length > 0 else None
            
            # Proxy request to user's real primary server destination
            with urllib.request.urlopen(req, data=body, timeout=4.0) as response:
                self.send_response(response.status)
                for k, v in response.getheaders():
                    self.send_header(k, v)
                self.end_headers()
                self.wfile.write(response.read())
        except Exception:
            # 🔴 USER SERVER DOWN: Intercept traffic and serve failover screen
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            failover_screen = f"""
            <html>
            <body style="background:#efefef;color:#333;font-family:monospace;padding:50px;text-align:center;">
                <h1>{{ lucky.failover }}</h1>
                <p>The primary cluster environment for <strong>{host}</strong> is currently unreachable.</p>
                <p>Lucky backup proxy node is maintaining active session survival context.</p>
            </body>
            </html>
            """
            self.wfile.write(failover_screen.encode('utf-8'))

    def do_GET(self): self.handle_request("GET")
    def do_POST(self): self.handle_request("POST")

if __name__ == '__main__':
    load_community_nodes()
    if not ROUTING_TABLE:
        print("⚠️ No community server configurations loaded. Awaiting pull requests.")
    
    print(f"Master cluster initialization sequence complete. Listening on port {PORT}...")
    http.server.HTTPServer(('0.0.0.0', PORT), LuckyClusterProxy).serve_forever()
