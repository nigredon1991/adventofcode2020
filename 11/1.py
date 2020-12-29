from itertools import permutations, combinations
from pprint import pprint

with open("input_1") as f:
    inp = [list(l.strip()) for l in f.readlines()]


print(inp)
m = len(inp)
n = len(inp[0])


def get_nex_elem(x, y, cur_seat):
    count_occupied_around = 0
    # breakpoint()
    for i in 1, 0, -1:
        for j in 1, 0, -1:
            if x + i < 0 and y + j < 0 and x + i > m and y + j > n:
                continue
            if cur_seat[x + i][y + j] == "#":
                count_occupied_around += 1
    if cur_seat[x][y] == "L" and count_occupied_around == 0:
        return "#"
    if cur_seat[x][y] == "#" and count_occupied_around >= 4:
        return "L"
    return cur_seat[x][y]


def get_nex_seat(cur_seat):
    next_seat = [list(range(n)) for _ in range(m)]
    for i_line, line in enumerate(cur_seat):
        for j_row, elem in enumerate(line):
            next_seat[i_line][j_row] = get_nex_elem(i_line, j_row, cur_seat)
    print(next_seat)
    return next_seat


cur = inp
new_seat = [list(range(n)) for _ in range(m)]
while True:
    nex = get_nex_seat(cur)
    breakpoint()
    if nex == cur:
        break
    cur = nex
print(cur)
