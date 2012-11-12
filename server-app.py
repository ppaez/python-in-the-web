import BaseHTTPServer, SimpleHTTPServer, CGIHTTPServer
import os
 
def send_head(self):
    """Version of send_head that finds index.py in CGI directories."""
    path = self.path
    # separate the query
    i = path.find( '?' )
    if i >= 0:
        query = path[ i: ]
        path = path[ : i ]
    else:
        query = ''
    if os.path.isdir( '.' + path ):  # os.getcwd() ?
        # check if index.py exists
        pathindexpy = os.path.join( path, 'index.py' )
        if os.path.exists( '.' + pathindexpy ):
            path = pathindexpy + query
            self.path = path
    if self.is_cgi():
        return self.run_cgi()
    else:
        return SimpleHTTPServer.SimpleHTTPRequestHandler.send_head(self)
 
PORT = 1234
server_address = ('localhost', PORT)
 
Handler = CGIHTTPServer.CGIHTTPRequestHandler
 
# overwrite the existing send_head() method
Handler.send_head = send_head
 
# add paths to the cgi directories
Handler.cgi_directories.append( '/contacto' )
Handler.cgi_directories.append( '/wiki' )
Handler.cgi_directories.append( '/blog' )
 
httpd = BaseHTTPServer.HTTPServer( ( server_address, Handler )
 
print("servidor con CGI en puerto", PORT)
httpd.serve_forever()
