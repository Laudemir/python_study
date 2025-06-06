#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
#
# @Autor: Laudemir Oliveira
#
import os

def main():
    # Your code here
    nome_arquivo = input('nome do arquivo: ')

    e = ler_extensao_arquivo(nome_arquivo)

    print('A extensão do arquivo é:', e[1])

def ler_extensao_arquivo(nome_arquivo):
    extensao = os.path.splitext(nome_arquivo)
    return extensao

if __name__ == '__main__':
    main()
