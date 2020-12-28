from itertools import permutations, combinations

with open("input") as f:
    inp = [int(l) for l in f.readlines()]


s_inp = sorted(inp)
# print(s_inp)

# Parte One
# nearby_list = []

# last_elem = 0
# for elem in s_inp + [max(s_inp) + 3]:
#     nearby_list.append(abs(elem - last_elem))
#     last_elem = elem

# print(nearby_list)
# print("1", nearby_list.count(1))
# print("2", nearby_list.count(2))
# print("3", nearby_list.count(3))
# print(nearby_list.count(1) * nearby_list.count(3))

# Parte One
elem_del = []

s_inp = [0] + s_inp + [max(s_inp) + 3]

# print(s_inp)

for num, elem in enumerate(s_inp):
    if num == 0 or num == len(s_inp)-1:
        continue
    print("num", num, elem)
    print(s_inp[num] - s_inp[num - 1])
    if abs(s_inp[num + 1] - s_inp[num - 1]) < 3:
        # print(s_inp[num - 1], elem, s_inp[num + 1])
        elem_del.append(elem)
print("elem del")
print(elem_del)


def check_perm(perm):
    last_elem = 0
    # print("check_perm", perm)
    for p_elem in perm:
        if p_elem - last_elem <= 3:
            last_elem = p_elem
        else:
            # print("False", perm)
            return False
    # breakpoint()
    # print("True", perm)
    return True


def get_all_could_del(elem_dels, cur_inp):
    c = 0
    # print("elem_dels", elem_dels)
    for del_elem in elem_dels:
        # print(del_elem)
        cur_inp_new = cur_inp.copy()
        cur_inp_new.remove(del_elem)
        # breakpoint()
        new_dels = elem_dels.copy()
        new_dels.remove(del_elem)
        if check_perm(cur_inp_new):
            c += get_all_could_del(new_dels, cur_inp_new)
        else:
            c += 1
    return c


# print(get_all_could_del(elem_del, s_inp))
end_count = 1

for r in range(0, len(elem_del)):
    for e in combinations(elem_del, r):
        if check_perm(sorted(set(s_inp) ^ set(e))):
            end_count += 1
    # print(end_count)
# breakpoint()
