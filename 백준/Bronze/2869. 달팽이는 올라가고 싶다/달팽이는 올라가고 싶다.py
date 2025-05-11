import sys

A, B, V = map(int, sys.stdin.readline().split())

# V-(A-B)*i<=A
a = (V - A) / (A - B)

if a % 1 == 0:
    print(int(a + 1))
elif a % 1 != 0:
    print(int(a + 2))
