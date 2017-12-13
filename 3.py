def next_square(n, side=1):
    """
    Return side length
    """
    if side * side >= n:
        return side
    return next_square(n, side+2)


def position(n, side):
    """
    0 is always corner position; range is (1:side-1)
    """
    square = side * side
    pos = (square - n) % (side - 1)
    return pos


def steps_from_side_center(n, side):
    center = (side - 1) / 2
    pos = position(n, side)
    return abs(pos - center)


def distance_from_corner(n, side):
    return (side - 1) / 2 - steps_from_side_center(n, side)


def steps_from_center(n):
    side = next_square(n)
    on_side = steps_from_side_center(n, side)
    to_center = (side - 1) / 2
    return int(on_side + to_center)


class GraphPoint(object):
    def __init__(self, side, touches, value):
        self.side = side
        self.touches = touches
        self.value = value

    def __str__(self):
        return "[side: {0}; touches: {1}; value: {2}]".format(self.side, self.touches, self.value)

    def __repr__(self):
        return self.__str__()


def straight_in_index(index, side):
    if side == 3:
        return 0
    last_side = side-2
    # Calculate equivalent by side
    last_level_len = (last_side - 1) * 4
    side_index = int((index - last_side ** 2) / (side - 1))
    # Offset 2 for each corner and 1 for first point in level
    side_offset = side_index * 2 + 1
    return index - last_level_len - side_offset


def diagonal_index(index, side, offset):
    # Second point needs to wrap
    if offset == -1 and index == (side - 2) ** 2 + 1:
        return index - 2
    # All others are easier
    return straight_in_index(index + offset, side)


def build_next_graph_point(graph):
    index = len(graph)
    side = next_square(index+1, graph[-1].side)
    touches = []
    pos = position(index+1, side)
    distance = distance_from_corner(index + 1, side)
    # Always touches last point
    touches.append(index - 1)
    if side == graph[-1].side:
        # Diagonal point across corner - last position except on first side of level
        if pos == side - 2:
            touches.append(index - 2)
        # Straight in
        if distance > 0:
            touches.append(straight_in_index(index, side))
    # Corner wrap
    if index >= (side * side - 2):
        touches.append((side - 2) ** 2)
    # Diagonal to last level (includes only corners on level with side 3)
    if side > 3 or pos == 0:
        if pos >= 2:
            touches.append(diagonal_index(index, side, 1))
        if pos <= (side - 3):
            touches.append(diagonal_index(index, side, -1))
    value = 0
    assert len(set(touches)) == len(touches), "Error - duplicate value: {}".format(touches)
    for point in touches:
        value += graph[point].value
    graph.append(GraphPoint(side, touches, value))
    print(graph[-1])
    return graph


def iterate_through_graph(graph):
    if graph[-1].value > 289326:
        print("that's it!")
    else:
        graph = build_next_graph_point(graph)
        return iterate_through_graph(graph)


starting_graph=[GraphPoint(1, [], 1)]
print(starting_graph[0])
iterate_through_graph(starting_graph)
