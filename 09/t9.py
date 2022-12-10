from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
import santa
from day import Day
from pprint import pprint
import os

def nei(x,y):

    neigh_2d_4 = ((x-1,y), (x+1,y), (x, y-1), (x, y+1))
    neigh_2d_5 = neigh_2d_4  + ((x,y),)
    neigh_2d_4_skew = ((x-1,y-1), (x+1,y-1), (x-1, y+1), (x+1, y+1))
    neigh_2d_8 = neigh_2d_4  + neigh_2d_4_skew
    neigh_2d_9 = neigh_2d_8 + ((x,y),)
    return neigh_2d_9


# def view(plane, hist, head):
#     if not santa.debug:
#         return
#     pl = np.zeros_like(plane)
#     pl[head[1], head[0]] = 2
#     pl[hist[-1][1], hist[-1][0]] = 1
#     sdf(np.fliplr(np.flip(pl)))

plane = np.zeros((20,20))

def view2(hist):
    if not santa.debug:
        return
    pl = np.zeros_like(plane)
    for i in range(10):
        head = hist[i][-1]
        print(head)
        pl[head[1], head[0]] = i
    sdf(np.fliplr(np.flip(pl)))

# def move(mov, hist, head):
#     a,b = mov
#     nhead = head[0]+a,head[1]+b
#     nai = nei(*nhead)
#     if hist[-1] not in nai:
#         hist.append(head)
#     head = nhead
#     # view(plane, hist, head)
#     return head, hist

def move2(mov, hist, head):
    a,b = mov
    nhead = head[0]+a,head[1]+b
    nai = nei(*nhead)
    if hist[-1] not in nai:
        hist.append(head)
    head = nhead
    # view(plane, hist, head)
    return head, hist


# def p1():
#     day = Day(9)
#     # day = Day(9, 'ex.in')
#     commands = []
#     spoint = (0,0)
#     head = (0,0)
#     tail = (10,10)
#     for d in day.lines:
#         a = d.split(' ')
#         commands.append((a[0], int(a[1])))
#     sdf(commands)

#     tail = (0,0)
#     # hist = [[tail]]*9
#     hist = [tail]
#     for c, s in commands:
#         pl = np.zeros_like(plane)
#         if c == "R":
#             v = (+1,0)
#         if c == "L":
#             v = (-1,0)
#         if c == "U":
#             v = (0,+1)
#         if c == "D":
#             v = (0,-1)
#         sdf(c,s)
#         for i in range(s):
#             head, _ = move(v, hist, head)
#         print(head)
#         print(hist[-1])

#     if santa.debug:
#         for a,b in hist:
#             plane[b,a] = 1
#     sdf(np.fliplr(np.flip(plane)))
#     c= Counter(hist)
#     sdf(c)
#     res= len(c)
#     sdf(res)
#     print(res)

#     #6687


def view2(hist):
    if not santa.debug:
        return
    pl = np.zeros_like(plane)
    for i in range(10):
        head = hist[i][-1]
        pl[head[1], head[0]] = i
    tmp= np.fliplr(np.flip(pl))
    print('---------------')
    for k in tmp:
        l = k.astype(int).tolist()
        w = "".join(map(str,l))
        w= w.replace('0','.')
        sdf(w)

def p2():
    day = Day(9,'ex2.in')
    # day = Day(9, 'ex.in')
    commands = []
    spoint = (0,0)
    head = (0,0)
    tail = (0,0)
    for d in day.lines:
        a = d.split(' ')
        commands.append((a[0], int(a[1])))
    sdf(commands)

    tail = (5,5)
    hist = [[(5,5),] for _ in range(10)]
    # hist = [tail]
    for c, s in commands:
        pl = np.zeros_like(plane)
        if c == "R":
            v = (+1,0)
        if c == "L":
            v = (-1,0)
        if c == "U":
            v = (0,+1)
        if c == "D":
            v = (0,-1)
        sdf(c,s)
        for i in range(s):
            a,b = v

            head = hist[0][-1]
            nhead = head[0]+a,head[1]+b
            prevhead = head
            hist[0].append(nhead)
            # breakpoint()
            for j in range(1,10):
                nhead = hist[j-1][-1]
                nai = nei(*nhead)
                now = hist[j][-1]
                if now not in nai:
                    hist[j].append((now[0]+a,now[1]+b))
                # view(plane, hist, head)
                # prevh = hist[j-1]
                # head = prevh[-1]
                # hi = hist[j]
                # nhead, hi = move(v, hi, head)
                # hist[j-1].append(nhead)
                # hist[j] = hi
            # pprint(hist)
            view2(hist)
        # break

        # print(head)
        # print(hist[-1])

    # if santa.debug:
    #     for a,b in hist:
    #         plane[b,a] = 1
    # sdf(np.fliplr(np.flip(plane)))
    c= Counter(hist[-1])
    # sdf(c)
    res= len(c)
    # sdf(res)
    print(res)

def p2():

    #6687

if __name__ == "__main__":
    main = bake_main2()
    main()
    # p1()
    p2()
