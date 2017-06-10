#!/usr/bin/python
import time
import json
from properties import read_properties

properties,out_properties_file=read_properties()
print properties
time.sleep(60)


with open(out_properties_file) as json_file:
    json_decoded = json.load(json_file)

json_decoded['ADDED_KEY'] = 'ADDED_VALUE'

with open(json_file, 'w') as json_file:
    json.dump(json_decoded, json_file)

print 'SE HAN CARGADO TODOS LOS FICHEROS'