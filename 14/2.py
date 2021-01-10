from itertools import permutations, combinations, product
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


def apply_full_mask(addr, mas):
    temp_mask = list("000000000000000000000000000000000000")  # "0" * 36
    addr_str = "{0:036b}".format(addr)
    for num, elem in enumerate(mas):
        if elem == "0":
            temp_mask[num] = addr_str[num]
        elif elem == "1":
            temp_mask[num] = "1"
        elif elem == "X":
            temp_mask[num] = "X"
        else:
            assert False, "lalal"
    return "".join(temp_mask)


def generate_addresses(address, mask):
    count_x = mask.count("X")
    # print(f"generate_addresses {address=}, {mask=}")
    address_mask = apply_full_mask(address, mask)
    for comb in product("01", repeat=count_x):
        temp_mask = address_mask
        for x in comb:
            temp_mask = temp_mask.replace("X", x, 1)
        # print(f"{temp_mask=}")
        # print("ads       ={0:036b}".format(address))
        # print("address   ={0:036b}".format(address | int(temp_mask, 2)))
        yield int(temp_mask, 2)


full_sum = 0
values = {}
for block in blocks:
    mask = block[0].split("=")[1].strip()
    for mem in block[1:]:
        value = int(mem.split("=")[1].strip())
        address = mem.split("=")[0].strip().replace("mem[", "").replace("]", "")
        for ads in generate_addresses(int(address), mask):
            # print(f"{ads=}")
            values[ads] = value
pprint(values)
full_sum += sum(values.values())
print(full_sum)
