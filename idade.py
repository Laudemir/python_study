#!/usr/bin/env python3
#
# @Autor: Laudemir Oliveira
# @E-mail: laudemir.oliveira@gmail.com
# @Date: 2024-03-25 Monday
#
from datetime import datetime

nascimento = input("Data de nascimento (dd/mm/aaaa): ")
# nascimento = "10/07/1962"
nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
data_atual = datetime.now()

idade = data_atual.year - nascimento.year

mes_atual = data_atual.month
dia_atual = data_atual.day
mes_nascimento = nascimento.month
dia_nascimento = nascimento.day

if mes_nascimento > mes_atual:
    idade -= 1
elif mes_nascimento == mes_atual and dia_nascimento > dia_atual:
    idade -= 1

print(f"Sua idade: {idade} anos")
