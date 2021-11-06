import http.server

server = http.server.HTTPServer

port = 5501
address = ("", port)

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print("Server online, started at port :", port)


httpd.serve_forever()