from itertools import permutations, combinations
from pprint import pprint

with open("input") as f:
    inp = [int(l) for l in f.read().strip().split(",")]
pprint(inp)
start_elem = inp
all_elements = {}
numbers = []

def add_index(l, index):
    if l is None:
        l = []
        l.append(None)
        l.append(index)
        return l
    l[0] = l[1]
    l[1] = index
    return l


# 2021
# 30000001
for i in range(1, 30000001):
    # print()
    # print(f"{i=}")
    # print(f"{numbers=}")
    # print(f"{all_elements}")
    if start_elem:
        new = start_elem.pop(0)
        numbers.append(new)
        all_elements[new] = add_index(all_elements.get(new), i)
        continue
    prev_elem = numbers[-1]
    if  None in all_elements[prev_elem]:
        new = 0
    else:
        new = all_elements[prev_elem][1] - all_elements[prev_elem][0]
    all_elements[new] = add_index(all_elements.get(new), i)
    numbers.append(new)
print(numbers)
