from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os


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
