

from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os
import re
from pprint import pprint



def p1():
    day = Day(22)
    # day = Day(22, 'ex.in')
    mapa = {}
    readmap = True
    xs, ys = [], []
    vals = []
    for m,d in enumerate(day.lines[:-2]):
        if d == '':
            readmap = False
            continue
        if readmap:
            for k,c in enumerate(d):
                if c == ' ':
                    continue
                else:
                    i = k + 1
                    j = m + 1
                    mapa[(i,j)] = c
                    xs.append(i)
                    ys.append(j)
                    vals.append(c)

    moves = []
    print(xs[:3], ys[:3])
    pprint(mapa)
    for x in re.findall('([0-9]+[A-Z])', day.lines[-1]):
        x = x.strip()
        r = x[-1:]
        step = x[:-1]
        moves.append((int(step),r))
    start = xs[0], ys[0]
    dire = 0
    # start = min(filter(lambda x: x[0]==0, mapa.keys()), key=lambda x: x[1])
    sdf(moves)
    sdf('start', start, vals[0])
    pos = start
    dire = 0
    for step, r in moves:
        for s in range(step):
            x,y = pos
            nx,ny = x,y
            if dire==0:
                nx = x+1
            elif dire==1:
                ny = y+1
            elif dire==2:
                nx = x-1
            elif dire==3:
                ny = y-1
            else:
                1/0
            if (nx,ny) not in mapa.keys():
                if dire==0:
                    nx = min(filter(lambda x: x[1]==ny,mapa.keys()), key=lambda x:x[0])[0]
                elif dire==1:
                    ny = min(filter(lambda x: x[0]==nx,mapa.keys()), key=lambda x:x[1])[1]
                elif dire==2:
                    nx = max(filter(lambda x: x[1]==ny,mapa.keys()), key=lambda x:x[0])[0]
                elif dire==3:
                    ny = max(filter(lambda x: x[0]==nx,mapa.keys()), key=lambda x:x[1])[1]
                else:
                    1/0


            if mapa[(nx,ny)] == '.':
                pos = nx,ny
            else:
                pos = x,y
                break

            sdf(pos, (nx,ny), (x,y), mapa[pos])
        if r == 'R':
            dire +=1
        else:
            dire -= 1
        dire = (dire)%4
        sdf(r, dire)
    x,y = pos
    res = 1000* y + 4*x + dire
    sdf(pos)
    sdf(res)
    day/res








def p2():
    # day = Day(22)
    # data = day.lines
    # data = day.content
    pass


if __name__ == "__main__":
    main = bake_main2()
    main()
    p1()
    p2()
