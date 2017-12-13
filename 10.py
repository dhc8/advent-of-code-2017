input = '88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205'


def tie_knot(lengths, skip_size=0, start_index=0, seq=[i for i in range(256)]):

    for length in lengths:
        # Reverse length
        seq = seq[length:] + seq[:length][::-1]
        start_index -= length
        # Skip
        seq = seq[skip_size:] + seq[:skip_size]
        start_index -= skip_size
        skip_size += 1

    return seq, skip_size, start_index


def add_extra_lengths(lengths):
    return lengths + [17, 31, 73, 47, 23]


def tie_multiple_knots(lengths, rounds):
    skip_size = 0
    start_index = 0
    seq = [i for i in range(256)]
    for _ in range(rounds):
        seq, skip_size, start_index = tie_knot(lengths, skip_size, start_index, seq)

    # Resequence
    start_index = start_index % 256
    seq = seq[start_index:] + seq[:start_index]
    return seq


def convert_to_list(input_string):
    return [ord(c) for c in input_string]


def dense_hash(sparse_hash):
    assert len(sparse_hash) % 16 == 0
    dense_h = []
    while len(sparse_hash):
        element = sparse_hash[:16]
        del sparse_hash[:16]

        x = element[0]
        for i in range(1, 16):
            x = x ^ element[i]
        dense_h.append(x)
    return dense_h


def knot_hash(input_string):
    byte_codes = convert_to_list(input_string)
    byte_codes = add_extra_lengths(byte_codes)
    print(byte_codes)
    sparse_hash = tie_multiple_knots(byte_codes, 64)
    print(sparse_hash)
    dh = dense_hash(sparse_hash)
    print(dh)
    return ''.join([format(e, '02x') for e in dh])


# # Part 1
# input_list = [int(i) for i in input.split(',')]
# output = tie_multiple_knots(input_list, 1)
# print(output)
# print(output[0] * output[1])


# Part 2
print(knot_hash('AoC 2017'))
# print(knot_hash(input))
# test_lengths = [2, 2]
# print(tie_multiple_knots(test_lengths, 2))
