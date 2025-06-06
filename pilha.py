#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
from time import sleep

class copiar_pilha:
    def __init__(self, p):
        self.__p = p

    def recupera(self):
        return self.__p


def inserir_dados_na_pilha(pilha):
    n = int(input('Quantos dados deseja inserir? '))

    for i in range(n):
        st = input('Inserir dado nr {}: '.format(i+1))
        pilha.append(st)
    return pilha


def remover_dados_da_pilha(pilha):
    if(pilha):
        print(pilha.pop(), 'saiu ')
        return pilha


def mostrar_pilha(pilha):
    if (pilha):
        print('Pilha >>> ', pilha)
    else:
        print('\nA pilha está vazia!')



def main():
    # Criar uma pilha vazia
    pilha=[]
    print(pilha)
    mostrar_pilha(pilha)

    while True:    
        # Menu
        print('\n-------------------------------')
        print('       Pilha em Python')
        print('-------------------------------')
        print('\n')
        print('  [1] Inserir dados na pilha')
        print('  [2] Remover dados da pilha')
        print('  [3] Mostrar dados da pilha')
        print('  [0] Sair')
        print('\n')
        print('-------------------------------')
        
        try:
            opcao = int(input('   Opção: '))
            if 0 > opcao > 3 :
                    main()
        except:
            print('Opção invalida!')
            break

        print('\n')
        if opcao == 0:
            break

        if opcao == 1:
            pilha = inserir_dados_na_pilha(pilha)
            print('\n')
            mostrar_pilha(pilha)

        if opcao == 2:
            pilha = remover_dados_da_pilha(pilha)
            print('\n')
            mostrar_pilha(pilha)

        if opcao == 3:
            print('\n')
            mostrar_pilha(pilha)

if __name__ == '__main__':
    main()
    
