#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

# Lista
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

word = input("Uma palavra ou frase: ")



# Dicionario
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

print()
for k, v in sorted(found.items()): 
    print (k, 'was found', v, 'time(s)')
print()


