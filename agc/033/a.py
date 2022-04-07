from collections import deque


class Solver:
    def __init__(self):
        self.h, self.w = map(int, input().split())
        self.field = [list(input()) for _ in range(self.h)]
        self.ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def solve(self):
        blacks = deque()
        new_blacks = deque()
        for y in range(self.h):
            for x in range(self.w):
                if self.field[y][x] == "#":
                    blacks.append((y, x))

        ans = 0
        while blacks:
            while blacks:
                y, x = blacks.popleft()
                for dy, dx in self.ds:
                    ny = y + dy
                    nx = x + dx
                    if (
                        0 <= ny < self.h
                        and 0 <= nx < self.w
                        and self.field[ny][nx] == "."
                    ):
                        self.field[ny][nx] = "#"
                        new_blacks.append((ny, nx))
            blacks, new_blacks = new_blacks, blacks
            ans += 1

        print(ans - 1)


Solver().solve()
