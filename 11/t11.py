from collections import Counter, defaultdict
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from copy import deepcopy
from math import prod
from santa import sdf, bake_main2
from day import Day
import os


class Monkey:
    def __init__(self, items, operators, test_val):
        self.items = items
        self.operators = operators
        self.test_val = test_val
        self.count = 0

    def ope(self, orig, re):
        operand, val = self.operators
        if "old" in val:
            b = re
        else:
            b = int(val)

        if operand == "*":
            re = re * b
            re = re % orig
        elif operand == "+":
            re = re + b
            re = re % orig
        return re

    def test(self, number):
        ca, cb, div = self.test_val
        re = number[div]
        if re == 0:
            return ca
        else:
            return cb

    def operate_number(self, number):
        self.count += 1
        new = {}
        for orig, re in number.items():
            new[orig] = self.ope(orig, re)
        return new.copy()


def p2():
    day = Day(11)
    mli = []
    monkeys = []
    for d in day.lines:
        x2 = "Starting items: "
        x2b = "Operation: new = old "
        x3 = "Test: divisible by "
        cona = "If true: throw to monkey "
        conb = "If false: throw to monkey "
        if "Monkey" in d:
            _, b = d.split(" ")
            n = int(b[:-1])
        elif x2 in d:
            left = d.replace(x2, "")
            ks = list(map(int, left.split(", ")))
        elif x3 in d:
            left = d.replace(x3, "")
            div = int(left)
        elif x2b in d:
            left = d.replace(x2b, "").strip()
            operand, val = left.split(" ")
        elif cona in d:
            left = d.replace(cona, "")
            ca = int(left)
        elif conb in d:
            left = d.replace(conb, "")
            cb = int(left)
            monkeys.append(Monkey(ks, (operand, val), (ca, cb, div)))
    divisors = [m.test_val[-1] for m in monkeys]
    for m in monkeys:
        m.items = [{d: it % d for d in divisors} for it in m.items]
    for ci in range(10000):
        for i in range(len(monkeys)):
            m = monkeys[i]
            monkey_list = m.items.copy()
            m.items = []
            for number in monkey_list:
                new_number = m.operate_number(number)
                next_m = m.test(new_number)
                monkeys[next_m].items.append(new_number)
    lista = [m.count for m in monkeys]
    res = prod(sorted(lista)[-2:])
    sdf(res)
    day // res


if __name__ == "__main__":
    main = bake_main2()
    main()
    # p1()
    p2()
