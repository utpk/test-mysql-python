import mysql.connector
import os
import http.server
import socketserver
from http import HTTPStatus

mydb = mysql.connector.connect(
  host= os.environ['MYSQL_HOST'],
  user= os.environ['MYSQL_USERNAME'],
  password= os.environ['MYSQL_PASSWORD']
)

print(mydb)

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write('hello world'.encode())

httpd = socketserver.TCPServer(('', 8080), Handler)
httpd.serve_forever()
