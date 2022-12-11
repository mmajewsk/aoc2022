from aocd import submit
import argparse

debug = False

def nei(x,y):

    neigh_2d_4 = ((x-1,y), (x+1,y), (x, y-1), (x, y+1))
    neigh_2d_5 = neigh_2d_4  + ((x,y),)
    neigh_2d_4_skew = ((x-1,y-1), (x+1,y-1), (x-1, y+1), (x+1, y+1))
    neigh_2d_8 = neigh_2d_4  + neigh_2d_4_skew
    neigh_2d_9 = neigh_2d_8 + ((x,y),)
    return neigh_2d_9

def sdf(*args):
    if len(args)==0:
        args = [""]
    if debug:
        print(*args)


def bake_main(script_name, p1, p2):
    def main():
        day = script_name.replace("t", "").replace(".py", "")
        print(day)
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--debug", action="store_true", help="Enable debug")
        defname = f"p{day}.in"
        parser.add_argument(
            "path", nargs="?", default=defname, help="Path to the input file"
        )
        parser.add_argument("-p1", action="store_true", help="submit p1")
        parser.add_argument("-p2", action="store_true", help="submit p2")
        parser.add_argument("--year", type=int, default=None, help="select year")
        args = parser.parse_args()
        global debug
        debug = args.debug
        res = p1(args)
        if args.p1:
            submit(res, part="a", day=int(day), year=args.year)
        res = p2(args)
        if args.p2:
            submit(res, part="b", day=int(day), year=args.year)
        # run(args)

    return main

def bake_main2():
    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--debug", action="store_true", help="Enable debug")
        args = parser.parse_args()
        global debug
        debug = args.debug

    return main
