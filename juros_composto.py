#!/usr/bin/env python3
#
# @Autor: Laudemir Oliveira
# @E-mail: laudemir.oliveira@gmail.com
# @Date: 2024-08-05 Monday
#
#i
APORTE = 753.00
def calcular(vlr_inicial, taxa, periodo):
    vlr_futuro = vlr_inicial * (1 + taxa/periodo) ** periodo
    return vlr_futuro


PV = float(input("Valor inicial? "))
# vlr_inicial = 992247.13
i = float(input("Taxa? "))
# taxa = 0.037
n = int(input("Periodo? "))
i = i / 100

print()
print('-' * 30)
print(f"   PV: R$ {PV:.2f}")

for temp in range(n, 0, -1):
    FV = calcular(PV, i, n)
    PV = FV

print(f"   i: {i*100:.3f} %")
print(f"   n: {n}")
#print(f"   Aporte mensal : R$ {APORTE:.2f}")
print(f"   FV: R$ {FV:.2f}")
print('-' * 30)
print()
