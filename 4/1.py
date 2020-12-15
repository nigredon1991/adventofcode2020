from itertools import combinations
import re


def check_pole(pole, value):
    # breakpoint()
    if pole == "byr" and value.isdigit():
        return 1920 <= int(value) <= 2002
    if pole == "iyr" and value.isdigit():
        return 2010 <= int(value) <= 2020
    if pole == "eyr" and value.isdigit():
        return 2020 <= int(value) <= 2030
    if pole == "hgt":
        if value.endswith("cm") and value[:-2].isdigit():
            return 150 <= int(value[:-2]) <= 193
        if value.endswith("in") and value[:-2].isdigit():
            return 59 <= int(value[:-2]) <= 76
        return False
    if pole == "hcl":
        return re.findall(r"^#[0-9a-f]{6}$", value)
    if pole == "ecl":
        return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    if pole == "pid":
        return re.findall(r"^[0-9]{9}$", value)
    assert False
    return False


with open("input") as f:
    inp = [l for l in f.readlines()]

passports = []
cur_lines = []
for line in inp:
    if line == "\n":
        cur_lines_dict = {l.split(":")[0]: l.split(":")[1] for l in cur_lines}
        passports.append(cur_lines_dict)
        cur_lines = []
    else:
        cur_lines = cur_lines + line.split()
cur_lines_dict = {l.split(":")[0]: l.split(":")[1] for l in cur_lines}
passports.append(cur_lines_dict)
print(len(passports))

count = 0

for past in passports:
    # try:
    #     if past['pid'] == '858020233':
    #         breakpoint()
    # except Exception:
    #     pass
    for pole in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if past.get(pole) is None:
            print(pole)
            print(past)
            break
        if not check_pole(pole, past.get(pole)):
            break
    else:
        print(past)
        count += 1
print(count)
