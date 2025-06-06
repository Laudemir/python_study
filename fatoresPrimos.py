#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

def fatorialPrimo(n):
    fatoresPrimos = []
    d = 2
    while n > 1:
        while n % d == 0:
            fatoresPrimos.append(d)
            n /= d
        d += 1
    return fatoresPrimos

def main():
    num = 1
    while num>0:
        num = int(input('Entre com um numero decimali [0 pra sair]: '))
        print()
        print(num, end=': ')
        print(fatorialPrimo(num))
        print()

if __name__ == '__main__':
    main()
        
