import cgi

with open("server.html", "r") as f:
    html_content = f.read()
    f.close()

print("Content-type: text/html; charset=utf-8\n")
print(html_content)