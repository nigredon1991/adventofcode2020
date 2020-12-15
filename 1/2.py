from itertools import combinations

with open("input") as f:
    inp = [int(l) for l in f.readlines()]
print(inp)

for pair in combinations(inp, r=3):
    if pair[0] + pair[1] + pair[2] == 2020:
        print(pair[0], pair[1], pair[2])
        print(pair[0] * pair[1] * pair[2])
