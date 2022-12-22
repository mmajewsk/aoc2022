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

faces = {}
for k, v in faces_k.items():
    faces[k] = {
        "x": (1 + SIZE * v["x"], SIZE * (v["x"] + 1)),
        "y": (1 + SIZE * v["y"], SIZE * (v["y"] + 1)),
    }

cube = {
    1: [None, None, (0, 5), (0, 6)],
    2: [(2, 4), (2, 3), None, (3, 6)],
    3: [(3, 2), None, (1, 5), None],
    4: [(2, 2), (2, 6), None, None],
    5: [None, None, (0, 1), (0, 3)],
    6: [(3, 4), (1, 2), (1, 1), None],
}


def go(dire, pos, expos):
    px, py = expos
    x, y = pos
    face = None
    for f, r in faces.items():
        if r["x"][0] <= px <= r["x"][1] and r["y"][0] <= py <= r["y"][1]:
            face = f
            break
    assert face is not None, (expos, pos)
    ndire = cube[face][dire]
    if ndire is None:
        return None
    ndire, nface = cube[face][dire]
    if abs(dire-ndire) == 2:
        ny = faces[nface]["y"][-1] + 1 - (y % SIZE)
    elif dire == ndire:
        nx = faces[nface]["x"][0] + ((x - 1) % SIZE)
    elif (ndire-1) %4 == dire:
        ny = faces[nface]["y"][0] + ((x - 1) % SIZE)
    elif (ndire-1) %4 != dire:
        nx = faces[nface]["x"][0] + ((y - 1) % SIZE)

    if ndire == 0:
        nx = faces[nface]["x"][0]
    elif ndire == 1:
        ny = faces[nface]["y"][0]
    elif ndire == 2:
        nx = faces[nface]["x"][-1]
    elif ndire == 3:
        ny = faces[nface]["y"][-1]
    sdf("exit go", "ndire", ndire, "ncords", (nx, ny))
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
