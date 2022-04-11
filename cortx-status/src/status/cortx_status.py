#!/bin/env python3

import sys
import json
from cortx.db import const
from http.server import HTTPServer, BaseHTTPRequestHandler

with open(const.CLUSTER_DB) as data_file:
    data = json.load(data_file)

class ServiceHandler(BaseHTTPRequestHandler):
	#sets basic headers for the server
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type','text/json')
		#reads the length of the Headers
		length = int(self.headers['Content-Length'])
		#reads the contents of the request
		content = self.rfile.read(length)
		temp = str(content).strip('b\'')
		self.end_headers()
		return temp
		
	def do_GET(self):
		#defining all the headers
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		#prints all the keys and values of the json file
		self.wfile.write(json.dumps(data).encode())
		self.wfile.close()

def main():
	server = HTTPServer((const.HOST,const.PORT), ServiceHandler)
	server.serve_forever()

if  __name__ == '__main__':
	sys.exit(main())
