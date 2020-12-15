from itertools import combinations

with open("input") as f:
    inp = [l for l in f.readlines()]
number_success = 0
for line in inp:
    # print(line)
    num, alpha, word = line.split(" ")
    num_first, num_last = num.split("-")
    num_first_i = int(num_first)
    num_last_i = int(num_last)
    alpha = alpha.replace(":", "")
    # num_in_word = word.count(alpha)
    # if int(num_first) <= num_in_word <= int(num_last):
    #     number_success += 1
    if word[num_first_i - 1] == alpha and word[num_last_i - 1] == alpha:
        continue
    if word[num_first_i - 1] == alpha or word[num_last_i - 1] == alpha:
        number_success += 1


print(number_success)
