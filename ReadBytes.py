import binascii
import optparse

filename = 'CSJOKE.txt'
file_obj = open(filename, 'r+')

output = ''
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
                # print('the ascii value for {} is {}'.format(letter, ascVal))
                # # print(ascVal)
                h = hex(ascVal)
                # print(h)
                output += h
                output += ' '

    output += '\n'
print(output)

