N = int(input())
S = input()

if N % 2 != 0:
    print("No")

else:
    if S[: int(len(S) / 2)] == S[int(len(S) / 2) :]:
        print("Yes")
    else:
        print("No")
