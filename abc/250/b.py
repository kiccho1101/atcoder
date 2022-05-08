N, A, B = map(int, input().split())


ans = []
for i in range(N):
    if i % 2 == 0:
        block = "\n".join(
            [
                "".join(
                    [
                        "".join(["." if j % 2 == 0 else "#" for _ in range(B)])
                        for j in range(N)
                    ]
                )
                for _ in range(A)
            ]
        )
    else:
        block = "\n".join(
            [
                "".join(
                    [
                        "".join(["#" if j % 2 == 0 else "." for _ in range(B)])
                        for j in range(N)
                    ]
                )
                for _ in range(A)
            ]
        )
    print(block)
