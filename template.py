from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main
import os



def p1(args):
    data = open(args.path).read().splitlines()
    d = ...
    sdf(d)
    return d


def p2(args):
    data = open(args.path).read().splitlines()
    d = ...
    #dbg(d)
    #return d


if __name__ == "__main__":
    script_name = os.path.basename(__file__)
    main = bake_main(script_name, p1, p2)
    main()
