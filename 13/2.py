from itertools import permutations, combinations
from pprint import pprint
from math import prod, gcd

with open("input_1") as f:
    inp = [l.strip() for l in f.readlines()]

pprint(inp)
depart = int(inp[0])
raw_buses = [x for x in inp[1].split(",")]


def raw_to_bus(x):
    if x == "x":
        return 0
    return int(x)


def bezout_recursive(a, b):
    """A recursive implementation of extended Euclidean algorithm.
    Returns integer x, y and gcd(a, b) for Bezout equation:
        ax + by = gcd(a, b).
    """
    if not b:
        return (1, 0, a)
    y, x, g = bezout_recursive(b, a % b)
    return (x, y - (a // b) * x, g)


buses = [raw_to_bus(x) for x in raw_buses]

cur_time = 0

print(f"{buses=}")

prod_bus = prod([b for b in buses if b != 0])
print(f"{prod_bus=}")

bus_and_r = [(x, -num) for num, x in enumerate(buses) if x != 0]
print(bus_and_r)

cur_time = 0

m_i = [int(prod_bus / x[0]) for x in bus_and_r]
print(f"{m_i=}")
x_i = []
for num, m in enumerate(m_i):
    x_i.append(int(bezout_recursive(m, bus_and_r[num][0])[0]))
print(f"{x_i=}")

end_count = 0

for num, item in enumerate(x_i):
    print(f"{end_count=}")
    end_count += int(bus_and_r[num][1] * m_i[num] * x_i[num])
print(end_count % prod_bus)
# print(end_count % prod_bus - bus_and_r[-1][1])


# while True:
#     cur_time += buses[0]
#     print(f"{cur_time=}")
#     for bus, r in bus_and_r:
#         if -cur_time % bus == r:
#             continue
#         else:
#             break
#     else:
#         print("got break")
#         break
# print(f"{cur_time=}")
