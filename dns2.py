#!/usr/bin/env python3
# coding: utf-8
#
# @Autor....: Laudemir Oliveira
# @E-mail...: laudemir.oliveira@gmail.com
# @Date.....: 06-01-2025 - Mon - 07:30
# @Version..: 2025-6
#
#
import socket

d = input("Qual o dominio? ")

with open("brute-force.txt") as arquivo:
    nomes = arquivo.readlines()

for nome in nomes:
    DNS = nome.strip("\n") + "." + d
    try:
        print(f"{DNS}: {socket.gethostbyname(DNS)}")
    except (socket.gaierror):
        #print(f"{nome}: null")
        pass


