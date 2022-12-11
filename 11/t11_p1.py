
from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os


class Monkey:
    def __init__(self, items, operand, val, test_val, debug):
        self.items = items
        self.operand = operand
        self.test_val = test_val
        self.d = debug
        self.val = val
        self.count = 0

    def ope(self, inp):
        self.count += 1
        fgh = {
            "*": lambda a,b: a*b,
            "/": lambda a,b: a/b,
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
        }
        if "old" in self.val:
            return fgh[self.operand](inp, inp)
        else:
            val = int(self.val)
            return fgh[self.operand](inp, val)

    def test(self, inp):
        ca,cb,div = self.test_val
        if inp%div==0:
            return ca
        else:
            return cb
# def p1():
#     # day = Day(11, 'ex.in')
#     day = Day(11)
#     mli = []
#     mo = {}
#     for d in day.lines:
#         x2 = "Starting items: "
#         x2b = "Operation: new = old "
#         x3 = 'Test: divisible by '
#         cona = "If true: throw to monkey "
#         conb = "If false: throw to monkey "


#         if "Monkey" in d:
#             _,b = d.split(" ")
#             n = int(b[:-1])
#         elif x2 in d:
#             left = d.replace(x2, '')
#             ks = list(map(int,left.split(', ')))
#         elif x3 in d:
#             left = d.replace(x3, '')
#             div = int(left)
#         elif x2b in d:
#             left = d.replace(x2b, '').strip()
#             # sdf("|"+left+"|")
#             operand, val = left.split(' ')
#         elif cona in d:
#             left = d.replace(cona, '')
#             ca = int(left)
#         elif conb in d:
#             left = d.replace(conb, '')
#             cb = int(left)
#             debug = (operand, val, ca,cb ,div)
#             mo[n] = Monkey(ks, operand, val, (ca,cb,div), debug)


#     for _ in range(20):
#         for i in range(len(mo)):
#             m = mo[i]
#             dlist = m.items[:]
#             m.items = []
#             for it in dlist:
#                 # breakpoint()
#                 worry = m.ope(it)
#                 bored = worry//3
#                 next_m = m.test(bored)
#                 mo[next_m].items.append(bored)
#                 sdf(i, it, worry, bored, next_m, m.d)
#     lista = []
#     for m in mo:
#         # print(mo[m].items)
#         lista.append(mo[m].count)
#     ma,mi = sorted(lista)[-2:]
#     res=mi*ma
#     sdf(lista)
#     sdf(res)
#     day/res








def p2():
    day = Day(11, 'ex.in')
    # day = Day(11)
    mli = []
    monkeys = []
    for d in day.lines:
        x2 = "Starting items: "
        x2b = "Operation: new = old "
        x3 = 'Test: divisible by '
        cona = "If true: throw to monkey "
        conb = "If false: throw to monkey "


        if "Monkey" in d:
            _,b = d.split(" ")
            n = int(b[:-1])
        elif x2 in d:
            left = d.replace(x2, '')
            ks = list(map(int,left.split(', ')))
        elif x3 in d:
            left = d.replace(x3, '')
            div = int(left)
        elif x2b in d:
            left = d.replace(x2b, '').strip()
            # sdf("|"+left+"|")
            operand, val = left.split(' ')
        elif cona in d:
            left = d.replace(cona, '')
            ca = int(left)
        elif conb in d:
            left = d.replace(conb, '')
            cb = int(left)
            debug = (operand, val, ca,cb ,div)
            monkeys.append(Monkey(ks, operand, val, (ca,cb,div), debug))

    for m in monkeys:
        print(m.test_vals, m.d)


    # lista = []
    # for m in mo:
    #     # print(mo[m].items)
    #     lista.append(mo[m].count)
    # ma,mi = sorted(lista)[-2:]
    # res=mi*ma
    # sdf(lista)
    # sdf(res)
    # # day/res


if __name__ == "__main__":
    main = bake_main2()
    main()
    # p1()
    p2()
