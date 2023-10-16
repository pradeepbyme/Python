cipher = """       88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88                                  """
print(cipher)
lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                       'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                       'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                       'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
                       'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                       'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                       'w', 'x', 'y', 'z']

def ceaser_cipher():
    encdec = input("Type 'encode' or 'decode' \n -- ").lower()
    inp = input("Enter the text : ").lower()
    shift = int(input("Enter the number to be shifted : "))


    def encode(plain_text, shift_amount):
        encoding = ''
        for char in plain_text:
            encoding += lowercase_alphabets[lowercase_alphabets.index(char) + shift_amount]
        print(encoding)


    def decode(cipher_text, shift_amount):
        decoding = ''
        for char in cipher_text:
            decoding += lowercase_alphabets[lowercase_alphabets.index(char) - shift_amount]
        print(decoding)


    if encdec == 'encode':
        encode(inp, shift)
    elif encdec == 'decode':
        decode(inp, shift)
    opinion = input("Do you wanna again ? y / n : ")
    if opinion == 'y':
        ceaser_cipher()
    else:
        print("Thanks for choosing us, ceasing your data !")

ceaser_cipher()