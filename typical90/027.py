n = int(input())

db = set()

us = [input() for _ in range(n)]
for i, username in enumerate(us):
    if username not in db:
        print(i + 1)
        db.add(username)
