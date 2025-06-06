#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#


def desloc(n):
    return n >> 1

i = int(input("Informe um número inteiro: "))
while i > 0:
    print(i, end=" | ")
    i = desloc(i)
print()
