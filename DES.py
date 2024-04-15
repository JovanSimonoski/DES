import transformations
from modes_of_operation import ecb_mode


def encrypt(plaintext, key):
    plaintext_blocks = transformations.plaintext_transformation(plaintext)
    key_bits = transformations.key_transformation(key)
    encrypted_data = ecb_mode(plaintext_blocks, key_bits, 1)
    return transformations.ciphertext_transformation(encrypted_data)
