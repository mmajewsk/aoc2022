from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os


def p1():
    day = Day(4)
    p1, p2 = 0, 0
    start, end = [], []
    for d in day.lines:
        d1, d2 = d.split(",")
        a, b = map(int, d1.split("-"))
        c, d = map(int, d2.split("-"))
        s1 = set(range(a, b + 1))
        s2 = set(range(c, d + 1))
        if a <= d <= c or a <= c <= b:
            p1 += 1
        if s1 & s2:
            p2 += 1
    sdf(p1, p2)
    # day / p1
    # day // p2


def p2():
    # day = Day(4)
    # data = day.lines
    # data = day.content
    pass


if __name__ == "__main__":
    main = bake_main2()
    main()
    p1()
    p2()
