# Pypacket 

A python module that can make files packet for send a request file to a server or create a log.

## How to create a packet ?

### create a json packet

to create a json packet we are using the class json.
and the function 'create_json_packet()'
then the code look's like this : 

```python
import py_packet

json.create_json_packet("you're file name.json")
```

### create a txt packet

to create a txt packet we are using the class txt.
and the function 'create_txt_packet()'
then the code look's like this : 

```python
import py_packet

txt.create_txt_packet("you're file name.txt")
```
## How to install it ?

To install pypacket module please follow the following steps :
- open your terminal,
- type the following command:
```
pip install py_packet
```

## Launch the project

### Requires :

- Intrpreter : python 38
- system : Minimal : Windows 7
- py_launcher
- pip