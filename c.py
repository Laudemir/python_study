#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

class A:
    def __init__(self, i=100):
	self.i = i
	
class B(A):
    def __init__(self, j=0):
	self.j = j

	
def main():
    b = B()
    print(b.i)
    print(b.j)
    
    
main()

