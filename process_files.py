#!/usr/bin/python
import time
from properties import read_properties

properties=read_properties()
print properties
time.sleep(20)

print properties['PARAMETROS']
print 'SE HAN CARGADO TODOS LOS FICHEROS'

raise Exception('a ver que pasa')