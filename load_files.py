#!/usr/bin/python

import argparse

from properties import read_properties
from properties import write_properties

properties=read_properties()
print properties

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--from_date', help="fecha inicio de la carga "
                                              "de datos (inclusive).  "
                                              "formato yyyy-mm-dd",
                    required=False)

parser.add_argument('-t', '--to_date',
                    help="fecha fin de la carga de datos (inclusive). "
                         "formato yyyy-mm-dd or 'now' ",
                    required=False)

args = parser.parse_args()

print

json_decoded={}
json_decoded['PARAMETROS'] = 'PARAMETRO PASADO ENTRE PROCESOS'

write_properties(json_decoded)

print 'SE HAN CARGADO TODOS LOS FICHEROS'

