from typing import Optional


class Train:
    def __init__(self, val):
        self.val = val
        self.before: Optional[Train] = None
        self.after: Optional[Train] = None


N, Q = map(int, input().split())
qs = [list(map(int, input().split())) for _ in range(Q)]

trains = {i: Train(i) for i in range(1, N + 1)}

for q in qs:
    if q[0] == 1:
        x, y = q[1:]
        trains[x].after = trains[y]
        trains[y].before = trains[x]

    if q[0] == 2:
        x, y = q[1:]
        trains[x].after = None
        trains[y].before = None

    if q[0] == 3:
        x = q[1]
        head = trains[x]
        while head.before is not None:
            head = head.before
        ans = []
        while head is not None:
            ans.append(head.val)
            head = head.after
        print(len(ans), *ans)
