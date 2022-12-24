from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os
import math


def step(wall, w, h, bliz):
    newbliz = defaultdict(list)
    for k, b in bliz.items():
        for c in b:
            x, y = k
            if c == "<":
                nx, ny = x - 1, y
            elif c == ">":
                nx, ny = x + 1, y
            elif c == "^":
                nx, ny = x, y - 1
            elif c == "v":
                nx, ny = x, y + 1
            newdir = nx, ny
            if newdir in wall:
                if c == "<":
                    nx = w - 2
                elif c == ">":
                    nx = 1
                elif c == "^":
                    ny = h - 2
                elif c == "v":
                    ny = 1
            newdir = nx, ny
            newbliz[newdir].append(c)
    return newbliz


def nei(x, y):
    neigh_2d_4 = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
    neigh_2d_5 = neigh_2d_4 + ((x, y),)
    return neigh_2d_5


def draw(w, h, wall, bliz, pos={}):
    for ly in range(h):
        line = []
        for lx in range(w):
            if (lx, ly) in wall:
                line.append("#")
            elif (lx, ly) in bliz:
                bl = bliz[(lx, ly)]
                if len(bl) > 1:
                    line.append(str(len(bl)))
                else:
                    line.append(bl[0])
            elif (lx, ly) in pos:
                line.append("E")
            else:
                line.append(".")
        print("".join(line))


def solve(start, end, nobliz, step, lcm):
    search = [(start[0], start[1], step)]
    checked = set()
    solved = set()
    while len(search) != 0:
        x, y, s = search.pop(0)
        neigh = nei(x, y)
        all_possible = nobliz[s % lcm]
        possible = []
        checked.add((x, y, s % lcm))
        for na in neigh:
            if na in all_possible:
                possible.append(na)
        if end in possible:
            solved = (x, y, s)
            break
        for nx, ny in possible:
            newcase = (nx, ny, s + 1)
            if (nx, ny, (s + 1) % lcm) not in checked and newcase not in search:
                search.append(newcase)
    _, _, res = solved
    return res


def p2():
    day = Day(24)
    # day = Day(24, "ex.in")
    space = set()
    wall = set()
    bliz = defaultdict(list)
    h = len(day.lines)
    w = len(day.lines[0].strip())
    print("sizes:", w, h)
    fa, fb = w - 2, h - 2
    lcm = math.lcm(fa, fb)
    print("inner sizes and lcm", fa, fb, lcm)
    # assumption: no blizard reaches start or end
    for j, d in enumerate(day.lines):
        for i, a in enumerate(d.strip()):
            if a == ".":
                if j == 0:
                    start = (i, j)
                elif j == h - 1:
                    end = (i, j)
            elif a == "#":
                wall.add((i, j))
            elif a in "<>v^":
                bliz[(i, j)].append(a)

    draw(w, h, wall, bliz)
    static_anti_bliz = []
    for k in range(lcm):
        static_anti_bliz.append(set())
        for j in range(h):
            for i in range(w):
                p = i, j
                if p not in wall and p not in bliz:
                    static_anti_bliz[-1].add(p)
        bliz = step(wall, w, h, bliz)
    t1 = solve(start, end, static_anti_bliz, 0, lcm)
    print("P1:", t1)
    t2 = solve(end, start, static_anti_bliz, t1, lcm)
    t3 = solve(start, end, static_anti_bliz, t2, lcm)
    print("P2:", t3)
    # p1: 269 p2: 825



if __name__ == "__main__":
    main = bake_main2()
    main()
    p2()
