import sys

A, B = sys.stdin.readline().split()
A = A[::-1]
B = B[::-1]
if int(A) >= int(B):
    print(A)
else:
    print(B)
