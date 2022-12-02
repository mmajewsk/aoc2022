from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os



def p1():
    day = Day(1)
    data = day.lines
    al = [[]]
    for a in data:
        if a == '':
            al.append([])
        else:
            al[-1].append(int(a))
    daa = list(map(sum, al))
    d = max(daa)
    day/d


def p2():
    day = Day(1)
    data = day.lines
    al = [[]]
    for a in data:
        if a == '':
            al.append([])
        else:
            al[-1].append(int(a))
    daa = list(map(sum, al))
    top = sorted(daa)[-3:]
    d = sum(top)
    day//d


if __name__ == "__main__":
    main = bake_main2()
    main()
    p1()
    p2()
