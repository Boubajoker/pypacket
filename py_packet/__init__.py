r"""
# Pypacket Copyright (c) Boubajoker 2021. All right reserved. Project under MIT License.

# Pypacket therms:
    DO NOT DO A COPY OF THIS PROJECT WITHOUT THOSE FILES:
        - CopyRight.txt
        - ThirdPartyNotice.txt
        - AUTHORS.md
        - LICENSE

# MIT License:
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

========================================================== !*/

"""
__all__ = [
    "Json", 
    "Txt", 
    "Html", 
    "Xml", 
    "JavaScript", 
    "TypeScript", 
    "Read", 
    "pypacket",
    "Packets"
]


import webbrowser

class Json:
# this command is for create a .json packet, For more info check docs.
    def create_json_packet(json_file_name, json_content) -> str:
        with open(json_file_name, "a+") as f:
            f.write("// generated from pypacket\n")
            f.write("{\n")
            f.write(json_content + "\n")
            f.write("}")
            f.close()

# this command is for create a .txt packet, For more info check docs.
class Txt:
    def create_txt_packet(txt_file_name, txt_content) -> str:
        with open(txt_file_name, "a+") as f:
            f.write("INFO: Generated from pypacket\n")
            f.write(txt_content + "\n")
            f.close()

class Html:
    def create_html_packet(html_file_name, html_content) -> str:
        with open(html_file_name, "a+") as f:
            f.write("<!--generated from pypacket-->\n")
            f.write("<!DOCTYPE html>\n")
            f.write("<html>\n")
            f.write(html_content + "\n")
            f.write("</html>")
            f.close()

class Xml:
    def create_xml_packet(xml_file_name, xml_content) -> str:
        with open(xml_file_name, "a+") as f:
            f.write("<!--generated from pypacket-->\n")
            f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            f.write(xml_content + "\n")
            f.close()

class JavaScript:
    def create_js_packet(js_file_name, js_content) -> str:
        with open(js_file_name, "a+") as f:
            f.write("// generated from pypacket\n")
            f.write(js_content + "\n")
            f.close()

class TypeScript:
    def create_ts_packet(ts_file_name, ts_content) -> str:
        with open(ts_file_name, "a+") as f:
            f.write("// generated from pypacket\n")
            f.write(ts_content + "\n")
            f.close()
        with open("tsconfig.json", "w+") as f:
            f.write("{\n")
            f.write("//tsconfig file generated from pypacket.\n")
            f.write("}")
            f.close()

class Read:
    def file_content(file_name_read) -> str:
        with open(file_name_read, "r") as f:
            content = f.read()
            f.close()
            print(content)

class pypacket:
    def Zen() -> str:
        """
        This text is the description of the module.
        """
        print("""
        pypacket is a simple python module that can create packets files
        """)
    def get_started() -> str:
        print("Get started at https://bit.ly/3CGB08g")
        webbrowser.open("https://bit.ly/3CGB08g")

print("Hello from the pypacket community !! Get started at https://bit.ly/3CGB08g. Happy coding :)!")