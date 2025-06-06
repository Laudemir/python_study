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


k = int(input("Um inteiro positivo: "))

for i in range (2, k+1):
    if is_prime(i):
        print(i, end=' ')
print()

