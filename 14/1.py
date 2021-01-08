from itertools import permutations, combinations
from pprint import pprint

with open("input") as f:
    inp = [l.strip() for l in f.readlines()]

blocks = []
temp = []
for line in inp:
    if line.startswith("mask"):
        if temp:
            blocks.append(temp)
            temp = []
    temp.append(line)
blocks.append(temp)

full_sum = 0
values = {}
for block in blocks:
    mask = block[0].split("=")[1].strip()
    mask_0 = int(mask.replace("X", "1"), 2)  # &
    mask_1 = int(mask.replace("X", "0"), 2)  # |
    for mem in block[1:]:
        value_raw_new = int(mem.split("=")[1].strip())
        if value_raw_new >= 68719476735 - 1000:
            print("got")
        address = mem.split("=")[0].strip()
        value_old = 0 if values.get(address) is None else values[address]
        # print(f"{value_old=}")
        value_0 = mask_0 & value_raw_new
        # print(f"{value_0=}")
        value_1 = mask_1 | value_0
        # print(f"{value_1=}")
        values[address] = value_1
    # print(sum(values.values()))
full_sum += sum(values.values())
print(full_sum)
