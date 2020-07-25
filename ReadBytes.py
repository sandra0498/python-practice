import binascii
import optparse

filename = ' '
file_obj = open(filename, 'r+')
for line in file_obj:
    print(line)
