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
qtnumeros = 4
try:
    qt_numeros_cartela = int(input("Quantos numeros por cartela? ")) 
    while palpites <= 0:
        palpites = int(input("Quantos palpites? "))
    while qtnumeros <= 4: 
        qtnumeros = int(input("Quantos numeros? "))
except:
    print('\nErro: Voce deve informar um numero inteiro!')

print()
for k in range(palpites):
    loto = list(range(1,qt_numeros_cartela+1))
    x=qt_numeros_cartela-qtnumeros
    y=qt_numeros_cartela-1
    while x != 0:
        del loto[random.randint(0, y)]
        y-=1
        x-=1
    print(amarelo+negrito+'palpite: %3d' %(k+1) + limpa, end='  |')
    
    for i in range (qtnumeros):
        loto[i] = ('%02d' %(loto[i]))
        print(vermelho+negrito+loto[i]+limpa, end='|')
    print()
print() 
