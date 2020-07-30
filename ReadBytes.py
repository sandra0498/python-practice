filename = 'CSJOKE.txt'

out_file = open('output.txt', 'w')

output = ''
try:
    file_obj = open(filename, 'r+')  # input file
    for line in file_obj:
        for word in line:
            # binVal = ' '.join(format(x, 'b') for x in bytearray(word, 'utf-8'))
            for letter in word:
                if not letter.isspace():
                    # getting the ascii value of the char
                    ascVal = ord(letter)
                    # print(ascVal)
                    # print('the ascii value for {} is {}'.format(letter, ascVal))

                    # converting the ascii value to hex
                    h = hex(ascVal)
                    # print(h)
                    output += h
                    output += ' '

        output += '\n'
    print(output)
    out_file.write(output)
except FileNotFoundError:
    print('File not found! ')

