from itertools import permutations, combinations
from pprint import pprint

with open("input_1") as f:
    inp = [l.strip() for l in f.readlines()]

pprint(inp)
depart = int(inp[0])
buses = sorted([int(x) for x in inp[1].split(",") if x != "x"])
print(depart)
print(buses)

times_buses = []
for num, bus in enumerate(buses):
    cur_time = 0
    cur_times = set()
    for time in range(1000):
        cur_time += bus
        cur_times.add(cur_time)
first = times_buses[0]
for i in times_buses[1:]:
    print(first & i)


