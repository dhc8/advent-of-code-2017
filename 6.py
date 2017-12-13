def reallocate_blocks(blocks):
    max_mem = max(blocks)
    index = blocks.index(max_mem)
    blocks[index] = 0
    size = len(blocks)
    min_to_add = int(max_mem / size)
    blocks_with_extra = max_mem % size
    blocks = blocks[index+1:] + blocks[:index+1]
    for i in range(size):
        mem_to_add = min_to_add
        if (i < blocks_with_extra):
            mem_to_add += 1
        blocks[i] += mem_to_add
    reverse_index = size - index
    return blocks[reverse_index-1:] + blocks[:reverse_index-1]


def find_infinite_loop(blocks):
    past_states = dict()
    counter = 0
    while True:
        blocks_hash = ','.join([str(b) for b in blocks])
        if blocks_hash in past_states:
            return counter, counter - past_states[blocks_hash]
        past_states[blocks_hash] = counter
        blocks = reallocate_blocks(blocks)
        counter += 1


# print(find_infinite_loop([0, 2, 7, 0]))
print(find_infinite_loop([14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]))