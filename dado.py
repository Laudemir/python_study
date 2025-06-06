#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#
# Play Dice
#

from random import randint

# Display dice
def dice(x):
    if x == 1:
        print('''
   +-----+
   :     :
   :  º  :
   :     :
   +-----+
''')
    elif x == 2:
        print('''
   +-----+
   :º    :
   :     :
   :    º:
   +-----+
''')
    elif x==3:
        print('''
   +-----+
   :º    :
   :  º  :
   :    º:
   +-----+
 ''')
    elif x == 4:
        print('''
   +-----+
   :º   º:
   :     :
   :º   º:
   +-----+
''')
    elif x == 5:
        print('''
   +-----+
   :º   º:
   :  º  :
   :º   º:
   +-----+
''')
    else:
        print('''
   +-----+
   :º   º:
   :º   º:
   :º   º:
   +-----+
''')

print()
 
# Amount of play
#   
amount_play = 1

# Start variables
#
your_score = 0
computer_score = 0

# Your play
#
print()    
print('-=-=-=-=-=-=-')
print('    YOU!')
print('-=-=-=-=-=-=-')
for i in range(1, amount_play+1):
    d = randint(1, 6)
    dice(d)
    your_score += d

# computer play
#
print()
print('-=-=-=-=-=-=-')
print('  COMPUTER!')
print('-=-=-=-=-=-=-')
for i in range(1, amount_play+1):
    d = randint(1, 6)
    dice(d)
    computer_score += d 


# Results
#
print()
if your_score > computer_score:
    print('    -=-=- You Won! -=-=-')
    print('\nYour score ......: {:2} points'.format(your_score))
    print('Computer score ..: {:2} points'.format(computer_score))
elif computer_score > your_score:
    print(' -=-=- Computer Won! -=-=-')
    print('\nComputer score ..: {:2} points'.format(computer_score))
    print('Your score ......: {:2} points'.format(your_score)) 
else:
    print(' -=-=- Game tied! -=-=-')
    print('\nYour score ......: {:2} points'.format(your_score))
    print('Computer score ..: {:2} points'.format(computer_score))
print('\n\n')

# End
#
