#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
from math import pow, sqrt, acos, asin, atan, degrees

co = float(input("Qual o valor do cateto oposto (frente ao angulo) ? "))
ca = float(input("Qual o valor do cateto adjacente (ao lado do angulo) ? " ))

h = sqrt(pow(co,2) + pow(ca,2))  
sen = co/h
cos = ca/h
tang = co/ca 

print()
print("--- Voce sabia que:")
print("hipotenusa = sqrt(cateto oposto² + cateto adjacente²)")
print("seno do angulo = cateto oposto / hipotenusa")
print("cosseno do angulo = cateto adjacente / hipotenusa")
print("tangente do angulo = cateto oposto / cateto adjacente\n")

print()
print("cateto adjacente....: {}".format(ca))
print("Cateto oposto.......: {}\n".format(co))
print("Hipotenusa..........: {:.2f}\n".format(h))
print("Seno do angulo......: {:.5f} | {:.2f} graus".format(sen, degrees(asin(sen))))
print("Coseno do angulo....: {:.5f} | {:.2f} graus".format(cos, degrees(acos(cos))))
print("Tangente do angulo..: {:.5f} ! {:.2f} graus".format(tang, degrees(atan(tang))))
print()
