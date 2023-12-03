import numpy as np
import re

def window(s, num):
    # checks other lines
    # s = match object
    # num = finditer
    pass

def core(engines):
    for i in range(1, len(engines)-1):
        l = engines[i]
        # print(l)
        l_past = engines[i-1]
        l_next = engines[i+1]
        # match
        symb = re.finditer(r'[^\w\.]', l)
        num_p = re.finditer(r'\d+', l_past)
        numbers_past = [(n.group(), n.start(), n.end()) for n in num_p]
        num_n = re.finditer(r'\d+', l_next)
        numbers_next = [(n.group(), n.start(), n.end()) for n in num_n]
        for s in symb:
            pass

            

def main():
    with open("03/input.txt", "r") as f:
        txt = f.read().strip()
    sample = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.strip()
    engines  = sample.split("\n")
    core(engines)