import sys

T = int(sys.stdin.readline())

for i in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)
    for j in S:
        for k in range(R):
            print(j, end="")
    print("")
