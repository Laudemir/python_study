#!/usr/bin/env python3

def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
             L1.remove(e)
 
L1 = [1, 2, 3, 4, 6, 7, 8, 9]
L2 = [1, 2, 5, 6, 7, 9, 10, 11]

print("L1: ", L1)
print("L2: ", L2)

remove_dups(L1, L2)
print()
print("L1: ", L1)
print("L2: ", L2)
