from itertools import permutations, combinations
from pprint import pprint

with open("input") as f:
    inp = [list(l.strip()) for l in f.readlines()]


pprint(inp)
m = len(inp)
n = len(inp[0])
print("m: ", m)
print("n: ", n)


def get_nex_elem_part_one(x, y, cur_seat):
    # print(x, y)
    count_occupied_around = 0
    for i in 1, 0, -1:
        for j in 1, 0, -1:
            if i == 0 and j == 0:
                continue
            if x + i < 0 or y + j < 0 or x + i >= m or y + j >= n:
                continue
            # print("for: ", x + i, y + j)
            if cur_seat[x + i][y + j] == "#":
                count_occupied_around += 1
    if cur_seat[x][y] == "L" and count_occupied_around == 0:
        return "#"
    if cur_seat[x][y] == "#" and count_occupied_around >= 4:
        return "L"
    return cur_seat[x][y]


def get_elem_see_in_direction(x, y, i, j, cur_seat):
    for k in range(1, 1000):
        # print("for: ", x + i * k, y + j * k)
        if x + i * k < 0 or y + j * k < 0 or x + i * k >= m or y + j * k >= n:
            return "."
        if cur_seat[x + i * k][y + j * k] != ".":
            return cur_seat[x + i * k][y + j * k]


def get_nex_elem_part_two(x, y, cur_seat):
    # print(x, y)
    count_occupied_around = 0
    for i in 1, 0, -1:
        for j in 1, 0, -1:
            if i == 0 and j == 0:
                continue
            if x + i < 0 or y + j < 0 or x + i >= m or y + j >= n:
                continue
            # print("for: ", x + i, y + j)
            if cur_seat[x + i][y + j] == ".":
                if get_elem_see_in_direction(x, y, i, j, cur_seat) == "#":
                    count_occupied_around += 1
                continue
            if cur_seat[x + i][y + j] == "#":
                count_occupied_around += 1
    if cur_seat[x][y] == "L" and count_occupied_around == 0:
        return "#"
    if cur_seat[x][y] == "#" and count_occupied_around >= 5:
        return "L"
    return cur_seat[x][y]


def get_nex_seat(cur_seat):
    next_seat = [list(range(n)) for _ in range(m)]
    for i_line, line in enumerate(cur_seat):
        for j_row, elem in enumerate(line):
            next_seat[i_line][j_row] = get_nex_elem_part_two(i_line, j_row, cur_seat)
    # print(next_seat)
    return next_seat


cur = inp
new_seat = [list(range(n)) for _ in range(m)]
count = 0
while True:
    nex = get_nex_seat(cur)
    pprint(nex)
    # breakpoint()
    if nex == cur:
        break
    cur = nex
    count += 1
print(count)


def get_occup_count(seat):
    c = 0
    for line in seat:
        for elem in line:
            if elem == "#":
                c += 1
    return c


print(get_occup_count(nex))
