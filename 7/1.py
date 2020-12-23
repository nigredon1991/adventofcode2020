from itertools import combinations
from pprint import pprint

with open("input") as f:
    inp = [l for l in f.readlines()]

# ###################################3

# Part One

# parsed = {}
# for line in inp:
#     p = [
#         l.strip()
#         for l in line.replace("bags", "bag")
#         .replace("contain", "")
#         .replace(".", "")
#         .replace(",", "")
#         .split("bag")
#         if l.strip()
#     ]
#     # parsed[p[0]] = [(l.split(maxsplit=1)[1], l.split(maxsplit=1)[0]) for l in p[1:]]
#     for child in [(l.split(maxsplit=1)[1], l.split(maxsplit=1)[0]) for l in p[1:]]:
#         if parsed.get(child[0]):
#             parsed[child[0]].add(p[0])
#         else:
#             parsed[child[0]] = {p[0]}

# pprint(parsed)

# count = set()

# def find_parents(name):
#     print(name)
#     # if name == "other":
#     #     return 0
#     if not parsed.get(name):
#         return
#     for elem in parsed[name]:
#         count.add(elem)
#         find_parents(elem)


# find_parents("shiny gold")
# pprint(count)
# print(len(count))


# ###################################3

# Part Two

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

print(parsed)


def find_depth_count(name):
    print(name)
    count = 0
    for elem in parsed[name]:
        print(name, elem, count)
        if elem[0] == "other":
            return 0
        count += int(elem[1]) + int(elem[1]) * find_depth_count(elem[0])
        print(name, elem, count)
    print(name, elem, count)
    return count


count = find_depth_count("shiny gold")
print(count)
