from dataclasses import dataclass
from re import I


a, target = list(map(int, input().split()))


def multiply(original: int, a: int) -> int:
    return original * a


def move(original: int) -> int:
    last_num = original % 10
    if original < 10 or last_num == 0:
        return -1

    return int(f"{last_num}{str(original)[:-1]}")


visited = {}
visit_num = 1
visiting = set([1])
result = 10e10

while len(visiting) > 0:
    visiting_tmp = visiting.copy()
    to_be_removed = set()
    to_be_added = set()
    for v in visiting_tmp:
        mul = multiply(v, a)
        mo = move(v)

        visiting.remove(v)

        if (mul == target or mo == target) and result > visit_num:
            result = visit_num

        to_be_added.add(mul)
        if len(str(mul)) > len(str(target)) or mul in visited:
            to_be_removed.add(mul)

        if mo != -1:
            to_be_added.add(mo)
            if len(str(mo)) > len(str(target)) or mo in visited:
                to_be_removed.add(mo)

    for r in to_be_added:
        visited[r] = True
        visiting.add(r)
    for r in to_be_removed:
        visiting.remove(r)

    visit_num += 1

if result == 10e10:
    print(-1)
else:
    print(result)
