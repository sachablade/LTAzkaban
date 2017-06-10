#!/usr/bin/python
import time
import json
from properties import read_properties
from properties import write_properties

properties=read_properties()
print properties
time.sleep(20)

json_decoded={}
json_decoded['PARAMETROS'] = 'PARAMETRO PASADO ENTRE PROCESOS'

write_properties(json_decoded)

print 'SE HAN CARGADO TODOS LOS FICHEROS'