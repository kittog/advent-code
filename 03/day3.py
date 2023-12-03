# gondolas
import re
import numpy as np

def init(engine0, engine1):
    s = 0
    res = re.finditer(r'\d+', engine0)
    for r in res:
        n = r.group()
        a = r.start()-1 if r.start() != 0 else r.start()
        b = r.end()+1 if r.end() != len(engine0) else r.end()
        if re.findall(r'[^\w\.]', engine0[a:b]):
            # part number
            s += int(n)
        elif re.findall(r'[^\w\.]', engine1[a:b]):
            print(re.findall(r'[^\w\.]', engine1[a:b]))
            s += int(n)
        else:
            continue
        print(a, b, n, s)
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
        txt = f.read().strip()
    
    engines = txt.split("\n")
    print(engines)
    # init
    sum_init = init(engines[0], engines[1])
    # 1 to n-1
    sum_core = core(engines)
    # last
    sum_last = init(engines[-1], engines[-2])
    print(sum_init, sum_core, sum_last)
    #print(sum_init)

main()