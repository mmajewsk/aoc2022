from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os


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

def p1(cnt):
    day = Day(6)
    # day = Day(6,'pb.in')
    cha = []
    for d in day.lines:
        for i in range(len(d)-cnt):
            l = d[i:i+cnt]
            print(l)
            s1 = set(l)
            if len(s1) == cnt:
                cha.append(i)
                break
    res = cha[0]+cnt
    sdf(res)
    if cnt==4:
        day/res
    elif cnt==14:
        day//res



if __name__ == "__main__":
    main = bake_main2()
    main()
    p1(4)
    p1(14)
