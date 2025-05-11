import sys

S = sys.stdin.readline().strip()
#'baekjoon'

for i in range(ord("a"), ord("z") + 1):
    try:
        print(S.index(chr(i)), end=" ")
    except ValueError:
        print(-1, end=" ")
