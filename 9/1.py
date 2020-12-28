from itertools import combinations
from pprint import pprint
import sys

with open("input") as f:
    inp = [int(l) for l in f.readlines()]

count_preamble = 25

# print(inp)


def num_can_turn_out(value, preamble):
    for com in combinations(preamble, r=2):
        if sum(com) == value:
            return True
    return False


def find_not_valid_value(preamble, remain):
    if num_can_turn_out(remain[0], preamble):
        if len(remain) == 1:
            print("full success")
            return 0
        return find_not_valid_value(preamble[1:] + [remain[0]], remain[1:])
    # pprint(preamble)
    # pprint(remain)
    return remain[0]


value = find_not_valid_value(inp[:count_preamble], inp[count_preamble:])
print(value)
print("##########")
search_list = inp[: inp.index(value)]
print(search_list)

cur_list = []

for item in reversed(search_list):
    cur_list.append(item)
    sum_cur = sum(cur_list)
    print(sum_cur)
    if sum_cur == value:
        print("Finded")
        print(cur_list)
        break
    if sum_cur > value:
        cur_list = cur_list[1:]

print(cur_list)
ma = max(cur_list)
mi = min(cur_list)
su = ma + mi
print(f"max: {ma}")
print(f"min: {mi}")
print(f"sum: {su}")
