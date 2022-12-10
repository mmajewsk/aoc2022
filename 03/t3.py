from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os
import string
from itertools import zip_longest
# from itertools import groupby

def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')

def p1():
    day = Day(3)
    comps = []
    s = 0
    for d in [day.lines, day.lines, day.lines]:
        l = len(d)//2
        a,b = (d[:l], d[l:])
        z,y = map(set, (a,b))
        comps.append((a,b))
        c = list(z & y)[0]

        if c.islower():
            i = string.ascii_lowercase.index(c) +1
        else:
            i = string.ascii_uppercase.index(c) + 27
        s += i

    day/s






def p2():
    day = Day(3)
    s = 0
    for a,b,c in grouper(day.lines, 3):
        a,b,c = map(set, (a, b, c))
        z = a & b & c
        ch  = list(z)[0]
        if ch.islower():
            i = string.ascii_lowercase.index(ch) +1
        else:
            i = string.ascii_uppercase.index(ch) + 27
        s += i
    day//s



if __name__ == "__main__":
    main = bake_main2()
    main()
    # p1()
    p2()
