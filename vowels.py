#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
word = input("Uma palavra ou frase: ")
v=0
c=0
for letter in word:
    if letter in vowels:
        v+=1
    else:
        c+=1
print()
print("Vogais......:", v)
print("Consoantes..:", c)
print()


