# from ceaser import settings
from . import settings


def ceaser_encrypt(source: str) -> str:
    shift = settings.SHIFT
    alpha = settings.ALPHABET

    part_end = alpha[-shift:]
    part_start = alpha[:-shift]
    encrypt_alpha = part_end + part_start

    encrypted_source = []
    for symbol in source:
        encrypted_symbol = symbol
        pos = alpha.find(symbol)
        if pos >= 0:
            encrypted_symbol = encrypt_alpha[pos]
        encrypted_source.append(encrypted_symbol)
    
    return ''.join(encrypted_source)


def ceaser_decrypt(encrypted: str) -> str:
    # TODO Add decryption logic
    return encrypted