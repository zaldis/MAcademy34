from . import settings


def ceaser_encrypt(source: str) -> str:
    shift = settings.SHIFT
    alpha = settings.ALPHABET

    encrypted_source = []
    for symbol in source:
        encrypted_symbol = symbol
        pos = alpha.find(symbol)
        if pos >= 0:
            # encrypted_symbol = alpha[(pos + shift) % len(alpha)]
            encrypted_symbol = alpha[(pos-shift) % len(alpha)]
        encrypted_source.append(encrypted_symbol)
    
    return ''.join(encrypted_source)


def ceaser_decrypt(encrypted: str) -> str:
    shift = settings.SHIFT
    alpha = settings.ALPHABET

    part_end = alpha[-shift:]
    part_start = alpha[:-shift]
    encrypt_alpha = part_end + part_start

    decrypted_source = []
    for symbol in encrypted:
        decrypted_symbol = symbol
        pos = encrypt_alpha.find(symbol)
        if pos >= 0:
            decrypted_symbol = alpha[pos]
        decrypted_source.append(decrypted_symbol)
    
    return ''.join(decrypted_source)
