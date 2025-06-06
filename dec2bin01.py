#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
def bits(num):
    bits = 0
    temp = num
    while temp > 1:
        temp = temp // 2
        bits = bits + 1
    return int(bits+1)

def dec2bin(num, bits):
    r = ''
    for i in range(bits-1, -1, -1):
        if (num >> i) % 2 == 0:
            r = r + '0'
        else:
            r = r + '1'
    return r

i = 1
while i > 0:
   i = int(input("Um número decimal: "))
   print()
   print("nº {} tem ........: {} bits".format(i, bits(i)))
   print("nº {} em binário .: {}".format(i, dec2bin(i, bits(i))))
   print()

