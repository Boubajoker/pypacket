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

import typing

class json:
    def create_json_packet(json_file_name, json_content) -> None:
        file = open(json_file_name, "a+")
        file.write("{")
        file.write(json_content)
        file.write("}")
        file.close()
class txt:
    def creat_txt_packet(txt_file_name, txt_content) -> None:
        file = open(txt_file_name, "a+")
        file.write(txt_content)
        file.close()

print("Hello from the pypacket community !! get started at https://boubajoker.github.io/pypacket/. Happy coding :)!")