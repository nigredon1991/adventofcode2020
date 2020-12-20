from itertools import combinations

with open("input") as f:
    inp = [l for l in f.readlines()]

groups = []
cur_group = {}
for line in inp:
    if cur_group == {}:
        cur_group = {c for c in line.strip()}
    if line != "\n":
        cur_group = cur_group & {c for c in line.strip()}
    else:
        groups.append(len(cur_group))
        cur_group = {}
groups.append(len(cur_group))

print(groups)

count = 0
for group in groups:
    count += group
print(count)
