# Pypacket 

A python module that can make files packet for send a request file to a server or create a log.

## How to create a packet ?

### create a json packet

to create a json packet we are using the class json.
and the function 'create_json_packet()'
then the code look's like this : 

```python
import py_packet

json.create_json_packet("Hello.json", json_content='"msg" : "Hello World !"')
```

### create a txt packet

to create a txt packet we are using the class txt.
and the function 'create_txt_packet()'
then the code look's like this : 

```python
import py_packet

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

## Launch the project

### Requires :

- Intrpreter : python 3.8
- system : Minimal : Windows 7 64bits
- py_launcher
- pip 21.2.1
- git

for more info visit <a href="https://bit.ly/3CGB08g">pypacket documentation</a>