from itertools import permutations, combinations
from pprint import pprint
from pandas import Interval

types = []
name_types = []
your_ticket = []
nearby_tickets = []


def str_to_intervals(t):
    out = []
    for elem in t:
        t = []
        for substr in elem.split("or"):
            left, right = int(substr.split("-")[0]), int(substr.split("-")[1])
            t.append(Interval(left, right, closed="both"))
        out.append(t)
    return out


def elem_in_list_intervals(elem, intervals):
    for interval in intervals:
        if elem in interval:
            return True
    return False


with open("input") as f:
    inp = f.readline().strip()
    while inp != "":
        name_types.append(inp.split(":")[0].strip())
        types.append(inp.split(":")[1].strip())
        inp = f.readline().strip()
    types = str_to_intervals(types)
    inp = f.readline().strip()
    if inp == "your ticket:":
        your_ticket = f.readline().strip().split(",")
    inp = f.readline().strip()
    inp = f.readline().strip()
    if inp == "nearby tickets:":
        inp = f.readline().strip().split(",")
        while inp != [""]:
            nearby_tickets.append([int(e) for e in inp])
            inp = f.readline().strip().split(",")
# print(f"{types=}")
for num, typ in enumerate(types):
    print(f"{num=} {typ=}")


# print(f"{name_types=}")
print(f"{your_ticket=}")
# print(f"{nearby_tickets=}")

sum_error = 0
correct_ticket = []

for ticket in nearby_tickets:
    go_next = 0
    for row in ticket:
        for typ in types:
            if elem_in_list_intervals(row, typ):
                break
        else:
            sum_error += row
            go_next = 1
    if go_next == 1:
        continue
    correct_ticket.append(ticket)
# print(f"{correct_ticket=}")
# print(f"{len(correct_ticket)=}")
# print(f"{len(nearby_tickets)=}")

numbers_free = set(range(len(types)))
numbers_correct = {x: set() for x in range(len(types))}
numbers_maybe = {x: set() for x in range(len(types))}

for number in numbers_free:
    for num in set(range(len(types))):
        for ticket in correct_ticket:
            if not elem_in_list_intervals(ticket[num], types[number]):
                break
        else:
            numbers_maybe[number].add(num)

out = [-1] * len(types)

while numbers_free:
    for num, elem in enumerate(numbers_maybe):
        cur_set = numbers_maybe[elem] & numbers_free
        if len(cur_set) == 1:
            cur_elem = cur_set.pop()
            numbers_free.remove(cur_elem)
            out[num]= cur_elem



print(f"{out=}")
answer = 1
for num, name in enumerate(name_types):
    if name.startswith("departure"):
        print(f'{name=} {your_ticket[out[num]]}')
        answer *= int(your_ticket[out[num]])
print(answer)
