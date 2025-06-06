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
        print(s[c], end='', flush='True')
        sleep(t)
    print()

while True:
    aposta = ('PEDRA', 'TESOURA', 'PAPEL')
    pontos_jogador = 0
    pontos_computador = 0
    computador = randint(0,2)

    print()
    print ( '  -=-=-=-=-=-=-=-=-=-')
    print ( '     [0] = PEDRA' )
    print ( '     [1] = TESOURA')
    print ( '     [2] = PAPEL')
    print ( '     [3] = Sair')
    print ( '  -=-=-=-=-=-=-=-=-=-')
    print()
    
    jogador=int(input('   Escolha: '))
    if jogador == 3:
        break
    
    if jogador < 0 or jogador > 2:
        print()
        print('Opção inválida!')
        print()
        exit(0)
        print()

    print('\n   JA')
    sleep(0.2)
    print('\n   KEN')
    sleep(0.2)
    print('\n   PÔoo')
    sleep(0.2)

    print('\n\n')
    if jogador == computador:
        print('EMPATOU!!!')
    elif (jogador==0 and computador==1) or (jogador==1 and computador==2) or (jogador==2 and computador==0):
        print('O vencedor é', end=' ')
        mostrar('...', 0.5)
        print()
        print('****** VODÊ. PARABÉNS! *****')
    else:
        print('O vencedor é', end=' ')
        mostrar('...', 0.2)
        print()
        print('Ahhhh!') 
        print('VOCÊ PERDEU!')

    print()
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print()
    print('Você Jogou.........: {}'.format(aposta[jogador]))
    print('O Computador jogou.: {}'.format(aposta[computador]))
    print()
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
     

    print('\n\n')

print('\nThanks for gaming!')
