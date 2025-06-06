#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
# Verificando IMC

def main():
    nome = str(input('\nInforme o nome do paciente: '))
    altura = float(input(' Informe sua altura em (m): ' ))
    peso   = float(input('     Informe seu peso (Kg): ' ))
    imc = peso/(altura**2)

    st = ''
    if imc < 18.5:
        st='Abaixo do peso'
    elif imc >= 18.5 and imc <= 24.9:
        st='Peso Normal'
    elif imc >= 25 and imc <= 29.9:
        st='Sobrepeso'
    elif imc >= 30 and imc <= 34.9:
        st='Obesidade Grau I'
    elif imc >= 35 and imc <= 39.9:
        st='Obesidade Grau II'
    else:
        st='Obesidade Mórbida'

    print('\nPaciente: ', nome)
    print('IMC = {:.1f}'.format(imc))
    print(st)
    print()

if __name__ == '__main__':
    main()
 
