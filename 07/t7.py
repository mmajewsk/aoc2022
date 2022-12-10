from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import pprint
import os



def p1():
    # day = Day(7, 'ex.in')
    day = Day(7)
    tree = {}
    point = ''
    listing = False
    for d in day.lines:
        l = d.split(' ')
        if l[0] == '$':
            listing = False
        if l[1] == 'cd':
            if l[2] == '/':
                point = '/'
            elif l[2]=='..':
                point = '/'.join(point.split('/')[:-1])
            else:
                point = point+"/"+l[2].rstrip()
            continue
        elif l[1]=='ls':
            listing = True
            continue
        if listing:
            if point not in tree:
                tree[point] = {}
            if l[0] == 'dir':
                tree[point][l[1].rstrip()] = {}
            else:
                tree[point][l[1].rstrip()] = int(l[0])
    counted = {}
    for _ in range(5):
        for k,v in tree.items():
            for a in v:
                if v[a] == {}:
                    path = k+'/'+a
                    if path in counted:
                        v[a] = counted[path]
                continue
            if {} in v.values():
                continue
            else:
                counted[k] = sum(v.values())
    data = np.array(list(counted.values()))
    sa = np.sum(data[data<100000])
    day/sa

def p2():
    # day = Day(7, 'ex.in')
    day = Day(7)
    tree = {}
    point = ''
    listing = False
    for d in day.lines:
        l = d.split(' ')
        if l[0] == '$':
            listing = False
        if l[1] == 'cd':
            if l[2] == '/':
                point = '/'
            elif l[2]=='..':
                point = '/'.join(point.split('/')[:-1])
            else:
                point = point+"/"+l[2].rstrip()
            continue
        elif l[1]=='ls':
            listing = True
            continue
        if listing:
            if point not in tree:
                tree[point] = {}
            if l[0] == 'dir':
                tree[point][l[1].rstrip()] = {}
            else:
                tree[point][l[1].rstrip()] = int(l[0])
    pprint.pprint(tree)
    counted = {}
    for _ in range(10):
        for k,v in tree.items():
            for a in v:
                if v[a] == {}:
                    path = k+'/'+a
                    if path in counted:
                        v[a] = counted[path]
                continue
            if {} in v.values():
                continue
            else:
                counted[k] = sum(v.values())
    mest = list(filter(lambda x: Counter(x[0])['/'] == 2, [(k,v) for k,v in counted.items()]))

    s = sum(v for k,v in mest)
    # s += sum(filter(lambda x: x!={}, tree['/'].values()))
    s += sum([150961,28669,133395,256180,257693])
    maxspace = 70000000
    left = maxspace-s
    needed = 30000000
    f = needed - left
    sdf(s)
    sdf(left)
    sdf(f)

    # sdf(counted)
    mest = list(filter(lambda x: x[1] >= f, [(k,v) for k,v in counted.items()]))
    res= min(v for k,v in mest)

    sdf(mest)
    sdf(res)

    day//res







if __name__ == "__main__":
    main = bake_main2()
    main()
    # p1()
    p2()
