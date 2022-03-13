V, A, B, C = map(int, input().split())

while V >= 0:
    V -= A
    if V < 0:
        exit(print("F"))
    V -= B
    if V < 0:
        exit(print("M"))
    V -= C
    if V < 0:
        exit(print("T"))
