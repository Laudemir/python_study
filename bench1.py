#!/usr/bin/env python3
#
# @Autor: Laudemir Oliveira
# @E-mail: laudemir.oliveira@gmail.com
# @Date: 2024-05-16 Thursday
#
#
from timeit import Timer

# Define o código a ser medio como uma função
def code_to_test():
    for i in range(100_000_000):
        pass

# Cria um objeto Timer
t = Timer(code_to_test)

# Mede o tempo de execução
elapsed_time = t.timeit(number=1)

print(f"Tempo decorrido: {elapsed_time:.6f} segundos")


