#!/usr/bin/env python3
#
# @Autor: Laudemir Oliveira
# @E-mail: laudemir.oliveira@gmail.com
# @Date: 2024-05-16 Thursday
#
#
def crivo_eratostenes(n):
    # inicializa uma lista de booleanos
    primos = [True] * (n+1)
    p = 2

    while (p * p <= n):
        # Se primos[p] não for alterado, então é um número primo
        if primos[p]: 
            # Atualiza todos os múltiplos de p para False
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1

        # Coleta todos os números primos
        numeros_primos = [p for p in range(2, n + 1) if primos[p]]
        return numeros_primos

# Exemplo de uso
n = int(input("Qual o limite gafanhoto? "))
print(f"Numeros primos até {n}: {crivo_eratostenes(n)}")

