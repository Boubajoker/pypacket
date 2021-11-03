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

class json:
# this command is for create a .json packet, For more info check docs.
    def create_json_packet(json_file_name, json_content) -> None:
        with open(json_file_name, "a+") as f:
            f.write("// generated from pypacket")
            f.write("{")
            f.write(json_content)
            f.write("}")
            f.close()
# this command is for create a .txt packet, For more info check docs.
class txt:
    def creat_txt_packet(txt_file_name, txt_content) -> None:
        with open(txt_file_name, "a+") as f:
            f.write("INFO: Generated from pypacket")
            f.write(txt_content)
            f.close()

print("Hello from the pypacket community !! get started at https://bit.ly/3CGB08g. Happy coding :)!")