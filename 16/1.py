from itertools import permutations, combinations
from pprint import pprint
from pandas import Interval

types = []
your_ticket = []
nearby_tickets = []

def str_to_intervals(t):
    out = []
    for elem in t:
        t = []
        for substr in elem.split('or'):
            left, right = int(substr.split('-')[0]), int(substr.split('-')[1])
            t.append(Interval(left,right, closed='both'))
        out.append(t)
    return out


def elem_in_list_intervals(elem, intervals):
    for interval in intervals:
        if elem in interval:
            return True
    return False



with open("input") as f:
    inp = f.readline().strip()
    while inp != '':
        types.append(inp.split(':')[1].strip())
        inp = f.readline().strip()
    types = str_to_intervals(types)
    inp = f.readline().strip()
    if inp == 'your ticket:':
        your_ticket= f.readline().strip()
    inp = f.readline().strip()
    inp = f.readline().strip()
    if inp == "nearby tickets:":
        inp = f.readline().strip().split(',')
        while inp != ['']:
            nearby_tickets.append([int(e) for e in inp])
            inp = f.readline().strip().split(',')
print(f"{types=}")
print(f"{your_ticket=}")
print(f"{nearby_tickets=}")

sum_error = 0

for ticket in nearby_tickets:
    for row in ticket:
        for typ in types:
            if elem_in_list_intervals(row, typ):
                break
        else:
            sum_error += row
print(sum_error)
