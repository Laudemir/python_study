#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Simple program explain How:
# to using lambda functions
# bitwise logic
# calculate subnet Ip
#
# @autor   : Laudemir
# @version : 18.05.1
#
#

# Lambda functions
ipRemoveSpaces = lambda x: x.split(' ')
ipRemoveDots   = lambda x: x.split('.')

# Functions
def dec2bin(n):
   if type(n) != int:
      n = int(n) # Define as int
   num = ''
   for i in range(7, -1, -1):
      if (n >> i) % 2 == 0:
         num = num + '0'
      else:
         num = num + '1'

   return num



# global vars
net_ip = []
bcast  = []



# Start
try:
   # Getting IP and NETMASK 
   print()
   n = input('IP and NETMASK : ')

   # Remove spaces between IP and NETMASK
   n = ipRemoveSpaces(n)

   # Remove dots between IP and NETMASK
   ip      = ipRemoveDots(n[0])
   netmask = ipRemoveDots(n[1])


   # NETWORK and BROADCAST calculation
   #     NETWORK   = IP .and. NETMASK
   #     BROADCAST = NETWORK .or. (255 xor NETMASK)
   for i in range(4):
      net_ip.append( int(ip[i]) & int(netmask[i]) )
      bcast.append ( int(net_ip[i]) | (255 ^ int(netmask[i])) )



   # Printing all the information
   print ('\n\n')
   print('Decimal Notation')
   print('IP...........: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))
   print('NETMASK......: {}.{}.{}.{}'.format(netmask[0], netmask[1], netmask[2], netmask[3]))
   print('NETWORK......: {}.{}.{}.{}'.format(net_ip[0], net_ip[1], net_ip[2], net_ip[3]))
   print('BROADCAST....: {}.{}.{}.{}'.format(bcast[0], bcast[1], bcast[2], bcast[3]))
   print('FIRST HOST...: {}.{}.{}.{}'.format(net_ip[0], net_ip[1], net_ip[2], net_ip[3]+1))
   print('LAST HOST....: {}.{}.{}.{}'.format(bcast[0], bcast[1], bcast[2], bcast[3]-1))

   print ('\n')
   print ('Binary Notation')
   print('IP...........: {}.{}.{}.{}'.format( dec2bin(ip[0]), dec2bin(ip[1]), dec2bin(ip[2]), dec2bin(ip[3])) )
   print('NETMASK......: {}.{}.{}.{}'.format( dec2bin(netmask[0]), dec2bin(netmask[1]), dec2bin(netmask[2]), dec2bin(netmask[3])) )
   print('               -----------------------------------')
   print('NETWORK......: {}.{}.{}.{}'.format( dec2bin(net_ip[0]), dec2bin(net_ip[1]), dec2bin(net_ip[2]), dec2bin(net_ip[3])) )
   print()
   print('BROADCAST....: {}.{}.{}.{}'.format( dec2bin(bcast[0]), dec2bin(bcast[1]), dec2bin(bcast[2]), dec2bin(bcast[3])) )
   print()
   print('FIRST HOST...: {}.{}.{}.{}'.format( dec2bin(net_ip[0]), dec2bin(net_ip[1]), dec2bin(net_ip[2]), dec2bin(net_ip[3]+1)) )
   print('LAST HOST....: {}.{}.{}.{}'.format( dec2bin(bcast[0]), dec2bin(bcast[1]), dec2bin(bcast[2]), dec2bin(bcast[3]-1)) )

   print('\n\n')
except:
   print()
   print(' Invalid input: ')
   print('    valid ex. : 192.168.10.1 255.255.255.0')
   print()

#End.

