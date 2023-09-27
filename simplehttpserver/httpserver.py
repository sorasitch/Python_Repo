# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:59:29 2022

@author: schomsin
"""

# http://localhost:8080/

# Import libraries
import http.server
import socketserver
  
# Defining PORT number
PORT = 8080
  
# Creating handle
Handler = http.server.SimpleHTTPRequestHandler
  
# Creating TCPServer
http = socketserver.TCPServer(("", PORT), Handler)
  
# Getting logs
print("serving at port", PORT)
http.serve_forever()