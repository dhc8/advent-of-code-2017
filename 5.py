def jump(jumps, start_index=0, counter=0):
    try:
        this_jump = jumps[start_index]
        next_index = start_index + this_jump
        if this_jump >= 3:
            jumps[start_index] -= 1
        else:
            jumps[start_index] += 1
        counter += 1
    except IndexError:
        raise Exception(counter)
    return jumps, next_index, counter


with open("5.txt") as f:
    input_jumps = [int(l) for l in f.readlines()]
    # input_jumps = [0, 3, 0, 1, -3]
    jumps, next_index, counter = jump(input_jumps)
    while(True):
        jumps, next_index, counter = jump(jumps, next_index, counter)