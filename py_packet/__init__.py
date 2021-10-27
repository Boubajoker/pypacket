class json:
    def create_packet_json(json_file_name):
        file = open(json_file_name, "a+")
        file.write('{"test" : true}')
        file.close()
class txt:
    def creat_packet_txt(txt_file_name):
        file = open(txt_file_name, "a+")
        file.write('test : true')
        file.close()

print("Hello from the pypacket community !! get started at https://www.pypacket.dev/. Happy coding :)!")
