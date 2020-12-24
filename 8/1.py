from itertools import combinations
from pprint import pprint
import sys

with open("input") as f:
    inp = [l.split() + [""] for l in f.readlines()]

# print(inp)

all_jumps = []
# all_nop = []


def got_to_end(all_jumps_need=False):
    acc = 0
    cur_ref = 0
    for i in inp:
        i[2] = ""
    while cur_ref < len(inp) and inp[cur_ref][2] == "":
        inp[cur_ref][2] = "1"
        if inp[cur_ref][0] == "nop":
            if all_jumps_need:
                all_jumps.append([cur_ref, "nop"])
            cur_ref += 1
            continue

        if inp[cur_ref][0] == "acc":
            # all_jumps.append((cur_ref + 1, "acc"))
            acc += int(inp[cur_ref][1])
            cur_ref += 1
            continue

        if inp[cur_ref][0] == "jmp":
            if all_jumps_need:
                all_jumps.append([cur_ref, "jmp"])
            cur_ref += int(inp[cur_ref][1])
    print("next")
    if cur_ref >= len(inp):
        print("Finded")
        print(cur_ref)
        print(acc)
        return True
    return False


if got_to_end(all_jumps_need=True):
    sys.exit(0)

for ref in all_jumps:
    print(ref)
    if ref[1] == "nop":
        saved = "nop"
        inp[ref[0]][0] = "jmp"
    else:
        saved = "jmp"
        inp[ref[0]][0] = "nop"
    if got_to_end():
        sys.exit(0)
    inp[ref[0]][0] = saved
