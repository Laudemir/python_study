#!/usr/bin/env python3
#
# @Autor: Laudemir Oliveira
# @E-mail: laudemir.oliveira@gmail.com
# @Date: 2024-08-05 Monday
#
#
QTD = 365 * 24 * 60 * 60

def calcular(n):
    e = (1 + 1 / n) ** n
    return e

n = int(input("Qual o valor de iterações para calculo de e? "))
e = calcular(n)


print()
#print(f"Calculando baseado em {n} valores ...")
print(f"Número aproximado de euler: {e}")
print()
