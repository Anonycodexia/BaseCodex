#!/bin/python2

import base64
import os
import sys
import binascii
os.system("clear")
os.system("figlet BaseCodex")
print("\033[1;33;40m            Programmed by : Anonycodexia\n \033[0;0m")

def en_base2(string_to_encode):
    return "0" + bin(int(binascii.hexlify(string_to_encode), 16))[2:]


def de_base2(string_to_decode):
    try:
        s = int(string_to_decode, 2)
        binascii.unhexlify('%x' % s)
    except (TypeError, ValueError) :
        print ("\033[1;31;40m Non-Binary String Provided \033[0;0m")


def en_base16(string_to_encode):
    return base64.b16encode(string_to_encode)


def de_base16(string_to_decode):
    try:
        if string_to_decode[:2].lower() == '0x':
            string_to_decode = string_to_decode[2:]
        decoded_string = base64.b16decode(string_to_decode)
        return decoded_string
    except TypeError:
        print ("\033[1;31;40m Non-Hexadecimal String Provided \033[0;0m")


def en_base32(string_to_encode):
    return base64.b32encode(string_to_encode)


def de_base32(string_to_decode):
    try:
        decoded_string = base64.b32decode(string_to_decode)
        return decoded_string
    except TypeError:
        print ("\033[1;31;40m Non-Base32 String Provided \033[0;0m")


def en_base64(string_to_encode):
    return base64.b64encode(string_to_encode)


def de_base64(string_to_decode):
    try:
        decoded_string = base64.b64decode(string_to_decode)
        return decoded_string
    except TypeError:
        print ("\033[1;31;40m Non-Base64 String Provided \033[0;0m")


def en_all(string_to_encode):
    print ("\033[1;32;40m Binary : \033[0;0m" + str(en_base2(string_to_encode)))
    print ("\033[1;33;40m Base16 : \033[0;0m" + str(en_base16(string_to_encode)))
    print ("\033[1;35;40m Base32 : \033[0;0m" + str(en_base32(string_to_encode)))
    print ("\033[1;36;40m Base64 : \033[0;0m" + str(en_base64(string_to_encode)))


def de_all(string_to_decode, string_type):
    if string_type == "bin":
        print ("\033[1;31;40m Decoded String : \033[0;0m" + str(de_base2(string_to_decode)))
    elif string_type == "b16":
        print ("\033[1;31;40m Decoded String : \033[0;0m" + str(de_base16(string_to_decode)))
    elif string_type == "b32":
        print ("\033[1;31;40m Decoded String : \033[0;0m" + str(de_base32(string_to_decode)))
    elif string_type == "b64":
        print ("\033[1;31;40m Decoded String : \033[0;0m" + str(de_base64(string_to_decode)))
    else:
        print ("\033[1;31;40m Error \033[0;0m")


# Main menu
def main_menu():

    print ("\033[1;34;40m 1. Encode your String \033[0;0m")
    print ("\033[1;34;40m 2. Decode your String \033[0;0m")
    print ("\033[1;34;40m 3. Back \033[0;0m")
    print ("\033[1;34;40m 0. Exit \033[0;0m")
    choice = str(raw_input(" >>  "))
    exec_menu(choice)

    return


# Execute menu
def exec_menu(choice):
    print ("\n")
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "\033[1;31;40m Invalid selection, please try again.\n \033[0;0m"
            menu_actions['main_menu']()
    return


# Encode Menu
def encode_menu():
    string_to_encode = str(raw_input("\033[1;34;40m Enter the string you want to ENCODE : \033[0;0m"))
    en_all(string_to_encode)
    exec_menu("3")
    return


# Decode Menu
def decode_menu():
    string_to_decode = str(raw_input("\033[1;34;40m Enter the string you want to DECODE : \033[0;0m"))
    string_type = str(raw_input("\033[1;34;40m Enter the string type (bin: Binary, b16: Base16, b32: Base32, b64: Base64) : \033[0;0m"))
    de_all(string_to_decode, string_type)
    exec_menu("3")
    return


# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit_():
    sys.exit()


# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': encode_menu,
    '2': decode_menu,
    '3': back,
    '0': exit_,
}

# Main Program
if __name__ == "__main__":
    main_menu()
