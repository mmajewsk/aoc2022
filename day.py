from pathlib import Path
from aocd import submit

class Day:

    def __init__(self, day_number, *args, **kwargs):
        self.day_number = day_number
        self.year = kwargs.get('year', 2022)
        self.additional_file_list = args
        if self.additional_file_list:
            self.read_input(self.additional_file_list[-1])
        else:
            self.read_input("p{}.in".format(self.day_number))

    def read_input(self, file_str):
        with open(file_str, 'r') as f:
            self.content = f.read()
        self.lines = self.content.splitlines()

    def __truediv__(self, res):
        submit(res, part="a", day=int(self.day_number), year=self.year)

    def __floordiv__(self, res):
        submit(res, part="b", day=int(self.day_number), year=self.year)
