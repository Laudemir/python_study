#!/usr/bin/env python3
# code: utf-8
#
#
import sys
import os

# verifica credencial de superusuario
#
if os.geteuid() != 0:
   print('** Requer privilégio Superusuário.')
else:
   print('** Ok! você acessou como superusuário.')




