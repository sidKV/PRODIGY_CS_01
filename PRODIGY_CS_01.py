# -*- coding: utf-8 -*-
"""Intership.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ot0KpvOR4Lh6XhY-zWMKtVfrBnsej4Yz
"""

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) - 65 + shift_amount) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift_amount) % 26 + 97)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").upper()
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        print("Encrypted message:", encrypt(text, shift))
    elif choice == 'D':
        print("Decrypted message:", decrypt(text, shift))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()