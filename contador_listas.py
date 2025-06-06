#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

from random import sample

try:
    qt_cart = int(input('Quantidade de números por cartela: '))
    qt_num = int(input('Quantidade de números a sortear: '))
except:
    print('\nErro: deve informar um número inteiro')
    exit(1)

print()

try:
    sorteados = sample(range(1, qt_cart+1), qt_num)

    print(sorted(sorteados))

    par = 0
    impar = 0

    for i in sorteados:
        if i % 2 == 0:
            par += 1
        else:
            impar += 1

    print()
    print('  par ocorre: {} vezes'.format( par ))
    print('impar ocorre: {} vezes'.format( impar ))
    print()

except:
    print('Erro: Quantidade de números maior que a cartela?')
    print()
