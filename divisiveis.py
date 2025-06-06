#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

def is_prime(n):
    for i in range(1, n):
        if n % i == 0:
            print ('{} divivisel por: {}'.format(n, i))
  
i = int(input("Um inteiro positivo: "))
is_prime(i)
print()
print('Tchau!')


