import sys

while True:
    N = list(map(int, sys.stdin.readline().split()))
    if len(N) == 2:
        print(N[0] + N[1])
    else:
        break
