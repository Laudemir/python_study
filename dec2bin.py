#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#


# Função para verificar quantidade
# de bits que tem o número passado
#
def bits(num):
    bits = 0
    while num > 0:
	# Deslocar nr para a direita
        # Divisão por dois
        num = num >> 1
        bits += 1
    # Retorna qtd de bits + 1
    return bits


# Função para transformar número
# decimal em binário
#
def dec2bin(num, bits):
    binario = ''
    for i in range(bits-1, -1, -1):
        if (num >> i) % 2 == 0:
            binario += '0'
        else:
            binario += '1'
    return binario

try:
    while True:
       i = int(input("Um número decimal: "))
       print()
       print("nº {} tem ........: {} bits".format(i, bits(i)))
       print("nº {} em binário .: {}".format(i, dec2bin(i, bits(i))))
       print()
except:
    print('\n\nTchau!')

