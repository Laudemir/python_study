#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Entra com dois valores
#
n1 = input('Informe o primeiro numero inteiro? ')
n2 = input(' Informe o segundo numero inteiro? ')

# Verifica se eh inteiro
#
if type(n1) != int:
   n1 = int(n1)	
if type(n2) != int:
   n2 = int(n2)

if type(n1) != int:
   n2=str(n2)
 
if type(n2) != int:
   n1=str(n1)

print(type(n1))
print(type(n2))

'''
# Somar os dois numeros
#
soma = n1+n2

# Apresentar o resultado
#
if type(soma) == int:
   print('A soma de {0} com {1} vale {2}'.format(n1, n2, soma))
else:
   print("A concatenacao de '{0}' com '{1}' vale {2}".format(n1, n2, soma))
'''
