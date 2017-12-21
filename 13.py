def calculate_score(layers, delay=0):
    severity = 0
    ever_caught = False
    for d, r in layers.items():
        cycle_length = 2 * (r - 1)
        caught = (d + delay) % cycle_length == 0
        if caught:
            severity += r * d
            ever_caught = True
    return severity, ever_caught


with open('13.txt') as f:
    lines = f.readlines()
    walls = {}
    for line in lines:
        d, r = [int(i) for i in line.split(': ')]
        walls[d] = r

    # walls = {0: 3,
    #          1: 2,
    #          4: 4,
    #          6: 4}

    print(calculate_score(walls))

    wait = 0
    while True:
        score, caught = calculate_score(walls, wait)
        if score == 0 and not caught:
            print(wait)
            break
        wait += 1
