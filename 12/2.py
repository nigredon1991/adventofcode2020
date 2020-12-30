from itertools import permutations, combinations
from pprint import pprint

with open("input") as f:
    inp = [(l[0], int(l.strip()[1:])) for l in f.readlines()]

pprint(inp)


def get_rotate(rotate_o):
    """return angle and swap or not"""
    direc = rotate_o[0]
    angle = rotate_o[1]
    if angle == 270:
        if direc == "R":
            direc = "L"
        else:
            direc = "R"
        angle = 90
    if direc == "R" and angle == 90:
        return (1, -1, 1)
    if direc == "L" and angle == 90:
        return (-1, 1, 1)
    if angle == 180:
        return (-1, -1, 0)
    assert False, f"{direc=}, {angle=}"


def get_next_coordinate(direction, cur_pos, way):
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
    if x != 0 or y != 0:
        return cur_pos, [way[0] + x * direction[1], way[1] + y * direction[1]]

    if direction[0] in {"L", "R"}:
        rotate = get_rotate(direction)
        if rotate[2]:
            return cur_pos, [way[1] * rotate[0], way[0] * rotate[1]]
        return cur_pos, [way[0] * rotate[0], way[1] * rotate[1]]

    if direction[0] == "F":
        return (
            [cur_pos[0] + way[0] * direction[1], cur_pos[1] + way[1] * direction[1]],
            way,
        )
    assert False


coord = [0, 0]
waypoint = [10, 1]  # x , y , rotate, waypoint
for elem in inp:
    print(elem)
    print(coord)
    print(waypoint)
    coord, waypoint = get_next_coordinate(elem, coord, waypoint)
print(coord)
print(abs(coord[0]) + abs(coord[1]))
