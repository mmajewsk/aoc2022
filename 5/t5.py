from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os
import pandas as pd
from io import StringIO



def p1(reverted = True):
    day = Day(5)
    crates = []
    commands = []
    cr = True
    for d in day.lines:
        if d == "":
            cr = False
            continue
        if cr:
            g = tuple(a for a in d[1::4])
            crates.append(g)
        else:
            d = d.replace('move ','')
            d = d.replace(' from ',';')
            d = d.replace(' to ',';')
            n, a,b = map(int,d.split(';'))
            commands.append((n,a,b))
    df = pd.DataFrame(crates[:-1], columns=crates[-1])
    stacks = []
    for ci in df.columns:
        stacks.append([])
        for l in df[ci].values.tolist():
            if l!=' ':
                stacks[-1].append(l)
    for c in commands:
        n,a,b = c
        take = stacks[a-1][:n]
        del stacks[a-1][:n]
        if reverted:
            rt = list(reversed(take))
        stacks[b-1] = rt + stacks[b-1]
    message = "".join([a[0] for a in stacks])
    sdf(message)
    # day/message


def p2():
    p1(reverted = False)
    # day//message


if __name__ == "__main__":
    main = bake_main2()
    main()
    p1()
    p2()
