from itertools import groupby

with open("input") as f:
    inp = list(f.readlines())


def get_seat(line, min_l, max_l):
    if len(line) == 1:
        if line in {"F", "L"}:
            return min_l
        return max_l
    if line[0] in {"F", "L"}:
        return get_seat(line[1:], min_l, min_l + (max_l - min_l) // 2)
    return get_seat(line[1:], min_l + (max_l - min_l) // 2 + 1, max_l)


def get_seat_id(row_l, col_l):
    return row_l * 8 + col_l


max_seat_id = 0
full_set = set()
for inp_l in inp:
    row = get_seat(inp_l[:7], 0, 127)
    col = get_seat(inp_l[7:10], 0, 7)
    seat_id = get_seat_id(row, col)
    full_set.add((row, col))
    if max_seat_id < seat_id:
        max_seat_id = seat_id

print(max_seat_id)
for elem in groupby(sorted(full_set), lambda x: x[0]):
    print([x for x in elem[1]])

print(get_seat_id(77, 3))
