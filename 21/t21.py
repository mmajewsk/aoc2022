
from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os


class monke:
    data = {}
    def __init__(self, s):
        self.number = None
        self.name1 = None
        self.name2 = None
        self.operation = None
        if len(s) == 2:
            name = s[0][:-1]
            self.name = name
            self.number = int(s[1])
        else:
            self.name = s[0][:-1]
            self.name1 = s[1]
            self.operation =  s[2]
            self.name2 = s[3]
        monke.data[self.name] = self

    def __str__(self):
        if self.name == 'root':
            name1 = self.name1
            name2 = self.name2
            return str(monke.data[name1])+'=='+str(monke.data[name2])
        elif self.number is None:
            operation = self.operation
            name1 = self.name1
            name2 = self.name2
            return "("+str(monke.data[name1])+operation+str(monke.data[name2])+")"

        else:
            return str(self.number)

    def run(self):
        if self.name == 'root':
            name1 = self.name1
            name2 = self.name2
            return  monke.data[name1].run()- monke.data[name2].run()
        elif self.number is None:
            operation = self.operation
            name1 = self.name1
            name2 = self.name2

            if operation == '+':
                return  monke.data[name1].run() + monke.data[name2].run()
            elif operation == '-':
                return  monke.data[name1].run()- monke.data[name2].run()
            elif operation == '/':
                return  monke.data[name1].run()/ monke.data[name2].run()
            elif operation == '*':
                return  monke.data[name1].run()* monke.data[name2].run()
        else:
            return self.number

def fun(guess):
    monke.data['humn'].number = guess
    res = monke.data['root'].run()
    return res

from scipy.optimize import bisect, fsolve

def p1():
    # day = Day(21, 'ex.in')
    day = Day(21)
    data = {}
    for d in day.lines:
        s = d.split(' ')
        monke(s)
    res = int(monke.data['root'].run())
    sdf(res)
    day/res

def p2():
    day = Day(21)
    # day = Day(21)
    data = {}
    for d in day.lines:
        s = d.split(' ')
        monke(s)
    res = int(monke.data['root'].run())
    res = fsolve(fun, 2*83056452900)

    sdf(int(res))
    sdf(fun(res))
    sdf()


if __name__ == "__main__":
    main = bake_main2()
    main()
    # p1()
    p2()
