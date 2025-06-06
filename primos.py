#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

def is_prime(n):
    p=0
    for i in range(1, n):
        if n % i == 0:
            p+=1;
        if p>1:
            print('{} nao eh numero primo'.format(n))
            break
    if p == 1:
        print('{} eh numero primo'.format(n))

i = int(input("Um inteiro positivo: "))
is_prime(i)
print('Tchau!')


