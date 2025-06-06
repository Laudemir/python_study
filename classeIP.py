#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
i = 0
while(i >= 0 or i < 256):
    i = int(input('Valor de 0 a 255: '))

    if not( i & 0x80 ):
        print('Classe A')
        print('Máscara padrão: 255.0.0.0')

    if ( i & 0xC0 ) == 0x80:
        print('Classe B')
        print('Máscara padrão: 255.255.0.0')

    if ( i & 0xE0 ) == 0xC0:
        print('Classe C')
        print('Máscara padrão: 255.255.255.0')

    if ( i & 0xE0 ) > 0xC0:
        print('Multicast')
