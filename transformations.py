def key_transformation(key):
    return string_to_bit_array(key)


def plaintext_transformation(plaintext):
    return get_blocks(
        hex_array_to_bit_array(
            padding(
                string_to_hex_array(
                    plaintext
                )
            )
        )
    )


def ciphertext_transformation(ciphertext):
    return bit_array_to_hex_array(
        combine_blocks(
            ciphertext
        )
    )


def combine_blocks(blocks):
    for i in range(1, len(blocks)):
        blocks[0].extend(blocks[i])
    return blocks[0]


def get_blocks(ar):
    return [ar[i:i + 64] for i in range(0, len(ar), 64)]


def string_to_hex_array(s):
    hex_array = []
    for char in s:
        hex_value = hex(ord(char))[2:]
        hex_array.append(hex_value)
    return hex_array


def string_to_bit_array(s):
    bit_array = []
    for char in s:
        ascii_value = ord(char)
        binary_representation = bin(ascii_value)[2:].zfill(8)
        bit_array.extend([int(bit) for bit in binary_representation])
    return bit_array


def hex_array_to_bit_array(ar):
    bit_array = []
    for hex_value in ar:
        decimal_value = int(hex_value, 16)
        binary_string = bin(decimal_value)[2:]
        padded_binary = binary_string.zfill(len(hex_value) * 4)
        bit_array.extend([int(bit) for bit in padded_binary])
    return bit_array


def hex_array_to_string(hex_array):
    string = ""
    for hex_value in hex_array:
        string += chr(int(hex_value, 16))
    return string


def bit_array_to_hex_array(bit_array):
    hex_array = []
    chunks = [bit_array[i:i + 8] for i in range(0, len(bit_array), 8)]
    for chunk in chunks:
        hex_digit_1 = hex(int(''.join(map(str, chunk[:4])), 2))[2:]
        hex_digit_2 = hex(int(''.join(map(str, chunk[4:])), 2))[2:]
        hex_array.append(str(hex_digit_1)+(str(hex_digit_2)))
    return hex_array


def padding(ar):
    if len(ar) % 8 == 0:
        for i in range(8):
            ar.append('10')
    else:
        index = 8 - (len(ar) % 8)
        index_hex = hex(index)[2:].zfill(2)
        for i in range(index):
            ar.append(index_hex)
    return ar


def remove_padding(ar):
    p = int(ar[len(ar) - 1], 16)
    for i in range(p):
        del ar[len(ar) - 1]
    return ar
