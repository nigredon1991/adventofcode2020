from itertools import permutations, combinations
from pprint import pprint

with open("input_1") as f:
    inp = [(l[0], int(l.strip()[1:])) for l in f.readlines()]

pprint(inp)


def get_next_coordinate(direction, cur_pos):
    x, y = 0, 0
    if direction[0] == "N":
        x = 0
        y = 1
    if direction[0] == "S":
        x = 0
        y = -1
    if direction[0] == "E":
        x = 1
        y = 0
    if direction[0] == "W":
        x = -1
        y = 0
    if direction[0] == "W":
        x = -1
        y = 0
    if x != 0 or y != 0:
        return [cur_pos[0] + x * direction[1], cur_pos[1] + y * direction[1], cur_pos[2]]

    variant = ((1, 0), (0, 1), (-1, 0), (0, -1))
    if direction[0] == "L":
        cur_var = variant.index(cur_pos[2])
        cur_var += direction[1] / 90
        cur_var = int(cur_var % 4)
        return [cur_pos[0], cur_pos[1], variant[cur_var]]

    if direction[0] == "R":
        variant = list(reversed(variant))
        cur_var = variant.index(cur_pos[2])
        cur_var += direction[1] / 90
        cur_var = int(cur_var % 4)
        return [cur_pos[0], cur_pos[1], variant[cur_var]]
    if direction[0] == "F":
        return [
            cur_pos[0] + cur_pos[2][0] * direction[1],
            cur_pos[1] + cur_pos[2][1] * direction[1],
            cur_pos[2],
        ]
    assert False


coord = [0, 0, (1, 0)]
for elem in inp:
    print(elem)
    print(coord)
    coord = get_next_coordinate(elem, coord)
print(coord)
print(abs(coord[0]) + abs(coord[1]))
