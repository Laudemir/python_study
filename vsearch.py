#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

def search4vowels(phrase:str) -> str:
    """Return any vowels found in a supplied phrase"""
    vowels = set('aeiouAEIOU')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str) -> set:
    """Return a set of the 'letters' found in a 'phrase'."""
    return set(letters).intersection(set(phrase))

s = str(input('Escreva uma frase: '))
print(search4letters(s, 'air'))
print(search4vowels(s))
