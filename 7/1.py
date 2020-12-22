from itertools import combinations
from pprint import pprint

with open("input") as f:
    inp = [l for l in f.readlines()]

parsed = {}

for line in inp:
    p = [
        l.strip()
        for l in line.replace("bags", "bag")
        .replace("contain", "")
        .replace(".", "")
        .replace(",", "")
        .split("bag")
        if l.strip()
    ]
    parsed[p[0]] = [(l.split(maxsplit=1)[1], l.split(maxsplit=1)[0]) for l in p[1:]]

pprint(parsed)


def find_depth(name):
    c = 0
    print(name)
    # if name == "other":
    #     return 0
    for elem in parsed[name]:
        if elem[0] == "other":
            continue
        c += 1 + find_depth(elem[0])
    return c


print(find_depth("shiny gold"))
