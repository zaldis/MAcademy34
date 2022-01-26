# import ceaser.settings
# print(ceaser.settings.ALPHABET, ceaser.settings.SHIFT)

# from ceaser import settings as s
# print(s.ALPHABET, s.SHIFT)

# from ceaser.settings import ALPHABET, SHIFT
# print(ALPHABET, SHIFT)


# from ceaser import settings
# print(settings.ALPHABET, settings.SHIFT)


from ceaser import encrypt


def run():
    answer = input('Encrypt/Decrypt: ')

    if answer == 'Encrypt':
        file = open('data/source.txt', 'r')
        lines = file.readlines()
        file.close()

        encrypted_lines = []
        for line in lines:
            encrypted_line = encrypt.ceaser_encrypt(line)
            encrypted_lines.append(encrypted_line)
        
        # file = open('data/encrypted.txt', 'w')
        # file.writelines(encrypted_lines)
        # file.close()

        with open('data/encrypted.txt', 'w') as file:
            file.writelines(encrypted_lines)

    elif answer == 'Decrypt':
        pass


if __name__ == '__main__':
    run()