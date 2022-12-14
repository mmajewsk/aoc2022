from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os
import time


def view2(ar):
    for k in ar:
        l = k.astype(int).tolist()
        w = "".join(map(str,l))
        w= w.replace('0','.')
        w= w.replace('1','#')
        w= w.replace('2','o')
        sdf(w)

def p1():
    # day = Day(14)
    day = Day(14, 'ex.in')
    rocks = []
    for d in day.lines:
        a = [ tuple(map(int,d2.split(','))) for d2 in  d.split(" -> ") ]
        rocks.append(a)

    minx = a[0][0]
    maxx =  a[0][0]
    miny =  a[0][1]
    maxy =  a[0][1]
    for rock in rocks:
        for x,y in rock:
            if x > maxx:
                maxx = x
            if x < minx:
                minx = x
            if y > maxy:
                maxy = y
            if y < miny:
                miny = y
    sdf(minx, maxx, miny, maxy)

    minx -=3
    maxx += 4
    miny = 0
    sx = maxx-minx
    sy = maxy+3
    data = np.zeros((sy,sx))
    sdf(maxx, minx, sx,sy)
    for rock in rocks:
        for start, end in zip(rock[:-1], rock[1:]):
            if start[0]==end[0]:
                # sdf('x',start,end)
                rang = list(sorted([start[1], end[1]]))
                rang[-1] += 1
                for i in range(*rang):
                    a,b = i, start[0]-minx
                    # sdf(a,b,i)
                    data[a,b] = 1
            if start[1]==end[1]:
                # sdf('y',start,end)

                rang = list(sorted([start[0], end[0]]))
                rang[-1] += 1
                for i in range(*rang):
                    a, b = start[1], i-minx
                    # sdf(a,b,i)
                    data[a,b] = 1
    moremap = True
    while moremap:
    # for i in range(400):
        sand = (500,0)
        sandgo = True
        x,y = sand
        lx = x-minx
        if data[y,lx] == 2:
            break

        while sandgo:
            time.sleep(0.02)
            x,y = sand
            lx = x-minx
            if y+1>=sy:
                print('endmap')
                moremap = False
                break
            if data[y+1, lx] >0:
                ground = "".join(map(str,data[y+1,lx-1:lx+2].astype(int).tolist()))
                if '0' not in ground:
                    sand = x, y
                    sandgo = False
                    break
                elif ground  in ['022', '021', '020', '010', '012', '011']:
                    sand = x-1, y+1
                    data[y,lx] = 0
                elif ground  in ['220', '120', '210', '110']:
                    sand = x+1, y+1
                    data[y,lx] = 0

            else:
                sand = x,y+1
                data[y,lx] = 0
            # view2(data)

            x,y = sand
            lx = x-minx
            data[y,lx] = 2
        view2(data)
        sdf()
        sdf()
        sdf()

    res = Counter(data.ravel().astype(int).tolist())[2]
    sdf(res)






def p2():
    # day = Day(14)
    # data = day.lines
    # data = day.content
    pass


if __name__ == "__main__":
    main = bake_main2()
    main()
    p1()
    p2()
