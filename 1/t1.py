from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main
import os



def p1(args):
    data = open(args.path).read().splitlines()
    al = [[]]
    for a in data:
        if a == ' ':
            al.append([])
        else:
            al[-1].append(int(a))
    daa = list(map(sum, al))
    d = max(daa)
    return d


def p2(args):
    data = open(args.path).read().splitlines()
    al = [[]]
    for a in data:
        if a == '':
            al.append([])
        else:
            al[-1].append(int(a))
    daa = list(map(sum, al))
    top = sorted(daa)[-3:]
    d = sum(top)
    return d

p2=p1

if __name__ == "__main__":
    script_name = os.path.basename(__file__)
    main = bake_main(script_name, p1, p2)
    main()
