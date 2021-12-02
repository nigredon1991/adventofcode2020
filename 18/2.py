from itertools import product
import re

import numpy as np

with open("input_big") as f:
    inp = [line.strip() for line in f.readlines()]
print(inp)


def change_prior(line):
    return line

def calc(line):
    val = None
    oper = None
    if len(line) == 1:
        return line
    for item in line.split():
        if item.isdecimal():
            if oper:
                val = eval(f"{val} {oper} {item}")
                oper = None
            else:
                val = item
        else:
            oper = item
    return val


def parse(line):
    while x := re.search(r"\([^()]+\)", line):
        line = line[0 : x.start()] + str(calc(line[x.start()+1 : x.end()-1])) + line[x.end() :]
    return calc(line)


full = 0
for i in inp:
    full += int(parse(i))
print(full)
