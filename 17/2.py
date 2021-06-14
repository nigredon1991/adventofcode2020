from itertools import product

import numpy as np

with open("input") as f:
    inp = [line.strip() for line in f.readlines()]
print(inp)

# 1 # - active
# 0 . - inactive

elem_to_check = list(product([0, 1, -1], [0, 1, -1], [0, 1, -1], [0, 1, -1]))
elem_to_check.remove((0, 0, 0, 0))


def get_elem_alive(i, j, k, w, array):
    count_alive_around = 0
    for elem in elem_to_check:
        if (
            i + elem[0] > (len(array) - 1) or i + elem[0] < 0
            or j + elem[1] > (len(array) - 1) or j + elem[1] < 0
            or k + elem[2] > (len(array) - 1) or k + elem[2] < 0
            or w + elem[3] > (len(array) - 1) or w + elem[2] < 0
        ):
            continue
        if array[i + elem[0]][j + elem[1]][k + elem[2]][w + elem[3]] == 1:
            count_alive_around += 1
    if array[i][j][k][w] == 1 and 2 <= count_alive_around <= 3:
        return 1
    if array[i][j][k][w] == 0 and count_alive_around == 3:
        return 1
    return 0


n = 16

area = np.zeros((n, n, n, n))

k = len(inp)

for num_i, i in enumerate(inp):
    for num_j, j in enumerate(i):
        area[n // 2][n // 2 - k + num_i][n // 2 - k // 2 + num_j] = 0 if j == "." else 1

for _ in range(6):
    print("Step")
    area_new = np.zeros((n, n, n, n))
    for elem in product(range(n), range(n), range(n), range(n)):
        area_new[elem[0]][elem[1]][elem[2]][elem[3]] = get_elem_alive(elem[0], elem[1], elem[2], elem[3], area)
    area = area_new

count_out = 0
for elem in area:
    count_out += elem.sum()

print(area)
print(count_out)
