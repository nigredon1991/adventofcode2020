from itertools import permutations, combinations
from pprint import pprint

with open("input") as f:
    inp = [l.strip() for l in f.readlines()]

pprint(inp)
depart = int(inp[0])
raw_buses = [x for x in inp[1].split(",")]


def raw_to_bus(x):
    if x == "x":
        return 0
    return int(x)


buses = [raw_to_bus(x) for x in raw_buses]

cur_time = 0

print(f"{buses=}")

while True:
    cur_time += buses[0]
    print(f"{cur_time=}")
    for num, bus in enumerate(buses[1:]):
        # print(f"{bus=}")
        # print(f"{num=}")
        if bus == 0:
            continue
        if (cur_time + num + 1) % bus != 0:
            break
    else:
        print("got break")
        break
print(f"{cur_time=}")
# for num, bus in enumerate(buses[1:]):
#     if bus == 0:
#         continue
#     print(f"{bus}")
#     print(f"{num}")
#     print(cur_time + num)
#     print(cur_time + num % bus)
