#!/usr/bin/python
import time
from properties import read_properties

properties,out_properties_file=read_properties()
print properties
time.sleep(60)

with open(out_properties_file, "a") as myfile:
    myfile.write("mijob=valorrrrrrr")

print 'SE HAN CARGADO TODOS LOS FICHEROS'