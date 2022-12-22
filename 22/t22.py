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

SIZE = 50
faces_k = {
    1: {"x": 1, "y": 0},
    # 50<x<=100
    # 0<y<=50
    2: {"x": 2, "y": 0},
    3: {"x": 1, "y": 1},
    4: {"x": 1, "y": 2},
    5: {"x": 0, "y": 2},
    6: {"x": 0, "y": 3},
}

faces_m = {}
for k,v in faces_k.items():
    faces_m[k] = {
        'x': (1+SIZE*v['x'], SIZE*(v['x']+1)),
        'y': (1+SIZE*v['y'], SIZE*(v['y']+1))
    }

faces = {
    1: {"x": (51, 100), "y": (1, 50)},
    # 50<x<=100
    # 0<y<=50
    2: {"x": (101, 150), "y": (1, 50)},
    3: {"x": (51, 100), "y": (51, 100)},
    4: {"x": (51, 100), "y": (101, 150)},
    5: {"x": (1, 50), "y": (101, 150)},
    6: {"x": (1, 50), "y": (151, 200)},
}

assert faces==faces_m, faces_m

def go(dire, pos, expos):
    px, py = expos
    x, y = pos
    face = None
    for f, r in faces.items():
        if r["x"][0] <= px <= r["x"][1] and r["y"][0] <= py <= r["y"][1]:
            face = f
            break

    assert face is not None, (expos, pos)

    sdf("face", face, expos, "dire", dire, "---", pos)
    # nx, ny = expos
    ndire = dire
    if face == 1:
        if dire in (0, 1):
            return None
        elif dire == 2:
            ndire = 0
            nface = 5
            ny = faces[nface]["y"][-1]+1 - (y % SIZE)
        elif dire == 3:
            ndire = 0
            nface = 6
            ny = faces[nface]["y"][0] + (x-1) % SIZE
    elif face == 2:
        if dire == 2:
            return None
        elif dire == 0:
            ndire = 2
            nface = 4
            ny = faces[nface]["y"][-1]+1 - ((y % SIZE))
        elif dire == 1:
            ndire = 2
            nface = 3
            ny = faces[nface]["y"][0] + ((x-1) % SIZE)
        elif dire == 3:
            ndire = 3
            nface = 6
            nx = faces[nface]["x"][0] + ((x-1) % SIZE)
        else:
            1 / 0
    elif face == 3:
        if dire in (1, 3):
            return None
        elif dire == 0:
            ndire = 3
            nface = 2
            nx = faces[nface]["x"][0] + ((y-1) % SIZE)
        elif dire == 2:
            ndire = 1
            nface = 5
            nx = faces[nface]["x"][0] + ((y-1) % SIZE)
        else:
            1 / 0
    elif face == 4:
        if dire in (2, 3):
            return None
        elif dire == 0:
            ndire = 2
            nface = 2
            ny = faces[nface]["y"][-1]+1 - (y % SIZE)
        elif dire == 1:
            ndire = 2
            nface = 6
            ny = faces[nface]["y"][0] + ((x-1) % SIZE)
    elif face == 5:
        if dire in (0, 1):
            return None
        elif dire == 2:
            ndire = 0
            nface = 1
            ny = faces[nface]["y"][-1]+1 - (y % SIZE)
        elif dire == 3:
            ndire = 0
            nface = 3
            ny = faces[nface]["y"][0] + ((x-1) % SIZE)
        else:
            1 / 0
    elif face == 6:
        if dire == 3:
            return None
        elif dire == 0:
            ndire = 3
            nface = 4
            nx = faces[nface]["x"][0] + ((y-1) % SIZE)
        elif dire == 1:
            ndire = 1
            nface = 2
            nx = faces[nface]["x"][0] + ((x-1) % SIZE)
        elif dire == 2:
            ndire = 1
            nface = 1
            nx = faces[nface]["x"][0] + ((y-1) % SIZE)
        else:
            1 / 0

    if ndire == 0:
        nx = faces[nface]["x"][0]
    elif ndire == 1:
        ny = faces[nface]["y"][0]
    elif ndire == 2:
        nx = faces[nface]["x"][-1]
    elif ndire == 3:
        ny = faces[nface]["y"][-1]
    sdf("exit go", 'ndire', ndire, 'ncords', (nx, ny))
    return ndire, (nx, ny)


def p1():
    day = Day(22)
    # day = Day(22, 'ex.in')
    mapa = {}
    readmap = True
    xs, ys = [], []
    vals = []
    for m, d in enumerate(day.lines[:-2]):
        if d == "":
            readmap = False
            continue
        if readmap:
            for k, c in enumerate(d):
                if c == " ":
                    continue
                else:
                    i = k + 1
                    j = m + 1
                    mapa[(i, j)] = c
                    xs.append(i)
                    ys.append(j)
                    vals.append(c)

    moves = []
    print(xs[:3], ys[:3])
    pprint(mapa)
    for x in re.findall("([0-9]+[A-Z])", day.lines[-1]):
        x = x.strip()
        r = x[-1:]
        step = x[:-1]
        moves.append((int(step), r))
    start = xs[0], ys[0]
    dire = 0
    # start = min(filter(lambda x: x[0]==0, mapa.keys()), key=lambda x: x[1])
    sdf(moves)
    sdf("start", start, vals[0])
    pos = start
    dire = 0
    for step, r in moves:
        for s in range(step):
            x, y = pos
            nx, ny = x, y
            ndire = dire
            if dire == 0:
                nx = x + 1
            elif dire == 1:
                ny = y + 1
            elif dire == 2:
                nx = x - 1
            elif dire == 3:
                ny = y - 1
            else:
                1 / 0
            if (nx, ny) not in mapa.keys():
                # mx, my = nx,ny
                # if dire == 0:
                #     mx = min(
                #         filter(lambda x: x[1] == ny, mapa.keys()), key=lambda x: x[0]
                #     )[0]
                # elif dire == 1:
                #     my = min(
                #         filter(lambda x: x[0] == nx, mapa.keys()), key=lambda x: x[1]
                #     )[1]
                # elif dire == 2:
                #     mx = max(
                #         filter(lambda x: x[1] == ny, mapa.keys()), key=lambda x: x[0]
                #     )[0]
                # elif dire == 3:
                #     my = max(
                #         filter(lambda x: x[0] == nx, mapa.keys()), key=lambda x: x[1]
                #     )[1]
                # else:
                #     1 / 0
                edge = go(dire, (nx, ny), (x, y))
                ndire, npos = edge
                nx, ny = npos
                sdf("edge", ndire, npos)
            if mapa[(nx, ny)] == ".":
                pos = nx, ny
                dire = ndire
            else:
                pos = x, y
                dire = dire
                break

            sdf("outer", pos, (nx, ny), (x, y), mapa[pos])
        if r == "R":
            dire += 1
        else:
            dire -= 1
        dire = (dire) % 4
        sdf(r, dire)
    x, y = pos
    res = 1000 * y + 4 * x + dire
    sdf(pos)
    sdf(res)
    # day // res


if __name__ == "__main__":
    main = bake_main2()
    main()
    p1()
    # p2()
