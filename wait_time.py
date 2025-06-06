#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
import sys
import os
import random
import time


wait_time = random.randint(1, 60)

print('\n\n')
print("Conte mentalmente de 1 a 60 segundos")
print("Pressione <Enter> para comecar ....")
input()
os.system('setterm -cursor off')
time.sleep(wait_time)
os.system('setterm -cursor on')

print()
print('Terminou ...')
i = int(input("Quantos segundos contou?  "))


if i ==  wait_time:
    print()
    print("Uhuuuu! Voce acertou, foram mesmo : ", wait_time)
    print()
else:
    print()
    print("aaaaah! Voce errou, foram: ", wait_time)
    print()


