# Pypacket 

A python module that can make files packet for send a request file to a server or create a log.

## How to create a packet ?

### create a json packet

to create a json packet we are using the class json.
and the function 'create_json_packet()'
then the code look's like this : 

```python
from pypacket import *

json.create_json_packet("Hello.json", json_content='"msg" : "Hello World !"')
```

### create a txt packet

to create a txt packet we are using the class txt.
and the function 'create_txt_packet()'
then the code look's like this : 

```python
from pypacket import *

txt.create_txt_packet("Hello.txt", txt_content='Hello World !')
```
## How to install it ?

To install pypacket module please follow the following steps :
- open your terminal,
- type the following command:
```
pip install py_packet
```
WARNING! : py_packet is not aividable for the moment in pip platform !

For the moment you can copy and past "pypacket" directory to you're local project. But don't worry, project in pypi will become soon !

## Launch the project

execute <a href="pypacket.sh">pypacket.sh</a>.

### Requires :

- Intrpreter : python 3.8
- system : Minimal : Windows 7 64bits
- py_launcher
- pip 21.3.1
- git

for more info visit <a href="https://bit.ly/3CGB08g">pypacket documentation</a>

### Requied to send this project

The files you need for publish this project is:
- <a href="AUTHORS.md">AUTHORS.md</a>
- <a href="CopyRight.txt">CopyRight.txt</a>
- <a href="LICENSE">LICENSE</a>
- <a href="ThirdPartyNotice.txt">ThirdPartyNotice.txt</a>
AND DO NOT EDIT THOSE FILES !!