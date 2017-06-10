#!/usr/bin/python
import time
import json
from properties import read_properties

properties,out_properties_file=read_properties()
print properties
#time.sleep(60)

print out_properties_file

json_decoded={}
json_decoded['ADDED_KEY'] = 'ADDED_VALUE'

with open(out_properties_file, 'w') as json_file:
    json.dump(json_decoded, json_file)

print 'SE HAN CARGADO TODOS LOS FICHEROS'