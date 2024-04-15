from des_round import des_block_iteration


def ecb_mode(blocks, key, enc):
    for i in range(len(blocks)):
        blocks[i] = des_block_iteration(blocks[i], key, enc)
    return blocks


def cbc_mode(blocks, key, iv, enc):
    blocks[0] = list(map(lambda x, y: x ^ y, blocks[0], iv))
    blocks[0] = des_block_iteration(blocks[0], key, enc)

    for i in range(1, len(blocks)):
        blocks[i] = list(map(lambda x, y: x ^ y, blocks[i], blocks[i - 1]))
        blocks[i] = des_block_iteration(blocks[i], key, enc)

    return blocks
