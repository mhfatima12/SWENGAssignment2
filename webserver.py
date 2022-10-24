from http.server import HTTPServer, BaseHTTPRequestHandler


class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        content = ''
        with open('webpage.html') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                content = content + line.strip()
        self.wfile.write(content.encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        content = ''
        with open('webpage.html') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                content = content + line.strip()
        self.wfile.write(content.encode())

def main():
    PORT = 8080
    server = HTTPServer(('',PORT),helloHandler)
    print("Server running on localhost:%s" % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()