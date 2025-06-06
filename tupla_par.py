#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
'''
   Vamos resolver um exercicio que envolve tuplas.
   desenvolver uma funcao chamada tupla_par. Essa funcao
   recebe uma tupla com entrada e retorna uma nova tupla
   como saida onde os elementos dessa nova tupla sao os
   elementos curjos indices sao numeros pares.
   Lembrando que o indice comeca a partir de zero.

   Exemplo de tupa de entrada: ('oi', 'estou', 'estudando', 'poo')
   Deve retornar ('oi', 'estudando')
'''

def tupla_par(tupla):
   tuplaPar=()
   for i in range(len(tupla)):
      if(i%2==0):
         tuplaPar = tuplaPar + (tupla[i],)
   return(tuplaPar)


t = ('oi', 'estou', 'estudando', 'poo')
print(tupla_par(t))



