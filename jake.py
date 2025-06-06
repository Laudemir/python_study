#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
# Jogo Ja Ke Pôi
from time import sleep
from random import randint

def mostrar(s, t):
    for c in range(0, len(s)):
        print(s[c], end='', flush='False')
        sleep(t)
    print()

aposta = ('PEDRA', 'TESOURA', 'PAPEL')
pontos_jogador = 0
pontos_computador = 0
computador = randint(0,2)
print()
print ( '  -=-=-=-=-=-=-=-=-=-')
print ( '     [0] = PEDRA' )
print ( '     [1] = TESOURA')
print ( '     [2] = PAPEL')
print ( '  -=-=-=-=-=-=-=-=-=-')
print()
    
jogador=int(input('   Escolha: '))
    
if jogador < 0 or jogador > 2:
    print()
    print('Opção inválida!')
    print()
    exit(0)
    print()

print('\n   JA')
sleep(0.5)
print('\n   KEN')
sleep(0.5)
print('\n   PÔoo')
sleep(0.3)

print('\n\n')
if jogador == computador:
    mostrar('   EMPATOU!!!', 0.05)
elif (jogador==0 and computador==1) or (jogador==1 and computador==2) or (jogador==2 and computador==0):
    print('The Winner is', end=' ')
    mostrar('.......', 0.5)
    print()
    print('****** VOCÊ! *****')
else:
    print('The Winner is', end=' ')
    mostrar('.......', 0.5)
    print()
    print('Ahhhh!, O COMPUTADOR!')
print()
print('   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print()
print('    VOCÊ APOSTOU.........: {}'.format(aposta[jogador]))
print('    O COMPUTADOR APOSTOU.: {}'.format(aposta[computador]))
print()
print('   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
     

print('\n\n')
