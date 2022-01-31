import os
from ceaser import encrypt


def run():
    answer = input('Encrypt/Decrypt: ')
    if answer == 'Encrypt':
        _handle_encrypt()
    elif answer == 'Decrypt':
        _handle_decrypt()


def _handle_encrypt():
    with open('data/source.txt', 'r') as file:
        lines = file.readlines()

    encrypted_lines = []
    for line in lines:
        encrypted_line = encrypt.ceaser_encrypt(line)
        encrypted_lines.append(encrypted_line)

    with open('data/encrypted.txt', 'w') as file:
        file.writelines(encrypted_lines)


def _handle_decrypt():
    lines = []
    with open('data/encrypted.txt', 'r') as file:
        lines = file.readlines()

    decrypted_lines = []
    for line in lines:
        decrypted_line = encrypt.ceaser_decrypt(line)
        decrypted_lines.append(decrypted_line)

    with open('data/decrypted.txt', 'w') as file:
        file.writelines(decrypted_lines)


if __name__ == '__main__':
    run()
