#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
import random

# Tabela cores
vermelho= '\033[31m'
amarelo = '\033[33m'
negrito = '\033[1m'
limpa   = '\033[0;0m'


palpites = int(input("Quantos palpites? "))
print()
for k in range(palpites):
    loto = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    x=10
    y=24
    while x != 0:
        del loto[random.randint(0, y)]
        y-=1
        x-=1
    print(amarelo+negrito+'palpite: '+limpa, end='|')
    for i in range (15):
        print('%02d' %(loto[i]), end='|')
    print()

print() 
