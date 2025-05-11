import sys

N, X = map(int, sys.stdin.readline().split())
lst = sys.stdin.readline().split()
lst = list(map(int, lst))
a = []
for i in range(N):
    if lst[i] < X:
        a.append(lst[i])
    else:
        pass
print(*a, sep=" ")
