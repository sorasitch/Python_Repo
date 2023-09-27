# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 18:35:09 2022

@author: schomsin
"""

# http://localhost:5555/

# importing all the functions 
# from http.server module
from http.server import *
  
# creating a class for handling 
# basic Get and Post Requests

gl_i = 0
gl_st = 'let start ..'

class GFG(BaseHTTPRequestHandler):
    
    global gl_i
    global gl_st
    
    # creating a function for Get Request
    def do_GET(self):
        
        global gl_i
        global gl_st
        
        # Success Response --> 200
        self.send_response(200)
          
        # Type of file that we are using for creating our
        # web server.
        self.send_header('content-type', 'text/html')
        self.end_headers()
          
        # what we write in this function it gets visible on our
        # web-server
        # self.wfile.write('<h1>GFG - (GeeksForGeeks)</h1>'.encode())
        
# try
        self.wfile.write('<html>'.encode())
        self.wfile.write('<head>'.encode())
        self.wfile.write('<title>Python HTTP Server</title>'.encode())
        self.wfile.write('<meta http-equiv="refresh" content="10"> <!-- Refresh every -->'.encode())
        self.wfile.write('</head>'.encode())
        self.wfile.write('<body>'.encode())
        self.wfile.write('<h1>Simple HTTP Server</h1>'.encode())
        self.wfile.write('<p>Congratulations! The HTTP Server is working! Welcome to GeeksForGeeks</p>'.encode()) 
        P = "<p>Congratulations! {0}</p>".format(gl_st)  
        self.wfile.write(P.encode())
        self.wfile.write('</body>'.encode())
        self.wfile.write('</html>'.encode())
        
        gl_i=gl_i+1
        gl_st=str(gl_i)

# 
# this is the object which take port 
# number and the server-name
# for running the server
port = HTTPServer(('', 5555), GFG)
  
# this is used for running our 
# server as long as we wish
# i.e. forever
port.serve_forever()

print('end here')