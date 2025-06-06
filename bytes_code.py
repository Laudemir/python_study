#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Autor: Laudemir Ap. de Oliveira
#


def main():
    # Your code here
    print('Hello World!')
    input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
    input_characters = input_bytes.decode('utf-16')
    print(repr(input_characters))

    # Conversao de caracteres em bytes antes de seu envio
    output_characters = 'We copy you down, Eagle.\n'
    output_bytes = output_characters.encode('utf-8')

    with open('eagle.txt', 'wb') as f:
        f.write(output_bytes)

if __name__ == '__main__':
    main()
    
