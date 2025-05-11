import sys

A, B, C = sys.stdin.readline().split()
A = int(A)
B = int(B)
C = int(C)
earn = C - B


if A + B < C:
    print(1)
elif C > B:
    total = A // earn + 1
    print(f"{total:.0f}")
else:
    print(-1)
