from feistel_function import feistel_function
from key_schedule import key_schedule

initial_permutation = [
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8, 0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6
]

final_permutation = [
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
    32, 0, 40, 8, 48, 16, 56, 24
]


def des_block_iteration(block, key, enc):
    block = list(map(lambda x: block[x], initial_permutation))
    round_keys = key_schedule(key)

    if enc != 1:
        round_keys = round_keys[::-1]

    left_block = block[:32]
    right_block = block[32:]

    final_block = des_round(left_block, right_block, round_keys, 1)
    final_block = list(map(lambda x: final_block[x], final_permutation))

    return final_block


def des_round(left_block, right_block, round_keys, round_number):
    if round_number > 16:
        right_block.extend(left_block)
        return right_block

    round_key = round_keys[round_number - 1]
    right_block_feistel = feistel_function(right_block, round_key)
    left_block = list(map(lambda x, y: x ^ y, left_block, right_block_feistel))
    return des_round(right_block, left_block, round_keys, round_number + 1)
