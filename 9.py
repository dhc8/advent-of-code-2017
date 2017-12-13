def remove_cancels(stream):
    remove_next = False
    for char in stream:
        if remove_next:
            remove_next = False
            continue
        elif char == '!':
            remove_next = True
            continue
        else:
            yield char


chars_removed = 0


def remove_garbage(stream):
    global chars_removed
    stream = remove_cancels(stream)
    is_garbage = False
    for char in stream:
        if is_garbage:
            if char == '>':
                is_garbage = False
            else:
                chars_removed += 1
            continue
        elif char == '<':
            is_garbage = True
            continue
        else:
            yield char


def remove_commas(stream):
    stream = remove_garbage(stream)
    for char in stream:
        yield char.replace(',', '')


def calculate_score(stream):
    score = 0
    points = 0
    stream = remove_commas(stream)
    for char in stream:
        if char == '{':
            points += 1
            score += points
        elif char == '}':
            points -= 1
    return score

with open("9.txt") as s:
    str = s.readline()
    print(calculate_score(str))
    print(chars_removed)