from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os



def p1():
    day = Day(2)
    cnt1 = {'A':1, "B":2, "C":3}
    cnt2 = {'X':1, "Y":2, "Z":3}
    s = []
    for d in day.lines:
        a,b = d.split(" ")
        c1 = cnt1[a]
        c2 = cnt2[b]
        out = 0
        if (c2==2 and c1==1) or (c2==1 and c1==3) or (c2==3 and c1==2):
            out = 6
        elif c1==c2:
            out = 3
        else:
            out =0
        sdf(a,b, c1,c2, out)
        s.append(c2+out)

    res = sum(s)
    sdf(s)
    sdf(res)
    # day/res






def p2():
    day = Day(2)
    cnt1 = {'A':1, "B":2, "C":3}
    cnt2 = {'X':1, "Y":2, "Z":3}
    s = []
    for d in day.lines:
        a,b = d.split(" ")
        c1 = cnt1[a]
        c2 = cnt2[b]
        out = 0
        if c2==3:
            out = 6
            if c1<3:
                sign = c1+1
            else:
                sign = 1
        elif 2==c2:
            out = 3
            sign = c1
        else:
            out =0
            if c1>1:
                sign = c1-1
            else:
                sign = 3
        s.append(sign+out)

    res = sum(s)
    sdf(s)
    sdf(res)
    # day//res


if __name__ == "__main__":
    main = bake_main2()
    main()
    # p1()
    p2()
