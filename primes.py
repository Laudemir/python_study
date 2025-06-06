#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#


def is_prime(n):
    p=0
    for i in range(1, n):
        if n % i == 0:
            p+=1
            if  p==2:
                break
    if p<2:    
        return True       
i=1
while i > 0:
    i = int(input("Um inteiro positivo: "))

    if is_prime(i):
        print("{} é um numero primo".format(i))
    else:
        print("{} nao é um numero primo".format(i))
print()
print('Tchau!')


