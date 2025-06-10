#!/usr/bin/env python3
#
# @Autor: Laudemir Oliveira
# @E-mail: laudemir.oliveira@gmail.com
# @Date: 2024-03-16 Saturday
#
#

import locale
import time

# Definir a localizaçao para o portugues
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S", tempo_em_struct)
print(f"Tempo formatado: {tempo_formatado}")
