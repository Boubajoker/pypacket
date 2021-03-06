"""
MIT License

Copyright (c) 2021 Boubajoker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
from py_packet import *
import security
import os

security.check.paths()
# {} symbols automaticly added.

# To create .json packet file.
Json.create_json_packet("build/Hello.jsonc", json_content='"msg" : "Hello World !"')

#To create .txt packet file.
Txt.create_txt_packet("build/Hello.txt", txt_content="Hello World !")

#to create a .html packet file.
Html.create_html_packet("build/Hello.html", html_content="<h1>Hello World !</h1>")

#to create a .xml packet file.
Xml.create_xml_packet("build/Hello.xml", xml_content="<template>Hello World !</template>")

#to create a .js packet file.
JavaScript.create_js_packet("build/Hello.js", js_content="console.log('Hello World !')")

#to create a .ts packet file.
TypeScript.create_ts_packet("build/Hello.ts", ts_content="console.log('Hello World !')")

#to read a packet file.
Read.file_content("build/Hello.jsonc")

#download a release module.
os.system("pip install requests")

import requests

downloadUrl = 'https://boubajoker.github.io/pypacket/assets/others/py_packet.zip'

req = requests.get(downloadUrl)
filename = req.url[downloadUrl.rfind('/')+1:]

with open(filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

def download_file(url, filename=''):
    try:
        if filename:
            pass            
        else:
            filename = req.url[downloadUrl.rfind('/')+1:]

        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None