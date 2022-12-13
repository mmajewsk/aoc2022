from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os
from pprint import pprint

def compare(a,b):
    sdf("Compare: ", (a,b), type(a), type(b))

    result = None
    if type(a) == list and type(b) == int:
        result = compare(a, [b])
    elif type(a) == int and type(b) == list:
        result= compare([a], b)
    if result != None:
        sdf("result:", result)
        return result
    for x,y in zip(a,b):
        if type(x) == type(y) == int:
            if x==y:
                sdf('x,y', x,y, None)
                continue
            elif x<y:
                sdf('x,y', x,y, True)
                return True
            else:
                sdf('x,y', x,y, False)
                return False
        elif type(x) == type(y) == list:
            result = compare(x,y)
        elif type(x) == int and type(y) == list:
            result = compare([x], y)
        elif type(x) == list and type(y) == int:
            result = compare(x, [y])
        else:
            1/0
        if result != None:
            return result
    if len(a)<len(b):
        result= True
    elif len(a)>len(b):
        result= False


    sdf("Ordered:", result)
    return result


def p1():
    day = Day(13)
    # day = Day(13, 'ex.in')
    pair = []
    data = []
    for d in day.lines:
        if d == '':
            continue
        else:
            pair.append(eval(d))
        if len(pair)==2:
            data.append(tuple(pair))
            pair = []

    ind = []
    for i,(a,b) in enumerate(data):
        print(i+1)
        result = compare(a,b)
        if result == True:
            ind.append(i+1)
        if result == None:
            print("wrong!")
            break
        sdf('res', result)
        sdf()
        sdf()
    res = sum(ind)
    sdf("ans",res)
    day/res





def p2():
    day = Day(13)
    # day = Day(13, 'ex.in')
    pair = []
    data = []
    for d in day.lines:
        if d == '':
            continue
        data.append(eval(d))

    data.append([[2]])
    data.append([[6]])

    ind = []
    counts = Counter()
    for i,d1 in enumerate(data):
        for j,d2 in enumerate(data):
            if i==j:
                continue
            else:
                sdf(d1,d2)
                res = compare(d1,d2)
                counts[i] += res*1
    sdf(counts)
    di = []
    found = []
    for c in counts:
        di.append((data[c], counts[c]))


    sdf(di)
    endli = list(reversed(sorted(di, key= lambda x: x[1])))
    for i,e in enumerate(endli):
        if e[0] == data[-1] or e[0] == data[-2]:
            found.append(i+1)

    res = prod(found)
    sdf("ans",res)
    day//res



if __name__ == "__main__":
    main = bake_main2()
    main()
    # p1()
    p2()
