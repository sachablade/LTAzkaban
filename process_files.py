#!/usr/bin/python
import time
from properties import read_properties

properties,out_properties_file=read_properties()
print properties
time.sleep(60)

print 'SE HAN CARGADO TODOS LOS FICHEROS'