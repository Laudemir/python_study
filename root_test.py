#!/usr/bin/env python3

# imports utilizados
#
import sys
import os

# verifica credencial de root
#
if os.geteuid() != 0:
   print('**************************')
   print('** Requer Superusuario! **')
   print('**************************')
#   exit()
else:
   print('**************************')
   print('*** Blz, voce eh root! ***')
   print('**************************')




