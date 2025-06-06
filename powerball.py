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

palpites = 0
while palpites <= 0:
    palpites = int(input("Quantos palpites? "))


print()
for k in range(palpites):
    loto = list(range(1,61))
    x=54
    y=59
    while x != 0:
        del loto[random.randint(0, y)]
        y-=1
        x-=1
    print(amarelo+negrito+'palpite: '+limpa, end=' | ')
    
    for i in range (5):
        loto[i] = ('%02d' %(loto[i]))
        print(vermelho + negrito + loto[i] + limpa, end=' | ')
    print(' (' + vermelho + negrito + str(random.randint(1,25)) + limpa, end=')')
    print()
print() 
