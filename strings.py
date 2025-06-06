#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
# Curso.......: Python 3 - Mundo 1
# Professor...: Gustavo Guanabara
# site........: cursoemvideo.com
# Data........: 27/07/2020
#
#


def formate(frase):
    lista=['|']
    for i in range(len(frase)):
        lista.append(frase[i] + "|")
    return(''.join(lista))
        




frase = "Curso Python é com Hashtag"
print()
print ("Frase..:", frase)
print()

print("""
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---!
| C | u | r | s | o |   | P | y | t | h | o | n |   | é |   | c | o | m |   | H | a | s | h | t | a | g |
+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  
""")


print("")
print("len(frase) .......................: ", len(frase))
print("frase[9] .........................: ", frase[9])
print("frase[6:11] ......................: ", frase[6:11]) 
print("frase[9:21] ......................: ", frase[9:21])
print("frase[9:21:2] ....................: ", frase[9:21:2]) 
print("frase[:5] ........................: ", frase[:5])
print("frase[15:] .......................: ", frase[15:])
print("frase[9::3] ......................: ", frase[9::3])
print("frase.count('o') .................: ", frase.count('o'))
print("frase.count('o',0,13) ............: ", frase.count('o',0,13))
print("frase.find('Android') ............: ", frase.find('Android'))
print("frase.find('Python')..............: ", frase.find('Python'))
print("'Curso' in frase .................: ", 'Curso' in frase)
print("'Android' in frase................: ", 'Android' in frase)
print("frase.replace('Python','Android') : ", frase.replace('Python','Android'))
print("frase.upper(() ...................: ", frase.upper())
print("frase.lower() ....................: ", frase.lower())
print("frase.capitalize() ...............: ", frase.capitalize())
print("frase.title() ....................: ", frase.title())
print("frase.split() ....................: ", frase.split())
print("','.join(frase.split()) ..........: ", ','.join(frase.split()))
print("'-'.join(frase.split()) ..........: ", '-'.join(frase.split()))
print("'.'.join(['192','168','15','1']) .: ", '.'.join(['192','168','15','1']))
print()

# Transformação
#
frase="                   Aprenda Python     "
print("frase ............................: ", formate(frase))
print("frase.strip() ....................: ", formate( frase.strip() ))
print("frase.rstrip() ...................: ", formate( frase.rstrip() ))
print("frase.lstrip() ...................: ", formate( frase.lstrip() ))
print("frase.replace(\" \", \"\") ...........: ", formate( frase.replace(" ", "")))
print()

