#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

'''
Um numero perfeito e um numero para o qual a soma de todos os
seus divisores positivos( excluindo proprio numero ) eh igual a ele

Exemplo: 28 eh um numero perfeito, pois seus divisores sao
1, 2, 4, 7, 14 onde 1+2+4+7+14 = 28
'''
def numero_perfeito(num):
   soma = 0
   for i in range(1, num):
      if(num % i == 0):
         soma += i
         if (soma > num):
             break
   if (soma == num):
      return True
   else:
      return False

n = int(input("Entre com o numero positivo: "))

for i in range (1, n+1):
   if(numero_perfeito(i)):
      print(i, " Perfeito!")


