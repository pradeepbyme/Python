import random
import string  # for alphabets and numbers

uppercase_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                       'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                       'Y', 'Z']

lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                       'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                       'y', 'z']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*',
                      '(', ')']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
choices = [uppercase_alphabets, lowercase_alphabets, numbers, special_characters]


def tryagain():

    """This generates a strong password"""

    characters = int(input('How many digits it should be ? \n'))
    pypass = ''
    for i in range(0, characters):
        pypass += random.choice(choices)[random.randint(0, len(choices) - 1)]
    print(pypass)
    op = input("Do you wanna try again ? y/n ")
    if op == 'y':
        tryagain()
    elif op == 'n':
        print("That's your opinion !")
    else:
        print("Thanks for choosing us !")


tryagain()
