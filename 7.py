def convert_file():
    with open("7.txt") as f:
        p_list = []
        for line in f.readlines():
            pieces = line.split(" -> ")
            (name, weight) = pieces[0].split(" (")
            p = {'name': name, 'weight': int(weight.split(")")[0])}
            if len(pieces) == 2:
                supports = [s.strip() for s in pieces[1].split(", ")]
                p['supports'] = supports
            p_list.append(p)
        return p_list


programs = convert_file()
supported = set()
supporting = set()
for program in programs:
    supporting.add(program['name'])
    if 'supports' in program:
        for p in program['supports']:
            supported.add(p)
print(supporting - supported)


def find_program(p_name):
    return [p for p in programs if p['name'] == p_name][0]


def calculate_weight(p_name):
    p = find_program(p_name)
    weight = p['weight']
    if 'supports' in p:
        for sp in p['supports']:
            weight += calculate_weight(sp)
    return weight


def find_bad_balance(p_name):
    print('Checking {0}'.format(p_name))
    p = find_program(p_name)
    total_child_weight = 0
    p_weights = {}
    weights = {}
    for sp in p['supports']:
        weight = calculate_weight(sp)
        total_child_weight += weight
        p_weights[weight] = sp
        if weight in weights:
            weights[weight] += 1
        else:
            weights[weight] = 1
    print('Do something here')
    if len(weights) == 1:
        print('This one must be the problem: {0}, with current weight of {1}'.format(p_name, p['weight']))
        cur_weight = total_child_weight + p['weight']
        print('Returning current total including children of {0}'.format(cur_weight))
        return cur_weight, p['weight']
    else:
        print('Child weights: {}'.format(weights))
        odd_one_out = [w for w in weights if weights[w] == 1][0]
        problem_p = p_weights[odd_one_out]
        print('Checking on child program {0} with weight {1}'.format(problem_p, odd_one_out))
        total_weight, p_weight = find_bad_balance(problem_p)
        correct_total = [w for w in weights if weights[w] != 1][0]
        print('Total weight should be {}'.format(correct_total))
        diff = correct_total - total_weight
        correct_weight = p_weight + diff
        print('Program needs to be {}'.format(correct_weight))
        raise ValueError



base_p_name = 'hlqnsbe'
print(find_bad_balance(base_p_name))
