#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

from datetime import datetime

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

right_this_minute = datetime.today().minute
right_this_second = datetime.today().second

print (datetime.today().hour)
print (datetime.today().minute)
print (datetime.today().second)

if right_this_second in odds:
    print ("This minute seems a little odd : ") 
    print (right_this_second)
else:
    print ("Not an odd second : ") 
    print (right_this_second)


