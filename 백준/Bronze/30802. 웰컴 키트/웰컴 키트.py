import sys

Ps = int(sys.stdin.readline())
Ts = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

Ts = [0 if i == 0 else i // T if i % T == 0 else i // T + 1 for i in Ts]
print(sum(Ts))
print(Ps // P, Ps % P)
