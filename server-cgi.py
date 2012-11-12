from http.server import HTTPServer, CGIHTTPRequestHandler
 
PORT = 1234
server_address = ('localhost', PORT)
 
Handler = CGIHTTPRequestHandler
 
httpd = HTTPServer(server_address, Handler)
 
print("servidor con CGI en puerto", PORT)
httpd.serve_forever()
