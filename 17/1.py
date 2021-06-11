from itertools import product

import numpy as np

with open("input") as f:
    inp = [line.strip() for line in f.readlines()]
print(inp)

# 1 # - active
# 0 . - inactive

elem_to_check = list(product([0, 1, -1], [0, 1, -1], [0, 1, -1]))
elem_to_check.remove((0, 0, 0))


def get_elem_alive(i, j, k, array):
    count_alive_around = 0
    for variant in elem_to_check:
        if array[i + elem_to_check[0]][j + elem_to_check[1]][k + elem_to_check[2]] == 1:
            count_alive_around += 1
    if array[i][j][k] == 1 and 2 <= count_alive_around <= 3:
        return 1
    if array[i][j][k] == 0 and count_alive_around == 3:
        return 1
    return 0


n = 10

area = np.zeros((n, n, n))

k = len(inp)

for num_i, i in enumerate(inp):
    for num_j, j in enumerate(i):
        area[n // 2][n // 2 - k + num_i][n // 2 - k // 2 + num_j] = 0 if j == "." else 1

for _ in range(2):
    area_new = np.zeros((n, n, n))

print(area)
