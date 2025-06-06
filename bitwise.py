#!/usr/bin/env python3
#
# @Autor: Laudemir Oliveira
# @E-mail: laudemir.oliveira@gmail.com
# @Date: 2024-03-11 Monday

READ_PERMISSION    = 4
WRITE_PERMISSION   = 2
EXECUTE_PERMISSION = 1

userPermission = READ_PERMISSION

print(userPermission)
print(bin(userPermission))

userPermission = READ_PERMISSION | WRITE_PERMISSION
print(userPermission)
print(bin(userPermission))


userPermission = READ_PERMISSION | EXECUTE_PERMISSION
print(userPermission)
print(bin(userPermission))


userPermission = READ_PERMISSION | WRITE_PERMISSION | EXECUTE_PERMISSION
print(userPermission)
print(bin(userPermission))





