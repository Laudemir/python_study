#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

# Alfabeto
#
# Referência <http://www.abbra.com.br/numerologia3.htm>
#

def alfa(nome):
    a = {
    'A': 1,'B': 2,'C': 3,'D': 4,'E': 5,'F': 6,'G': 7,'H': 8,'I': 9,
    'J': 1,'K': 2,'L': 3,'M': 4,'N': 5,'O': 6,'P': 7,'Q': 8,'R': 9,
    'S': 1,'T': 2,'U': 3,'V': 4,'W': 5,'X': 6,'Y': 7,'Z': 8,
    'Ã': 1, 'Â':1,'É':5
    }

    soma = 0
    for c in nome:
        soma = soma + a[c]
    return soma

def char_sum(soma):
    n = 0
    print('soma depois da função é', soma)
    if soma > 9:
        print('soma depois de soma > 9=', soma)
        for i in str(soma):
            n = n+int(i)
        char_sum(n)
    else:
        print('soma final vale: ', soma)
        resultado = int(soma) 
        print('resultado = ', resultado)    
        return resultado
    #return soma



nome = str(input('Digite um nome para ser analizado: ').strip())
strippedName = nome.upper().replace(" ", "")
soma = alfa(strippedName)
cabala = char_sum(soma)
print()
print("O nome \'{}\' tem a soma total de: {} ".format(nome, soma))
print("A soma cabalistica é {}".format(cabala))
print()
