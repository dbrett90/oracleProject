# title          : launch_cloud2
# description    : Python application that launches cloud
# author         : Daniel Brett
# date           : Monday, May 7th 2018
# python_version : 3.5
# ==================================================
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
PORT_NUMBER = int(os.environ.get('PORT', 8084))
myFile = open("output.txt","r") 
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

	def do_HEAD(self):
		self.send_response(10000)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		return

	myFile = open("output.txt","r") 
	def do_GET(self):
		self.send_response(10000)
		self.send_header('Content-type','text/html')
		self.end_headers()
		for line in myFile:
			self.wfile.write(bytes(line, "utf8"))
		return

def run():
	print("STARTING UP...")
	server_address = ('0.0.0.0', PORT_NUMBER)
	httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
	print("SERVER IS NOW RUNNING")
	httpd.serve_forever()

run()


