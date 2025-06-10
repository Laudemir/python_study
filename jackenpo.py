#!/usr/bin/env python3
# coding: utf-8
#
#
# @Autor: Laudemir Ap. de Oliveira
#
# Jogo Ja Ke Pô
from time import sleep
from random import randint

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
sleep(1)
print('\n   KEN')
sleep(1)
print('\n   PooooÔ')

print('\n\n')
if jogador == computador:
    print('   EMPATOU!!!')
elif (jogador==0 and computador==1) or (jogador==1 and computador==2) or (jogador==2 and computador==0):
    print('   VOCÊ VENCEU!')
else:
    print('   O COMPUTADOR VENCEU!')
print()
print('   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print()
print('    VOCÊ APOSTOU.........: ', aposta[jogador])
print('    O COMPUTADOR APOSTOU.: ', aposta[computador])
print()
print('   -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
