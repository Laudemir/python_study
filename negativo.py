#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
def negativo(x):
    return x<0


i = int(input("Entre com um numero? "))
if(negativo(i)):
    print("{} eh um numero negativo".format(i))
else:
    print("{} sh um numero positivo".format(i))
