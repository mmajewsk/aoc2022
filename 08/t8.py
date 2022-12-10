from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os


def p1():
    # day = Day(8, 'ex.in')
    day = Day(8)
    dat = []
    for d in day.lines:
        print(d)
        dat.append(list(map(int, list(d.rstrip()))))
    w = np.array(dat)
    sh, sw = w.shape
    sdf(sh, sw)
    sdf(w)

    pl = np.zeros_like(w)
    for j in range(sh):
        mil = -1
        mir = -1
        for i in range(sw):
            z = w[j, i]
            y = w[j, sw - i - 1]
            # print(y, y>mir, mir)
            if z > mil:
                mil = z
                pl[j, i] = 1
            if y > mir:
                mir = y
                pl[j, sw - i - 1] = 1

    pl2 = np.zeros_like(w)
    for i in range(sh):
        mil = -1
        mir = -1
        for j in range(sw):
            z = w[j, i]
            y = w[sh - j - 1, i]
            # print("z", z, z>mil, mil)
            # print("y", y, y>mir, mir)
            if z > mil:
                mil = z
                pl2[j, i] = 1
            if y > mir:
                mir = y
                pl2[sh - j - 1, i] = 1
        print()

    sdf(pl)
    sdf(pl2)
    res = pl | pl2
    res2 = np.sum(res)
    sdf(res2)

def ext(mid, x):
    l = list((x >= mid) * 1)
    if 1 in l:
        return l.index(1) + 1
    else:
        return len(x)

def p2():
    day = Day(8)
    dat = []
    for d in day.lines:
        dat.append(list(map(int, list(d.rstrip()))))
    w = np.array(dat)
    sh, sw = w.shape
    pl = np.zeros_like(w)
    for j in range(sh):
        for i in range(sw):
            mid = w[j, i]
            up = w[j - 1 :: -1, i]
            down = w[j + 1 :, i]
            left = w[j, i - 1 :: -1]
            right = w[j, i + 1 :]
            s = [
                ext(mid, up),
                ext(mid, down),
                ext(mid, left),
                ext(mid, right),
            ]
            pl[j, i] = prod(s)
    res = np.max(pl)
    day // res


if __name__ == "__main__":
    main = bake_main2()
    main()
    # p1()
    p2()
