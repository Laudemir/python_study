#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
def obter_mais_longa_substring(s):
   print()
   for i in range(len(s)):
      if(s[i:i+1] <= s[i+1:i+2]):
         print(s[i], end="")
   print('\n\n')

entrada = "azcbobobegghaki"

print()
print(entrada)

obter_mais_longa_substring(entrada)
#print(obter_mais_longa_substring(entrada))


