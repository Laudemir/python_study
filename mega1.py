#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
import random

# Global
MEGA = 6
LOTO = 15
RANGE_MEGA = 60
RANGE_LOTO = 25

# Cores
vermelho= '\033[31m'
verde   = '\033[32m'
azul    = '\033[34m'

ciano   = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto   = '\033[30m'

branco  = '\033[37m'

limpa   = '\033[0;0m'
negrito = '\033[1m'
reverso = '\033[2m'




palpites = int(input("Quantos palpites? "))


print()
for k in range(palpites):
    n=[]
    for i in range(MEGA):
        n.append('%02d' %(random.randint(1, RANGE_MEGA)))
    em_ordem = sorted(n)
    print (amarelo+negrito+'palpite:'+limpa, end=" |")
    for i in range(MEGA):
        print(vermelho+negrito+em_ordem[i]+limpa, end="|")
    print()
print()

