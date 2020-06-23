vowels = ['a', 'e', 'i', 'o', 'u', 'y']


def countVowels(question):
    amountofvowels = 0
    for letter in question:
        if letter in vowels:
            amountofvowels += 1

    FirstRule(amountofvowels, question)
    # print('this is the amount of vowels ', amountofvowels)


def FirstRule(num, word):  # passing in the num of vowels and the word itself as arguments
    print('Enter this method ')
    print('This is the word argument:', word)
    print('This is the int argument:', num)
    word = word.lower()

    print('This is the new casing of the same word ', word)

    # check if q is in the word
    if 'q' in word:
        # if q IS in the word, then we determine the index
        index = word.index('q')
        if index != len(word) - 1:  # as long as Q is not the last letter
            if word[index + 1] == 'u':  # check if u follows the q
                num -= 1

    SecondRule(num, word)
    # print('This is the new vowel count ', num)


def SecondRule(num, word):
    # this one determines what to look for if there is a 'y' in the word
    if 'y' in word:
        index = word.index('y')
        if index == 0:
            for i in range(1, 3):  # check two spaces after the 'y'
                if word[i] in vowels:
                    num -= 1  # decrements count for every vowel found after the 'y'
        elif word.endswith('y'):
            # option if 'y' is at the end of the word
            if word[index - 1] in vowels:  # if vowel is before the char
                num -= 1  # decrement

        else:  # conditional if 'y' is in the middle
            if word[index - 1] in vowels or word[index + 1] in vowels:
                # if a vowel is on either side of 'y'
                num -= 1

    print('count --> ', num)


def thirdRule(num, word):
    # this one determines what to do if there's at least
    # >> an 'e' in the word
    if 'e' in word:
        index = word.rfind('e')
        if index == len(word) - 1:  # while 'e' is @ the end of the word
            if word[index - 2] in vowels:  # if the char two spaces in front is a vowel
                #  >> ex) kite --> 2 vowels --> b/c 'i' is 2 spaces in front
                #   >>> of 'e' --> it removes the vowel count --> as a result, 1 syllable
                num -= 1  # decrements the initial vowel count

            if 'es' in word:  # checks if substring is in the string
                place = word.rfind('es')  # gets the index of the rightmost side


question = input("Enter a word please : ")
countVowels(question)
