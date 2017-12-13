directions = ["n", "ne", "se", "s", "sw", "nw"]


def get_totals(direction_list):
    totals = {d: 0 for d in directions}
    for direction in direction_list:
        totals[direction] += 1
    return totals


def reduce(totals):
    global directions
    opposites = {directions[i]: directions[i+3] for i in range(3)}
    for a, b in opposites.items():
        cancel_out = min(totals[a], totals[b])
        totals[a] -= cancel_out
        totals[b] -= cancel_out
    directions_left = get_dirs_left(totals)
    if len(directions_left) <= 2:
        return steps_sum(totals)
    for d in directions_left:
        index = directions.index(d)
        if directions[index - 2] in directions_left:
            right = d
            left = directions[index - 2]
            sum = directions[index - 1]
            break
        elif directions[index - 4] in directions_left:
            right = directions[index - 4]
            left = d
            sum = directions[index - 5]
            break
    assert right, 'Error: {}'.format(totals)
    sum_steps = min(totals[right], totals[left])
    totals[sum] += sum_steps
    totals[right] -= sum_steps
    totals[left] -= sum_steps
    directions_left = get_dirs_left(totals)
    if len(directions_left) == 2:
        return steps_sum(totals)
    else:
        print("totals after iteration: {}".format(totals))
        return reduce(totals)


def get_dirs_left(totals):
    return [d for d in totals if totals[d] > 0]


def steps_sum(t):
    s = 0
    for d in t:
        s += t[d]
    return s


with open("11.txt") as f:
    direction_list = f.readline().split(',')
    farthest = 0
    for i in range(len(direction_list)):
        totals = get_totals(direction_list[:i])
        steps = reduce(totals)
        if steps > farthest:
            farthest = steps
    print(steps)
    print(farthest)
