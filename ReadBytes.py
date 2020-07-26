import binascii
import optparse

filename =' '
file_obj = open(filename, 'r+')
for line in file_obj:
    for word in line:
        # getting the binary representation 
        binVal = bin(int.from_bytes(word.encode(), 'big'))
        binVal = binVal[2:]
        print(binVal)
        for letter in word:
            if not letter.isspace():
                # getting the ascii value of the char
                ascVal = ord(letter)
                # print('the ascii value for {} is {}'.format(letter, ascVal))
                # print(ascVal)
                str_to_bin = binascii.a2b_uu(letter)
                # # print(str_to_bin)
                # bin_to_hex = binascii.hexlify(str_to_bin)
                # print(bin_to_hex)

