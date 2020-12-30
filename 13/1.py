from itertools import permutations, combinations
from pprint import pprint

with open("input_1") as f:
    inp = [l.strip() for l in f.readlines()]

pprint(inp)
depart = int(inp[0])
buses = sorted([int(x) for x in inp[1].split(',') if x != 'x'])
print(depart)
print(buses)

nearest_buses = []
min_bus = float("inf")
min_bus_index = -1
for num, bus in enumerate(buses):
    cur_time = 0
    while cur_time < depart:
        cur_time += bus
    nearest_buses.append(cur_time)
    if min_bus > cur_time - depart:
        min_bus = cur_time - depart
        min_bus_index = num

print(nearest_buses)
print(min_bus)
print(buses[min_bus_index])
print(buses[min_bus_index] * min_bus)
