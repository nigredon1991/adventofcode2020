import math

with open("input") as inp:
    f = inp.readlines()
trees = []


def form(t):
    if t == "#":
        return 1
    if t == ".":
        return 0
    assert False
    return True


for line in f:
    trees.append([form(t) for t in line if t != "\n"])
index = 0
count_trees = 0
count_trees_array = []
for line in trees:
    if line[index] == 1:
        count_trees += 1
    index += 3
    if index >= len(line):
        index = index - len(line)
print(count_trees)

index = 0
count_trees = 0
count_trees_array = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for num_slope, slope in enumerate(slopes):
    index = 0
    count_trees = 0
    contin_next = 0
    for line in trees:
        if slope[1] == 2:
            if contin_next == 1:
                contin_next = 0
                continue
            contin_next = 1
        if line[index] == 1:
            count_trees += 1
        index += slope[0]
        if index >= len(line):
            index = index - len(line)
    count_trees_array.append(count_trees)

print(count_trees_array)
print(math.prod(count_trees_array))
