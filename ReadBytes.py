import binascii
import optparse

filename =' '
file_obj = open(filename, 'r+')
for line in file_obj:
    for word in line.strip():
        for letter in word:
            str_to_bin = binascii.a2b_uu(letter)
            # print(str_to_bin)
            bin_to_hex = binascii.hexlify(str_to_bin)
            print(bin_to_hex)

