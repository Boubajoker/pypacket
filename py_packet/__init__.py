class json:
    def create_json_packet(json_file_name):
        file = open(json_file_name, "a+")
        file.write('{"test" : true}')
        file.close()
class txt:
    def creat_txt_packet(txt_file_name):
        file = open(txt_file_name, "a+")
        file.write('test : true')
        file.close()

print("Hello from the pypacket community !! get started at https://boubajoker.github.io/pypacket/. Happy coding :)!")