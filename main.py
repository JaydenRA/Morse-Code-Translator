from sys import exit

DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 
        'D':'-..', 'E':'.', 'F':'..-.', 
        'G':'--.', 'H':'....', 'I':'..', 
        'J':'.---', 'K':'-.-', 'L':'.-..', 
        'M':'--', 'N':'-.', 'O':'---', 
        'P':'.--.', 'Q':'--.-', 'R':'.-.', 
        'S':'...', 'T':'-', 'U':'..-', 
        'V':'...-', 'W':'.--', 'X':'-..-', 
        'Y':'-.--', 'Z':'--..', ' ':' '}

def main():
    print('''
MORSE CODE TRANSLATOR - BY SYSKEY
1: Encrypt
2: Decrypt

9: Quit
    ''')
    option = int(input("Choose an Option: "))

    if option == 1:
        subject = input("Plain text to convert: ")
        print(encrypt(subject.upper()))
    elif option == 2:
        subject = input("Morse code to convert: ")
        print(decrypt(subject))
    elif option == 9:
        exit(0)
    else:
        print("That is not an option, please try again.")
        main()

def encrypt(x):
    encrypted = ""
    for char in x:
        encrypted += DICT[char]
        encrypted += " "

    return encrypted

def decrypt(x):
    x += " "
    decrypted = ""
    EncryptedLetter = ""
    for char in x:
        if char != " ":
            EncryptedLetter += char
        else:
            for key, value in DICT.items():
                if value == EncryptedLetter:
                    decrypted += key
            decrypted += " "
            EncryptedLetter = ""

    return decrypted


main()