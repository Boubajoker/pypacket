import os

class check:
    def paths():
        if (os.path.exists("py_packet/__init__.py")):
            print("module detected.")
        else:
            print("module py_packet not detected.")
            quit()