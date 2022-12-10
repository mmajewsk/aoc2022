import re

MOVE_RE = re.compile(r'(\w) (\d+)')

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def dx(self, other):
        return other.x - self.x

    def dy(self, other):
        return other.y - self.y

    def move(self, direction):
        if direction == 'U':
            return Point(self.x, self.y + 1)
        if direction == 'UR':
            return Point(self.x + 1, self.y + 1)
        if direction == 'R':
            return Point(self.x + 1, self.y)
        if direction == 'DR':
            return Point(self.x + 1, self.y - 1)
        if direction == 'D':
            return Point(self.x, self.y - 1)
        if direction == 'DL':
            return Point(self.x - 1, self.y - 1)
        if direction == 'L':
            return Point(self.x - 1, self.y)
        if direction == 'UL':
            return Point(self.x - 1, self.y + 1)

def slither():
    visited.add(snake[9])
    with open('p9.in') as fp:
        line = fp.readline()
        while line:
            movement = MOVE_RE.match(line)
            direction = movement.group(1)
            distance = int(movement.group(2))
            for _ in range(1, distance + 1):
                move(0, direction)
                visited.add(snake[9])
            line = fp.readline().rstrip()

def move(section, direction):
    snake[section] = snake[section].move(direction)
    if section == len(snake) - 1:
        return

    dy = snake[section + 1].dy(snake[section])
    dx = snake[section + 1].dx(snake[section])
    if(abs(dx) < 2 and abs(dy) < 2):
        return

    follow = ''
    if dy > 0:
        follow += 'U'
    elif dy < 0:
        follow += 'D'

    if dx > 0:
        follow += 'R'
    elif dx < 0:
        follow += 'L'

    if follow != '':
        move(section + 1, follow)

visited = set()
snake = [Point(0,0) for _ in range(10)]
slither()
print(len(visited))
