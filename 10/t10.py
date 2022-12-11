
from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os



def p1():
    # day = Day(10, 'ex.in')
    day = Day(10)
    commands = []
    ad = {}
    s = 1
    i = 0
    for d in day.lines:
        if "noop" in d:
            commands.append(("noop", None))

        else:
            c, val = d.split(" ")
            val = int(val)
            commands.append((c,val))

    i = 0
    strength = 0
    while len(commands)!=0:
        i += 1
        if 1 in ad:
            s += ad.pop(1)
        if 2 in ad:
            ad[1] = ad.pop(2)
        c, v = commands.pop(0)
        if c=="noop":
            pass
        else:
            ad[2] = v
            commands.insert(0, ("noop",None))


        # sdf(i,c ,s)
        if (i-20)%40==0 :

            strength += i*s
            sdf(i,c ,s)
            # break
    sdf(strength)
    # day/strength



def pix(br):
    reg = br
    ar = np.zeros((40,))
    if reg<40:
        ar[reg] = 1
    if reg>0:
        ar[reg-1] = 1
    if reg<39:
        ar[reg+1] = 1
    return ar

def pr(tmp):
    for k in tmp:
        l = k.astype(int).tolist()
        w = "".join(map(str,l))
        w= w.replace('0','.')
        w= w.replace('1','#')
        sdf(w)

def p2():
    # day = Day(10, 'ex.in')
    day = Day(10)
    commands = []
    ad = {}
    i = 0
    for d in day.lines:
        if "noop" in d:
            commands.append(("noop", None))

        else:
            c, val = d.split(" ")
            val = int(val)
            commands.append((c,val))

    i = 0
    strength = 0
    tmp_ar = np.zeros((40,))

    s = 1
    reg = 1
    lines = np.zeros((6,40))
    for j in range(240):
        if 1 in ad:
            reg += ad.pop(1)
        if 2 in ad:
            ad[1] = ad.pop(2)
        pos = j%40
        l = j//40
        ar = pix(reg)
        g =  ar[pos]
        lines[l,pos] = g
        c, v = commands.pop(0)
        if c=="noop":
            pass
        else:
            ad[2] = v
            commands.insert(0, ("noop",None))
        sdf('-------------')
        sdf(j, c, pos, ad, l, reg)
        # pr([ar])
        sdf('B')
        # pr(lines)
        # if j > 20:
        #     break
    pr(lines)
    # print(lines)

if __name__ == "__main__":
    main = bake_main2()
    main()
    # p1()
    p2()
