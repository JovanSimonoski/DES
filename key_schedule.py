permuted_choice_1 = [
    56, 48, 40, 32, 24, 16, 8, 0,
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 60, 52, 44, 36,
    28, 20, 12, 4, 27, 19, 11, 3
]

permuted_choice_2 = [
    13, 16, 10, 23, 0, 4, 2, 27,
    14, 5, 20, 9, 22, 18, 11, 3,
    25, 7, 15, 6, 26, 19, 12, 1,
    40, 51, 30, 36, 46, 54, 29, 39,
    50, 44, 32, 47, 43, 48, 38, 55,
    33, 52, 45, 41, 49, 35, 28, 31
]

left_rotations = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]


def key_schedule(key):
    round_keys = []
    key_pc_1 = list(map(lambda x: key[x], permuted_choice_1))

    key_left = key_pc_1[:28]
    key_right = key_pc_1[28:]

    for i in range(16):
        for j in range(left_rotations[i]):
            key_left.append(key_left[0])
            del key_left[0]

            key_right.append(key_right[0])
            del key_right[0]

        key_append = key_left
        key_append.extend(key_right)
        key_pc_2 = list(map(lambda x: key_append[x], permuted_choice_2))
        round_keys.append(key_pc_2)

    return round_keys
