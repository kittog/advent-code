# gondolas
import re
import numpy as np


def init_last(engines, id):
    s = 0
    id_next = 1 if id==0 else -2
    print(id_next)
    l = engines[id]
    l_next = engines[id_next]
    print(l_next)
    res = re.finditer('\d+', l)
    for r in res:
        n = r.group()
        print(n)
        a = r.start()-1 if r.start() != 0 else r.start()
        b = r.end()+1 if r.end() != len(l) else r.end()
        if re.findall(r'[^\w\.]', l[a:b]):
            s += int(n)
        elif re.findall(r'[^\w\.]', l_next[a:b]):
            s += int(n)
    return s

def core(engines):
    s = 0
    for i in range(1, len(engines)-1):
        l = engines[i]
        l_past = engines[i-1]
        l_next = engines[i+1]
        # match
        res = re.finditer(r'\d+', l)
        # check all matches
        for r in res:
            n = r.group() # potential number
            # bounds
            a = r.start()-1 if r.start() != 0 else r.start()
            b = r.end()+1 if r.end() != len(l) else r.end()
            # TODO : turn into function??
            if re.findall(r'[^\w\.]', l_past[a:b]):
                # part number
                s += int(n)
            elif re.findall(r'[^\w\.]', l_next[a:b]):
                s += int(n)
            elif re.findall(r'[^\w\.]', l[a:b]):
                s += int(n)
            print(n, s)
    return s

def main():
    with open("03/input.txt", "r") as f:
        txt = f.read()
    sample = '''467..114..
            ...*......
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598..'''
    engines = sample.split("\n")
    # init
    sum_init = init_last(engines, 0)
    # 1 to n-1
    sum_core = core(engines)
    # last
    sum_last = init_last(engines, 1)
    print(sum_init+sum_core+sum_last)

main()