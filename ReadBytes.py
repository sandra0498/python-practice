import binascii
import optparse

filename =' '
file_obj = open(filename, 'r+')
for line in file_obj:
    for word in line:
        binVal = ' '.join(format(x, 'b') for x in bytearray(word, 'utf-8'))
        # print(binVal)
        # print(type(binVal))
        for letter in word:
            if not letter.isspace():
                # getting the ascii value of the char
                ascVal = ord(letter)
                # print(ascVal)
                print('the ascii value for {} is {}'.format(letter, ascVal))
                # # print(ascVal)
                h = hex(ascVal)
                print(h)
                binData = bin(ascVal)
                # print(type(binData))
                # str_to_bin = binascii.a2b_uu(binData)
                # print(str_to_bin)
                # bin_to_hex = binascii.hexlify(str_to_bin)
                # print(bin_to_hex)

