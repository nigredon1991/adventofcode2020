from itertools import permutations

with open("input_2") as f:
    inp = [int(l) for l in f.readlines()]


s_inp = sorted(inp)
print(s_inp)

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
count = 0
elem_del = []

s_inp = s_inp + [max(s_inp) + 3]

for num, elem in enumerate(s_inp[1:-1]):
    if s_inp[num + 1] - s_inp[num - 1] < 3:
        print(s_inp[num - 1], elem, s_inp[num + 1])
        count += 1
        elem_del.append(elem)
print(count)
print(elem_del)


def check_perm(perm):
    last_elem = 0
    for e in perm:
        if e - last_elem <= 3:
            last_elem = e
        else:
            # print("False", perm)
            return False
    # breakpoint()
    print("True", perm)
    return True


def get_all_could_del(elem_dels, cur_inp):
    c = 0
    # print("elem_dels", elem_dels)
    if not elem_dels:
        return 1
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


print(get_all_could_del(elem_del, s_inp))
